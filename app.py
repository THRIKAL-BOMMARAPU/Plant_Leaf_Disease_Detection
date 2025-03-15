import streamlit as st
import tensorflow as tf
import numpy as np

# Set page config
st.set_page_config(
    page_title="Plant Disease Detector",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for navigation buttons
st.markdown("""
    <style>
    .nav-button {
        background-color: transparent !important;
        border: 2px solid #4CAF50 !important;
        color: #2E8B57 !important;
        padding: 10px 24px !important;
        margin: 5px !important;
        border-radius: 5px !important;
        width: 200px !important;
    }
    .nav-button:hover {
        background-color: #E8F5E9 !important;
    }
    .selected {
        background-color: #4CAF50 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation handler
def set_page(page: str):
    st.query_params["page"] = page

# Get current page from query parameters
current_page = st.query_params.get("page", "home")

# Navigation bar
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.button("🏠 Home", 
             on_click=set_page, args=("home",), 
             disabled=(current_page == "home"),
             use_container_width=True,
             key="home_btn",
             help="Go to Home Page")
with col2:
    st.button("📚 About", 
             on_click=set_page, args=("about",), 
             disabled=(current_page == "about"),
             use_container_width=True,
             key="about_btn",
             help="Learn about the project")
with col3:
    st.button("🔍 Diagnosis", 
             on_click=set_page, args=("diagnosis",), 
             disabled=(current_page == "diagnosis"),
             use_container_width=True,
             key="diagnosis_btn",
             help="Start disease diagnosis")

# Tensorflow Model Prediction (keep this function unchanged)
def model_prediction(test_image):
    model = tf.keras.models.load_model("plant_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

# Page content based on current page
if current_page == "home":
    st.header("🌿 Smart Plant Disease Detection System")
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("homepage.jpg", use_container_width=True, caption="Healthy Crops, Better Harvest")
    
    with col2:
        st.markdown("""
        ### Welcome to Agricultural AI Guardian
        Our cutting-edge system helps farmers and gardeners identify plant diseases 
        with **95%+ accuracy** using deep learning technology.
        
        **Key Features:**
        - 🚀 Instant disease detection
        - 🌾 Supports 38+ plant species
        - 📸 Simple image-based analysis
        - 📊 Real-time results
        
        ### How It Works
        1. **Capture** a clear photo of the affected plant leaf
        2. **Upload** using our simple interface
        3. **Analyze** with our AI engine
        """)
        st.success("Start by visiting the **Disease Recognition** page from the sidebar!")


elif current_page == "about":
    st.header("📚 About This Project")
    st.markdown("---")
    
    with st.expander("🌐 Project Overview", expanded=True):
        st.markdown("""
        This project aims to democratize plant health diagnostics using accessible AI technology.
        Our system helps:
        - Small farmers detect crop issues early
        - Gardeners maintain plant health
        - Agricultural students learn about plant pathology
        """)
    
    with st.expander("📂 Dataset Information"):
        st.markdown("""
        **Dataset Overview:**
        - Source: PlantVillage dataset
        - Total Images: ~87,000 RGB images
        - Categories: 38 plant disease classes
        - Split: 80% training, 20% validation
        """)
    
    with st.expander("🛠️ Technical Details"):
        st.markdown("""
        **Model Architecture:**
        - Deep CNN with residual connections
        - Transfer learning from ImageNet
        - Optimized for mobile deployment
        
        **Performance Metrics:**
        - Training Accuracy: 98.7%
        - Validation Accuracy: 96.2%
        - Inference Time: <500ms
        """)

elif current_page == "diagnosis":
    st.header("🔍 Disease Diagnosis")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("1. Upload Image")
        test_image = st.file_uploader("Choose a plant leaf image:", 
                                    type=["jpg", "png", "jpeg"],
                                    label_visibility="collapsed")
        
        if test_image:
            st.subheader("2. Image Preview")
            st.image(test_image, use_container_width=True, caption="Uploaded Leaf Image")
            
            # Place button in the same column after image preview
            analyze_button = st.button("🧪Analyze Disease", type="primary")
    
    with col2:
        if test_image and analyze_button:
            with st.spinner("Analyzing leaf patterns..."):
                result_index = model_prediction(test_image)
                
                class_name = ['Apple - Apple Scab', 'Apple - Black Rot', 
                            'Apple - Cedar Rust', 'Apple - Healthy',
                            'Blueberry - Healthy', 'Cherry - Powdery Mildew', 
                            'Cherry - Healthy', 'Corn - Gray Leaf Spot', 
                            'Corn - Common Rust', 'Corn - Northern Blight', 
                            'Corn - Healthy', 'Grape - Black Rot', 
                            'Grape - Esca', 'Grape - Leaf Blight', 
                            'Grape - Healthy', 'Orange - Citrus Greening', 
                            'Peach - Bacterial Spot', 'Peach - Healthy', 
                            'Bell Pepper - Bacterial Spot', 'Bell Pepper - Healthy', 
                            'Potato - Early Blight', 'Potato - Late Blight', 
                            'Potato - Healthy', 'Raspberry - Healthy', 
                            'Soybean - Healthy', 'Squash - Powdery Mildew', 
                            'Strawberry - Leaf Scorch', 'Strawberry - Healthy', 
                            'Tomato - Bacterial Spot', 'Tomato - Early Blight', 
                            'Tomato - Late Blight', 'Tomato - Leaf Mold', 
                            'Tomato - Septoria Spot', 'Tomato - Spider Mites', 
                            'Tomato - Target Spot', 'Tomato - Yellow Curl Virus', 
                            'Tomato - Mosaic Virus', 'Tomato - Healthy']
                
                result = class_name[result_index]
                plant, status = result.split(" - ")
                
                st.markdown("---")
                st.subheader("Diagnosis Results")
                
                if "Healthy" in status:
                    st.success(f"**{plant} Status:** 🍃 {status}")
                    st.markdown("🎉 Great news! No significant disease detected!")
                else:
                    st.error(f"**{plant} Status:** ⚠️ {status}")
                    st.markdown(f"""
                    **Recommended Actions:**
                    - 🚨 Isolate affected plants immediately
                    - 🌱 Apply recommended treatment for {status}
                    - 📅 Monitor plant health daily
                    - 📚 Consult agricultural extension services
                    """)
                    
                st.markdown("""
                **Next Steps:**
                1. Confirm diagnosis with local expert
                2. Implement treatment plan
                3. Rescan after 3 days
                """)

        elif not test_image and 'analyze_button' in locals():
            st.warning("⚠️ Please upload an image first!")
