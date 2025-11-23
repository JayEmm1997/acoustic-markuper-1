import streamlit as st
import ezdxf
import io

st.title("📐 DXF Line Counter")
st.write("Upload a DXF file and I will count all LINE entities inside it.")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file is not None:
    try:
        # Read file as bytes
        raw_bytes = uploaded_file.read()

        # DXF is a TEXT-BASED format → decode to string
        text_data = raw_bytes.decode("utf-8", errors="ignore")

        # Load DXF from decoded text
        doc = ezdxf.readtext(text_data)

        # Access modelspace
        msp = doc.modelspace()

        # Count LINE entities
        line_count = len(msp.query("LINE"))

        st.success(f"Total LINE entities: **{line_count}**")

    except Exception as e:
        st.error(f"Error reading DXF file: {str(e)}")
