"""Libraries of project"""
import typer 
import json
from pathlib import Path
from datetime import datetime
from enum import Enum

"""Start Typer app"""
app = typer.Typer()

"""json path"""
TODO_FILE = Path("todos.json")

"""Status class for the status of task"""
class Status(str, Enum):
    """Task status enum"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    def __str__(self):
        return self.value

"""Loading json"""    
def load_todos():
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text())
    return []

"""Saving json"""
def save_todos(todos):
    TODO_FILE.write_text(json.dumps(todos,indent=2))


"""Add command"""
@app.command()
def add(task: str = typer.Argument(...,help="The task description"),
    status: Status = typer.Option(Status.TODO,help="Initial status")
):
    todos = load_todos()
    todo = {
        "id":len(todos)+1,
        "task":task,
        "status":status.value,
        "created_at":datetime.now().isoformat(),
        "updated_at":datetime.now().isoformat()
    }
    todos.append(todo)
    save_todos(todos)
    typer.echo(f"✅ Task added successfully: (ID:{todo['id']})")


"""Update task"""
@app.command()
def update(
    id:int = typer.Argument(...,help="The ID you want to update"),
    task:str = typer.Argument(...,help = "Write task that you want to be new")
    ):
    todos = load_todos()
    todo = None
    for item in todos:
        if item['id']==id:
            todo = item
            break
    if todo:
        todo['task']=task
        todo['updated_at'] = datetime.now().isoformat()
        save_todos(todos)
        typer.echo("✅ Your task was updated successfully!")


"""list command"""
@app.command()
def list():
    """List all todos"""
    todos = load_todos()
    if not todos:
        typer.echo("📭 No todos yet")
        return

    typer.echo("\n📋 Your todos:")
    typer.echo("-"*30)
    for todo in todos:
        typer.echo(f"[{todo['id']}] {todo['task']} status:{todo['status']}")
    
if __name__ == "__main__":
    app()