from fastapi import FastAPI 
from pydantic import BaseModel 

# Create fastapi app 
app = FastAPI() 

from fastapi.middleware.cors import CORSMiddleware 

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int 
    name: str 
    grade: int 

students = [

]

@app.get("/students/")
def Read_student():
    return students

@app.post("/students/")
def Create_student(New_student: Student):
    students.append(New_student)
    return New_student 

@app.put("/students/{student_id}") 
def update_student(student_id:int, update_student: Student): 
    for index, student in enumerate(students):
        if student.id == student_id: 
            students[index] = update_student 
            return update_student 
    return {"error": "Student not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id:int): 
    for index, student in enumerate(students): 
        if student.id == student_id: 
            del students[index]
            return {"Delete": "Student Deleted"}
    return {"error": "Student not found"}