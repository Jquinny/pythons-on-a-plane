import pygame
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCeenNw5LLxwKzSIrIBllcBtShWrw2KeS4",
  'databaseURL': 'https://pythons-on-a-plane-default-rtdb.firebaseio.com/',
  'authDomain': "pythons-on-a-plane.firebaseapp.com",
  'projectId': "pythons-on-a-plane",
  'storageBucket': "pythons-on-a-plane.appspot.com",
  'messagingSenderId': "216316196816",
  'appId': "1:216316196816:web:5c80882ca271baebf2ebd5",
  'measurementId': "G-SYX921C8GG"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def addScore(username, score): 
    db.child('users').child(username).update({'score': score})

def retrieveLeaderboard():
    leaderboard = []
    users_by_score = db.child('users').order_by_child('score').get()

    for person in users_by_score.each():
        leaderboard.append(person)  

    leaderboard = leaderboard.reverse()[:4]
    return leaderboard