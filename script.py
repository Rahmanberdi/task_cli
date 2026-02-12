import typer 
import json
from pathlib import Path
from typing import Optional
from datetime import datetime
from enum import Enum
app = typer.Typer()
TODO_FILE = Path("todos.json")

class Status(str, Enum):
    """Task status enum"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    def __str__(self):
        return self.value
    
def load_todos():
    if TODO_FILE.exists():
        return json.loads(TODO_FILE.read_text())
    return []

def save_todos(todos):
    TODO_FILE.write_text(json.dumps(todos,indent=2))



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