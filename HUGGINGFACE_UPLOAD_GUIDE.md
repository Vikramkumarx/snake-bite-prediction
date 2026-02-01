# 🚀 HUGGING FACE MANUAL UPLOAD GUIDE

## Your Space: https://huggingface.co/spaces/DeSeRtSoLU/Snake-prediction

---

## ✅ FILES TO UPLOAD (Copy-Paste Method)

### **FILE 1: Dockerfile**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p static/uploads

# Expose port
EXPOSE 7860

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]
```

**How to upload:**
1. Go to your Space
2. Click "Add file" → "Create a new file"
3. Filename: `Dockerfile` (exactly, no extension)
4. Paste above content
5. Click "Commit new file to main"

---

### **FILE 2: requirements.txt**

```
Flask==3.1.0
Pillow==11.0.0
```

**How to upload:**
1. Click "Add file" → "Create a new file"
2. Filename: `requirements.txt`
3. Paste above content
4. Click "Commit new file to main"

---

### **FILE 3: app.py**

**Location on your PC:**
```
c:\Users\Chitranjan Kumar\.gemini\antigravity\scratch\snake-bite-prediction\app.py
```

**How to upload:**
1. Click "Add file" → "Upload files"
2. Select `app.py` from your project folder
3. Click "Commit changes to main"

**OR** Create new file and copy content from your local app.py

---

### **FILE 4: README.md**

**Location on your PC:**
```
c:\Users\Chitranjan Kumar\.gemini\antigravity\scratch\snake-bite-prediction\README.md
```

**How to upload:**
1. Click "Add file" → "Upload files"
2. Select `README.md`
3. Click "Commit changes to main"

---

### **FOLDER 1: templates/**

Upload all 7 HTML files:

**Method A: One by one**
```
1. Click "Add file" → "Create a new file"
2. Filename: templates/index.html
3. Copy content from: c:\Users\...\templates\index.html
4. Click "Commit"
5. Repeat for all 7 files:
   - templates/index.html
   - templates/about.html
   - templates/species.html
   - templates/safety.html
   - templates/statistics.html
   - templates/emergency.html
   - templates/quiz.html
```

**Method B: Upload folder (Easier)**
```
1. Click "Add file" → "Upload files"
2. Drag entire "templates" folder
3. Click "Commit changes to main"
```

---

### **FOLDER 2: demo_images/**

**Already uploaded!** ✅ (I can see them in your Space)

---

### **FOLDER 3: static/**

```
1. Click "Add file" → "Create a new file"
2. Filename: static/uploads/.gitkeep
3. Content: (leave empty)
4. Click "Commit"
```

---

## 📋 UPLOAD CHECKLIST

After uploading, verify these files exist:

```
✅ Dockerfile
✅ requirements.txt  
✅ app.py
✅ README.md
✅ templates/index.html
✅ templates/about.html
✅ templates/species.html
✅ templates/safety.html
✅ templates/statistics.html
✅ templates/emergency.html
✅ templates/quiz.html
✅ demo_images/ (already done)
✅ static/uploads/.gitkeep
```

---

## 🔄 AFTER UPLOAD

1. **Wait for Build** (2-5 minutes)
   - Check "App" tab
   - Build logs will show progress

2. **Check for Errors**
   - If red badge appears, click "Logs"
   - Fix any missing files

3. **Test Your App**
   - Once green badge appears
   - Click "App" tab
   - Test all features!

---

## 🌐 YOUR LIVE URL

After successful build:

**Space URL:**
```
https://huggingface.co/spaces/DeSeRtSoLU/Snake-prediction
```

**Direct App URL:**
```
https://desertsolu-snake-prediction.hf.space
```

---

## 💡 QUICK TIP

**Fastest Method:**

1. Upload `Dockerfile` (create new file, paste content)
2. Upload `requirements.txt` (create new file, paste content)
3. Upload `app.py` (upload file from PC)
4. Upload `templates/` folder (drag & drop entire folder)
5. Create `static/uploads/.gitkeep` (empty file)
6. Wait for build!

---

## 🆘 IF BUILD FAILS

Common issues:

1. **Missing Dockerfile** → Upload it
2. **Missing requirements.txt** → Upload it
3. **Missing app.py** → Upload it
4. **Missing templates/** → Upload folder
5. **Port issue** → app.py should use port 7860 (already fixed)

---

**Start with uploading Dockerfile and requirements.txt first!**

**Then upload app.py and templates folder!**

**Your app will be live in 5 minutes!** 🚀
