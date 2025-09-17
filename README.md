🌐 Personal Portfolio Website

A Django-powered portfolio website showcasing my projects, education, and contact details. Designed with a modern, responsive UI and deployed on PythonAnywhere.

🚀 Features

🖥️ Responsive Design – Optimized for desktop & mobile
📂 Projects Showcase – With GitHub/demo links
🎓 Education Timeline – "Path of Knowledge" section
📧 Contact Integration – Email me directly
🎨 Custom Styling – Bootstrap, Animate.css, AOS for animations


🛠️ Tech Stack
Backend: Python, Django
Frontend: HTML, CSS, Bootstrap, Animate.css, AOS
Deployment: PythonAnywhere
Version Control: Git, GitHub

📂 Project Structure
Portfolio/
├── main/ # Main app with templates & static files
├── myportfolio/ # Django project settings
├── templates/ # HTML templates (base, home, projects, etc.)
├── static/ # CSS, images, JS
├── manage.py
└── requirements.txt


=======
│── main/ # Main app with templates & static files
│── myportfolio/ # Django project settings
│── templates/ # HTML templates (base, home, projects, etc.)
│── static/ # CSS, images, JS
│── manage.py
│── requirements.txt


Clone the repository

git clone https://github.com/Harini3104/Portfolio.git
cd Portfolio


**Create & activate virtual environment**

python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

**Install dependencies**

pip install -r requirements.txt


**Run migrations & start server** 

python manage.py migrate

python manage.py runserver


👉 Open in browser: http://127.0.0.1:8000/

🌍 Deployment

Hosted live on PythonAnywhere.


