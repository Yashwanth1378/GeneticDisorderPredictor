# 🧬 Genetic Disorder Risk Predictor

A **clinical machine learning web application** built with **Django** and **Scikit-learn** to predict the likelihood of **genetic disorders or birth-related conditions** based on **family history**, **pregnancy information**, and **clinical features**. This project demonstrates the intersection of **AI and healthcare** by simulating real-world diagnostics in a web interface.

---

## 💡 Key Features

- 🔎 **Clinical Risk Prediction**: Uses a trained `RandomForestClassifier` to analyze medical history and clinical features for predicting genetic disorder risk.
- ⚙️ **Medical Input Workflow**: Inputs include maternal/paternal genes, blood cell counts, birth asphyxia, maternal illness, etc.—mimicking real hospital data collection.
- 🧠 **Integrated ML Pipeline**: Encoded input handling and ML model loaded with `joblib` for rapid, modular predictions.

---

## 🛠️ Tech Stack

- **Frontend**: HTML (`index.html`, `result.html`)
- **Backend**: Django (`views.py`, `urls.py`)
- **Machine Learning**: Scikit-learn (Random Forest), joblib
- **Environment**: Python 3.x

---

## 📁 Project Structure

```
GeneticDisorderPredictor/
│
├── predictor/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── predictor/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── disorder/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── models.py
│       ├── tests.py
│       ├── train_model.py
│       ├── urls.py
│       ├── views.py
│       ├── model.pkl
│       ├── encoders.pkl
│       ├── Training_set.csv
│       └── templates/
│           └── disorder/
│               ├── index.html
│               └── result.html
│
├── README.MD
└── .gitignore
```

---

## 🚀 How to Run the Project

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Yashwanth1378/GeneticDisorderPredictor.git
   cd GeneticDisorderPredictor/predictor
   ```

2. **Create and Activate Virtual Environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Requirements**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Django Server**
   ```sh
   python manage.py runserver
   ```

5. **Visit in Browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🤖 Machine Learning Model Info

- **Algorithm**: RandomForestClassifier
- **Preprocessing**: Label Encoding of categorical medical inputs
- **Storage**: ML model (`model.pkl`) and encoders (`encoders.pkl`) stored with joblib for real-time use in Django

### 🔍 Sample Features

- Maternal Gene
- Paternal Gene
- Blood cell count (mcL)
- Birth asphyxia
- H/O serious maternal illness

---

## 🏥 Use Cases

- Genetic counseling applications
- Prenatal risk prediction tools
- Clinical decision support systems for obstetrics

---

⚠️ **Disclaimer:** This project is for educational and demonstration purposes only. It does not provide actual medical advice.

---