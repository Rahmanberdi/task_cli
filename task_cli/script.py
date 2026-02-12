"""Libraries of project"""
import typer 
import json
from pathlib import Path
from datetime import datetime
from enum import Enum

"""Start Typer app"""
app = typer.Typer()

"""json path"""
TODO_FILE = Path("tasks.json")

"""Status class for the status of task"""
class Status(str, Enum):
    """Task status enum"""
    TODO = "todo"
    IN_PROGRESS = "in-progress"
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
    status: Status = typer.Argument(Status.TODO,help="Initial status")
):
    todos = load_todos()
    try: 
        id = todos[-1]['id']+1
    except:
        id = 1
    todo = {
        "id":id,
        "task":task,
        "status":status.value,
        "created_at":datetime.now().isoformat(),
        "updated_at":datetime.now().isoformat()
    }
    todos.append(todo)
    save_todos(todos)
    typer.echo(f"✅ Task added successfully: (ID:{todo['id']})")
@app.command(name="mark-in-progress")
def mark_in_progress(id:int = typer.Argument(...,help="The ID you want to update")):
    todos = load_todos()
    todo = None
    for item in todos:
        if item['id']==id:
            todo = item
            break
    if todo:
        todo['status'] = "in-progress"
        todo['updated_at'] = datetime.now().isoformat()
        save_todos(todos)
        typer.echo("✅ Your task was updated successfully!")
    else:
        typer.echo("There was no such task with that ID number.")

@app.command(name="mark-done")
def mark_in_progress(id:int = typer.Argument(...,help="The ID you want to update")):
    todos = load_todos()
    todo = None
    for item in todos:
        if item['id']==id:
            todo = item
            break
    if todo:
        todo['status'] = "done"
        todo['updated_at'] = datetime.now().isoformat()
        save_todos(todos)
        typer.echo("✅ Your task was updated successfully!")
    else:
        typer.echo("There was no such task with that ID number.")


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
    else:
        typer.echo("There was no such task with that ID number.")

"""Delete task"""
@app.command()
def delete(
    id:int = typer.Argument(...,help="The ID you want to update"),
    ):
    todos = load_todos()
    todo = None
    for item in todos:
        if item['id']==id:
            todo = item
            break
    if todo:
        del todos[id-1]
        save_todos(todos)
        typer.echo("🗑️✅ Your task was deleted successfully!")
    else:
        typer.echo("There was no such task with that ID number.")

"""list command"""

@app.command()
def list(status: Status = typer.Argument(None,help="Initial status")):

    """List all todos"""

    todos = load_todos()
    if todos:
        if status!=None:
            filtered_todos = [todo for todo in todos if todo['status']==status.value]
            if filtered_todos:
                typer.echo("\n📋 Your todos:")
                typer.echo("-"*30)
                for todo in filtered_todos:
                    typer.echo(f"[{todo['id']}] {todo['task']}")
                return
            else:
                typer.echo(f"There is no task that is {status.value}")    
                return
        else:
            typer.echo("\n📋 Your tasks:")
            typer.echo("-"*30)
            for todo in todos:
                typer.echo(f"[{todo['id']}] {todo['task']} status:{todo['status']}")
            return
    if not todos:
        typer.echo("📭 No tasks yet")
        return

    typer.echo("\n📋 Your tasks:")
    typer.echo("-"*30)
    for todo in todos:
        typer.echo(f"[{todo['id']}] {todo['task']} status:{todo['status']}")


if __name__ == "__main__":
    app()
