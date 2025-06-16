# 🌿 Plant Leaf Disease Detection

A deep learning-based web application for identifying diseases in plant leaves using image classification. Built with Python and TensorFlow, this app helps detect common plant diseases early by analyzing uploaded leaf images.

---

## 🧠 Project Objective

To assist in **early detection of plant diseases** by analyzing images of leaves and classifying them into healthy or diseased categories using a trained deep learning model.

---

## ✨ Features

- 🖼️ Upload a plant leaf image
- 🤖 Predict whether the plant is healthy or diseased
- 📊 Model trained using TensorFlow/Keras
- 💻 Simple and interactive web interface using Streamlit

---

## 🛠️ Technologies Used

| Tool/Library      | Purpose                                 |
|-------------------|------------------------------------------|
| Python            | Core language                            |
| TensorFlow / Keras| Deep learning model for image classification |
| Streamlit         | Web interface for interaction            |
| Pillow            | Image processing                         |

---

## 📁 Project Structure

```

plant-leaf-disease-detection/
├── app.py                 # Streamlit app logic
├── plant\_model.keras      # Trained deep learning model
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md

````

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure Python is installed. Then install the required dependencies:

```bash
pip install -r requirements.txt
````

---

### ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`.

---

## 🔮 How It Works

1. User uploads an image of a plant leaf.
2. Image is preprocessed and passed into the trained CNN model.
3. Model returns a prediction label (e.g., "Healthy", "Bacterial Spot", "Leaf Mold").
4. The app displays the result with relevant confidence.

---

## 🎯 Future Improvements

* Add camera capture support for mobile users
* Show prediction confidence and remedy tips
* Expand dataset to cover more plant species
* Deploy to a cloud platform (Streamlit Cloud, Heroku, etc.)

---

