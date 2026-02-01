# 🚀 Hugging Face Deployment Guide

## Quick Deployment Steps

### **Method 1: Using Hugging Face Web Interface (Easiest)**

1. **Create Hugging Face Account**
   - Go to https://huggingface.co/join
   - Sign up with email/GitHub

2. **Create New Space**
   - Go to https://huggingface.co/new-space
   - **Space name**: `snake-bite-prediction`
   - **License**: MIT
   - **SDK**: Docker
   - **Hardware**: CPU (free tier)
   - Click "Create Space"

3. **Upload Files**
   - Click "Files" tab
   - Click "Add file" → "Upload files"
   - Upload these files:
     ```
     app.py
     Dockerfile
     requirements.txt
     README.md
     .gitignore
     templates/ (entire folder)
     demo_images/ (entire folder)
     static/ (entire folder)
     ```

4. **Wait for Build**
   - Hugging Face will automatically build your Docker container
   - Wait 2-5 minutes for deployment
   - Check "Logs" tab for progress

5. **Access Your App**
   - Your app will be live at:
     `https://huggingface.co/spaces/YOUR_USERNAME/snake-bite-prediction`

---

### **Method 2: Using Git (Advanced)**

1. **Install Git LFS**
   ```bash
   git lfs install
   ```

2. **Clone Your Space**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/snake-bite-prediction
   cd snake-bite-prediction
   ```

3. **Copy Project Files**
   ```bash
   # Copy all files from your project to the cloned repo
   ```

4. **Commit and Push**
   ```bash
   git add .
   git commit -m "Initial deployment: Snake Bite Prediction System"
   git push
   ```

5. **Wait for Build**
   - Check your Space URL for live deployment

---

### **Method 3: Using Hugging Face CLI (Recommended)**

1. **Install Hugging Face CLI**
   ```bash
   pip install huggingface_hub
   ```

2. **Login to Hugging Face**
   ```bash
   huggingface-cli login
   ```
   - Enter your Hugging Face token from: https://huggingface.co/settings/tokens

3. **Create Space**
   ```bash
   huggingface-cli repo create snake-bite-prediction --type space --space_sdk docker
   ```

4. **Push Files**
   ```bash
   cd c:\Users\Chitranjan Kumar\.gemini\antigravity\scratch\snake-bite-prediction
   
   git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/snake-bite-prediction
   git add .
   git commit -m "Deploy Snake Bite Prediction System"
   git push hf main
   ```

---

## 📋 Required Files Checklist

Make sure these files exist before deployment:

✅ `app.py` - Main Flask application  
✅ `Dockerfile` - Docker configuration  
✅ `requirements.txt` - Python dependencies  
✅ `README.md` - Hugging Face Space README  
✅ `.gitignore` - Git ignore rules  
✅ `templates/` - All HTML templates (7 files)  
✅ `demo_images/` - Demo snake images (13 files)  
✅ `static/` - Static files folder  

---

## 🔧 Troubleshooting

### **Build Failed?**

1. Check Dockerfile syntax
2. Verify requirements.txt has all dependencies
3. Check logs in Hugging Face Space

### **App Not Loading?**

1. Ensure port 7860 is used
2. Check app.py has `host='0.0.0.0'`
3. Verify all templates exist

### **Images Not Showing?**

1. Make sure `demo_images/` folder is uploaded
2. Check `static/uploads/` folder exists
3. Verify file paths in code

---

## 🌐 Your Live URLs

After deployment, your app will be available at:

**Space URL**: `https://huggingface.co/spaces/YOUR_USERNAME/snake-bite-prediction`

**Direct App**: `https://YOUR_USERNAME-snake-bite-prediction.hf.space`

**Embed**: `https://YOUR_USERNAME-snake-bite-prediction.hf.space/embed`

---

## 📊 Deployment Status

Check deployment status:
- ✅ Green badge = Running
- 🟡 Yellow badge = Building
- 🔴 Red badge = Failed

---

## 🎯 Post-Deployment

After successful deployment:

1. **Test All Features**
   - Upload image
   - Check theme toggle
   - Test PDF download
   - Try share feature
   - Test voice output
   - Check statistics
   - Verify quiz

2. **Share Your App**
   - Copy the Space URL
   - Share with teacher/friends
   - Add to your portfolio

3. **Monitor Usage**
   - Check Space analytics
   - View logs for errors
   - Monitor performance

---

## 💡 Tips

- **Free Tier**: CPU is free, sufficient for demo
- **GPU**: Upgrade if you add real model
- **Storage**: 50GB free storage
- **Bandwidth**: Unlimited for public Spaces
- **Uptime**: 24/7 availability

---

## 🔗 Useful Links

- **Hugging Face Spaces**: https://huggingface.co/spaces
- **Documentation**: https://huggingface.co/docs/hub/spaces
- **Docker SDK Guide**: https://huggingface.co/docs/hub/spaces-sdks-docker
- **Your Profile**: https://huggingface.co/YOUR_USERNAME

---

**Ready to deploy! Follow any method above and your app will be live in minutes! 🚀**
