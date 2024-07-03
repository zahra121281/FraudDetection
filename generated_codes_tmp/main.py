import logging
from pyvis.network import Network
from sys import stdout
from neo4j import GraphDatabase
import  settings
from timing import timeit
import pandas as pd
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
	def show_result_function(self , result , msg):
		print(msg)
		data = [record.data() for record in result]
		df = pd.DataFrame(data)
		print(df)
	@timeit
	def query_cc_relationship_with_degree(self, tx, k=6, limit=4):
		"""Handles third query of the project proposal:"""
		n = (k * 4) + 4
		query = (
			f"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) \n"
			f"RETURN path \n"
			f"LIMIT $limit"
		)
		result = tx.run(query, limit=limit)
		self.visualize_result_Query3(result)
		query = (
			f"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) \n"
			f"RETURN c1, c2\n"
			f"LIMIT $limit"
		)
		result = tx.run(query, limit=limit)
		self.show_result_function( result ,"result of Query3")
		return result
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
	@timeit
	def query_customer_payments(self, tx, start_date="2020-04-01", end_date="2020-07-01", limit=4):
		"""Handles first query of the project proposal"""
		query = (
			"MATCH (c:Customer)-[r:HAS_TX]->(tx:Transaction) "
			'WHERE tx.date >= $start_date AND tx.date <= $end_date '
			"RETURN c, sum(tx.amount), tx.date ORDER BY c, tx.date LIMIT $limit "
		)
		result = tx.run(query,
						start_date=start_date,
						end_date=end_date,
						limit=limit)
		# self.show_result(result, 'Result of customer daily payments: ')
		self.visualize_result_Query1(result)
		return result
	def visualize_result_Query1(self, data):
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
	@timeit
	def query_terminal_fraud_transactions(self, tx, start_date="2020-04-01", end_date="2020-07-01", limit=4):
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
		self.show_result_function( result ,"result of Query2")
		return result
	@timeit
	def query_structured_transactions(self,tx, start_date="2020-04-01", end_date="2020-07-01", limit=4):
		"""Handles detection of structured transactions (Scenario 5)"""
		query = (
			"MATCH (c:Customer)-[:HAS_TX]->(tx:Transaction) "
			"WHERE tx.date >= $start_date AND tx.date <= $end_date "
			"WITH c, tx, count(tx) AS num_tx, sum(tx.amount) AS total_amount "
			"WHERE num_tx > 5 AND total_amount > 5000 "
			"RETURN c, total_amount, num_tx, collect(tx) AS transactions "
			"ORDER BY total_amount DESC LIMIT $limit"
		)
		result = tx.run(query, start_date=start_date, end_date=end_date, limit=limit)
		self.visualize_q5(result)
		return result
	def visualize_q5(self , data):
		visual_graph = Network(height="1000px", width="100%", notebook=False, directed=True)
		# Define color for each group
		color_map = {
			"Customer": "#ff9999",  # Light red
			"Transaction": "#99ff99"  # Light green
		}
		for record in data:
			customer = record['c']
			total_amount = record['total_amount']
			num_tx = record['num_tx']
			transactions = record['transactions']
			customer_id = customer.id
			customer_label = f"Customer {customer_id}"
			visual_graph.add_node(customer_id, label=customer_label, group="Customer", color=color_map["Customer"])
			for tx in transactions:
				tx_id = tx.id
				tx_label = f"Transaction {tx_id}\nAmount: {tx['amount']}\nDate: {tx['date']}"
				visual_graph.add_node(tx_id, label=tx_label, group="Transaction", color=color_map["Transaction"])
				visual_graph.add_edge(customer_id, tx_id, title=f"Transaction {tx_id}")
		visual_graph.show('structured_transactions.html', notebook=False)
	def run_queries(self):
		with self.driver.session() as session:
			session.execute_read(self.query_customer_payments)
			session.execute_read(self.query_terminal_fraud_transactions)
			session.execute_read(self.query_cc_relationship_with_degree)
			session.execute_read(self.query_structured_transactions )
	
def main():
	"""This function runs requested queries."""

	Handler.enable_log(logging.INFO, stdout)
	handler = Handler(settings.DB_URL, settings.USERNAME, settings.PASSWORD, settings.WORKING_DB)
	handler.run_queries()
	handler.close()
if __name__ == "__main__":
	main()
