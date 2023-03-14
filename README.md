# Feeder Backend

## In a Nutshell
"Feeder" is a webapplication that allows users to post, edit, and delete feeds. The app also offers the ability to post, edit, and delete comments on the feeds. With Feeder, users can share their thoughts and opinions, receive feedback from other users, and connect with others. The user interface is user-friendly and easy to navigate.

## Technologies
### Django
"Feeder" was developed using the Django technology. Django is a popular web framework that is widely used for building high-quality web applications quickly and efficiently. It provides a powerful and secure infrastructure for developing complex applications, and it is known for its scalability and flexibility. With Django, developers can easily create web applications with clean and maintainable code, making it a popular choice for building web applications. The use of Django in the development of "Feeder" ensures that the app is reliable, secure, and easy to maintain.


## Functionalities & Permissions
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
- Can change roles and influence other users except administrators
