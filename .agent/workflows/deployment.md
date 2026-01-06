---
description: How to Deploy AstraFit to Production (Phone App)
---

This guide steps you through deploying your gym app so you can use it on your phone like a real app.

## 1. Prerequisites
- A GitHub account.
- A free account on **Render.com** (recommended for ease) or **PythonAnywhere** (good for Python specific).

## 2. Push Code to GitHub
First, we need to get your code into a repository.

1. Initialize Git (if not done):
   ```powershell
   git init
   git add .
   git commit -m "Initial AstraFit commit"
   ```

2. Create a new repository on GitHub (e.g., `astrafit-gym-app`).
3. Link and push:
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/astrafit-gym-app.git
   git branch -M main
   git push -u origin main
   ```

## 3. Deployment Option A: Render.com (Easiest)
1. Go to [dashboard.render.com](https://dashboard.render.com).
2. Click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Settings:
   - **Name**: `astrafit-app`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn gym_backend.wsgi:application`
   - **Plan**: Free

5. Click **Create Web Service**.
6. Wait for deployment to finish. You will get a URL like `https://astrafit-app.onrender.com`.

## 4. Deployment Option B: PythonAnywhere
1. Sign up/Log in.
2. Go to **Web** tab -> **Add a new web app**.
3. Choose **Manual Configuration** -> **Python 3.10**.
4. Use the **Bash** console to clone your repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/astrafit-gym-app.git
   ```
5. Set up virtualenv and install requirements (in the console).
6. Edit the **WSGI configuration file** (link in Web tab) to point to your project path.
7. Go to **Static Files** section in Web tab:
   - URL: `/static/`
   - Directory: `/home/yourusername/astrafit-gym-app/staticfiles`
8. Click **Reload**.

## 5. Install on Phone (PWA)
Once the URL is live (e.g., `https://astrafit.onrender.com`):

1. Open the URL in **Chrome (Android)** or **Safari (iOS)** on your phone.
2. **Android**: Tap the three dots menu -> **Add to Home Screen** (or "Install App").
3. **iOS**: Tap the Share button -> **Add to Home Screen**.

The app will now appear on your home screen with the icon. When you open it, it will look like a native app (full screen, no browser bar).

## 6. Updating the App
To add new features in the future:
1. Make changes in your code (VS Code).
2. Commit and push:
   ```powershell
   git add .
   git commit -m "Added new features"
   git push
   ```
3. Render/PythonAnywhere will automatically detect the push and redeploy! Your phone app will update automatically the next time you open it.
