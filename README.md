
## Readme.md
# Task Unity

Task Unity is a **project management software** designed to simplify task management through a Kanban interface. Built using **Django** for the backend and **Tailwind CSS** for the frontend, it allows teams to create, track, and manage tasks across various projects with an intuitive drag-and-drop interface.

## Features

- **Kanban Board**: Organize tasks visually into `To-Do`, `In Progress`, `Review`, and `Done` columns.
- **Project Management**: Create and manage projects, assign users, and view all related tasks.
- **Task Creation**: Add tasks with title, description, status, project, assignees, and file attachments.
- **Multiple Assignees**: Assign tasks to multiple team members.
- **Event Management**: Create and manage events with fields for title, description, location, and timing.
- **Role-Based Access**: Role-based filtering to ensure only authorized users see specific tasks and projects.
- **File Attachments**: Attach files to tasks for better collaboration.
  
<h2 align="center">⚒️Technologies Used ⚒️</h2>
<br/>
<div align="center">
    <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> 
        <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> 
    </a>
    <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> 
    </a>
    <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> 
    </a>
    <a href="https://tailwindcss.com/" target="_blank" rel="noreferrer"> 
        <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwind" width="40" height="40"/> 
    </a>
    <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> 
        <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> 
    </a>
    <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
        <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
    </a>
    <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> 
        <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> 
    </a>
</div>

<br/>
<hr/>

## Installation

Follow these steps to get a local copy of the project:

### Clone the repository
```bash
git clone https://github.com/sarajdhakal/project_taskunity.git
cd project_taskunity
```
Create and activate a virtual environment

```bash
  python3 -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate
```

Install dependencies

```bash
    pip install -r requirements.txt
```
Apply Migrations
 
 ```bash
    python manage.py migrate
```
Run the Development Server

```bash
    python manage.py runserver
```
Now, you can access the application at http://127.0.0.1:8000/.

    

## Usage
Project Management

 - Create projects with unique names and descriptions.
 - View project details, including task breakdown.
 - Assign multiple users to the project.

Kanban Board

- Create tasks and assign them to different columns (To-Do, In Progress, Review, Done).
- Change the status of a task by dragging and dropping between columns.

Event Creation and Filtering

- Users can create events with start and end times.
- Events are filtered based on user roles, ensuring proper visibility for each type of user.


## Contributions

Contributions are always welcome!

  - Fork the project.

  - Create a feature branch:
      ```bash
              git checkout -b feature-name
      ```
  -  Commit your changes:
      ```bash
              git commit -m "Add new feature"
      ```
  - Push to the branch
      ```bash
              git push origin feature-name
      ```
  - Create a pull request


