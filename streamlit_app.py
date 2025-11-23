import streamlit as st
import ezdxf
import io

st.title("📐 DXF Preview Tool")
st.write("Upload a DXF file and I will display its basic contents.")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file:
    try:
        # Read file as raw bytes
        data = uploaded_file.getvalue()

        # Convert bytes to stream
        stream = io.BytesIO(data)

        # Load DXF (correct call)
        doc = ezdxf.read(stream)

        # Access modelspace
        msp = doc.modelspace()

        # Count LINE entities
        line_count = len(msp.query("LINE"))

        st.success(f"DXF loaded successfully! Total LINE entities: {line_count}")

        # Preview first 20 entities
        preview = []
        for entity in msp:
            preview.append(str(entity))
            if len(preview) >= 20:
                break

        st.code("\n".join(preview))

    except Exception as e:
        st.error(f"Failed to read DXF: {str(e)}")
