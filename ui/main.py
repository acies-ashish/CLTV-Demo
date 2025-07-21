# ui/main.py

import streamlit as st
from collections import defaultdict
from ui.data_dictionary import SHEET_NAME_MAP, show_data_dictionary, show_data_dictionary_combined

def render_main_content(DATA_DEFINITIONS, generate_cltv_analysis):
    st.title("CLV Potential Analysis")

    selected = sorted(st.session_state.selected_sources)
    analysis = generate_cltv_analysis(selected)

    if not selected:
        st.info("Select data sources from the sidebar to view the CLV analysis. Once selected, a detailed breakdown of CLV capabilities, outcomes, and limitations will appear here.")
        return

    # --- Section 1: The Selected Data & How It Connects ---
    st.subheader("The Selected Data & How It Connects")
    st.markdown("<h5>Your Selected Data Sources:</h5>", unsafe_allow_html=True)

    # Display icons/names for each source selected
    icons_row = " ".join(
        f"<span class='selected-source-item'>{DATA_DEFINITIONS[source]['icon']} {source}</span>"
        for source in selected
    )
    st.markdown(icons_row, unsafe_allow_html=True)

    # --- Combined Data Dictionary Table ---
    st.markdown("<h6>Available Fields & Connections:</h6>", unsafe_allow_html=True)
    sheet_names = [SHEET_NAME_MAP[source] for source in selected]
    if len(selected) == 1:
        show_data_dictionary(SHEET_NAME_MAP[selected[0]])
    else:
        show_data_dictionary_combined(selected)
        st.markdown(
            "<p class='info-note'><i>Rows highlighted in blue are fields common to multiple selected data sources, indicating potential connection points. The left-most column specifies the original source for each field.</i></p>",
            unsafe_allow_html=True
        )

    # --- Section 2: CLTV Capabilities and Insights ---
    st.subheader("CLTV Capabilities and Insights")

    st.markdown("<h5>What CLTV Can Be Calculated?</h5>", unsafe_allow_html=True)
    st.markdown(f"<p>{analysis['cltv_type']}</p>", unsafe_allow_html=True)

    # --- Outcomes Block ---
    st.markdown("""
    <div style='border: 1px solid #E5E7EB; border-radius: 8px; padding: 16px; background-color: #F9FAFB; margin-bottom: 24px;'>
        <h5>Outcomes:</h5>
        <div style='color:#4B5563; line-height:1.6;'>
            """ + analysis['outcome'] + """
    """, unsafe_allow_html=True)

    # --- Can Explain Block ---
    st.markdown("""
    <div style='border: 1px solid #10B981; border-radius: 8px; padding: 16px; background-color: #ECFDF5; margin-bottom: 24px;'>
        <h5 style='color:#065F46;'>Can Explain:</h5>
        <div style='color:#065F46; line-height:1.6;'>
            """ + analysis['explains'] + """
    """, unsafe_allow_html=True)

    # --- Cannot Explain Block ---
    st.markdown("""
    <div style='border: 1px solid #EF4444; border-radius: 8px; padding: 16px; background-color: #FEF2F2; margin-bottom: 24px;'>
        <h5 style='color:#991B1B;'>Cannot Explain:</h5>
        <div style='color:#991B1B; line-height:1.6;'>
            """ + analysis['does_not_explain'] + """
    """, unsafe_allow_html=True)
