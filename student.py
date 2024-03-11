from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

# กำหนด URI ของ MongoDB
mongo_uri = "mongodb+srv://domdypol:Dompol19@cluster0.hxrw0cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# เชื่อมต่อ MongoDB
client = MongoClient(mongo_uri)
db = client["myStudent"]
collection = db["product"]

app = Flask(__name__)

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