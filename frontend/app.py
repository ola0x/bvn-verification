import cv2
import numpy as np
import streamlit as st
from PIL import Image

if __name__ == "__main__":

    st.header('BVN Verification')

    img_file_buff = st.camera_input("Capture Face")

    if img_file_buff is not None:

        img = Image.open(img_file_buff)

        img_arr = np.array(img)

        st.write(img_arr.shape)
