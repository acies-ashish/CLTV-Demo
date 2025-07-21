import streamlit as st
from collections import defaultdict

def render_main_content(DATA_DEFINITIONS, generate_cltv_analysis):
    st.title("CLV Potential Analysis")
    
    selected = sorted(st.session_state.selected_sources)
    analysis = generate_cltv_analysis(selected)
    
    if not selected:
        st.info("Select data sources from the sidebar to view the CLV analysis. Once selected, a detailed breakdown of CLV capabilities, outcomes, and limitations will appear here.")
    else:
        # --- Section 1: The Selected Data & How It Connects ---
        st.subheader("The Selected Data & How It Connects")
        
        st.markdown("<h5>Your Selected Data Sources:</h5>", unsafe_allow_html=True)
        
        selected_display_html = "".join([
            f"<span class='selected-source-item'><span class='icon'>{DATA_DEFINITIONS[s]['icon']}</span> {s}</span>" 
            for s in selected
        ])
        st.markdown(f"<div style='display: flex; flex-wrap: wrap; margin-bottom: 1.5rem;'>{selected_display_html}</div>", unsafe_allow_html=True)
    
        st.markdown("<h6>Available Fields & Connections:</h6>", unsafe_allow_html=True)
        
        all_fields = defaultdict(list)
        for source in selected:
            for field in DATA_DEFINITIONS[source]['fields']:
                all_fields[field].append(source)
        
        field_tags = ""
        if selected:
            all_unique_fields = set()
            for source_name in selected:
                all_unique_fields.update(DATA_DEFINITIONS[source_name]['fields'])

            common_fields = {field for field, sources in all_fields.items() if len(sources) > 1}

            for field in sorted(list(all_unique_fields)):
                if field in common_fields:
                    field_tags += f"<span class='connected-field-tag'>{field}</span> "
                else:
                    field_tags += f"<span class='field-tag'>{field}</span> "
        
        if field_tags:
            st.markdown(field_tags, unsafe_allow_html=True)
            if len(selected) > 1:
                st.markdown(
                    "<p class='info-note'><i>Fields with a <strong>blue background</strong> are common across multiple selected data sources, indicating potential connection points.</i></p>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown("<p class='info-note'><i>Select more than one data source to see common fields highlighted.</i></p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='info-note'>No fields available from selected sources.</p>", unsafe_allow_html=True)
    
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
