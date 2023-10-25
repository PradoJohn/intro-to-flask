from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]
teachers = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22}
    ]

# "http://127.0.0.1:5000/"
# "http://127.0.0.1:5000/students"

@app.route('/students', methods=['GET'])
def get_students():
  id = request.args.get('id',default=0,type = str)
  for student in students:
    if student['id'] == id:
      stud = student
  return jsonify(stud)

@app.route('/', methods=['GET'])
def home():
  return jsonify(teachers)

@app.route('/students/old_students', methods=['GET'])
def old_students():
  return jsonify([student for student in students if student['age'] >20 ])

@app.route('/young_students', methods=['GET'])
def young_students():
  return jsonify([student for student in students if student['age'] <21 ])

@app.route('/advance_students', methods=['GET'])
def advance_students():
  return jsonify([student for student in students if student['age'] <21 and student['grade'] == 'A'])

@app.route('/student_names', methods =['GET'])
def student_names():
  # [{key: val for key, val in student if key == "first_name" or key == "last_name" }for student in students]
  # [{'first_name': student['first_name'],'last_name':student['last_name']} for student in students]
  return jsonify([{key: val for key, val in student.items() if key == "first_name" or key == "last_name" }for student in students])

@app.route('/student_ages', methods=['GET'])
def student_ages():
  student_names = [{'name': student['first_name'] + ' ' + student['last_name'], 'age': student['age']} for student in students]
  return jsonify(student_names)


app.run(debug=True)