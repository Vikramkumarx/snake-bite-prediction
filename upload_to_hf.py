"""
Upload all files to Hugging Face Space
Run this after logging in with: huggingface-cli login
"""

from huggingface_hub import HfApi, upload_folder
import os

# Your Hugging Face username and space name
USERNAME = "DeSeRtSoLU"  # Your username from screenshot
SPACE_NAME = "Snake-prediction"

# Create API instance
api = HfApi()

# Your space repo ID
repo_id = f"{USERNAME}/{SPACE_NAME}"
repo_type = "space"

print(f"🚀 Uploading to: {repo_id}")

# Files to upload
files_to_upload = [
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

# Upload individual files
for file in files_to_upload:
    if os.path.exists(file):
        print(f"📤 Uploading {file}...")
        api.upload_file(
            path_or_fileobj=file,
            path_in_repo=file,
            repo_id=repo_id,
            repo_type=repo_type
        )
        print(f"✅ {file} uploaded!")
    else:
        print(f"❌ {file} not found!")

# Upload folders
folders_to_upload = ["templates", "demo_images", "static"]

for folder in folders_to_upload:
    if os.path.exists(folder):
        print(f"📁 Uploading {folder}/ folder...")
        api.upload_folder(
            folder_path=folder,
            path_in_repo=folder,
            repo_id=repo_id,
            repo_type=repo_type
        )
        print(f"✅ {folder}/ uploaded!")
    else:
        print(f"❌ {folder}/ not found!")

print("\n🎉 All files uploaded successfully!")
print(f"🌐 Check your Space: https://huggingface.co/spaces/{repo_id}")
