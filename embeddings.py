from imgbeddings import imgbeddings
from PIL import Image
import os
from database import get_db_connection

def upload_face_embeddings(folder):
    conn = get_db_connection()
    cur = conn.cursor()
    for filename in os.listdir(f"{folder}"):
        # opening the image
        img = Image.open(f"{folder}/" + filename)
        # loading the `imgbeddings`
        ibed = imgbeddings()
        # calculating the embeddings
        embedding = ibed.to_embeddings(img)
        cur = conn.cursor()
        cur.execute("INSERT INTO pictures values (%s,%s)", (filename, embedding[0].tolist()))
        print(filename)
    conn.commit()
    cur.close()
    conn.close()
    
def create_embedding_string(file_path):
    img = Image.open(file_path)
    ibed = imgbeddings()
    embedding = ibed.to_embeddings(img)
    string_representation = "["+ ",".join(str(x) for x in embedding[0].tolist()) +"]"
    #print(string_representation)
    return string_representation
