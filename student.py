# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://domdypol:<password>@cluster0.hxrw0cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(uri, server_api=ServerApi('1'))
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from flask import request,Flask,jsonify
# from flask_basicauth import BasicAuth
app = Flask(__name__) 

# app.config['BASIC_AUTH_USERNAME']='username'
# app.config['BASIC_AUTH_PASSWORD']='password'
# basic_auth = BasicAuth(app)

students=[
    {"id":6530300100,"Fullname":"Pollapat","Major":"CPE","GPA":4.00},
    {"id":6530300101,"Fullname":"Tollapat","Major":"CPE","GPA":2.99},
    {"id":6530300102,"Fullname":"Hollapat","Major":"CPE","GPA":3.00}
]
@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students",methods=["GET"])
# @basic_auth.required
def get_all_students():
    return jsonify({"students":students})

@app.route("/students/<int:student_id>",methods=["GET"])
# @basic_auth.required
def get_student(student_id):
    student =  next(( s for s in students if s["id"]==student_id ),None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error":"Student not found"}),404

@app.route("/students",methods=["POST"])
# @basic_auth.required
def create_student():
    data = request.get_json()
    new_student={
        "Fullname":data["Fullname"],
        "GPA":data["GPA"],
        "Major":data["Major"],
        "id":data["id"],
    }
    students.append(new_student)
    return jsonify(new_student),200

@app.route("/students/<int:student_id>",methods=["PUT"])
# @basic_auth.required
def update_student(student_id):
    student = next((s for s in students if s["id"]==student_id),None)
    if student:
        data = request.get_json()
        student.update(data)
        return jsonify(student)
    else:
        return jsonify({"error":"Student not found"}),404

@app.route("/students/<int:student_id>",methods=["DELETE"])
# @basic_auth.required
def delete_student(student_id):
    student = next((s for s in students if s["id"]==student_id),None)
    if student:
        students.remove(student)
        return jsonify({"message":"Student deleted successfully"}),200
    else:
        return jsonify({"error":"Student not found"}),404
    




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)