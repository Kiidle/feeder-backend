# Feeder Backend

## In a Nutshell
"Feeder" is a webapplication that allows users to post, edit, and delete feeds. The app also offers the ability to post, edit, and delete comments on the feeds. With Feeder, users can share their thoughts and opinions, receive feedback from other users, and connect with others. The user interface is user-friendly and easy to navigate.

## Technologies
### Django
"Feeder" was developed using the Django technology. Django is a popular web framework that is widely used for building high-quality web applications quickly and efficiently. It provides a powerful and secure infrastructure for developing complex applications, and it is known for its scalability and flexibility. With Django, developers can easily create web applications with clean and maintainable code, making it a popular choice for building web applications. The use of Django in the development of "Feeder" ensures that the app is reliable, secure, and easy to maintain.


## Permissions
**Anonym User**
- No Permission

**Default User**
- Can read other feeds
- Can create Feeds
- Can update and delete own Feeds
- Can create Commentaries
- Can update and delete own Commentaries

**Verified User**
- All Default User Permissions
- Can create Feeds + can use more than 200 characters
- Can create Commentaries + can use more than 200 characters

**Moderator**
- All Verified User Permissions
- Can update and delete other Feeds
- Can update and delete other Commentaries
- Can warn verified and default users

**Admin**
- All Moderator Permissions
- Can verify and unverify other users
- Can give and remove moderator role to other users

## Setup
### Python
1. Visit the official Python website: https://www.python.org/downloads/
2. Scroll down to the "Stable Releases" section and select the latest version of Python 3 available for your operating system.
3. Click on the appropriate download link to download the installation package.
4. Open the downloaded installation package.
5. Select the "Install Python 3.x" option and click "Next".
6. Choose the destination directory for the installation (the default path should be fine) and click "Next".
7. Select the components you want to install. For starters, we recommend selecting all options. Click "Next".
8. Select "Add Python 3.x to PATH" and click "Install". This option adds Python to the path so you can call Python from the command line.
9. Wait for the installation to complete.
10. Check that Python was installed correctly by opening the command prompt and typing ```python --version```. The current version of Python you installed should be displayed.

Congratulations! You have successfully installed Python 3 on your computer. You are now ready to write and execute Python programs.
### Django
1. Make sure you have Python 3.x installed. If not, please follow the previous guide on how to install Python 3.x.
2. Open the command prompt or terminal.
3. Type the command ```pip install Django``` and press Enter.
4. Wait for the installation to complete. The installation process should automatically install all necessary dependencies.
5. Check that Django was installed correctly by typing the command "django-admin --version" in the command prompt or terminal. If Django was installed, the current version of Django should be displayed.

Congratulations! You have successfully installed Django on your computer. You are now ready to create and develop a new Django web application.

### Project
#### Clone using SSH
1. Open your command prompt or terminal.
2. Generate an SSH key by typing the command "ssh-keygen -t rsa" and following the prompts.
3. Log in to your GitHub account and navigate to the project you want to clone.
4. Click on the "Clone or download" button and select "Use SSH" in the top right corner of the pop-up.
5. Copy the SSH URL provided.
6. In the command prompt or terminal, navigate to the directory where you want to clone the project.
7. Type the command ```git clone git@github.com:Kiidle/feeder-backend.git``` and press Enter.
8. Wait for the project to be cloned.
#### Clone using HTTPS
1. Open your command prompt or terminal.
2. Log in to your GitHub account and navigate to the project you want to clone.
3. Click on the "Clone or download" button and select "Use HTTPS" in the top right corner of the pop-up.
4. Copy the HTTPS URL provided.
5. In the command prompt or terminal, navigate to the directory where you want to clone the project.
6. Type the command ```git clone https://github.com/Kiidle/feeder-backend.git``` and press Enter.
7. Wait for the project to be cloned.
#### Run
1. Open your command prompt or terminal.
2. Navigate to the directory where the cloned project is located using the "cd" command.
3. Once you are in the project's directory, you should see a file called "manage.py". This file is responsible for managing the Django project.
4. Type the command ```python manage.py runserver``` and press Enter.
5. Wait for the server to start up.
6. Once the server is up and running, open your web browser and type "http://localhost:8000" in the address bar.
7. If everything was set up correctly, you should see the project.
