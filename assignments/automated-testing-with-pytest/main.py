from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str


class Task(TaskCreate):
    id: int
    completed: bool = False


app = FastAPI()
app.state.tasks = {}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return list(app.state.tasks.values())


@app.post("/tasks", status_code=201, response_model=Task)
def create_task(task_data: TaskCreate) -> Task:
    task_id = max(app.state.tasks, default=0) + 1
    task = Task(id=task_id, title=task_data.title)
    app.state.tasks[task_id] = task
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = app.state.tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task