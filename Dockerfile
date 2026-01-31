FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create uploads directory
RUN mkdir -p static/uploads && chmod 777 static/uploads

# Expose port
EXPOSE 7860

# Start application
# Hugging Face Spaces uses 7860 as default port
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
