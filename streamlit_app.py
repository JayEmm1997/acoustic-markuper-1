import streamlit as st
import dxfgrabber
import matplotlib.pyplot as plt

st.set_page_config(page_title="DXF Preview", layout="wide")
st.title("📐 DXF Preview Tool")

uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

if uploaded_file:
    try:
        # Read the DXF file (works for ASCII + binary DXF)
        dxf = dxfgrabber.read(uploaded_file)

        # Extract LINE entities for preview
        lines = [e for e in dxf.entities if e.dxftype == "LINE"]

        st.success(f"DXF Loaded Successfully — {len(lines)} line entities found")

        # Plot
        fig, ax = plt.subplots()
        for line in lines:
            x = [line.start[0], line.end[0]]
            y = [line.start[1], line.end[1]]
            ax.plot(x, y, color="black")

        ax.set_aspect("equal", "box")
        ax.set_title("DXF Preview")
        ax.invert_yaxis()  # DXF coordinate system fix

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Failed to read DXF: {e}")
