from os.path import join

DB_URL = "bolt://localhost:7687"  # "bolt://localhost:7687"  bolt://localhost:7687
USERNAME = "neo4j"
PASSWORD = "compiler@proj"

DB50 = "db50"
DB100 = "db100"
DB200 = "db200"
WORKING_DB = "dslcompiler"

DATA_FOLDER = "data"
DATA_FOLDER_50_MB = join(DATA_FOLDER, '50_mb')
DATA_FOLDER_100_MB = join(DATA_FOLDER, '100_mb')
DATA_FOLDER_200_MB = join(DATA_FOLDER, '200_mb')
DATA_100 = join(DATA_FOLDER , 'test_db')
DELETE_TX_CHUNK_SIZE = 1000
WRITE_TX_CHUNK_SIZE = 1000
UPDATE_TX_CHUNK_SIZE = 100
LOADER_DATA_FOLDER = DATA_100
