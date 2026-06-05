import streamlit as st
from pathlib import Path
st.title('gunnchOS Wireless Engineering Readiness Dashboard')
st.caption('Independent portfolio — not target wireless communications engineering programs')
matrix = Path('results/oulu_wce_readiness_matrix.md')
if matrix.exists():
    st.markdown(matrix.read_text())
else:
    st.info('Run make e2e in gunnchos-wireless-engineering-readiness-dashboard')
