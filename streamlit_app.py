import streamlit as st
import ezdxf
import io

st.title("📏 DXF Line Counter")
st.write("Upload a DXF file and I will count all LINE entities inside it.")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file is not None:
    try:
        # Read uploaded file as bytes
        data = uploaded_file.read()
        stream = io.BytesIO(data)

        # Load DXF document (works for R12, ASCII, Binary)
        doc = ezdxf.read(stream)
        msp = doc.modelspace()

        # Count LINE entities
        line_count = len(msp.query("LINE"))

        st.success(f"Total LINE entities: **{line_count}**")

    except Exception as e:
        st.error(f"Error reading DXF file: {str(e)}")
