from firebase import firebase

firebase = firebase.FirebaseApplication('https://collapp-2605.firebaseio.com', None)

while True:

    rollno =input('Enter no here...')
    teacher=input('Enter teacher here...')
    ACLASS = input('Enter attended classes here...')
    date = input('Enter date here...')
    #a=['18EC407','18EC413']

    resultput = firebase.put('Attendance'+teacher,rollno,{"teacher":teacher,'total class':'26','attended classes':ACLASS,'last class':date})

    pag = firebase.put('NotAttendance','18EC407',
                             {"teacher": teacher})
    #g= firebase.put('NotAttended',{"not attended class":a[1]})
    #firebase.post('/Stream/',Stream )
    print(pag)
    print(resultput)
