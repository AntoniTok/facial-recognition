User Manual:
The application has been written to run from the command line.

First download the image using docker or if you wish to run everything from your code editor follow the instructions at the bottom of the page:

> docker pull antonitokarski/facial-recognition:latest

After downloading the image you are going to need to create 3 files on your device and mount them as volumes in order for the application to function correctly:

1 - A folder where you will place the images you wish to add to the database (eg. 'images')

2 - A folder where you will place a single reference image when you want to add a new person or update an existing one in the database (eg. 'reference_image') 

3 - A config.json file which you will use to alter the settings and give the program nessecary information (the name of the reference image and your Aiven URI)

Example of how to do this (after the image has been pulled):

> docker run -d \\
 
> -- name example_name \\
 
> -v /home/example_user/local_variables/images:/app/local_variables/images \\
 
> -v /home/example_user/local_variables/reference_image:/app/local_variables/reference_image \\
 
> -v /home/example_user/local_variables/config.json:/app/config.json \\
 
> facial_recognition


You are also going to need to make a free aiven.io account and then create a PostgreSQL service with a free trial. The video linked at the bottom also explains how to do this if you need any help.


Comments:

Make sure your images are also stored somwhere outside these directories as they will be cleared after the images have served their purpose.

For creating the config.json file just use the one in this repository.

The folders in the local_variables directory have .foo files in them you can get rid of them if you download the file from this repository, they are not present in the docker image. This is only to allow them to be added to this repository they are in no way needed for the functioning of the app.

Try to avoid uploading the same images multiple times, although is shouldn't really cause issues.


After this you are ready to run the app:

> python app.py --config /app/config.json


If you are just running the app directly in the code editor of your choice make sure to check 'requirements.txt' if you have all the nesseccary dependencies installed.
You will also need 'libgl1' and 'libgl1-mesa-glx'.
Also make sure to alter the 'base path' in the config file as well as the haarcascade_frontalface_default path in the main app.
For uploading all your images to the database use the /local_variables/images folder, and for creating profiles, place a single portrait image in /local_variables/reference_image folder.



Thanks to Aiven for making this project possible: https://aiven.io/developer/find-faces-with-pgvector?utm_source=youtube&utm_medium=referral&utm_content=MatthewBerman&utm_campaign=imp

Credit to Matthew Berman for his video: https://www.youtube.com/watch?v=Y0dLgtF4IHM&t=293s&ab_channel=MatthewBerman

Thank you to the creators of the haarcascade_frontalface_default algorith as well. 
