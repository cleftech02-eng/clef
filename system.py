from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Clef Management System",
    description="clefing everyday life",
    version="1.0.0",
)

students = {}

student_data = {
    "name": "",
    "age": 0,
    "gender": "",
    "classroom": "",
    "school": "",
    "course": ""
}

@app.get("/joseph")
def root():
    return {"message": "Hello Student Management System!"}


@app.post("/students/joseph")
def create_student(
    name: str,
    age: int,
    gender: str,
    classroom: str,
    school: str
):
    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": name,
        "age": age,
        "gender": gender,
        "classroom": classroom,
        "school": school
    }

    students[new_id] = new_student

    return {
        "message": "Student created successfully",
        "student": new_student
    }


@app.get("/student/joseph/{id}")
def get_student(id: int):
    student = students.get(id)

    if student is None:
        return {"error": "Student not found"}

    return student


@app.put("/student/joseph/{id}")
def update_student(
    id: int,
    name: str = None,
    age: int = None,
    classroom: str = None,
    school: str = None
):
    if id not in students:
        return {"error": "Student not found"}

    student = students[id]

    if name is not None:
        student["name"] = name
    if age is not None:
        student["age"] = age
    if classroom is not None:
        student["classroom"] = classroom
    if school is not None:
        student["school"] = school

    return {
        "message": "Student updated successfully",
        "student": student
    }


@app.delete("/student/joseph/{id}")
def delete_student(id: int):
    if id in students:
        del students[id]
        return {"message": "Student deleted successfully"}

    return {"error": "Student not found"}