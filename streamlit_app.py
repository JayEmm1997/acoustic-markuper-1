import streamlit as st
import ezdxf
import io

st.set_page_config(page_title="DXF Line Counter", layout="centered")

st.title("📐 DXF Line Counter")
st.write("Upload a DXF file and I will count all LINE entities inside it.")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file is not None:
    try:
        data = uploaded_file.read()
        stream = io.BytesIO(data)

        doc = ezdxf.read(stream)
        msp = doc.modelspace()
        line_count = len(msp.query("LINE"))

        st.success("DXF processed successfully!")
        st.metric("Total LINE entities", line_count)

    except Exception as e:
        st.error(f"Error reading DXF file: {e}")
