import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancev2-ac026-default-rtdb.firebaseio.com/"
})



ref = db.reference('Students')


data ={
    "321654":
    {
        "name":"Saksham Khanal",
        "major":"CSIT",
        "starting_year":2019,
        "total_attendance":6,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "852741":
    {
        "name":"Srijan pokhrel",
        "major":"CSIT",
        "starting_year":2019,
        "total_attendance":6,
        "standing":"G",
        "year":4,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "96385":
        {
            "name": "Kushal budathoki",
            "major": "CSIT",
            "starting_year": 2019,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
}

for key,value in data.items():
    ref.child(key).set(value)