import psycopg2
import json
import os

def get_db_connection():
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
        URL = config['URL']
    conn = psycopg2.connect(
        os.getenv("DATABASE_URL", URL)
    )
    return conn
