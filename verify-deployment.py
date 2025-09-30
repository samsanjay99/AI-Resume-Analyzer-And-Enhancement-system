#!/usr/bin/env python3
"""
Deployment verification script for Smart AI Resume Analyzer
Checks if all required files and configurations are ready for deployment
"""

import os
import sys
from pathlib import Path

def check_file_exists(file_path, description):
    """Check if a file exists and print status"""
    if Path(file_path).exists():
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ {description}: {file_path} - MISSING")
        return False

def check_file_content(file_path, required_content, description):
    """Check if file contains required content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if required_content in content:
                print(f"✅ {description}")
                return True
            else:
                print(f"❌ {description} - MISSING CONTENT")
                return False
    except FileNotFoundError:
        print(f"❌ {description} - FILE NOT FOUND")
        return False

def main():
    """Main verification function"""
    print("🔍 Smart AI Resume Analyzer - Deployment Verification")
    print("=" * 60)
    
    checks_passed = 0
    total_checks = 0
    
    # Check required files
    required_files = [
        ("app.py", "Main application file"),
        ("requirements.txt", "Python dependencies"),
        ("runtime.txt", "Python version specification"),
        ("Procfile", "Process file for Heroku"),
        (".streamlit/config.toml", "Streamlit configuration"),
        ("Dockerfile", "Docker configuration"),
        ("README.md", "Documentation")
    ]
    
    for file_path, description in required_files:
        if check_file_exists(file_path, description):
            checks_passed += 1
        total_checks += 1
    
    print("\n" + "=" * 60)
    print("📋 CONTENT VERIFICATION")
    print("=" * 60)
    
    # Check file contents
    content_checks = [
        ("requirements.txt", "streamlit", "Streamlit dependency"),
        ("requirements.txt", "openai", "OpenAI dependency"),
        ("requirements.txt", "google-generativeai", "Google AI dependency"),
        ("runtime.txt", "python-3.9", "Python version"),
        ("Procfile", "streamlit run app.py", "Streamlit start command"),
        (".streamlit/config.toml", "[server]", "Streamlit server config"),
        ("app.py", "AIResumeAnalyzer", "AI analyzer import"),
        ("app.py", "st.set_page_config", "Streamlit page config")
    ]
    
    for file_path, content, description in content_checks:
        if check_file_content(file_path, content, description):
            checks_passed += 1
        total_checks += 1
    
    print("\n" + "=" * 60)
    print("🔑 ENVIRONMENT VARIABLES")
    print("=" * 60)
    
    # Check environment variables
    env_vars = [
        ("GOOGLE_API_KEY", "Google Gemini API key")
    ]
    
    for var_name, description in env_vars:
        if var_name in os.environ:
            print(f"✅ {description}: Set")
            checks_passed += 1
        else:
            print(f"⚠️ {description}: Not set (will need to be set in deployment platform)")
        total_checks += 1
    
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)
    
    pass_rate = (checks_passed / total_checks) * 100
    print(f"Checks Passed: {checks_passed}/{total_checks}")
    print(f"Pass Rate: {pass_rate:.1f}%")
    
    if pass_rate >= 90:
        print("🎉 READY FOR DEPLOYMENT!")
        print("Your app is ready to deploy to any platform.")
    elif pass_rate >= 75:
        print("⚠️ MOSTLY READY - Minor issues to fix")
        print("Fix the missing items above before deploying.")
    else:
        print("❌ NOT READY - Major issues found")
        print("Please fix the issues above before attempting deployment.")
    
    print("\n" + "=" * 60)
    print("🚀 DEPLOYMENT PLATFORMS")
    print("=" * 60)
    print("Recommended platforms:")
    print("1. 🎨 Render: https://render.com (Free tier available)")
    print("2. 🚂 Railway: https://railway.app (Free $5 credit)")
    print("3. 🟣 Heroku: https://heroku.com (Free tier limited)")
    print("4. 💧 DigitalOcean: https://cloud.digitalocean.com (Paid)")
    
    print("\n📚 For detailed deployment instructions, see:")
    print("- DEPLOYMENT.md - Complete deployment guide")
    print("- deploy-render.md - Quick Render deployment")
    
    return pass_rate >= 75

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)