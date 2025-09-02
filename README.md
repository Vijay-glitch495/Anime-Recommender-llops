
# Anime Recommender App 🎬✨

A **Streamlit-based web app** that recommends anime using modern ML/NLP pipelines powered by Hugging Face and Groq. The app is fully containerized with **Docker** and can be deployed anywhere.

---

## 🚀 Features

* Interactive web UI built with **Streamlit**
* Anime recommendation pipeline with **Groq API**
* Hugging Face embeddings/models integration
* Dockerized for easy build, run, and CI/CD deployment
* Secure API key management via environment variables

---

## ⚙️ Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/anime-recommender-app.git
cd anime-recommender-app
```

### 2️⃣ Install dependencies (local dev)

```bash
pip install -r requirements.txt
```

### 3️⃣ Run locally

```bash
streamlit run app/app.py
```

---

## 🐳 Docker Usage

### Build the image

```bash
docker build -t anime-recommender-app .
```

### Run with environment variables

You must set **Groq** and **Hugging Face** API keys.

#### Option 1: Pass keys directly

```bash
docker run --platform linux/amd64 -p 8501:8501 \
  -e GROQ_API_KEY="your_groq_api_key" \
  -e HUGGINGFACE_AP_TOKEN="your_hf_token" \
  anime-recommender-app
```

#### Option 2: Use `.env` file

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
HUGGINGFACE_AP_TOKEN=your_hf_token
```

Run:

```bash
docker run --platform linux/amd64 -p 8501:8501 --env-file .env anime-recommender-app
```

---

## 🔑 Environment Variables

| Variable               | Description                   |
| ---------------------- | ----------------------------- |
| `GROQ_API_KEY`         | API key for Groq client       |
| `HUGGINGFACE_AP_TOKEN` | Hugging Face token for models |

See `.env.example` for a template.

---

## 🛠️ Development Notes

* CI/CD pipeline builds and pushes the Docker image to **Docker Hub** automatically.
* In CI/CD, only build & test jobs run (Streamlit is not continuously served).
* Locally or in production, you can serve Streamlit with `docker run` as shown above.

---

## 📷 Demo

Once running, open your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧾 License

MIT License – feel free to use and modify.


