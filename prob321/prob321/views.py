from django.shortcuts import render
import pyrebase

firebaseConfig = {
    'apiKey': "", //paste api key
    'authDomain': "mock-321.firebaseapp.com",
    'databaseURL': "https://mock-321.firebaseio.com",
    'projectId': "mock-321",
    'storageBucket': "mock-321.appspot.com",
    'messagingSenderId': "320939381703",
    'appId': "1:320939381703:web:5093b55c011d2e5ab4ffe2",
    'measurementId': "G-YJ2HKZXDV1"
  }
  firebase = pyrebase.initialize_app(config)
