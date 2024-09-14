from database import get_db_connection

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE EXTENSION IF NOT EXISTS vector;
        CREATE TABLE IF NOT EXISTS pictures (
            picture text PRIMARY KEY,
            embedding vector(768),
            similarity NUMERIC(17,16),
            id INT
        );
    """)
    conn.commit()
    cur.close()
