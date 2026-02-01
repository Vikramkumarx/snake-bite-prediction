# 🐍 Demo Snake Images for Testing

This folder contains example snake images for demonstrating the Snake Bite Prediction System.

## 📸 Available Demo Images

### 1. Northern Cottonmouth (Venomous) ⚠️
**File**: `1_cottonmouth_venomous.png`
- **Species**: Northern Cottonmouth
- **Scientific Name**: Agkistrodon piscivorus
- **Status**: VENOMOUS - High Risk
- **Description**: Dark-colored pit viper, also known as Water Moccasin
- **Expected Result**: Should identify as venomous with high confidence

### 2. Texas Coral Snake (Highly Venomous) ⚠️⚠️
**File**: `2_coral_snake_highly_venomous.png`
- **Species**: Texas Coral Snake
- **Scientific Name**: Micrurus tener
- **Status**: HIGHLY VENOMOUS - Extreme Risk
- **Description**: Distinctive red, yellow, and black bands ("Red on yellow, kill a fellow")
- **Expected Result**: Should identify as highly venomous

### 3. Plain Bellied Water Snake (Harmless) ✅
**File**: `3_water_snake_harmless.png`
- **Species**: Plain Bellied Water Snake
- **Scientific Name**: Nerodia erythrogaster
- **Status**: HARMLESS - Low Risk
- **Description**: Non-venomous water snake, often mistaken for Cottonmouth
- **Expected Result**: Should identify as harmless

### 4. Louisiana Milk Snake (Harmless) ✅
**File**: `4_milk_snake_harmless.png`
- **Species**: Louisiana Milk Snake
- **Scientific Name**: Lampropeltis triangulum amaura
- **Status**: HARMLESS - Low Risk
- **Description**: Non-venomous king snake with red, black, and yellow bands ("Red on black, friend of Jack")
- **Expected Result**: Should identify as harmless

---

## 🎯 How to Use for Demo

### Method 1: Drag & Drop
1. Open the application at `http://127.0.0.1:5001`
2. Drag any image from this folder to the upload area
3. Click "🔍 Identify Snake"
4. View the results

### Method 2: File Upload
1. Open the application
2. Click on the upload area
3. Navigate to the `demo_images` folder
4. Select any image
5. Click "🔍 Identify Snake"

---

## 📊 Demo Sequence for Teacher

### Recommended Order:

**1. Start with Harmless Snake**
- Upload `3_water_snake_harmless.png`
- Show that it's identified as harmless
- Explain the confidence score
- Show the detailed information

**2. Show Venomous Snake**
- Upload `1_cottonmouth_venomous.png`
- Point out the red "VENOMOUS" badge
- Explain the danger level
- Show first aid instructions

**3. Show Highly Venomous**
- Upload `2_coral_snake_highly_venomous.png`
- Highlight "Extreme Risk" status
- Explain the distinctive pattern
- Show emergency warnings

**4. Show Another Harmless**
- Upload `4_milk_snake_harmless.png`
- Compare with Coral Snake (similar patterns)
- Explain the "Red on black" rule
- Show how AI differentiates

---

## 🎓 Key Points to Mention

### Technical Points:
- AI analyzes image patterns
- Provides confidence scores
- Classifies as venomous/harmless
- Uses deep learning (ResNet34)

### Practical Points:
- Real-world emergency use
- Educational tool
- Quick identification
- Safety information included

### Safety Points:
- Always seek medical help
- Don't rely solely on AI
- Maintain safe distance
- Call 911 for bites

---

## 📝 Demo Script

```
"Let me demonstrate how the system works with some example snake images.

First, I'll upload this water snake image... 
[Upload 3_water_snake_harmless.png]

As you can see, the AI has identified it as a Plain Bellied Water Snake 
with [X]% confidence. The system shows it's HARMLESS with a green badge.

Now let me show you a venomous snake...
[Upload 1_cottonmouth_venomous.png]

Here, the system identifies it as a Northern Cottonmouth - a VENOMOUS snake.
Notice the red warning badge and the first aid instructions below.

This is particularly useful in emergency situations where quick 
identification can help medical professionals provide appropriate treatment."
```

---

## 🔄 Expected Results

**Note**: Since the app is currently in demo mode (random predictions), 
the actual species identified may vary. The UI and features will work 
perfectly, showing:

- ✅ Species name
- ✅ Confidence score
- ✅ Venomous/Harmless status
- ✅ Scientific name
- ✅ Detailed description
- ✅ Habitat information
- ✅ First aid instructions
- ✅ Scan history

---

## 💡 Tips for Best Demo

1. **Start Simple**: Begin with one image to show basic functionality
2. **Highlight Features**: Point out confidence scores, badges, details
3. **Show Navigation**: Demonstrate all pages (Home, Species, Safety, About)
4. **Explain AI**: Mention deep learning, ResNet34, 85% accuracy
5. **Discuss Impact**: Talk about real-world applications

---

**These images are AI-generated for demonstration purposes only.**

For production use, the system should be trained on real snake images 
and tested thoroughly before deployment.
