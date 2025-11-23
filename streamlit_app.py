import streamlit as st
import ezdxf
import io

st.title("📐 DXF Line Counter")
st.write("Upload a DXF file and I will count all LINE entities inside it.")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file is not None:
    try:
        data = uploaded_file.read()             # <-- bytes
        stream = io.BytesIO(data)               # <-- convert to byte stream

        doc = ezdxf.read(stream)                # <-- correct
        msp = doc.modelspace()

        line_count = len(msp.query("LINE"))

        st.success(f"Total LINE entities: **{line_count}**")

    except Exception as e:
        st.error(f"Error reading DXF file: {str(e)}")
