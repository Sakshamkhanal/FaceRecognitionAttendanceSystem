import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-c1b51-default-rtdb.firebaseio.com/"
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
        "name":"Emily blunt",
        "major":"Economics",
        "starting_year":2018,
        "total_attendance":12,
        "standing":"B",
        "year":4,
        "last_attendance_time":"2022-12-11 00:54:34"
    },
    "963852":
    {
        "name":"Elon Musk",
        "major":"Physics",
        "starting_year":2020,
        "total_attendance":6,
        "standing":"G",
        "year":2,
        "last_attendance_time":"2022-12-11 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)