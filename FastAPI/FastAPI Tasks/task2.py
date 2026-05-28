from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

# -----------------------------------
# Pydantic Model
# -----------------------------------
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    priority: str


# -----------------------------------
# Load Tasks
# -----------------------------------
def load_tasks():

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    return tasks


# -----------------------------------
# Save Tasks
# -----------------------------------
def save_tasks(tasks):

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------------
# Home Route
# -----------------------------------
@app.get("/")
def home():

    return {
        "message": "Welcome to Todo API"
    }


# -----------------------------------
# Get All Tasks
# -----------------------------------
@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None):

    tasks = load_tasks()

    # Filtering
    if completed is not None:

        filtered_tasks = []

        for task in tasks:

            if task["completed"] == completed:
                filtered_tasks.append(task)

        return filtered_tasks

    return tasks


# -----------------------------------
# Get Task By ID
# -----------------------------------
@app.get("/tasks/{id}")
def get_task(id: int):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# -----------------------------------
# Create Task
# -----------------------------------
@app.post("/tasks")
def create_task(task: Task):

    tasks = load_tasks()

    # Check duplicate ID
    for t in tasks:

        if t["id"] == task.id:

            raise HTTPException(
                status_code=400,
                detail="Task ID already exists"
            )

    tasks.append(task.dict())

    save_tasks(tasks)

    return {
        "message": "Task created successfully",
        "task": task
    }


# -----------------------------------
# Update Task
# -----------------------------------
@app.put("/tasks/{id}")
def update_task(id: int, updated_task: Task):

    tasks = load_tasks()

    for index, task in enumerate(tasks):

        if task["id"] == id:

            tasks[index] = updated_task.dict()

            save_tasks(tasks)

            return {
                "message": "Task updated successfully",
                "task": updated_task
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


# -----------------------------------
# Delete Task
# -----------------------------------
@app.delete("/tasks/{id}")
def delete_task(id: int):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == id:

            tasks.remove(task)

            save_tasks(tasks)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )