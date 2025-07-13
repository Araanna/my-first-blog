# 🧡 Django Girls Workshop Project Setup Guide
##madebymela

Welcome to the Django Girls Workshop! This README will walk you through setting up your Django project on your local machine.

---

## 🛠️ 1. Clone This Repository

Open **Git Bash** or **Command Prompt**, then run:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

Replace the link above with your actual GitHub repository URL.

---

## 📁 2. Navigate to the Project Folder

```bash
cd YOUR_REPO_NAME
```

---

## 🌱 3. Create a Virtual Environment

```bash
python -m venv env
```

---

## ⚡ 4. Activate the Virtual Environment

```bash
env\Scripts\activate
```

You'll know it's activated when you see `(env)` at the beginning of your command line prompt.

---

## 📦 5. Install the Required Packages

```bash
pip install -r requirements.txt
```

---

## 🚀 6. Run the Django Server

```bash
python manage.py runserver
```

Then open your browser and go to:

```
http://127.0.0.1:8000/
```

🎉 You should see the Django welcome page or the homepage of your project!

---

## 🧑‍💻 7. Create a Superuser (for Admin Access)

```bash
python manage.py createsuperuser
```

You’ll be asked to enter a username, email, and password.

Then visit:

```
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials.

---

## 🔧 8. Make Migrations and Migrate

If your models are ready, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🧩 9. Add Your App to `INSTALLED_APPS`

Open `settings.py` and ensure your app is listed in the `INSTALLED_APPS` section.

---

## 🛠️ 10. Build Your Website

Start editing your:

- **Templates** – Located in the `templates/` folder  
- **Views** – Inside your app’s `views.py`  
- **URLs** – Connect views and templates via `urls.py`  

---

## 🌍 Deploying to PythonAnywhere

During the workshop, we’ll guide you through deploying your Django website online using [PythonAnywhere](https://www.pythonanywhere.com/).  
Make sure you’ve already created your account.

Basic deployment steps (we’ll help with this later):

- Upload your project to PythonAnywhere  
- Set up a virtual environment  
- Configure your web app settings  
- Launch your live website 🎉

---

## 🆘 Need Help?

If you get stuck at any point:

- Ask in the workshop chat or group  
- Refer to the [Django Girls Tutorial](https://tutorial.djangogirls.org/)  
- Don’t be shy — we’re here to help! 💪

---

**Happy coding and see you at the workshop! 💜**
