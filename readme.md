User Manual:
The application has been written to run from the command line.

After downloading the image you are going to need to mount 3 volumes in order for the application to function correctly:

1 - A folder where you will place the images you wish to add to the database (eg. 'images')

2 - A folder where you will place a single reference image when you want to add a new person or update an existing one in the database (eg. 'reference_image') 

3 - A config.json file which you will use to alter the settings and give the program nessecary information

Example of how to do this (after the image has been pulled):

> docker run -d \
> -- name <name> \
> -v /home/<user>/local_variables/images:/app/local_variables/images \
> -v /home/<user>/local_variables/reference_image:/app/local_variables/reference_image \
> -v /home/<user>/local_variables/config.json:/app/config.json \
> facial_recognition


You are also going to need to make a free aiven.io account and then create a PostgreSQL service with a free trial. The video linked at the bottom also explains how to do this if you need any help.


Comments:

Make sure your images are also stored somwhere outside these directories as they will be cleared after the images have served their purpose.

The folders in the local_variables directory have .foo files in them. This is only to allow them to be added to this repository they are in no way needed for the functioning of the app.

Try to avoid uploading the same images multiple times, although is shouldn't really cause issues.


After this you are ready to run the app:

> python app.py --config /app/config.json


If you are just running the app directly in the code editor of your choice make sure to check 'requirements.txt' if you have all the nesseccary dependencies installed.
You will also need 'libgl1' and 'libgl1-mesa-glx'.
Also make sure to alter the 'base path' in the config file as well as the haarcascade_frontalface_default path in the main app.



Thanks to Aiven and their tutorial for making this project possible: https://aiven.io/developer/find-faces-with-pgvector?utm_source=youtube&utm_medium=referral&utm_content=MatthewBerman&utm_campaign=imp

Credit to Matthew Berman for his video: https://www.youtube.com/watch?v=Y0dLgtF4IHM&t=293s&ab_channel=MatthewBerman

Thank you to the creators of the haarcascade_frontalface_default algorith as well. 
