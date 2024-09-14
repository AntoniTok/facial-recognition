import person
from database import get_db_connection

conn = get_db_connection()
cur = conn.cursor()
# print(type(conn))

# Calculate scores and order by the similarity + Iterate over the values and update the table
def assign_identity(name, people, string_representation, threshold):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            WITH similarity_scores AS (
                SELECT
                    picture,
                    1 - (embedding <=> %s::vector) AS cosine_similarity
                FROM pictures
            )
            SELECT *
            FROM similarity_scores
            WHERE cosine_similarity >= %s
            ORDER BY cosine_similarity DESC;
        """, (string_representation, threshold))
        #print('similarity scores calculated')
        rows = cur.fetchall()    
    except Exception as e:
        print(f"An error occurred 1: {str(e)}")

    for row in rows:
        pic = row[0]
        similarity = row[1]
        id = person.get_person_id(name, people)
        try:
            cur.execute("""
                UPDATE pictures
                SET similarity = CASE
                    WHEN similarity IS NULL THEN %s
                    WHEN similarity <= %s THEN %s
                    ELSE similarity
                END,
                id = CASE
                    WHEN similarity IS NULL THEN %s
                    WHEN similarity <= %s THEN %s
                    ELSE id
                END
                WHERE picture = %s
            """, (similarity, similarity, similarity, id, similarity, id, pic))
            conn.commit()
            #print('identity assigned')
        except Exception as e:
            print(f"An error occurred 2: {str(e)}")
    
    cur.close()
    conn.close()
            

# Return a list of image names that correspond to the name of the person         
def search_by_name(name, profiles):
    conn = get_db_connection()
    cur = conn.cursor()
    identity = person.get_person_id(name, profiles)
    if identity == None:
        print('No such person found')
        return []
    try: 
        cur.execute(f"""
                SELECT picture
                FROM pictures
                WHERE id = {identity}
            """)
        images = cur.fetchall()
        return [image[0] for image in images]
    except Exception as e:
        print(f"An error occurred 3: {str(e)}")
        return []
    finally:
        cur.close()
        conn.close()
    

def clear_id_and_sim(provided_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"""
            UPDATE pictures
            SET id = NULL,
                similarity = NULL
            WHERE id = {provided_id}
        """)
        conn.commit()
    except Exception as e:
        print(f"An error occurred 4: {str(e)}")
    finally:
        cur.close()
        conn.close()
        
        
cur.close()