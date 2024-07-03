import os 

class ILMapper:
    def __init__(self , proj_path):
        self.stack = []
        self.py_codes = []
        self.proj_path = proj_path
        self.operator = ['Start', 'commands', 'Setting', 'Load_terminal', 'Load_customer' , 'Load_transaction',
                        'Detect_customer', 'Detect_terminal', 'Detect_date_range', 'Detect_degree_limit' , 'Detect_structured_transactions']
        self.queries = [0, 0, 0 , 0 , 0 ]
    
    # ['"bolt://localhost:7687"', '"neo4j"', 'compiler@proj', '"kjdkfjg"', 'Setting', '"./terminal.cvx"', 'Load_terminal', 
    #  '"./transaction.cvx"', 'Load_customer', '"./customer.cvx"', 'Load_transaction', '2003-02-12', '2004-02-12', '8', 
    #  'Detect_customer', '2003-02-12', '2004-04-12', 'Detect_date_range', 'commands', 'Start']

    def generate_py_based_on_operator(self , item ) : 
        if item == "Start":
            return self.generate_program()

        elif item == "commands":
            return self.set_commands()
        
        elif item == "Setting" :
            return self.generate_settings()

        elif item == "Load_terminal":
            return self.load_terminal()

        elif item == "Load_customer":
            return self.load_customer()

        elif item == "Load_transaction":
            return self.load_transaction()

        elif item == "Detect_customer":
            return self.detect_customer()

        elif item == "Detect_terminal":
            return self.detect_terminal()

        elif item == "Detect_date_range" :
            return self.detect_date_range()

        elif item == "Detect_degree_limit" :
            return self.detect_degree_limit()

        elif item == "Detect_structured_transactions" :
            return self.detect_structured_transactions()

    def detect_structured_transactions( self ) : 
        self.queries[4] = 1 
        limit = self.stack.pop()
        end_date = self.stack.pop()
        start_date = self.stack.pop()
        result = ""
        result += "@timeit\n"
        result += f"def query_structured_transactions(self,tx, start_date=\"{start_date}\", end_date=\"{end_date}\", limit={limit}):\n"
        result += "\t\"\"\"Handles detection of structured transactions (Scenario 5)\"\"\"\n"
        result += "\tquery = (\n"
        result += '\t\t"MATCH (c:Customer)-[:HAS_TX]->(tx:Transaction) "\n'
        result += '\t\t"WHERE tx.date >= $start_date AND tx.date <= $end_date "\n'
        result += '\t\t"WITH c, tx, count(tx) AS num_tx, sum(tx.amount) AS total_amount "\n'
        result += '\t\t"WHERE num_tx > 5 AND total_amount > 5000 "\n'
        result += '\t\t"RETURN c, total_amount, num_tx, collect(tx) AS transactions "\n'
        result += '\t\t"ORDER BY total_amount DESC LIMIT $limit"\n'
        result += "\t)\n"
        result += "\tresult = tx.run(query, start_date=start_date, end_date=end_date, limit=limit)\n"
        result += "\tself.visualize_q5(result)\n"
        result += "\treturn result\n"
        result += self.add_visulization_q5()
        last_code = self.py_codes.pop()
        if(last_code=="empty"):
            return result
        last_code += result 
        return last_code

    def add_visulization_q5(self):
        result = ''
        result += "def visualize_q5(self , data):\n"
        result += "\tvisual_graph = Network(height=\"1000px\", width=\"100%\", notebook=False, directed=True)\n"
        result += "\t# Define color for each group\n"
        result += "\tcolor_map = {\n"
        result += "\t\t\"Customer\": \"#ff9999\",  # Light red\n"
        result += "\t\t\"Transaction\": \"#99ff99\"  # Light green\n"
        result += "\t}\n"
        result += "\tfor record in data:\n"
        result += "\t\tcustomer = record['c']\n"
        result += "\t\ttotal_amount = record['total_amount']\n"
        result += "\t\tnum_tx = record['num_tx']\n"
        result += "\t\ttransactions = record['transactions']\n"
        result += "\t\tcustomer_id = customer.id\n"
        result += "\t\tcustomer_label = f\"Customer {customer_id}\"\n"
        result += "\t\tvisual_graph.add_node(customer_id, label=customer_label, group=\"Customer\", color=color_map[\"Customer\"])\n"
        result += "\t\tfor tx in transactions:\n"
        result += "\t\t\ttx_id = tx.id\n"
        result += "\t\t\ttx_label = f\"Transaction {tx_id}\\nAmount: {tx['amount']}\\nDate: {tx['date']}\"\n"
        result += "\t\t\tvisual_graph.add_node(tx_id, label=tx_label, group=\"Transaction\", color=color_map[\"Transaction\"])\n"
        result += "\t\t\tvisual_graph.add_edge(customer_id, tx_id, title=f\"Transaction {tx_id}\")\n"
        result += "\tvisual_graph.show('structured_transactions.html', notebook=False)\n"

        return result 

    def generate_program(self ) : 
        pre_code = self.py_codes.pop()
        tabed_code = self.add_tab_to_lines( pre_code)
        new_code = ''
        new_code += "class Handler:\n"
        new_code += tabed_code
        main_function_string = (
            "\ndef main():\n"
            "\t\"\"\"This function runs requested queries.\"\"\"\n"
            "\n"
            "\tHandler.enable_log(logging.INFO, stdout)\n"
            "\thandler = Handler(settings.DB_URL, settings.USERNAME, settings.PASSWORD, settings.WORKING_DB)\n"
            "\thandler.run_queries()\n"
            "\thandler.close()\n"
        )
        new_code += main_function_string
        new_code += "if __name__ == \"__main__\":\n"
        new_code += "\tmain()\n"
        imports = (
            "import logging\n"
            "from pyvis.network import Network\n"
            "from sys import stdout\n"
            "from neo4j import GraphDatabase\n"
            "import  settings\n"
            "from timing import timeit\n"
            "import pandas as pd\n"
        )
        last_code = ''
        last_code += imports
        last_code += new_code
        return last_code


    def add_tab_to_lines(self , input_string):
        lines = input_string.split('\n')
        indented_lines = ['\t' + line for line in lines]
        indented_string = '\n'.join(indented_lines)
        return indented_string
    

    def set_commands(self) :
        last_code = self.py_codes.pop()
        run_query = ""
        run_query += "def run_queries(self):\n"
        run_query += "\twith self.driver.session() as session:\n"

        if self.queries[0] == 1: 
            run_query += "\t\tsession.execute_read(self.query_customer_payments)\n"
        if self.queries[1] == 1: 
            run_query += "\t\tsession.execute_read(self.query_terminal_fraud_transactions)\n"
        if self.queries[2] == 1: 
            run_query += "\t\tsession.execute_read(self.query_cc_relationship_with_degree)\n"
        if self.queries[3] == 1: 
            run_query += "\t\tsession.execute_read(self.query_transactions_of_each_period)\n"
        if self.queries[4] == 1 : 
            run_query += "\t\tsession.execute_read(self.query_structured_transactions )\n"

        enable_log = ''
        enable_log += "@staticmethod\n"
        enable_log += "def enable_log(level, output_stream):\n"
        enable_log += "\thandler = logging.StreamHandler(output_stream)\n"
        enable_log += "\thandler.setLevel(level)\n"
        enable_log += "\tlogging.getLogger(\"neo4j\").addHandler(handler)\n"
        enable_log += "\tlogging.getLogger(\"neo4j\").setLevel(level)\n"

        close = ''
        close += "def close(self):\n"
        close += "\tself.driver.close()\n"

        show_res = ''
        show_res += "def show_result_function(self , result , msg):\n"
        show_res += "\tprint(msg)\n"
        show_res += "\tdata = [record.data() for record in result]\n"
        show_res += "\tdf = pd.DataFrame(data)\n"
        show_res += "\tprint(df)\n"

        init = ''
        init += "def __init__(self, uri, user, passwd, database):\n"
        init += "\tself.driver = GraphDatabase.driver(uri, auth=(user, passwd), database=database)\n"
        new_code = init + close + enable_log+ show_res + last_code + run_query
        return new_code

    def generate_settings(self ): 
        # ['"bolt://localhost:7687"', '"neo4j"', 'compiler@proj', 'Setting',    ///url username pass
        # DB_URL = "bolt://localhost:7687"  # "bolt://localhost:7687"  bolt://localhost:7687
        # USERNAME = "neo4j"
        # PASSWORD = "compiler@proj"
        # WORKING_DB = "dslcompiler"
        database = self.stack.pop()
        pwd = self.stack.pop()
        user = self.stack.pop()
        uri = self.stack.pop()
        
        result = (f"USERNAME = {user}\n"+
                    f"PASSWORD = \"{pwd}\"\n"+
                    f"DB_URL = {uri}\n"+
                    f"WORKING_DB = {database}\n")
        # self . temporary ??
        return result
    
    def load_terminal(self) :
        # c_path = "path"
        # t_path = "path"
        # tt_path = "path"
        path = self.stack.pop()
        path_str = f"t_path = {path}\n"
        setting = self.py_codes.pop()
        setting += path_str
        return setting

    def load_customer(self) : 
        # c_path = "path"
        # t_path = "path"
        # tt_path = "path"
        path = self.stack.pop()
        path_str = f"c_path = {path}\n"
        setting = self.py_codes.pop()
        setting += path_str
        return setting
    
    def load_transaction(self) : 
        # c_path = "path"
        # t_path = "path"
        # tt_path = "path"
        path = self.stack.pop()
        path_str = f"tt_path = {path}\n"
        setting = self.py_codes.pop()
        setting += path_str
        setting += ("DELETE_TX_CHUNK_SIZE = 1000\n" +
                    "WRITE_TX_CHUNK_SIZE = 1000\n"+
                    "UPDATE_TX_CHUNK_SIZE = 100")
        with open(self.proj_path+'\\'+"settings.py", 'w') as output_file:
            output_file.write(setting)
        return None
    
    def detect_customer(self ) : 
        #  '2003-02-12', '2004-02-12', '8', 
        #  'Detect_customer'
        self.queries[0] = 1 
        limit = self.stack.pop()
        end_date = self.stack.pop()
        start_date = self.stack.pop()
        result = ''
        result += "@timeit\n"
        result += f"def query_customer_payments(self, tx, start_date=\"{start_date}\", end_date=\"{end_date}\", limit={limit}):\n"
        result += "\t\"\"\"Handles first query of the project proposal\"\"\"\n"
        result += "\tquery = (\n"
        result += "\t\t\"MATCH (c:Customer)-[r:HAS_TX]->(tx:Transaction) \"\n"
        result += "\t\t'WHERE tx.date >= $start_date AND tx.date <= $end_date '\n"
        result += "\t\t\"RETURN c, sum(tx.amount), tx.date ORDER BY c, tx.date LIMIT $limit \"\n"
        result += "\t)\n"
        result += "\tresult = tx.run(query,\n"
        result += "\t\t\t\t\tstart_date=start_date,\n"
        result += "\t\t\t\t\tend_date=end_date,\n"
        result += "\t\t\t\t\tlimit=limit)\n"
        result += "\t# self.show_result(result, 'Result of customer daily payments: ')\n"
        result += "\tself.visualize_result_Query1(result)\n"
        result += "\treturn result\n"

        result += self.add_visulization_q1()
        last_code = self.py_codes.pop()
        if(last_code=="empty"):
            return result
        last_code += result 
        return last_code
            
    def add_visulization_q1(self) : 
        result = ''
        result += "def visualize_result_Query1(self, data):\n"
        result += "\tvisual_graph = Network()\n"
        result += "\tfor record in data:\n"
        result += "\t\tcustomer = record[0]\n"
        result += "\t\ttotal_amount = record[1]\n"
        result += "\t\tdate = record[2]\n"
        result += "\t\tcustomer_id = customer.id\n"
        result += "\t\tcustomer_name = f\"Customer {customer_id}\"\n"
        result += "\t\tvisual_graph.add_node(customer_id, customer_name, group=\"Customer\")\n"
        result += "\t\tvisual_graph.add_node(date, date, group=\"Date\")\n"
        result += "\t\tvisual_graph.add_edge(customer_id, date, title=f\"Total: {total_amount}\")\n"
        result += "\tvisual_graph.show('customer_payments_q1.html', notebook=False)\n"
        return result

    def detect_terminal(self):
        self.queries[1] = 1 
        limit = self.stack.pop()
        end_date = self.stack.pop()
        start_date = self.stack.pop()
        result = ''
        result += "@timeit\n"
        result += f"def query_terminal_fraud_transactions(self, tx, start_date=\"{start_date}\", end_date=\"{end_date}\", limit={limit}):\n"
        result += "\t\"\"\"Handles second query of the project proposal:\"\"\"\n"
        result += "\tquery = (\n"
        result += "\t\t'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '\n"
        result += "\t\t'WHERE date(tx.date) > date($start_date) - Duration({days: 30}) '\n"
        result += "\t\t'AND date(tx.date) < date($start_date) '\n"
        result += "\t\t'WITH t, avg(tx.amount) AS avg_tx '\n"
        result += "\t\t'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '\n"
        result += "\t\t'WHERE date(tx.date) > date($start_date) AND date(tx.date) < date($end_date) '\n"
        result += "\t\t'AND (avg_tx+(avg_tx/2)) < tx.amount '\n"
        result += "\t\t'RETURN t, count(tx), avg_tx LIMIT $limit'\n"
        result += "\t)\n"
        result += "\tresult = tx.run(query,\n"
        result += "\t\t\t\t\tstart_date=start_date,\n"
        result += "\t\t\t\t\tend_date=end_date,\n"
        result += "\t\t\t\t\tlimit=limit)\n"
        # result += "\tself.visualize_result_Query2(result)\n"
        result += "\tself.show_result_function( result ,\"result of Query2\")\n" #self.add_visualization_q2()
        result += "\treturn result\n"
        last_code = self.py_codes.pop()
        if (last_code == "empty"):
            return result
        last_code += result 
        return last_code

    # def add_visualization_q2(self):
    #     result = ''
    #     result += "def visualize_result_Query2(self, data):\n"
    #     result += "\tvisual_graph = Network()\n"
    #     result += "\ti = 0\n"
    #     result += "\tfor record in data:\n"
    #     result += "\t\tterminal = record[0]\n"
    #     result += "\t\ttx_count = record[1]\n"
    #     result += "\t\tavg_tx = record[2]\n"
    #     result += "\t\tterminal_id = terminal.id\n"
    #     result += "\t\tterminal_name = f\"Terminal {terminal_id}\"\n"
    #     result += "\t\tvisual_graph.add_node(terminal_id, label=terminal_name, group=\"Terminal\")\n"
    #     result += "\t\tvisual_graph.add_node(f\"AvgTx_{i}\", label=f\"AvgTx: {avg_tx:.2f}\", group=\"AverageTx\")\n"
    #     result += "\t\tvisual_graph.add_node(f\"Count_{i}\", label=f\"Count: {tx_count}\", group=\"TransactionCount\")\n"
    #     result += "\t\tvisual_graph.add_edge(terminal_id, f\"AvgTx_{i}\", title=f\"Average Transaction: {avg_tx:.2f}\")\n"
    #     result += "\t\tvisual_graph.add_edge(terminal_id, f\"Count_{i}\", title=f\"Suspicious Transactions: {tx_count}\")\n"
    #     result += "\t\ti += 1\n"
    #     result += "\tvisual_graph.show('terminal_fraud_transactions.html', notebook=False)\n"
    #     return result


    def detect_date_range(self): 
        self.queries[3] = 1 
        end_date = self.stack.pop()
        start_date = self.stack.pop()
        result = ''
        result += "@timeit\n"
        result += f"def query_transactions_of_each_period(self, tx, start_date=\"{start_date}\", end_date=\"{end_date}\"):\n"
        result += "\t\"\"\"Handles fourth query of the project proposal:\"\"\"\n"
        result += "\tquery = (\n"
        result += "\t\t'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '\n"
        result += "\t\t'WHERE date(tx.date) > date($start_date) - Duration({days: 30}) '\n"
        result += "\t\t'AND date(tx.date) < date($start_date) '\n"
        result += "\t\t'WITH t, avg(tx.amount) AS avg_tx '\n"
        result += "\t\t'MATCH (t:Terminal)<-[:PAYED_TO]-(tx:Transaction) '\n"
        result += "\t\t'WHERE date(tx.date) > date($start_date) AND date(tx.date) < date($end_date) '\n"
        result += "\t\t'AND (avg_tx + (avg_tx/2)) < tx.amount '\n"
        result += "\t\t'WITH tx.tx_period AS p, count(tx) AS ctx '\n"
        result += "\t\t'MATCH (tx:Transaction) where tx.tx_period = p '\n"
        result += "\t\t'RETURN p, ctx, count(tx)'\n"
        result += "\t)\n"
        result += "\tresult = tx.run(query, start_date=start_date, end_date=end_date)\n"
        # result += "\t# self.show_result(result, 'Result of transactions and fraud transactions for each period: ')\n"
        result += "\tself.show_result_function( result ,\"result of Query4\")\n"
        result += "\treturn result\n"
        last_code = self.py_codes.pop()
        if (last_code == "empty"):
            return result
        last_code += result 
        return last_code
        
    # def add_visulization_q4(self):
    #     result = ''
    #     result += "def visualize_result_Query4(self, data):\n"
    #     result += "\tvisual_graph = Network(height=\"1000px\", width=\"100%\", notebook=False, directed=True)\n"
    #     result += "\t# Define color for each group\n"
    #     result += "\tcolor_map = {\n"
    #     result += "\t\t\"Terminal\": \"#99ccff\",   # Light blue\n"
    #     result += "\t\t\"Transaction\": \"#99ff99\" # Light green\n"
    #     result += "\t}\n"
    #     result += "\t\n"
    #     result += "\t# Dictionary to store node IDs based on transaction periods\n"
    #     result += "\tperiod_nodes = {}\n"
    #     result += "\t\n"
    #     result += "\tfor record in data:\n"
    #     result += "\t\tperiod = record['p']\n"
    #     result += "\t\tcount_ctx = record['ctx']\n"
    #     result += "\t\tcount_tx = record['count(tx)']\n"
    #     result += "\t\t\n"
    #     result += "\t\tif period not in period_nodes:\n"
    #     result += "\t\t\tperiod_nodes[period] = visual_graph.add_node(period, label=f\"Period: {period}\", group=\"Transaction\")\n"
    #     result += "\t\t\n"
    #     result += "\t\tcount_ctx_node = visual_graph.add_node(f\"ctx_{period}\", label=f\"Fraud Transactions: {count_ctx}\", group=\"Transaction\")\n"
    #     result += "\t\tcount_tx_node = visual_graph.add_node(f\"count_tx_{period}\", label=f\"Total Transactions: {count_tx}\", group=\"Transaction\")\n"
    #     result += "\t\t\n"
    #     result += "\t\tvisual_graph.add_edge(period, f\"ctx_{period}\", title=\"Fraud Transactions\")\n"
    #     result += "\t\tvisual_graph.add_edge(period, f\"count_tx_{period}\", title=\"Total Transactions\")\n"
    #     result += "\t\n"
    #     result += "\tvisual_graph.show('transactions_of_each_period.html', notebook=False)\n"
    #     return result


    def detect_degree_limit(self):
        self.queries[2] = 1 
        limit = self.stack.pop()
        degree = self.stack.pop()
        result = ''
        result += "@timeit\n"
        result += f"def query_cc_relationship_with_degree(self, tx, k={degree}, limit={limit}):\n"
        result += "\t\"\"\"Handles third query of the project proposal:\"\"\"\n"
        result += "\tn = (k * 4) + 4\n"
        result += "\tquery = (\n"
        result += "\t\tf\"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) \\n\"\n"
        result += "\t\tf\"RETURN path \\n\"\n"
        result += "\t\tf\"LIMIT $limit\"\n"
        result += "\t)\n"
        result += "\tresult = tx.run(query, limit=limit)\n"
        # result += "\t# self.show_result(result, f'Result of Co-Customer relationship with degree {{k}}: ')\n"
        result += "\tself.visualize_result_Query3(result)\n"
        result += "\tquery = (\n"
        result += "\t\tf\"MATCH path=(c1:Customer)-[*{n}]-(c2:Customer) \\n\"\n"
        result += "\t\tf\"RETURN c1, c2\\n\"\n"
        result += "\t\tf\"LIMIT $limit\"\n"
        result += "\t)\n"
        result += "\tresult = tx.run(query, limit=limit)\n"
        result += "\tself.show_result_function( result ,\"result of Query3\")\n"
        result += "\treturn result\n"

        result += self.add_visualization_q3()
        last_code = self.py_codes.pop()
        if (last_code == "empty"):
            return result
        last_code += result 
        return last_code

    def add_visualization_q3(self):
        result = ''
        result += "def visualize_result_Query3(self, data):\n"
        result += "\tvisual_graph = Network()\n"
        result += "\t# Define color for each group\n"
        result += "\tcolor_map = {\n"
        result += "\t\t\"Customer\": \"#ff9999\",  # Light red\n"
        result += "\t\t\"Terminal\": \"#99ccff\",  # Light blue\n"
        result += "\t\t\"Transaction\": \"#99ff99\"  # Light green\n"
        result += "\t}\n\n"
        result += "\tfor record in data:\n"
        result += "\t\tpath = record['path']\n"
        result += "\t\tnodes = path.nodes\n"
        result += "\t\trelationships = path.relationships\n\n"
        result += "\t\tstart_node_id = nodes[0].id  # Assuming nodes[0] is the start node\n"
        result += "\t\tend_node_id = nodes[-1].id   # Assuming nodes[-1] is the end node\n\n"
        result += "\t\tfor node in nodes:\n"
        result += "\t\t\tnode_id = node.id\n"
        result += "\t\t\tnode_labels = node.labels\n"
        result += "\t\t\tnode_label = next(iter(node_labels))  # Assuming single label per node\n"
        result += "\t\t\t# Determine the group based on the label\n"
        result += "\t\t\tif 'Customer' in node_labels:\n"
        result += "\t\t\t\tgroup = \"Customer\"\n"
        result += "\t\t\t\tnode_label = f\"Customer {node['id']}\"\n"
        result += "\t\t\telif 'Terminal' in node_labels:\n"
        result += "\t\t\t\tgroup = \"Terminal\"\n"
        result += "\t\t\t\tnode_label = f\"Terminal {node['id']}\"\n"
        result += "\t\t\telif 'Transaction' in node_labels:\n"
        result += "\t\t\t\tgroup = \"Transaction\"\n"
        result += "\t\t\t\tnode_label = f\"Transaction {node['id']}\"\n"
        result += "\t\t\telse:\n"
        result += "\t\t\t\tgroup = \"Other\"\n"
        result += "\t\t\t\tcolor_map[group] = \"#cccccc\"  # Default color for other nodes\n"
        result += "\t\t\t# Bold the start and end nodes\n"
        result += "\t\t\tif node_id == start_node_id:\n"
        result += "\t\t\t\tvisual_graph.add_node(node_id, label=node_label, color=color_map[group], size=30, borderWidth=5)\n"
        result += "\t\t\telif node_id == end_node_id:\n"
        result += "\t\t\t\tvisual_graph.add_node(node_id, label=node_label, color=color_map[group], size=30, borderWidth=5)\n"
        result += "\t\t\telse:\n"
        result += "\t\t\t\tvisual_graph.add_node(node_id, label=node_label, color=color_map[group])\n\n"
        result += "\t\tfor rel in relationships:\n"
        result += "\t\t\tstart_node = rel.start_node.id\n"
        result += "\t\t\tend_node = rel.end_node.id\n"
        result += "\t\t\trel_type = rel.type\n"
        result += "\t\t\tvisual_graph.add_edge(start_node, end_node, title=rel_type)\n\n"
        result += "\tvisual_graph.show('customer_relationships.html', notebook=False)\n"
        return result
    
    def is_operator(self , item ) : 
        if item in self.operator : 
            return True 
        return False 
    
    def generate_intermediate_language(self, post_order_array):
        for item in post_order_array:
            if self.is_operator(item):
                outt = self.generate_py_based_on_operator(item)
                if outt != None : 
                    self.py_codes.append(outt)
                else:
                    self.py_codes.append("empty")
            else:
                self.stack.append(item)

        result = ''
        for string in self.py_codes:
            if string is not None:
                result += string

        with open(os.path.join(self.proj_path ,"main.py"), "w") as my_file:
            my_file.write(result)
            
        return result

    