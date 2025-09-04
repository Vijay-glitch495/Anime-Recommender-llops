
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

### 1. Initial Setup

- **Push code to GitHub**  
  Push your project code to a GitHub repository.

- **Create a Dockerfile**  
  Write a `Dockerfile` in the root of your project to containerize the app.

- **Create Kubernetes Deployemtn file**  
  Make a file named 'llmops-k8s.yaml' 

- **Create a VM Instance on Google Cloud**

  - Go to VM Instances and click **"Create Instance"**
  - Name: ``
  - Machine Type:
    - Series: `E2`
    - Preset: `Standard`
    - Memory: `16 GB RAM`
  - Boot Disk:
    - Change size to `256 GB`
    - Image: Select **Ubuntu 24.04 LTS**
  - Networking:
    - Enable HTTP and HTTPS traffic

- **Create the Instance**

- **Connect to the VM**
  - Use the **SSH** option provided to connect to the VM from the browser.



### 2. Configure VM Instance

- **Clone your GitHub repo**

  ```bash
  git clone https://github.com/data-guru0/TESTING-9.git
  ls
  cd TESTING-9
  ls  # You should see the contents of your project
  ```

- **Install Docker**

  - Search: "Install Docker on Ubuntu"
  - Open the first official Docker website (docs.docker.com)
  - Scroll down and copy the **first big command block** and paste into your VM terminal
  - Then copy and paste the **second command block**
  - Then run the **third command** to test Docker:

    ```bash
    docker run hello-world
    ```

- **Run Docker without sudo**

  - On the same page, scroll to: **"Post-installation steps for Linux"**
  - Paste all 4 commands one by one to allow Docker without `sudo`
  - Last command is for testing

- **Enable Docker to start on boot**

  - On the same page, scroll down to: **"Configure Docker to start on boot"**
  - Copy and paste the command block (2 commands):

    ```bash
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
    ```

- **Verify Docker Setup**

  ```bash
  systemctl status docker       # You should see "active (running)"
  docker ps                     # No container should be running
  docker ps -a                 # Should show "hello-world" exited container
  ```


### 3. Configure Minikube inside VM

- **Install Minikube**

  - Open browser and search: `Install Minikube`
  - Open the first official site (minikube.sigs.k8s.io) with `minikube start` on it
  - Choose:
    - **OS:** Linux
    - **Architecture:** *x86*
    - Select **Binary download**
  - Reminder: You have already done this on Windows, so you're familiar with how Minikube works

- **Install Minikube Binary on VM**

  - Copy and paste the installation commands from the website into your VM terminal

- **Start Minikube Cluster**

  ```bash
  minikube start
  ```

  - This uses Docker internally, which is why Docker was installed first

- **Install kubectl**

  - Search: `Install kubectl`
  - Run the first command with `curl` from the official Kubernetes docs
  - Run the second command to validate the download
  - Instead of installing manually, go to the **Snap section** (below on the same page)

  ```bash
  sudo snap install kubectl --classic
  ```

  - Verify installation:

    ```bash
    kubectl version --client
    ```

- **Check Minikube Status**

  ```bash
  minikube status         # Should show all components running
  kubectl get nodes       # Should show minikube node
  kubectl cluster-info    # Cluster info
  docker ps               # Minikube container should be running
  ```

### 4. Interlink your Github on VSCode and on VM

```bash
git config --global user.email "gyrogodnon@gmail.com"
git config --global user.name "data-guru0"

git add .
git commit -m "commit"
git push origin main
```

- When prompted:
  - **Username**: `data-guru0`
  - **Password**: GitHub token (paste, it's invisible)

---


### 5. Build and Deploy your APP on VM

```bash
## Point Docker to Minikube
eval $(minikube docker-env)

docker build -t llmops-app:latest .

kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN=""

kubectl apply -f llmops-k8s.yaml


kubectl get pods

### U will see pods runiing


# Do minikube tunnel on one terminal

minikube tunnel


# Open another terminal

kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0

## Now copy external ip and :8501 and see ur app there....


```

### 6. GRAFANA CLOUD MONITORING

```bash
## Open another VM terminal for Grfana cloud

kubectl create ns monitoring

kubectl get ns

## Make account on Grfaana cloud

### Install HELM - Search on Google
-- Copy commands from script section..
-- U will get 3 commands


## Come to grafana cloud --> Left pane observability --> Kubernetes--> start sending data
## In backend installation --> Hit install
## Give your clustername and namespace there : minikube and monitoring in our case
## Select kubernetes
## Keep other things on as default
## Here only create new access token give name lets give minikube-token & Create it and save it somewhere..
## Select helm and deploy helm charts is already generated...



## Come to terminal --> Create a file
vi values.yaml


## Paste all from there to your file now remove last EOF part & and also initial part save that initial part we need it..

Example : 

helm repo add grafana https://grafana.github.io/helm-charts &&
  helm repo update &&
  helm upgrade --install --atomic --timeout 300s grafana-k8s-monitoring grafana/k8s-monitoring \
    --namespace "monitoring" --create-namespace --values - <<'EOF'

### Remove this above intial part and save it somewhere

Then Esc+wq! amd save the file


## Now use the copied command just make some modification:
Remove that EOF part and instead write
--values values.yaml

Example:

helm repo add grafana https://grafana.github.io/helm-charts &&
  helm repo update &&
  helm upgrade --install --atomic --timeout 300s grafana-k8s-monitoring grafana/k8s-monitoring \
    --namespace "monitoring" --create-namespace --values values.yaml

## Paste this command on VM u will get status deployed revision 1
## It means it was a SUCESS

To check:

kubectl get pods -n monitoring

# These are all should be running.....

Go to grafana cloud again..
And below u will get go to homepage click it..
Just refresh the page and boom..


Now u can see metrics related to your kubernetes cluster..

---Explore it for yourself now 

---Make sure to do cleanup 

```

## 🧾 License

MIT License – feel free to use and modify.


