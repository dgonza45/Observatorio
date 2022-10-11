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
    return render(request, 'index.html')

def donaciones(request):
    return render(request, 'donaciones.html')


def vih(request):
    context = getfromdb('vih')
    return render(request, 'vih.html', context)
def mapa_vih(request):
    return render(request, 'mapa_vih.html')

def parotiditis(request):
    context = getfromdb('parotiditis')
    return render(request, 'parotiditis.html', context)
def mapa_parotiditis(request):
    return render(request, 'mapa_parotiditis.html')

def hepatitisa(request):
    context = getfromdb('hepatitisa')
    return render(request, 'hepatitisa.html', context)
def mapa_hepatitisa(request):
    return render(request, 'mapa_hepatitisa.html')

def hepatitisc(request):
    context = getfromdb('hepatitisc')
    return render(request, 'hepatitisc.html', context)
def mapa_hepatitisc(request):
    return render(request, 'mapa_hepatitisc.html')

def dengue(request):
    context = getfromdb('dengue')
    return render(request, 'dengue.html', context)
def mapa_dengue(request):
    return render(request, 'mapa_dengue.html')

def cancerDeMama(request):
    context = getfromdb('cancerDeMama')
    return render(request, 'cancerDeMama.html', context)
def mapa_cancerDeMama(request):
    return render(request, 'mapa_cancerDeMama.html')

def intentoSuicidio(request):
    context = getfromdb('intentoSuicidio')
    return render(request, 'intentoSuicidio.html', context)
def mapa_intentoSuicidio(request):
    return render(request, 'mapa_intentoSuicidio.html')

def getfromdb(enfermedad):
    casosxano2015 = database.child(enfermedad).child('CasosXano').child('2015').get().val()
    casosxano2016 = database.child(enfermedad).child('CasosXano').child('2016').get().val()
    casosxano2017 = database.child(enfermedad).child('CasosXano').child('2017').get().val()
    casosxano2018 = database.child(enfermedad).child('CasosXano').child('2018').get().val()
    casosxano2019 = database.child(enfermedad).child('CasosXano').child('2019').get().val()
    casosxano2020 = database.child(enfermedad).child('CasosXano').child('2020').get().val()
    casosxano2021 = database.child(enfermedad).child('CasosXano').child('2021').get().val()
    casosxano2022 = database.child(enfermedad).child('CasosXano').child('2022').get().val()
    casosxano2023 = database.child(enfermedad).child('CasosXano').child('2023').get().val()
    casosxano2024 = database.child(enfermedad).child('CasosXano').child('2024').get().val()
    casosmujer = database.child(enfermedad).child('CasosXsexo').child('F').get().val()
    casoshombre = database.child(enfermedad).child('CasosXsexo').child('M').get().val()
    casosxedad5 = database.child(enfermedad).child('CasosXedad').child('0-5').get().val()
    casosxedad11 = database.child(enfermedad).child('CasosXedad').child('6-11').get().val()
    casosxedad18 = database.child(enfermedad).child('CasosXedad').child('12-18').get().val()
    casosxedad26 = database.child(enfermedad).child('CasosXedad').child('19-26').get().val()
    casosxedad59 = database.child(enfermedad).child('CasosXedad').child('27-59').get().val()
    casosxedad100 = database.child(enfermedad).child('CasosXedad').child('60-100').get().val()
    context = {
        'casosxano2015': casosxano2015,
        'casosxano2016': casosxano2016,
        'casosxano2017': casosxano2017,
        'casosxano2018': casosxano2018,
        'casosxano2019': casosxano2019,
        'casosxano2020': casosxano2020,
        'casosxano2021': casosxano2021,
        'casosxano2022': casosxano2022,
        'casosxano2023': casosxano2023,
        'casosxano2024': casosxano2024,
        'casosmujer' : casosmujer,
        'casoshombre' : casoshombre,
        'casosxedad5' : casosxedad5,
        'casosxedad11' : casosxedad11,
        'casosxedad18' : casosxedad18,
        'casosxedad26' : casosxedad26,
        'casosxedad59' : casosxedad59,
        'casosxedad100' : casosxedad100,
    }
    return context