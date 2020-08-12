from django.shortcuts import render
from pyrebase import pyrebase


config = {
    'apiKey': "AIzaSyB0pIVHUVAJRrGLX25gnXEy6wkB7NLHUPI",
    'authDomain': "mock321-b0dd8.firebaseapp.com",
    'databaseURL': "https://mock321-b0dd8.firebaseio.com",
    'projectId': "mock321-b0dd8",
    'storageBucket': "mock321-b0dd8.appspot.com",
    'messagingSenderId': "625033989145",
    'appId': "1:625033989145:web:2f7391832adb4249582e88",
    'measurementId': "G-ZT0CS5PX06"
  }

firebase = pyrebase.initialize_app(config)

database = firebase.database()

def index(request):
    db = database.child('schools').child('abc').get().val()
    ret={}
    for i in db["grade1"].keys():
        ret[i]=db["grade1"][i]['highTech']

    print(ret)
    return render(request,'index.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'thrus_h': ret['thursday']})

def update(request):
    from datetime import date
    import calendar

    x=list(map(int,str(date.today()).split('-')))
    y=calendar.day_name[date(x[0],x[1],x[2]).weekday()].lower()
    print(y)
    

    item = y
    def update_sub(tech,item):
        db1 = database.child('schools').child('abc').get().val()

        val1 = db1['grade1'][item][tech]
            
        val = val1 + 1
        db1 = database.child('schools').child('abc').child('grade1').child(item).child(tech).set(val)

        db1 = database.child('schools').child('abc').get().val()
        ret={}
        for i in db1["grade1"].keys():
            ret[i]=db1["grade1"][i][tech]
        
        return ret

    db = database.child('links').get().val()
    for i in db.keys():
        print(i)
    for j in db[i].keys():
        print(j)
        for k in db[i][j].keys():
            print(db[i][j][k])
            if(db[i][j][k] == "http://127.0.0.1:8000/temp/"):
                tech=j
                ret=update_sub(tech,item)
                return render(request,'temp2.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'thrus_h': ret['thursday']})

            elif(db[i][j][k] == "http://127.0.0.1:8000/temp1/"):
                tech=j
                ret=update_sub(tech,item)
                return render(request,'temp1.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'thrus_h': ret['thursday']})

    # else:
    #     tech=j
    #     ret=update_sub(tech,item)
    #     return render(request,'temp.html',{'mon_h': ret['monday'], 'tue_h':ret['tuesday'],'thrus_h': ret['thursday']})

