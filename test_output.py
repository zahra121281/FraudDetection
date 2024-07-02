import logging
from pyvis.network import Network
from sys import stdout
from neo4j import GraphDatabase
import  settings
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
	logging.getLogger("neo4j").setLevel(level)@timeit
	def query_cc_relationship_with_degree(self, tx, k=6, limit=4):
		"""Handles third query of the project proposal:"""
		n = (k * 4) + 4
		query = (
			f"MATCH path=(c1:Customer)-[*{{n}}]-(c2:Customer) \n"
			f"RETURN path \n"
			f"LIMIT $limit"
		)
		result = tx.run(query, limit=limit)
		# self.show_result(result, f'Result of Co-Customer relationship with degree {{k}}: ')
		self.visualize_result_Query3(result)
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
	def run_queries(self):
		with self.driver.session() as session:
			session.execute_read(self.query_cc_relationship_with_degree)
	
def main():
	"""This function runs requested queries."""

	Handler.enable_log(logging.INFO, stdout)
	handler = Handler(settings.DB_URL, settings.USERNAME, settings.PASSWORD, settings.WORKING_DB)
	handler.run_queries()
	handler.close()
if __name__ == "__main__":
	main()
