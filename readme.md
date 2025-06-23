# 🌤️ WeatherApp Backend (Django)

A **Django-powered weather application** that:
- Fetches current and hourly forecasts from the **OpenWeather API**.
- Uses **PostgreSQL** for weather history storage.
- Displays real-time data and charts on a simple frontend.

---

## ✨ Features
- 🌍 Search for weather by city.
- 📊 Interactive hourly temperature chart.
- 💾 Stores weather queries in a **Postgres** database.
- 🧭 Django REST API endpoints for current weather and history.

---

## 🧰 Tech Stack
| Layer        | Tech                                              |
|--------------|--------------------------------------------------|
| Backend      | Django 4.x, Django REST Framework                |
| Database     | PostgreSQL                                       |
| External API | [OpenWeather API](https://openweathermap.org/)   |
| Frontend     | HTML, CSS, Vanilla JS, Chart.js                  |

---

## ⚙️ Prerequisites
Before running this project, make sure you have:
- ✅ Python 3.11+
- ✅ PostgreSQL installed and running
- ✅ Git
- ✅ An OpenWeather API key

---

## 🔧 Setup Instructions

### 📂 Clone the Repository
```bash
git clone https://github.com/your-username/weather-project.git
cd weather-project
```

### 🐍 Set up a Virtual Environment
#### On Windows:
```bash
python -m venv env
env\Scripts\activate
```
#### On MacOS/Linux:
```bash
python -m venv env
source env/bin/activate
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🛠️ Configure the Database
Edit `weather_project/settings.py` with your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_db_name>',
        'USER': '<your_db_user>',
        'PASSWORD': '<your_db_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 🔑 Add API Key
In `weather/views.py`, set your API key:
```python
API_KEY = "<YOUR_OPENWEATHER_API_KEY>"
```

### 🧪 Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 🚀 Run the Development Server
```bash
python manage.py runserver
```
Your app will be live at:
```
http://127.0.0.1:8000/
```

---

## 🧭 Usage
1. Open your browser at `http://127.0.0.1:8000/`.
2. Enter a city name.
3. Get current weather and hourly temperature chart.
4. View stored weather history at `http://127.0.0.1:8000/api/history/?city=<CITY_NAME>`.

---

## 🧑‍💻 Author
**Your Name** – [GitHub](https://github.com/Uttam1611)

---

## 💬 Acknowledgments
- Weather data powered by the [OpenWeather API](https://openweathermap.org/).
- Built with [Django](https://www.djangoproject.com/), [Postgres](https://www.postgresql.org/), and [Chart.js](https://www.chartjs.org/).

---

✨ **Happy Coding!** ✨

