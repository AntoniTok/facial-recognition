import argparse
import json
import os
import re
import person
import storage
import embeddings
import faces
import identity
from erase import clear_folder
import table

def main():
    parser = argparse.ArgumentParser(description="Run the facial recognition app.")
    parser.add_argument('--config', required=True, help='Path to the configuration file')

    args = parser.parse_args()

    with open(args.config, 'r') as config_file:
        config = json.load(config_file)

    base_path = config['base_path']
    images_folder = os.path.join(base_path, 'images')
    faces_folder = os.path.join(base_path, 'faces')
    haarcascade_path = os.path.join(base_path, 'haarcascade_frontalface_default/haarcascade_frontalface_default.xml')
    people_file = os.path.join(base_path, 'people')
    reference_face_folder = os.path.join(base_path, 'reference_face')
    reference_image_folder = os.path.join(base_path, 'reference_image')

    print("What do you want to do:")
    print("1 - Create the pictures table in the database (you need to do this first, once, if you haven't already)")
    print("2 - Process images and upload embeddings")
    print("3 - Assign a new person to, or update a profile in the database")
    print("4 - Search for images by name")
    print("5 - Delete a person from the database")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        table.create_table()
        print("Table created successfully.")
        
    elif choice == '2':
        faces.find_faces(images_folder, faces_folder, haarcascade_path)
        embeddings.upload_face_embeddings(faces_folder)
        clear_folder(faces_folder)
        clear_folder(images_folder)
        print("Images processed and embeddings uploaded successfully.")
        
    elif choice == '3':
        file_existance = os.path.exists(people_file)
        
        while True:
            input_name = input("Enter the name of the person you wish to create / update: ")
            if not re.match(r'^[a-zA-Z\s\-\.,!?]+$', input_name):
                print("Invalid input. Please enter a valid string.")
            else:
                creation_name = input_name.lower()
                break
            
        match file_existance:
            case True:
                profiles = storage.load_persons(people_file)
                
                if person.person_exists(creation_name, profiles):
                    update = input("A profile with the same name already exists. Do you want to update it? (y/n): ")
                    if update.lower() == 'y':
                        faces.reference_face(reference_image_folder, reference_face_folder, haarcascade_path)
                        string_representation = embeddings.create_embedding_string(os.path.join(reference_face_folder, config['image_name']))
                        identity.assign_identity(creation_name, profiles, string_representation, config['threshold'])
                        clear_folder(reference_image_folder)
                        clear_folder(reference_face_folder)
                        print("Identity updated successfully.")
                    else:
                        print("Operation cancelled.")
                
                else:
                    profile = person.create_person(creation_name)
                    profiles[profile.name] = profile.id
                    storage.save_persons(profiles, people_file)
                    faces.reference_face(reference_image_folder, reference_face_folder, haarcascade_path)
                    string_representation = embeddings.create_embedding_string(os.path.join(reference_face_folder, config['image_name']))
                    identity.assign_identity(creation_name, profiles, string_representation, config['threshold'])
                    clear_folder(reference_image_folder)
                    clear_folder(reference_face_folder)
                    print("Person instance created and identity assigned successfully.")
                    
            case False:
                profiles = {}
                profile = person.create_person(creation_name)
                profiles[profile.name] = profile.id
                storage.save_persons(profiles, people_file)
                profiles = storage.load_persons(people_file)
                faces.reference_face(reference_image_folder, reference_face_folder, haarcascade_path)
                string_representation = embeddings.create_embedding_string(os.path.join(reference_face_folder, config['image_name']))
                identity.assign_identity(creation_name, profiles, string_representation, config['threshold'])
                clear_folder(reference_image_folder)
                clear_folder(reference_face_folder)
                print("Person instance created and identity assigned successfully.")
                
        
    elif choice == '4':
        search_name = input("Enter the name of the person you wish to search for: ")
        profiles = storage.load_persons(people_file)
        
        if person.person_exists(search_name, profiles):
            results = identity.search_by_name(search_name, profiles)
            seen = set()
            
            for pic in results:
                parts = pic.rsplit('_', 1)
                original = parts[0]
                
                if original not in seen:
                    seen.add(original)
                    print(original)
            
        else:
            print("Name not recognized. Please try again.")
                
    elif choice == '5':
        profiles = storage.load_persons(people_file)
        deletion_name = input("Enter the name of the person you wish to delete: ").lower()
        if person.person_exists(deletion_name, profiles):
            target_id = person.get_person_id(deletion_name, profiles)
            identity.clear_id_and_sim(target_id)
            del profiles[deletion_name]
            storage.save_persons(profiles, people_file)
            print("Person deleted successfully.")
        else:
            print("Name not recognized. Please try again.")
            
    else:
        print("Invalid choice. Please run the script again and choose a valid option.")

if __name__ == "__main__":
    main()
