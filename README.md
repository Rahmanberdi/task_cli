# Task CLI 📋

A simple command-line task manager built with Python.

---

## 🚀 Quick Setup

### 1. Create virtual environment
<details>
<summary><b>🐧 macOS/Linux</b></summary>

```bash
python3 -m venv venv
source venv/bin/activate
```
</details>

<details>
<summary><b>🪟 Windows</b></summary>

```bash
python -m venv venv
venv\Scripts\activate
```
</details>

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install the CLI
```bash
pip install -e .
```

---

## 📖 Commands

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Add a new task | `task-cli add "Buy milk"` |
| `list` | List all tasks | `task-cli list` |
| `update` | Update a task | `task-cli update 1 "New task"` |
| `delete` | Delete a task | `task-cli delete 1` |
| `mark-in-progress` | Mark task as in progress | `task-cli mark-in-progress 1` |
| `mark-done` | Mark task as completed | `task-cli mark-done 1` |

### Filter tasks by status
```bash
task-cli list done
task-cli list todo
task-cli list in-progress
```

---

## 💡 Examples

```bash
# Add tasks
task-cli add "Buy groceries"
task-cli add "Write report"

# List all tasks
task-cli list

# Start a task
task-cli mark-in-progress 1

# Complete a task
task-cli mark-done 1

# Delete a task
task-cli delete 2
```

---

## 📁 Data Storage

Tasks are saved in: `~/.task-cli/tasks.json`

---

## 🛠️ Requirements

- Python 3.8+
- Typer

---

## 📄 License

MIT

---

<p align="center">Made with Python</p>
