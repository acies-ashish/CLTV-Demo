import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        body { 
            font-family: 'Inter', sans-serif; 
            background-color: #F0F2F6; 
            color: #333;
        }
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
    
        /* Adjustments for sidebar styling */
        .stSidebar > div:first-child {
            background-color: #ffffff;
            padding: 1.5rem;
            border-right: 1px solid #E5E7EB;
            box-shadow: 2px 0 10px rgba(0,0,0,0.05);
        }
    
        /* Main section containers for the entire page */
        .section-container {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            margin-bottom: 2rem;
            border: 1px solid #E5E7EB; 
        }
        .section-container h3 {
            color: #111827;
            border-bottom: 3px solid #3B82F6; 
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            text-align: left;
            font-weight: 600;
            font-size: 1.75rem;
        }
    
        /* Field tags */
        .field-tag {
            background-color:#F3F4F6; 
            color:#4B5563; 
            border:1px solid #E5E7EB;
            padding: 4px 10px; 
            border-radius: 6px; 
            margin: 3px; 
            display: inline-block;
            font-size: 0.85em;
            font-weight: 400;
        }
        .connected-field-tag {
            background-color:#E0E7FF; 
            color:#3730A3; 
            border:1px solid #C7D2FE;
            padding: 4px 10px; 
            border-radius: 6px; 
            margin: 3px; 
            display: inline-block;
            font-weight: 600;
            font-size: 0.85em;
        }
    
        /* Styling for the section describing 'What CLTV Can Be Calculated' */
        .cltv-type-block {
            background-color: #F9FAFB; 
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem; 
            border: 1px solid #E5E7EB;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }
        .cltv-type-block h5 {
            color: #1F2937;
            margin-bottom: 0.75rem;
            font-weight: 600;
            font-size: 1.15rem;
            text-align: left;
        }
        .cltv-type-block p {
            color: #4B5563;
            line-height: 1.6;
            text-align: left;
            font-size: 0.95em;
        }
    
        /* Styling for individual stacked content blocks */
        .analysis-content-block {
            background-color: #FFFFFF;
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid #E5E7EB; /* Main border for each block */
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
            margin-bottom: 1rem;
            text-align: center; /* Centers block-level content like heading and lists */
        }
        .analysis-content-block h5 {
            color: #1F2937;
            margin-bottom: 0.75rem;
            font-weight: 600;
            font-size: 1.2rem; 
            text-align: center;
        }
        .analysis-content-block ul {
            list-style-type: disc;
            margin: 0 auto; /* Centers the ul block itself */
            padding-left: 0;
            color: #4B5563;
            font-size: 0.95em;
            line-height: 1.6;
            max-width: 80%; /* Constrain width for readability when centered */
            display: table; /* Helps margin auto work for centering the ul block */
        }
        .analysis-content-block li {
            margin-bottom: 0.6rem; 
            text-align: center; /* Centers the text and bullet point within the list item */
            list-style-position: inside; /* Crucial: Puts the bullet inside the content box for centering */
        }
        .analysis-content-block p {
            color: #4B5563;
            font-size: 0.95em;
            line-height: 1.6;
            text-align: center;
            max-width: 90%;
            margin: 0.5rem auto; /* Center paragraphs as well */
        }
        .analysis-content-block ul {
            margin-top: 0; 
            padding-top: 0;
        }
    
        /* Specific styling for 'Can Explain' (Green) */
        .can-explain-block {
            background-color: #ECFDF5;
            border: 1px solid #34D399; /* Green border */
            color: #065F46;
        }
        .can-explain-block h5 {
            color: #065F46;
        }
        .can-explain-block ul, .can-explain-block p {
            color: #065F46;
        }
    
        /* Specific styling for 'Cannot Explain' (Red) */
        .cannot-explain-block {
            background-color: #FEE2E2;
            border: 1px solid #EF4444; /* Red border */
            color: #991B1B;
        }
        .cannot-explain-block h5 {
            color: #991B1B;
        }
        .cannot-explain-block ul, .cannot-explain-block p {
            color: #991B1B;
        }
    
    
        /* Styling for selected data source display (Section 1) */
        .selected-source-item {
            background-color: #EEF2FF; 
            color: #4338CA; 
            border: 1px solid #C7D2FE; 
            padding: 8px 15px; 
            border-radius: 20px; 
            margin-right: 10px;
            margin-bottom: 10px;
            display: inline-flex;
            align-items: center;
            font-weight: 600;
            font-size: 1.05em;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05); 
            transition: transform 0.2s ease-in-out;
        }
        .selected-source-item:hover {
            transform: translateY(-2px); 
        }
        .selected-source-item .icon {
            margin-right: 8px; 
            font-size: 1.3em; 
            color: #6366F1; 
        }
    
        .info-note {
            font-size: 0.85em;
            color: #6B7280;
            margin-top: 1rem;
            padding-top: 0.5rem;
            border-top: 1px dashed #E5E7EB;
        }
    
        /* Ensure Streamlit's column wrappers don't add extra space/background */
        div[data-testid="stColumn"] {
            padding: 0.75rem !important; 
            background-color: transparent !important;
        }
         
        /* Small adjustment for the main title, ensuring it's not too close to the main container */
        .stApp > header {
            background-color: #F0F2F6; 
        }
    
    </style>
    """, unsafe_allow_html=True)
