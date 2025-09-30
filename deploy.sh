#!/bin/bash

# Smart AI Resume Analyzer - Deployment Script
# This script helps deploy to various platforms

echo "🚀 Smart AI Resume Analyzer - Deployment Helper"
echo "================================================"

# Function to deploy to Railway
deploy_railway() {
    echo "🚂 Deploying to Railway..."
    echo "1. Make sure you have Railway CLI installed: npm install -g @railway/cli"
    echo "2. Login to Railway: railway login"
    echo "3. Initialize project: railway init"
    echo "4. Set environment variables:"
    echo "   railway variables set GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU"
    echo "5. Deploy: railway up"
    echo ""
    echo "Or use the web interface at https://railway.app"
}

# Function to deploy to Render
deploy_render() {
    echo "🎨 Deploying to Render..."
    echo "1. Go to https://render.com"
    echo "2. Click 'New' -> 'Web Service'"
    echo "3. Connect your GitHub repository"
    echo "4. Use these settings:"
    echo "   Build Command: pip install -r requirements.txt"
    echo "   Start Command: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0 --server.headless=true"
    echo "5. Add environment variable:"
    echo "   GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU"
}

# Function to deploy to Heroku
deploy_heroku() {
    echo "🟣 Deploying to Heroku..."
    if command -v heroku &> /dev/null; then
        echo "Heroku CLI found. Proceeding with deployment..."
        
        # Check if we're in a git repository
        if [ ! -d ".git" ]; then
            echo "Initializing git repository..."
            git init
            git add .
            git commit -m "Initial commit for Heroku deployment"
        fi
        
        echo "Creating Heroku app..."
        read -p "Enter your app name (or press Enter for auto-generated): " app_name
        
        if [ -z "$app_name" ]; then
            heroku create
        else
            heroku create $app_name
        fi
        
        echo "Setting environment variables..."
        heroku config:set GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU
        
        echo "Deploying to Heroku..."
        git add .
        git commit -m "Deploy to Heroku"
        git push heroku main
        
        echo "Opening your app..."
        heroku open
    else
        echo "Heroku CLI not found. Please install it first:"
        echo "https://devcenter.heroku.com/articles/heroku-cli"
    fi
}

# Function to deploy to DigitalOcean
deploy_digitalocean() {
    echo "💧 Deploying to DigitalOcean App Platform..."
    echo "1. Go to https://cloud.digitalocean.com"
    echo "2. Click 'Create' -> 'Apps'"
    echo "3. Connect your GitHub repository"
    echo "4. Configure the app with these settings:"
    echo "   Run Command: streamlit run app.py --server.port=8080 --server.address=0.0.0.0"
    echo "5. Add environment variable:"
    echo "   GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU"
}

# Function to deploy with Docker
deploy_docker() {
    echo "🐳 Building and running with Docker..."
    
    echo "Building Docker image..."
    docker build -t smart-resume-analyzer .
    
    echo "Running Docker container..."
    docker run -p 8501:8501 \
        -e GOOGLE_API_KEY=AIzaSyDorhD_LnZUS5D2zNE9fQ-vP0FbxaxC_qU \
        smart-resume-analyzer
}

# Main menu
echo "Choose your deployment platform:"
echo "1. Railway (Recommended)"
echo "2. Render"
echo "3. Heroku"
echo "4. DigitalOcean"
echo "5. Docker (Local)"
echo "6. Exit"

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        deploy_railway
        ;;
    2)
        deploy_render
        ;;
    3)
        deploy_heroku
        ;;
    4)
        deploy_digitalocean
        ;;
    5)
        deploy_docker
        ;;
    6)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Deployment instructions provided!"
echo "📚 For detailed instructions, check DEPLOYMENT.md"