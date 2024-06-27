import logging
from pyvis.network import Network
from sys import stdout

from neo4j import GraphDatabase

import settings
from timing import timeit


class Handler:

    def __init__(self, uri, user, passwd, database):
        self.driver = GraphDatabase.driver(uri, auth=(user, passwd), database=database)

    def close(self):
        self.driver.close()

    @staticmethod
    def enable_log(level, output_stream):
        handler = logging.StreamHandler(output_stream)
        handler.setLevel(level)
        logging.getLogger("neo4j").addHandler(handler)
        logging.getLogger("neo4j").setLevel(level)

    @timeit
    def query_customer_payments(self, tx, start_date="2020-04-01", end_date="2020-07-01", limit=20):
        """Handles first query of the project proposal"""
        query = (
            "MATCH (c:Customer)-[r:HAS_TX]->(tx:Transaction) "
            'where tx.date >= $start_date and tx.date <= $end_date '
            "RETURN c, sum(tx.amount), tx.date order by c, tx.date limit $limit "
        )
        result = tx.run(query,
                        start_date=start_date,
                        end_date=end_date,
                        limit=limit)
        self.show_result(result, 'Result of customer daily payments: ')
        # self.visualize_result_Query1( result)
        return result

    @timeit
    def query_terminal_fraud_transactions(self, tx, start_date="2020-04-01", end_date="2020-07-01", limit=100):
        """Handles second query of the project proposal:"""
        query = (
            'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '
            'WHERE date(tx.date) > date($start_date) - Duration({days: 30}) '
            'AND date(tx.date) < date($start_date) '
            'WITH t, avg(tx.amount) AS avg_tx '
            'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '
            'WHERE date(tx.date) > date($start_date) AND date(tx.date) < date($end_date) '
            'AND (avg_tx+(avg_tx/2)) < tx.amount '
            'RETURN t, count(tx), avg_tx LIMIT $limit'
        )
        result = tx.run(query,
                        start_date=start_date,
                        end_date=end_date,
                        limit=limit)
        self.show_result(result, 'Result of terminal fraud transactions: ')
        # self.visualize_result_Query2( result)
        return result

    @timeit
    # def query_cc_relationship_with_degree(self, tx, k=4, limit=20):
    #     """Handles third query of the project proposal:"""
    #     n = (k * 4) + 4
    #     query = (
    #         f"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) \n"
    #         f"RETURN c1, c2 \n"
    #         f"LIMIT $limit"
    #     )
    #     result = tx.run(query,
    #                     limit=limit)
    #     # self.show_result(result, f'Result of Co-Customer relationship with degree {k}: ')
    #     self.visualize_result_Query3( result)
    #     return result
    def query_cc_relationship_with_degree(self, tx, k=4, limit=20):
        """Handles third query of the project proposal:"""
        n = (k * 4) + 4
        query = (
            f"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) \n"
            f"RETURN path \n"
            f"LIMIT $limit"
        )
        result = tx.run(query, limit=limit)
        # self.show_result(result, f'Result of Co-Customer relationship with degree {k}: ')
        self.visualize_result_Query3(result)
        return result

    @timeit
    def query_transactions_of_each_period(self, tx, start_date="2020-04-01", end_date="2020-07-01"):
        """Handles fourth query of the project proposal:"""
        query = (
            'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '
            'WHERE date(tx.date) > date($start_date) - Duration({days: 30}) '
            'AND date(tx.date) < date($start_date) '
            'WITH t,avg(tx.amount) AS avg_tx '
            'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '
            'WHERE date(tx.date) > date($start_date) AND date(tx.date) < date($end_date) '
            'AND (avg_tx+(avg_tx/2)) < tx.amount '
            'WITH tx.tx_period AS p, count(tx) AS ctx '
            'MATCH (tx:Transaction) where tx.tx_period = p '
            'RETURN p,ctx,count(tx)'
        )
        result = tx.run(query,
                        start_date=start_date,
                        end_date=end_date)
        # self.show_result(result, 'Result of transactions and fraud transactions for each period: ')
        return result

    @staticmethod
    def show_result(result, message='query result: '):
        print(message)
        for row in result:
            print(row)

    def visualize_result_Query1(self , data):
        visual_graph = Network()
        for record in data:
            customer = record[0]
            total_amount = record[1]
            date = record[2]
            customer_id = customer.id
            customer_name = f"Customer {customer_id}"
            visual_graph.add_node(customer_id, customer_name, group="Customer")
            visual_graph.add_node(date, date, group="Date")
            visual_graph.add_edge(customer_id, date, title=f"Total: {total_amount}")
        visual_graph.show('customer_payments_q1.html', notebook=False)

    def visualize_result_Query2(self, data):
        
        visual_graph = Network()
        i = 0 
        for record in data:
            terminal = record[0]
            tx_count = record[1]
            avg_tx = record[2]
            
            terminal_id = terminal.id
            terminal_name = f"Terminal {terminal_id}"
            
            visual_graph.add_node(terminal_id, label=terminal_name, group="Terminal")
            visual_graph.add_node(f"AvgTx_{i}", label=f"AvgTx: {avg_tx:.2f}", group="AverageTx")
            visual_graph.add_node(f"Count_{i}", label=f"Count: {tx_count}", group="TransactionCount")
            
            visual_graph.add_edge(terminal_id, f"AvgTx_{i}", title=f"Average Transaction: {avg_tx:.2f}")
            visual_graph.add_edge(terminal_id, f"Count_{i}", title=f"Suspicious Transactions: {tx_count}")
            
            i += 1

        visual_graph.show('terminal_fraud_transactions.html', notebook=False)

    # def visualize_result_Query3(self, data):
    #     visual_graph = Network()

    #     for record in data:
    #         c1 = record['c1']
    #         c2 = record['c2']

    #         c1_id = c1['id']
    #         c2_id = c2['id']
    #         c1_name = f"Customer {c1_id}"
    #         c2_name = f"Customer {c2_id}"
    #         # Add customer nodes
    #         visual_graph.add_node(c1_id, label=c1_name, group="Customer")
    #         visual_graph.add_node(c2_id, label=c2_name, group="Customer")
    #         visual_graph.add_edge(c1_id, c2_id)
    #     visual_graph.show('customer_relationships.html', notebook=False)

    from pyvis.network import Network

    def visualize_result_Query3(self, data):
        visual_graph = Network()
        # Define color for each group
        color_map = {
            "Customer": "#ff9999",  # Light red
            "Terminal": "#99ccff",  # Light blue
            "Transaction": "#99ff99"  # Light green
        }

        for record in data:
            path = record['path']
            nodes = path.nodes
            relationships = path.relationships

            start_node_id = nodes[0].id  # Assuming nodes[0] is the start node
            end_node_id = nodes[-1].id   # Assuming nodes[-1] is the end node

            for node in nodes:
                node_id = node.id
                node_labels = node.labels
                node_label = next(iter(node_labels))  # Assuming single label per node      
                # Determine the group based on the label
                if 'Customer' in node_labels:
                    group = "Customer"
                    node_label = f"Customer {node['id']}"
                elif 'Terminal' in node_labels:
                    group = "Terminal"
                    node_label = f"Terminal {node['id']}"
                elif 'Transaction' in node_labels:
                    group = "Transaction"
                    node_label = f"Transaction {node['id']}"
                else:
                    group = "Other"
                    color_map[group] = "#cccccc"  # Default color for other nodes
                # Bold the start and end nodes
                if node_id == start_node_id:
                    visual_graph.add_node(node_id, label=node_label, color=color_map[group], size=30, borderWidth=5)
                elif node_id == end_node_id:
                    visual_graph.add_node(node_id, label=node_label, color=color_map[group], size=30, borderWidth=5)
                else:
                    visual_graph.add_node(node_id, label=node_label, color=color_map[group])

            for rel in relationships:
                start_node = rel.start_node.id
                end_node = rel.end_node.id
                rel_type = rel.type
                visual_graph.add_edge(start_node, end_node, title=rel_type)

        visual_graph.show('customer_relationships.html', notebook=False)




    def run_queries(self):
        with self.driver.session() as session:
            session.execute_read(self.query_customer_payments)  # query 1
            session.execute_read(self.query_terminal_fraud_transactions)  # query 2
            session.execute_read(self.query_cc_relationship_with_degree)  # query 3
            session.execute_read(self.query_transactions_of_each_period)  # query 4
        

def main():
    """This function runs requested queries."""

    Handler.enable_log(logging.INFO, stdout)
    handler = Handler(settings.DB_URL, settings.USERNAME, settings.PASSWORD, settings.WORKING_DB)
    handler.run_queries()
    handler.close()


if __name__ == "__main__":
    main()
