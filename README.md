# Incident Log API - HumanChain AI Safety Backend Assignment

A simple RESTful API built with Flask and PostgreSQL (with fallback to SQLite) to manage and log AI safety incidents, created for the HumanChain Backend Intern Take-Home Assignment.

---

## 🚀 Tech Stack
- **Language:** Python 3.9+
- **Framework:** Flask
- **Database:** Supabase PostgreSQL (fallback to local SQLite)
- **ORM:** SQLAlchemy
- **Migrations:** Flask-Migrate
- **API Documentation:** Swagger UI (via flask-swagger-ui)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Vivek96254/SparkleHood_Task.git
cd SparkleHood_Task
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory:
```env
DATABASE_URL=postgresql://youruser:yourpassword@yourhost:5432/yourdb
```
> 💡 If `DATABASE_URL` is not specified, it defaults to SQLite at `sqlite:///incidents.db`

### 4. Setup and Run (Automated)
Use the provided `setup.bat` script for Windows to automate database migration, seed sample data, and start the server:
```bash
setup.bat
```
> 🔥 This will:
> - Initialize and migrate the database
> - Prepopulate it with sample incidents
> - Launch the Flask server

### 5. Manual Setup (Optional)
If you prefer manual setup:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py
python run.py
```

---

## 🌐 API Endpoints

### ✅ `GET /incidents`
Retrieve all logged incidents.
```bash
curl -X GET http://localhost:5000/incidents
```

### ✅ `POST /incidents`
Create a new incident.
```bash
curl -X POST http://localhost:5000/incidents \
     -H "Content-Type: application/json" \
     -d '{
           "title": "System misclassified images",
           "description": "The AI model labeled people as objects.",
           "severity": "Medium"
         }'
```

### ✅ `GET /incidents/<id>`
Retrieve a specific incident by its ID.
```bash
curl -X GET http://localhost:5000/incidents/1
```

### ✅ `DELETE /incidents/<id>`
Delete an incident by its ID.
```bash
curl -X DELETE http://localhost:5000/incidents/1
```

### ✅ `GET /incidents/available-ids`
Retrieve a list of available incident IDs.
```bash
curl -X GET http://localhost:5000/incidents/available-ids
```

### ✅ `DELETE /incidents`
Delete **all** incidents.
> Requires a confirmation body `{ "confirm": "yes" }`

```bash
curl -X DELETE http://localhost:5000/incidents \
     -H "Content-Type: application/json" \
     -d '{"confirm":"yes"}'
```
> 🎯 After deleting all incidents, the ID sequence is reset to start from 1.

---

## 📜 Swagger API Documentation

You can access an interactive API documentation using Swagger UI.

- Open [http://localhost:5000/docs](http://localhost:5000/docs) in your browser.
- You will see a full list of available endpoints, parameters, and example responses.
- You can also **test endpoints directly from the browser**!

> Make sure the file `swagger.yaml` exists under the `static/` directory.
> If you encounter a CORS issue, ensure `flask-cors` is installed and CORS is enabled in `__init__.py`.

---

## 📌 Sample Data
The database is automatically prepopulated with 2–3 sample incidents when running `setup.bat` or manually running `seed.py`.

You can also create your own incidents using the `POST /incidents` endpoint.

---

## ⚠️ Validation Rules
- `title`, `description`, and `severity` are **required**.
- `severity` must be one of: `Low`, `Medium`, `High`.
- Confirmation is needed when deleting **all** incidents.

---

## ✨ Design Decisions
- Clean architecture using Flask Blueprints.
- Sequence reset after full deletion for ID consistency.
- Safe confirmation mechanism to avoid accidental mass deletion.
- SQLite fallback allows easy local development without setup friction.
- Integrated Swagger UI for easy API exploration.


