from fastai.vision.all import *
from duckduckgo_search import DDGS
from pathlib import Path
import time
import requests

def download_images_custom(label, query, path, max_images=30):
    dest = path/label
    dest.mkdir(exist_ok=True, parents=True)
    
    print(f"Searching: {label}")
    results = []
    try:
        with DDGS() as ddgs:
            # Use 'cobra' as a fallback to see if it's the query being too specific
            res = ddgs.images(query, max_results=max_images)
            for r in res:
                if r.get('image'):
                    results.append(r.get('image'))
    except Exception as e:
        print(f"Search error for {label}: {e}")

    download_count = 0
    for url in results:
        try:
            filename = f"img_{download_count:04d}.jpg"
            response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                with open(dest/filename, 'wb') as f:
                    f.write(response.content)
                download_count += 1
                if download_count >= max_images: break
        except Exception:
            continue
    print(f"Downloaded {download_count} images for {label}.")

def train_snake_model():
    print("Starting Snake Model Training...")
    
    # Generic names for better search success
    snake_types = ["Water Snake", "Cottonmouth Snake", 
                   "Coral Snake", "Milk Snake"]
    
    path = Path('snake_dataset_v2')
    if not path.exists(): path.mkdir()
    
    for s in snake_types:
        download_images_custom(s, s, path, max_images=20)
        time.sleep(2)

    # Check image count
    all_files = get_image_files(path)
    print(f"Total images found: {len(all_files)}")
    if len(all_files) < 10:
        print("CRITICAL: Not enough images. Training cancelled.")
        return

    # 2. Prepare DataLoaders
    print("Preparing DataLoaders...")
    dls = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=[Resize(224, method='squish')]
    ).dataloaders(path, bs=8)
    
    dls.to('cpu')


    # 3. Train Model
    print("Training Neural Network...")
    learn = vision_learner(dls, resnet18, metrics=accuracy)
    learn.fine_tune(2)

    # 4. Export Model
    print("Exporting model to snake.pkl...")
    learn.export('snake.pkl')
    print("SUCCESS: snake.pkl has been created in the project root!")

if __name__ == "__main__":
    try:
        train_snake_model()
    except Exception as e:
        import traceback
        traceback.print_exc()
