import logging
from pyvis.network import Network
from sys import stdout
from py2neo import Graph
import settings
from timing import timeit

class Handler:

    def __init__(self, uri, user, passwd):
        self.graph = Graph(uri, auth=(user, passwd))

    def close(self):
        self.graph = None

    @staticmethod
    def enable_log(level, output_stream):
        handler = logging.StreamHandler(output_stream)
        handler.setLevel(level)
        logging.getLogger("py2neo").addHandler(handler)
        logging.getLogger("py2neo").setLevel(level)

    @timeit
    def query_customer_payments(self, start_date="2020-04-01", end_date="2020-07-01", limit=10):
        """Handles first query of the project proposal"""
        query = (
            "MATCH (c:Customer)-[r:HAS_TX]->(tx:Transaction) "
            "WHERE tx.date >= $start_date AND tx.date <= $end_date "
            "RETURN c, sum(tx.amount) AS total_amount, tx.date "
            "ORDER BY c, tx.date LIMIT $limit"
        )
        result = self.graph.run(query, start_date=start_date, end_date=end_date, limit=limit)
        self.visualize_result_Query1(result)
        return result

    @timeit
    def query_terminal_fraud_transactions(self, start_date="2020-04-01", end_date="2020-07-01", limit=100):
        """Handles second query of the project proposal"""
        query = (
            "MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) "
            "WHERE date(tx.date) > date($start_date) - Duration({days: 30}) "
            "AND date(tx.date) < date($start_date) "
            "WITH t, avg(tx.amount) AS avg_tx "
            "MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) "
            "WHERE date(tx.date) > date($start_date) AND date(tx.date) < date($end_date) "
            "AND (avg_tx + (avg_tx / 2)) < tx.amount "
            "RETURN t, count(tx) AS tx_count, avg_tx LIMIT $limit"
        )
        result = self.graph.run(query, start_date=start_date, end_date=end_date, limit=limit)
        self.visualize_result_Query2(result)
        return result

    @timeit
    def query_cc_relationship_with_degree(self, k=4, limit=10):
        """Handles third query of the project proposal"""
        n = (k * 4) + 4
        query = (
            f"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) "
            f"RETURN c1, c2 LIMIT $limit"
        )
        result = self.graph.run(query, limit=limit)
        self.show_result(result, f'Result of Co-Customer relationship with degree {k}: ')
        self.visualize_result_Query3(result)
        return result

    @timeit
    def query_transactions_of_each_period(self, start_date="2020-04-01", end_date="2020-07-01"):
        """Handles fourth query of the project proposal"""
        query = (
            "MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) "
            "WHERE date(tx.date) > date($start_date) - Duration({days: 30}) "
            "AND date(tx.date) < date($start_date) "
            "WITH t, avg(tx.amount) AS avg_tx "
            "MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) "
            "WHERE date(tx.date) > date($start_date) AND date(tx.date) < date($end_date) "
            "AND (avg_tx + (avg_tx / 2)) < tx.amount "
            "WITH tx.tx_period AS p, count(tx) AS ctx "
            "MATCH (tx:Transaction) WHERE tx.tx_period = p "
            "RETURN p, ctx, count(tx)"
        )
        result = self.graph.run(query, start_date=start_date, end_date=end_date)
        self.show_result(result, 'Result of transactions and fraud transactions for each period: ')
        return result

    @staticmethod
    def show_result(result, message='query result: '):
        print(message)
        for row in result:
            print(dict(row))

    def visualize_result_Query1(self, data):
        visual_graph = Network()
        for record in data:
            customer = record['c']
            total_amount = record['total_amount']
            date = record['tx.date']
            customer_id = customer.identity
            customer_name = f"Customer {customer_id}"
            visual_graph.add_node(customer_id, customer_name, group="Customer")
            visual_graph.add_node(date, date, group="Date")
            visual_graph.add_edge(customer_id, date, title=f"Total: {total_amount}")
        visual_graph.show('customer_payments_q1.html', notebook=False)

    def visualize_result_Query2(self, data):
        visual_graph = Network()
        for i, record in enumerate(data):
            terminal = record['t']
            tx_count = record['tx_count']
            avg_tx = record['avg_tx']
            terminal_id = terminal.identity
            terminal_name = f"Terminal {terminal_id}"
            visual_graph.add_node(terminal_id, label=terminal_name, group="Terminal")
            visual_graph.add_node(f"AvgTx_{i}", label=f"AvgTx: {avg_tx:.2f}", group="AverageTx")
            visual_graph.add_node(f"Count_{i}", label=f"Count: {tx_count}", group="TransactionCount")
            visual_graph.add_edge(terminal_id, f"AvgTx_{i}", title=f"Average Transaction: {avg_tx:.2f}")
            visual_graph.add_edge(terminal_id, f"Count_{i}", title=f"Suspicious Transactions: {tx_count}")
        visual_graph.show('terminal_fraud_transactions.html', notebook=False)

    def visualize_result_Query3(self, data):
        visual_graph = Network()
        for record in data:
            c1 = record['c1']
            c2 = record['c2']
            c1_id = c1['id']
            c2_id = c2['id']
            c1_name = f"Customer {c1_id}"
            c2_name = f"Customer {c2_id}"
            visual_graph.add_node(c1_id, label=c1_name, group="Customer")
            visual_graph.add_node(c2_id, label=c2_name, group="Customer")
            visual_graph.add_edge(c1_id, c2_id)
        visual_graph.show('customer_relationships.html', notebook=False)

    def run_queries(self):
        self.query_customer_payments()
        self.query_terminal_fraud_transactions()
        self.query_cc_relationship_with_degree()
        self.query_transactions_of_each_period()


def main():
    """This function runs requested queries."""
    Handler.enable_log(logging.INFO, stdout)
    handler = Handler(settings.DB_URL, settings.USERNAME, settings.PASSWORD)
    handler.run_queries()
    handler.close()


if __name__ == "__main__":
    main()
