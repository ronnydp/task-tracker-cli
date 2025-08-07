# 📄 Task Tracker CLI

Una aplicación de línea de comandos para gestionar tus tareas de forma simple, rápida y sin dependencias externas. Las tareas se almacenan localmente en un archivo JSON.

## 🚀 Características

- Agregar nuevas tareas con descripción y estado.
- Listar tareas por estado: `todo`, `in-progress`, ``done`
- Marcar tareas como `in-progress` o `done`
- Editar la descripción de una tarea.
- Eliminar tareas por ID.
- Almacenamiento local en archivo JSON.
- Sin dependencias externas.

## 📦 Requisitos

- Python 3.7 o superior

## 🛠️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/ronnydp/task-tracker-cli.git
cd task-tracker-cli
```

2. Ejecuta el script principal

```bash
python task_cli.py
```

## 📌 Uso

Desde la terminal, podrás ejecutar diferentes comandos interactivos (seguidos de python task_cli.py) como:

- add: Agrega una nueva tarea.
- list: Muestra las tareas filtradas por estado (todo, in-progress, done o todas).
- update: Cambia el estado o descripcion de una tarea.
- delete: Elimina una tarea por ID.

## 📂 Estructura del proyecto

```
└── 📁taskTracker
    ├── instructions.txt
    ├── README.md
    ├── task_cli.py
    └── task.json
```

## 🗒️ Formato de una tarea

```
{
  "id": 1,
  "description": "Estudiar patrones de diseño",
  "status": "todo"
}
```

## 📢 Estados posibles de una tarea

- todo: Tarea pendiente.
- in-progress: Tarea en desarrollo.
- done: Tarea completada.
