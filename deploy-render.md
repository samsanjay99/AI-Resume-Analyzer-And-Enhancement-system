# 🎨 Deploy to Render - Quick Guide

## ✅ **Pre-Deployment Checklist**

Make sure you have these files in your repository:
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version (python-3.9.18)
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `app.py` - Main application file

## 🚀 **Deploy to Render (5 minutes)**

### **Step 1: Push to GitHub**
```bash
git add .
git commit -m "Deploy to Render"
git push origin main
```

### **Step 2: Create Render Account**
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Authorize Render to access your repositories

### **Step 3: Create Web Service**
1. Click **"New"** → **"Web Service"**
2. Select your `Smart-AI-Resume-Analyzer` repository
3. Click **"Connect"**

### **Step 4: Configure Service**
```
Name: smart-resume-analyzer (or your preferred name)
Region: Oregon (US West) - or closest to your users
Branch: main
Root Directory: (leave empty)
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

### **Step 5: Add Environment Variables**
1. Scroll down to **"Environment Variables"**
2. Click **"Add Environment Variable"**
3. Add:
   ```
   Key: GOOGLE_API_KEY
   Value: your api key
   ```

### **Step 6: Deploy**
1. Click **"Create Web Service"**
2. Wait for the build to complete (5-10 minutes)
3. Your app will be live at: `https://your-app-name.onrender.com`

## 🎯 **What Happens During Deployment**

1. **Build Phase:**
   - Render clones your repository
   - Installs Python 3.9.18
   - Runs `pip install -r requirements.txt`
   - Sets up the environment

2. **Deploy Phase:**
   - Starts your Streamlit app
   - Makes it available on the internet
   - Provides HTTPS automatically

## 🔧 **Troubleshooting**

### **Build Fails?**
- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version in `runtime.txt`

### **App Won't Start?**
- Check the deploy logs
- Verify the start command is correct
- Ensure environment variables are set

### **Slow Performance?**
- Free tier has limited resources
- Consider upgrading to paid plan ($7/month)
- Optimize your code with caching

## 🎉 **Success!**

Your Smart AI Resume Analyzer is now live! 

**Features Available:**
- ✅ 8 AI Models for resume analysis
- ✅ Portfolio generation
- ✅ Resume scoring (0-100)
- ✅ ATS optimization
- ✅ Professional recommendations

**Share your app:**
- URL: `https://your-app-name.onrender.com`
- Custom domain: Available in Render settings
- HTTPS: Enabled by default

## 💡 **Pro Tips**

1. **Custom Domain:**
   - Go to Settings → Custom Domains
   - Add your domain and configure DNS

2. **Auto-Deploy:**
   - Render automatically deploys when you push to main branch
   - No manual deployment needed

3. **Monitoring:**
   - Check logs in Render dashboard
   - Monitor performance metrics
   - Set up alerts for downtime

4. **Scaling:**
   - Upgrade to paid plan for better performance
   - Enable auto-scaling if needed

**Your AI-powered resume analyzer is now helping users worldwide! 🌍**
