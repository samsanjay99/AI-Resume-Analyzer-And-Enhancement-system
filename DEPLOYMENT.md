# Deployment Guide for Smart AI Resume Analyzer

This guide provides multiple deployment options for the Smart AI Resume Analyzer, focusing on professional hosting platforms that offer better performance than Streamlit Cloud.

## 🚀 **Recommended Deployment Platforms**

### 1. **Railway** (Recommended) 🚂

**Why Railway?** Fast, simple, and handles Python apps perfectly with automatic HTTPS.

#### Steps:

1. **Connect GitHub:**

   ```bash
   # Push your code to GitHub first
   git add .
   git commit -m "Deploy to Railway"
   git push origin main
   ```

2. **Deploy on Railway:**

   - Go to [railway.app](https://railway.app)
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect it's a Python app

3. **Environment Variables:**
   Add these in Railway dashboard:

   ```
   GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
   PORT=8501
   ```

4. **Custom Start Command:**
   ```bash
   streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

### 2. **Render** (Great Alternative) 🎨

**Why Render?** Professional hosting with great performance and easy setup.

#### Steps:

1. **Create Web Service:**

   - Go to [render.com](https://render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository

2. **Configuration:**

   ```
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
   ```

3. **Environment Variables:**
   ```
   GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
   PYTHON_VERSION=3.9.18
   ```

### 3. **Heroku** (Classic Choice) 🟣

**Why Heroku?** Reliable, well-documented, great for production apps.

#### Steps:

1. **Install Heroku CLI:**

   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Heroku App:**

   ```bash
   heroku create your-resume-analyzer
   heroku config:set GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
   ```

3. **Create Procfile:**

   ```bash
   echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

4. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### 4. **DigitalOcean App Platform** 💧

**Why DigitalOcean?** Great performance, competitive pricing, developer-friendly.

#### Steps:

1. **Create App:**

   - Go to [cloud.digitalocean.com](https://cloud.digitalocean.com)
   - Click "Create" → "Apps"
   - Connect your GitHub repository

2. **App Configuration:**
   ```yaml
   name: smart-resume-analyzer
   services:
     - name: web
       source_dir: /
       github:
         repo: your-username/Smart-AI-Resume-Analyzer
         branch: main
       run_command: streamlit run app.py --server.port=8080 --server.address=0.0.0.0
       environment_slug: python
       instance_count: 1
       instance_size_slug: basic-xxs
       envs:
         - key: GOOGLE_API_KEY
           value: AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
   ```

### 5. **Google Cloud Run** ☁️

**Why Google Cloud?** Serverless, scales automatically, pay-per-use.

#### Steps:

1. **Create Dockerfile:**

   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8080
   CMD streamlit run app.py --server.port=8080 --server.address=0.0.0.0 --server.headless=true
   ```

2. **Deploy:**
   ```bash
   gcloud run deploy smart-resume-analyzer \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
   ```

## 🔧 **Deployment Preparation**

### Required Files for Deployment

1. **Create `runtime.txt` (for some platforms):**

   ```bash
   echo "python-3.9.18" > runtime.txt
   ```

2. **Update `requirements.txt`:**

   ```txt
   streamlit
   streamlit-option-menu
   streamlit-lottie
   streamlit-extras
   python-docx
   pandas
   plotly
   pillow
   python-dotenv
   nltk
   scikit-learn
   sqlalchemy
   openpyxl
   requests
   spacy
   pypdf==4.2.0
   google-generativeai
   pdf2image
   pytesseract
   pdfplumber
   reportlab
   openai
   docx2pdf
   docx2txt
   python-pptx
   matplotlib
   seaborn
   ```

3. **Create `.streamlit/config.toml`:**

   ```toml
   [server]
   headless = true
   port = 8501
   enableCORS = false
   enableXsrfProtection = false

   [theme]
   primaryColor = "#4CAF50"
   backgroundColor = "#0E1117"
   secondaryBackgroundColor = "#262730"
   textColor = "#FAFAFA"
   ```

### Environment Variables Setup

For all platforms, you'll need these environment variables:

```bash
GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
PORT=8501  # or 8080 depending on platform
```

## 💻 **Local Development**

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/Smart-AI-Resume-Analyzer.git
cd Smart-AI-Resume-Analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 🎯 **Step-by-Step: Deploy to Render**

### **Method 1: Web Interface (Recommended)**

1. **Prepare Your Repository:**

   ```bash
   # Make sure all files are committed
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Go to Render:**

   - Visit [render.com](https://render.com)
   - Sign up/Login with your GitHub account

3. **Create New Web Service:**

   - Click **"New"** → **"Web Service"**
   - Connect your GitHub repository
   - Select your `Smart-AI-Resume-Analyzer` repository

4. **Configure Service:**

   ```
   Name: smart-resume-analyzer
   Region: Oregon (US West) or closest to you
   Branch: main
   Root Directory: (leave blank)
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
   ```

5. **Add Environment Variables:**

   - Click **"Advanced"**
   - Add environment variable:
     ```
     Key: GOOGLE_API_KEY
     Value: AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
     ```

6. **Deploy:**
   - Click **"Create Web Service"**
   - Wait for deployment (5-10 minutes)
   - Your app will be live at `https://your-app-name.onrender.com`

### **Method 2: Render CLI**

1. **Install Render CLI:**

   ```bash
   npm install -g @render/cli
   # or
   curl -fsSL https://cli.render.com/install | sh
   ```

2. **Login and Deploy:**
   ```bash
   render login
   render deploy
   ```

## 🚀 **Alternative Deployment Options**

### **Railway (Fastest Setup)**

1. **Deploy to Railway:**
   - Go to [railway.app](https://railway.app)
   - Click **"Start a New Project"**
   - Select **"Deploy from GitHub repo"**
   - Choose your repository
   - Add environment variable: `GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU`

### **Heroku (Classic)**

1. **Install Heroku CLI and Deploy:**
   ```bash
   # Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli
   heroku create your-app-name
   heroku config:set GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
   git push heroku main
   ```

### **DigitalOcean App Platform**

1. **Create App:**
   - Go to [cloud.digitalocean.com](https://cloud.digitalocean.com)
   - Click **"Create"** → **"Apps"**
   - Connect GitHub repository
   - Set run command: `streamlit run app.py --server.port=8080 --server.address=0.0.0.0`
   - Add environment variable: `GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU`

## 🐳 **Docker Deployment**

### **Option 1: Lightweight Cloud Docker (Recommended)**
```bash
# Use the cloud-optimized Dockerfile
docker build -f Dockerfile.cloud -t smart-resume-analyzer .
docker run -p 8501:8501 -e GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU smart-resume-analyzer
```

### **Option 2: Full Docker (with OCR support)**
```bash
# Use the full Dockerfile (requires more system dependencies)
docker build -t smart-resume-analyzer .
docker run -p 8501:8501 -e GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU smart-resume-analyzer
```

### **Docker Hub Deployment:**
```bash
# Build and push to Docker Hub (lightweight version)
docker build -f Dockerfile.cloud -t yourusername/smart-resume-analyzer .
docker push yourusername/smart-resume-analyzer
```

### **Fix Docker Build Issues:**
If you encounter Docker build errors:

1. **Use the lightweight version:**
   ```bash
   docker build -f Dockerfile.cloud -t smart-resume-analyzer .
   ```

2. **Clear Docker cache:**
   ```bash
   docker system prune -a
   ```

3. **Check logs for specific errors:**
   ```bash
   docker build --no-cache -f Dockerfile.cloud -t smart-resume-analyzer .
   ```

## 🔧 **Troubleshooting**

### **Common Issues:**

1. **Port Issues:**

   - Make sure your app uses `$PORT` environment variable
   - Default ports: Render (10000), Heroku (dynamic), Railway (dynamic)

2. **Memory Issues:**

   - Upgrade to paid plan if needed
   - Optimize your requirements.txt

3. **Build Failures:**

   - Check Python version compatibility
   - Ensure all dependencies are in requirements.txt

4. **API Key Issues:**
   - Verify environment variable is set correctly
   - Check for typos in the API key

### **Performance Tips:**

1. **Optimize Requirements:**

   - Remove unused packages
   - Use specific versions

2. **Enable Caching:**

   - Use `@st.cache_data` for expensive operations
   - Cache model loading

3. **Resource Management:**
   - Monitor memory usage
   - Use appropriate instance sizes

## 📊 **Platform Comparison**

| Platform         | Free Tier       | Performance | Ease of Use | Custom Domain |
| ---------------- | --------------- | ----------- | ----------- | ------------- |
| **Render**       | ✅ 750hrs/month | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐  | ✅            |
| **Railway**      | ✅ $5 credit    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐  | ✅            |
| **Heroku**       | ✅ 550hrs/month | ⭐⭐⭐      | ⭐⭐⭐⭐    | ✅            |
| **DigitalOcean** | ❌ Paid only    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐      | ✅            |

## 🎉 **Post-Deployment**

After successful deployment:

1. **Test Your App:**

   - Upload a resume
   - Try different AI models
   - Test portfolio generation

2. **Monitor Performance:**

   - Check response times
   - Monitor resource usage
   - Review error logs

3. **Custom Domain (Optional):**
   - Most platforms support custom domains
   - Configure DNS settings
   - Enable HTTPS

**Your Smart AI Resume Analyzer is now live and ready to help users! 🚀**
