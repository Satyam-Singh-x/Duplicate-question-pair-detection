import streamlit as st
import pickle
import helper
import zipfile
import os


# ------------------ Paths ------------------ #
zip_path = "model.zip"         # Your ZIP file containing model.pkl
extract_path = "model_folder"  # Folder to extract

# ------------------ Unzip the model ------------------ #
os.makedirs(extract_path, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# ------------------ Load the model ------------------ #
model_path = os.path.join(extract_path, "model.pkl")
model = pickle.load(open(model_path, "rb"))


# ------------------ Page Config ------------------ #
st.set_page_config(
    page_title="Duplicate Question Detector",
    page_icon="📝",
    layout="centered"
)

# ------------------ Header ------------------ #
st.markdown(
    """
    <div style="text-align:center; background-color:#0B3D91; padding:20px; border-radius:10px;">
        <h1 style="color:white;">Duplicate Question Pairs Detector</h1>
        <p style="color:white; font-size:16px;">Enter two questions to check if they are duplicates</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ------------------ Input Section ------------------ #
col1, col2 = st.columns(2)
with col1:
    q1 = st.text_area("Enter Question 1", height=100)
with col2:
    q2 = st.text_area("Enter Question 2", height=100)

st.write("")

# ------------------ Predict Button ------------------ #
if st.button("Predict", type="primary"):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("Please enter both questions!")
    else:
        # Convert questions to feature vector
        query = helper.query_point_creator(q1, q2)

        # Ensure correct shape for RandomForest
        result = model.predict(query)[0]

        # ------------------ Display Result ------------------ #
        if result:
            st.success("✅ These questions are Duplicates")
        else:
            st.error("❌ These questions are Not Duplicates")

st.write("---")

# ------------------ Footer ------------------ #
st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:12px; margin-top:20px;">
        Built with ❤️ using Python, Streamlit & Scikit-learn
    </div>
    """,
    unsafe_allow_html=True
)



