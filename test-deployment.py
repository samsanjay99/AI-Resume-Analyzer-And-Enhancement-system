#!/usr/bin/env python3
"""
Quick deployment test script
Tests if the app can start without heavy dependencies
"""

import sys
import os

def test_imports():
    """Test if all required imports work"""
    print("🧪 Testing Core Imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit")
    except ImportError as e:
        print(f"❌ Streamlit: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI")
    except ImportError as e:
        print(f"❌ Google Generative AI: {e}")
        return False
    
    try:
        from openai import OpenAI
        print("✅ OpenAI")
    except ImportError as e:
        print(f"❌ OpenAI: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas")
    except ImportError as e:
        print(f"❌ Pandas: {e}")
        return False
    
    try:
        import plotly
        print("✅ Plotly")
    except ImportError as e:
        print(f"❌ Plotly: {e}")
        return False
    
    return True

def test_optional_imports():
    """Test optional imports"""
    print("\n🔍 Testing Optional Imports...")
    
    optional_imports = [
        ("pdf2image", "convert_from_path"),
        ("pytesseract", None),
        ("selenium", "webdriver"),
        ("spacy", None)
    ]
    
    for module_name, attr in optional_imports:
        try:
            if attr:
                module = __import__(module_name, fromlist=[attr])
                getattr(module, attr)
            else:
                __import__(module_name)
            print(f"✅ {module_name} (optional)")
        except ImportError:
            print(f"⚠️ {module_name} (optional) - Not available")

def test_app_structure():
    """Test if app structure is correct"""
    print("\n📁 Testing App Structure...")
    
    required_files = [
        "app.py",
        "requirements.txt",
        "utils/ai_resume_analyzer.py",
        ".streamlit/config.toml"
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            return False
    
    return True

def test_environment():
    """Test environment variables"""
    print("\n🔑 Testing Environment...")
    
    # Check if API key is available (either in env or .env file)
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        print("✅ GOOGLE_API_KEY found in environment")
    else:
        # Try to load from .env file
        try:
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("GOOGLE_API_KEY")
            if api_key:
                print("✅ GOOGLE_API_KEY found in .env file")
            else:
                print("⚠️ GOOGLE_API_KEY not found (will need to be set in deployment)")
        except ImportError:
            print("⚠️ python-dotenv not available, can't check .env file")
    
    return True

def main():
    """Main test function"""
    print("🚀 Smart AI Resume Analyzer - Deployment Test")
    print("=" * 50)
    
    tests = [
        ("Core Imports", test_imports),
        ("App Structure", test_app_structure),
        ("Environment", test_environment)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"❌ {test_name} failed: {e}")
            results.append(False)
    
    # Test optional imports (doesn't affect pass/fail)
    test_optional_imports()
    
    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED - Ready for deployment!")
        print("\n🚀 Recommended deployment platforms:")
        print("1. Render: https://render.com")
        print("2. Railway: https://railway.app")
        print("3. Heroku: https://heroku.com")
        return True
    else:
        print("❌ Some tests failed - Fix issues before deployment")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)