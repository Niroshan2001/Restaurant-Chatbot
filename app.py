import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(layout="wide")

# Simulated Menu Data (Food Item, Price, and Image URL)
menu_data = [
    {"name": "Pizza", "price": 8, "image_path": "pizza.png"},
    {"name": "Biriyani", "price": 9, "image_path": "Biriyani.png"},
    {"name": "Samosa", "price": 5, "image_path": "samosa.jpg"},
    {"name": "Chole Bhature", "price": 7, "image_path": "chola bhature.png"},
    {"name": "Mango Lassi", "price": 5, "image_path": "mango lassi.jpg"},
    {"name": "Masala Dosa", "price": 6, "image_path": "masala dosa.jpg"},
    {"name": "Rava Dosa", "price": 7, "image_path": "rava dosa.png"},
    {"name": "Vada Pav", "price": 4, "image_path": "vada pav.jpg"},
]

# Function to load and resize local images
def load_and_resize_image(image_path, size=(200, 200)):
    img = Image.open(image_path)
    img = img.resize(size)
    return img


# Create tabs for navigation
st.title("Serandib Spice House")
tabs = st.tabs(["Home", "About", "Contact Us"])



# Home Page Tab
with tabs[0]:
    
    st.image("main.jpg", use_column_width=True)
    st.title("Menu")
    # Display the menu items in rows of three
    for i in range(0, len(menu_data), 3):
        cols = st.columns(3)  # Create three columns

        for idx, col in enumerate(cols):
            if i + idx < len(menu_data):  # To avoid out-of-range index errors
                item = menu_data[i + idx]
                resized_img = load_and_resize_image(item["image_path"])  # Resize image
                col.subheader(f"{item['name']} - ${item['price']:.2f}")
                col.image(resized_img, caption=item['name'], use_column_width=True)

# About Page Tab
with tabs[1]:
    st.markdown("<h1 style='text-align: center;'>About Us</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([3,2])
    
    with col1:
        
        st.header("Welcome to Serendib Spice House")
        st.write(
           """
            Established in 1998, Serendib Spice House has been a cornerstone of Colombo's dining scene, merging the rich culinary traditions of South and North India. Our restaurant offers a diverse menu that includes both vegetarian and non-vegetarian dishes, catering to a wide range of preferences.

            Our philosophy is rooted in using only the freshest ingredients and authentic spices to craft our flavorful dishes. Whether you're looking for vegan delights or indulgent non-veg options, our menu is designed to offer something for everyone. 

            Over the years, we have cultivated a reputation for excellence, thanks to our commitment to high standards in both food quality and service. Our loyal customers, many of whom have been with us since the beginning, are a testament to the enduring appeal of our cuisine.

            At Serendib Spice House, we strive to create a warm and inviting atmosphere where every meal is a celebration of tradition and taste. We invite you to experience our unique blend of flavors and enjoy a dining experience that has been cherished by many for decades.
        """)
    with col2:
        st.image("main.jpg", use_column_width=True)

# Contact Us Page Tab
with tabs[2]:
    st.markdown("<h1 style='text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
    with col1:
        st.write("""
        We'd love to hear from you! Please reach out to us with any questions or feedback.
            
            Phone: +94 11 123 4567
            Email: serendib@restaurant.com
            Address: No. 5,Fedrica Road,Wellawatte, Colombo 00600, Sri Lanka
                 
        
    """)
        st.markdown("### Hours of Operation")
        st.write("""
            **Monday to Friday**: 11:00 AM - 10:00 PM  
            **Saturday and Sunday**: 12:00 PM - 11:00 PM
           """) 
    with col2:
        st.image("map.png", use_column_width=True)
    