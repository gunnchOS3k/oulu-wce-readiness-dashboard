import streamlit as st
from pathlib import Path
st.title('Oulu WCE Readiness Dashboard')
st.caption('Independent portfolio — not University of Oulu')
matrix = Path('results/oulu_wce_readiness_matrix.md')
if matrix.exists():
    st.markdown(matrix.read_text())
else:
    st.info('Run make e2e in oulu-wce-readiness-dashboard')
