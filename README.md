# 📝 To-Do Management Module (Odoo 19)

## 📌 Overview

The **To-Do Management** module is a custom Odoo 19 addon designed to help users efficiently manage their daily tasks.  
It provides task tracking, assignment, and reporting functionalities with a clean and modular structure following Odoo best practices.

---

## 🧩 Features

- ✅ Create, update, and delete To-Do tasks.
- 👥 Assign tasks to users using a dedicated wizard.
- 🕒 Automatic sequence generation for task IDs.
- 📄 Task report generation (QWeb report).
- 🌐 Full Arabic translation support (`ar_001.po`).
- 🧠 REST API for managing tasks and responses.
- 🔒 Security and access rights defined by user roles.
- 🧪 Unit tests included for task functionality.
- 🎨 Custom fonts and styles for UI enhancement.

---

## 🏗️ Module Structure

```
todo_management/
├── controllers/
│   ├── __init__.py
│   ├── todo_response.py
│   └── todo_task_api.py
│
├── data/
│   └── sequence.xml
│
├── i18n/
│   ├── ar_001.po
│   └── todo_management.pot
│
├── models/
│   ├── __init__.py
│   └── todo_task.py
│
├── report/
│   └── todo_task_report.xml
│
├── security/
│   ├── ir.model.access.csv
│   └── security.xml
│
├── static/
│   ├── description/
│   │   └── icon.png
│   └── src/
│       ├── css/
│       │   ├── Fonts.css
│       │   └── todo_task.css
│       └── fonts/
│           ├── LobsterTwo-Bold.ttf
│           ├── LobsterTwo-BoldItalic.ttf
│           ├── LobsterTwo-Italic.ttf
│           └── LobsterTwo-Regular.ttf
│
├── tests/
│   ├── __init__.py
│   └── test_todo_task.py
│
├── views/
│   ├── base_view.xml
│   └── todo_task_view.xml
│
├── wizard/
│   ├── __init__.py
│   ├── assign_task.py
│   └── assign_task_view.xml
│
├── __init__.py
├── __manifest__.py
└── README.md
```

---

## ⚙️ Installation

1. Copy the folder **`todo_management`** to your Odoo addons directory:
   ```bash
   /odoo/custom/addons/
   ```
2. Update the app list:
   ```
   Settings → Apps → Update Apps List
   ```
3. Search for **"To-Do Management"** and install it.

---

## 🚀 Usage

1. Navigate to the **To-Do Management** menu.
2. Create new tasks and assign them to users.
3. View or print reports using the “Print Report” button.
4. Use the wizard to assign or reassign tasks.

---

## 🧱 Technical Details

| Component        | Description                            |
| ---------------- | -------------------------------------- |
| **Models**       | Task management logic (`todo_task.py`) |
| **Controllers**  | REST API and response handlers         |
| **Views**        | XML definitions for form/tree views    |
| **Reports**      | QWeb PDF report templates              |
| **Security**     | Access control via XML and CSV         |
| **Tests**        | Unit testing using Odoo’s framework    |
| **Wizard**       | Assign task popup window               |
| **Static Files** | Custom CSS and font styling            |

---

## 🌍 Translation

Arabic translation file included at:

```
i18n/ar_001.po
```

---

## 🧑‍💻 Author

**Abdelhameed Mohamed**  
Odoo Developer | Full-Stack Engineer  
📧 abdelhameed.m.hemida@gmail.com  
💼 [https://www.linkedin.com/in/abdelhameed-mohamed-iti]

---

## 🪪 License

This module is licensed under the **Odoo Proprietary License (OPL-1)** or your custom license if you prefer.

## 🌐 API Endpoints (Summary)

The module provides a lightweight REST API for integrating To-Do tasks with external systems.

| Method   | Endpoint                             | Description                                                    |
| -------- | ------------------------------------ | -------------------------------------------------------------- |
| `GET`    | `/v1/todo/read_tasks`                | Retrieve all tasks (supports **filtering** and **pagination**) |
| `GET`    | `/v1/todo/read_task/<int:task_id>`   | Retrieve a specific task by ID                                 |
| `POST`   | `/v1/todo/create_task/<int:task_id>` | Create a new task                                              |
| `PUT`    | `/v1/todo/update_task/<int:task_id>` | Update an existing task                                        |
| `DELETE` | `/v1/todo/delete_task/<int:task_id>` | Delete a task                                                  |

All API responses are returned in **JSON** format.  
Filtering and pagination parameters are supported for the `GET /v1/todo/read_tasks` endpoint.
