# 🌸 Iris Classification with MLOps (FastAPI + Docker + Render + CI/CD)

This project demonstrates a complete end-to-end **Machine Learning workflow** with a deployed **Iris flower classification model**. It integrates essential **MLOps practices** such as model saving, API serving, containerization, CI/CD, and deployment.

---

## 🚀 What’s Inside

- ✅ **ML Model**: Logistic Regression model trained on the Iris dataset
- ⚡ **API**: FastAPI backend to serve the model for predictions
- 🐳 **Docker**: Containerized application for consistent environment
- 🔁 **CI/CD**: GitHub Actions to automate build and deployment pipeline
- 🌐 **Deployment**: Live on Render.com for public use

---

## 📁 Project Structure
```bash
Simple Iris ML model/
│
├── app/
│ ├── main.py # FastAPI app
│ └── iris_model.pkl # Trained model
│
├── .github/
│ └── workflows/
│ └── ci-cd.yml # CI/CD GitHub Actions workflow
│
├── Dockerfile # Container setup
├── requirements.txt # Python dependencies
└── README.md
```

---

## 🌱 Model Training Summary

- Dataset: [Iris Dataset (sklearn)](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
- Model: Logistic Regression
- Preprocessing: Standardization
- Output Classes:
  - 0 = Setosa
  - 1 = Versicolor
  - 2 = Virginica

---

## 📦 API Usage

### ➤ Base URL

```bash
https://classification-iris-mlops.onrender.com/
```

### ➤ Swagger UI
Navigate to:

```bash
https://classification-iris-mlops.onrender.com/docs
```

### ➤ POST /predict
Send JSON like:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:

```json
{
  "prediction": 0
}
```

---

## 🧪 Local Development

### ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```
Ensure `iris_model.pkl` is present in the correct path.

### 🐳 Run with Docker

```bash
docker build -t iris-mlops .
docker run -p 8000:8000 iris-mlops
```

### 🔁 CI/CD (GitHub Actions)
Every push to the main branch:
  -  Builds the Docker image
  -  Pushes it to Docker Hub (optional)
  -  Deploys via Render (if configured for auto-deploy)

---

## 🌐 Deployment
Hosted on Render.com
Public API: https://your-url.onrender.com

---

## 📌 Milestone
This marks my first step into MLOps, including:
  -  Model packaging
  -  API development
  -  CI/CD with GitHub Actions
  -  Dockerization
  -  Cloud deployment
Stay tuned — more ML/DL projects with full MLOps pipelines coming soon!

---

## 🙌 Acknowledgements
  -  scikit-learn
  -  FastAPI
  -  Docker
  -  Render
  -  GitHub Actions

## 📬 Contact
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/awwab-mahimi-0b1905352/) or share feedback and suggestions via GitHub Issues.
