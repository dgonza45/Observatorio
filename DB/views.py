from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyApRDFW_LWlmChdsxpvDO7sRkR8Z7O6Bvc",
    "authDomain": "observatorio-4444b.firebaseapp.com",
    "databaseURL": "https://observatorio-4444b-default-rtdb.firebaseio.com",
    "storageBucket": "observatorio-4444b.appspot.com",
}

# here we are doing firebase authentication
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()


def index(request):
    # accessing our firebase data and storing it in a variable
    dato = "nuevo2Smith"
    name = database.child('Data').child('Name').get().val()
    stack = database.child('Data').child('Stack').get().val()
    framework = database.child('Data').child('Framework').get().val()
    database.child('Data').child("nuevo2").set(dato)

    context = {
        'name': name,
        'stack': stack,
        'framework': framework
    }
    return render(request, 'index.html', context)
