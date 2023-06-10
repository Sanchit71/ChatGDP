# ChatGDP
## Introduction
ChatGDP(Chat Group Discussion Program) is free and simple to use video calling tool. It allows the user to create a room with personalised names. The other users can join the same room, if same room name is provided. 
Maximum 10 members are allowed in a room.

## Key Features
#### The user can :
- mute his audio
- close the video 
- leave the room.
- create a personalised room

## Tech Stack
- HTML, CSS and JS for Frontend
- Django for Backend
- Sqlite for Database Storage

## How to Use
#### 1 - Clone the repository
#### 2 - Install the requirements
#### 3 - Update Agora Credentials
In order to use this project you will need to replace the agora credentials in views.py and streams.js.
Create an account at agora.io and create an app. Once you create your app, you will want to copy the appid & appCertificate to update views.py and streams.js.
#### 4 - Run the server