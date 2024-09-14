import cv2
import os

def find_faces(folder, target, algorithm):
    alg = algorithm
    haar_cascade = cv2.CascadeClassifier(alg)
    for file in os.listdir(folder):
        # Check if the file is an image 
        if file.endswith(('.jpg', '.jpeg', '.png')):
            # create the image path
            image_path = os.path.join(folder, file)
            # reading the image
            img = cv2.imread(image_path, 0)
            # creating a black and white version of the image
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # detecting the faces
            faces = haar_cascade.detectMultiScale(
                gray_img, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100)
            )
            # Now we store the faces
            i = 0
            for x, y, w, h in faces:
                # crop the image to select only the face
                cropped_image = img[y : y + h, x : x + w]
                # loading the target image path into target variable
                target_file_name = (f'{target}/' + str(os.path.splitext(file)[0]) + '_' + str(i) + '.jpg')
                cv2.imwrite(
                    target_file_name,
                    cropped_image,
                )
                i += 1
                

def reference_face(folder, target, algorithm):
    alg = algorithm
    haar_cascade = cv2.CascadeClassifier(alg)
    for file in os.listdir(folder):
        # Check if the file is an image 
        if file.endswith(('.jpg', '.jpeg', '.png')):
            # create the image path
            image_path = os.path.join(folder, file)
            # reading the image
            img = cv2.imread(image_path, 0)
            # creating a black and white version of the image
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # detecting the faces
            faces = haar_cascade.detectMultiScale(
                gray_img, scaleFactor=1.05, minNeighbors=0, minSize=(100, 100)
            )
            for x, y, w, h in faces:
                # crop the image to select only the face
                cropped_image = img[y : y + h, x : x + w]
                # loading the target image path into target_file_name variable
                target_file_name = (f'{target}/' + str(os.path.splitext(file)[0]) + '.jpg')
                cv2.imwrite(
                    target_file_name,
                    cropped_image,
                )
