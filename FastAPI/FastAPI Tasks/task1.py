from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import json

app = FastAPI()

class Student(BaseModel):
    id: int = Field(..., description="Student ID")
    name: str = Field(..., description="Student name", max_length=20)
    age: int = Field(..., description="Student age", gt=0, lt=100)
    course: str = Field(..., description="Student course", max_length=20)

def load_students():

    with open("students.json", "r") as file:
        students = json.load(file)

    return students

def save_students(students):

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

@app.get("/students")
def get_students():
    students = load_students()

    return students

@app.get("/students/{id}")
def get_student(id: int):
    students = load_students()

    for student in students:

        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.post("/students")
def create_student(student: Student):

    students = load_students()
    for s in students:

        if s["id"] == student.id:

            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student.dict())
    save_students(students)

    return {
        "message": "Student added successfully",
        "student": student
    }

@app.delete("/students/{id}")
def delete_student(id: int):

    students = load_students()

    for student in students:

        if student["id"] == id:

            students.remove(student)

            save_students(students)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )