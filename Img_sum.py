import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
api=os.getenv("GEMINI_API_KEY")


def get_gemini_response(sys_prompt,image,input_prompt):
    genai.configure(api_key=api)
    model=genai.GenerativeModel(model_name="gemini-pro-vision")
    res=model.generate_content([sys_prompt,image,input_prompt])
    
    return res.text

sys_prompt='''Embark on a journey of clarity with Pixel Precision. As a professional image summarizer, we decode visual narratives 
with unrivaled precision. Our algorithms dissect every pixel, unveiling the true essence of images. From vibrant cityscapes to serene landscapes,
we deliver concise yet insightful summaries that capture the essence of every scene. Let us redefine your understanding of images, where accuracy
meets artistry. Welcome to Pixel Precision, where clarity knows no bounds.'''
  
st.title("Image Summary Genrator")
st.text("Play with your Image")

image1=st.file_uploader("Upload the Image you want to summarize ",help="Please upload the file")


if image1 is not None :
    st.image(Image.open(image1),caption="Uploaded image",use_column_width=True)
    
    
input_prompt=st.text_area("Ask about your image")


submit=st.button("Submit")

if submit:
    
    if input_prompt is not None and image1 is not None:
        
        image=Image.open(image1)
        a=get_gemini_response(sys_prompt,image,input_prompt)
        st.subheader("The Genrated response is....")
        st.write(a)
        
        
    else:
        st.warning("Ask about the image")
    



