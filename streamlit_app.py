import streamlit as st
import ezdxf
import io

st.title("📐 DXF Preview Tool")
st.write("Upload a DXF file and I will display its basic contents.")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file:
    try:
        # ALWAYS use getvalue() → returns bytes
        data = uploaded_file.getvalue()

        # Feed bytes into BytesIO
        stream = io.BytesIO(data)

        # Load DXF from stream
        doc = ezdxf.read(stream=stream)

        # Access modelspace
        msp = doc.modelspace()

        # Count LINE entities
        line_count = len(msp.query("LINE"))

        st.success(f"DXF loaded successfully! Total LINE entities: {line_count}")

        # Show preview of first 20 entities
        preview = []
        for e in msp:
            preview.append(str(e))
            if len(preview) >= 20:
                break

        st.code("\n".join(preview))

    except Exception as e:
        st.error(f"Failed to read DXF: {str(e)}")
