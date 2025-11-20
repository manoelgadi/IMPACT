# 📘 Fintech TECHNOLOGY WITH IMPACT

## **Session 11 – Deploying a Machine Learning Model on PythonAnywhere**

Instructor: **Prof. Manoel Gadi**

This repository contains all files required for **Session 11** of the course **Fintech Technology with Impact**, where students learn how to:

1. **Train a machine-learning model**
2. **Export it using Joblib**
3. **Deploy it using Flask on PythonAnywhere**
4. **Query the model from an HTML form**

The goal is to simulate how a real Fintech deploys a scoring model into production.

---

# 🚀 1. What Students Will Build

During this session, students will:

✔ Create a logistic regression model that predicts **probability of default**
✔ Save it as `fintech.joblib` inside PythonAnywhere
✔ Deploy it through Flask (`flask_app.py`)
✔ Build a simple HTML interface (`templates/index.html`) that calls the API
✔ Test the scoring endpoint via browser or URL parameters

---

# 🧠 2. Model Training — `fintech.py`

`fintech.py` generates synthetic loan-level variables, trains a logistic-regression model, and saves:

* `fintech.xlsx` (dataset)
* `fintech.joblib` (trained model)

You **must run this script inside PythonAnywhere** so the generated `fintech.joblib` is stored in the correct working directory.

---

# 🌐 3. Deployment — Updated `flask_app.py`

This is the updated version used in class:

* The root URL (`/`) serves **index.html** via Flask templates
* `probdefaultfixed` returns a hard-coded score
* `probdefault` receives GET parameters from the HTML form
* The model is loaded from `fintech.joblib`

### HTML Form → Flask → Model → Response

Students learn how front-end parameters flow into a deployed Fintech scoring engine.

---

# 📂 4. Project Structure

Your repository should look like this:

```
IMPACT/
│
├── fintech.py                 # Script that trains and saves the model
├── fintech.xlsx               # Generated dataset
├── fintech.joblib             # Saved ML model (created after running fintech.py)
├── flask_app.py               # Flask app that deploys the scoring API
├── templates/
│     └── index.html           # HTML form (served from "/")
└── README.md
```

---

# 🛠 5. Steps to Deploy on PythonAnywhere

### **Step 1 — Upload Your Files**

Upload these into your PythonAnywhere project folder:

* fintech.py
* flask_app.py
* templates/index.html

Then run the model training script:

```
python3 fintech.py
```

This creates:
✔ `fintech.joblib` (required by Flask)

---

### **Step 2 — Configure the Web App**

1. Go to **Web** → **Add a new web app**
2. Choose **Manual configuration** → **Python 3.x**
3. Edit the WSGI file:

   * Import the Flask app in `flask_app.py`
4. Click **Reload Web App**

---

### **Step 3 — Test Your Endpoints**

#### Root page (HTML form)

```
https://<your-username>.pythonanywhere.com/
```

#### Hard-coded test

```
https://<your-username>.pythonanywhere.com/probdefaultfixed
```

#### GET parameters from URL

```
https://<your-username>.pythonanywhere.com/probdefault?time_on_books=12&total_paid_last_12_months=5000&total_debt_in_arrears=2000
```

#### GET parameters from the HTML form

Accessible via:

```
/
```

---

# 🖥 6. Sample `index.html`

A simple HTML form used in the session:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Probability of Default</title>
</head>
<body>
    <h2>Calculate Probability of Default</h2>
    <form action="/probdefault" method="get">
        <label>Time on Books:</label>
        <input type="number" name="time_on_books" required><br><br>

        <label>Total Paid Last 12 Months:</label>
        <input type="number" name="total_paid_last_12_months" required><br><br>

        <label>Total Debt in Arrears:</label>
        <input type="number" name="total_debt_in_arrears" required><br><br>

        <button type="submit">Predict</button>
    </form>
</body>
</html>
```

Place this inside:

```
templates/index.html
```

---

# 🎯 7. Learning Outcomes

By completing this session, students gain hands-on experience with:

✔ Training ML models
✔ Saving models using Joblib
✔ Deploying Python models using Flask
✔ Creating API endpoints
✔ Building lightweight Fintech scoring engines in the cloud
✔ Connecting HTML → Flask → Python model

These are core skills for modern Fintech product development.

