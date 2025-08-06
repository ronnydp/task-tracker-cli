import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'task.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f)
        return []
    
    with open(TASKS_FILE, 'r') as f:
        content = f.read().strip()
        if not content:
            with open(TASKS_FILE, 'w') as f_write:
                json.dump([], f_write)
            return []
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            print("⚠️ El archivo task.json está dañado o no tiene formato JSON válido.")
            return []
    
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def get_next_id(tasks):
    return max((task['id'] for task in tasks), default=0) + 1;

def add_task(description):
    tasks = load_tasks()

    if not description.strip():
        print("La descripcion no puede estar vacía.")

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea guardada (ID: {new_task['id']})")

def list_tasks(status = None):
    tasks = load_tasks()
    if not tasks:
        print("No existe una lista de tareas.")

    if not tasks:
        print('No hay tareas guardadas.')
        return
    
    print('=== Lista de Tareas ===\n')

    for task in tasks:
        if status and task['status'] != status:
            continue
        print_tasks(task)

def update_task(id, description):
    id = int(id)
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Tarea {task['id']} actualizada.")
            return
    
    print(f"No se encontró tarea con ID {id}")
    
def delete_task(id):
    tasks = load_tasks()
    initial_count = len(tasks)
    try:
        id = int(id)
        tasks = [task for task in tasks if task['id'] != id]
        if len(tasks) == initial_count:
            print(f"No se encontró tarea con ID {id}")  
            return
        save_tasks(tasks)
        print(f"Tarea con ID {id} eliminada.")
    except ValueError:
        print('El ID debe ser un numero entero')
        return
    
def mark_in_progress(id):
    tasks = load_tasks()
    try:
        id = int(id)
        for task in tasks:
            if task['id'] == id:
                task['status'] = 'in-progress'
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Tarea {task['id']} en progreso.")
                return
    except ValueError:
        print('El ID debe ser un numero entero')
        return
    print(f"No se encontró tarea con ID {id}")
def mark_done(id):
    tasks = load_tasks()
    try:
        id = int(id)
        for task in tasks:
            if task['id'] == id:
                task['status'] = 'done'
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Tarea {task['id']} terminada.")
                return
    except ValueError:
        print('El ID debe ser un numero entero')
        return
    print(f"No se encontró tarea con ID {id}")
        
def print_tasks(task):
    print(f"[ID: {task['id']}] [{task['status'].upper()}]")
    print(f"➡️  {task['description']}")
    print(f"🕛 Creada: {task['createdAt']}")
    print(f"🛠️  Actualizada: {task['updatedAt']}\n")

def main():    
    if len(sys.argv) < 2:
        print("Uso: python task_cli.py <comando> [argumentos]")
        return
    
    command = sys.argv[1]
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Uso: python task_cli.py add \"[Descripcion de la tarea]\"")
            return
        description = ''.join(sys.argv[2:])
        add_task(description)
    elif command == 'list':
        if len(sys.argv) > 2:
            status = sys.argv[2]
            if status not in {'todo', 'in-progress', 'done'}:
                print("Uso: python task_cli.py add \"Estado de la tarea (todo, in-progress o done.)\"")
                return
            list_tasks(status)
        else:
            list_tasks()
    elif command == 'update':
        if len(sys.argv) < 4:
            print('Uso: python task_cli.py update \'[ID] [Descripcion]\'')
            return
        id = sys.argv[2]
        description = ''.join(sys.argv[3:])
        update_task(id, description)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Uso: python task.cli.py delete \'[ID]\'")
            return
        id = sys.argv[2]
        delete_task(id)
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Uso: python task.cli.py mark-in-progress \'[ID]\'")
            return
        id = sys.argv[2]
        mark_in_progress(id)
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Uso: python task.cli.py mark-in-progress \'[ID]\'")
            return
        id = sys.argv[2]
        mark_done(id)
    else:
        print(f"Comando no reconocido: {command}")
   
if __name__ == "__main__":
    main()