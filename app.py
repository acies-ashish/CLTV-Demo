import streamlit as st
from collections import defaultdict

# --- Page Configuration ---
st.set_page_config(
    page_title="Strategic CLTV Data Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling (CSS) ---
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


# --- Data Definitions for Individual Sources ---
DATA_DEFINITIONS = {
    "Transactional": {
        "icon": "🛒",
        "key_fields": ["customer_id", "transaction_id"],
        "fields": [
            "customer_id", "transaction_date", "transaction_id", "product_id", "quantity",
            "price_per_unit", "discount_applied", "total_amount", "cost_of_goods_sold", "order_status"
        ]
    },
    "Demographic": {
        "icon": "👤",
        "key_fields": ["customer_id"],
        "fields": [
            "gender", "age", "dob", "location", "device_type", "preferred_language",
            "signup_date", "registration_status", "loyalty_program_member", "account_status"
        ]
    },
    "Behavioral": {
        "icon": "🖱️",
        "key_fields": ["session_id", "visit_id", "user_id", "device_id", "cookie_id"],
        "fields": [
            "session_id", "visit_id", "user_id", "key", "device_id", "cookie_id", "device",
            "entry_channel", "user_country", "entry_page", "number_of_page_viewed", "visit_datetime"
        ]
    },
    "Order": {
        "icon": "📦",
        "key_fields": ["order_item_id", "order_id"],
        "fields": [
            "order_item_id", "order_id", "user_id", "product_id", "product_name", "category",
            "quantity", "price_per_unit", "discount_applied", "total_item_value",
            "order_status", "delivery_date", "return_status"
        ]
    },
    "Audit Data": {
        "icon": "📄",
        "key_fields": ["user_id", "event_id"],
        "fields": [
            "event_id", "user_id", "event_type", "timestamp", "platform",
            "login_success_count", "login_failure_count", "session_timeout_count",
            "password_change_flag", "permission_change_flag", "failed_payment_count"
        ]
    },
    "Marketing Touchpoint": {
        "icon": "📣",
        "key_fields": ["campaign_id"],
        "fields": [
            "campaign_id", "channel", "touchpoint_type", "touch_date", "campaign_medium",
            "utm_source", "utm_campaign", "touchpoint_status", "conversion_flag", "time_to_conversion",
            "creative_id", "segment_id", "frequency", "reach", "click_through_rate", "cost_per_click", "landing_page_url"
        ]
    },
    "Referral / Network Data": {
        "icon": "🤝",
        "key_fields": ["CustomerID", "ReferralID"],
        "fields": ["CustomerID", "ReferralID", "ReferredBy", "ReferralBonus"]
    },
    "Subscription / Plan": {
        "icon": "🔄",
        "key_fields": ["CustomerID", "SubscriptionID"],
        "fields": ["SubscriptionID", "CustomerID", "MRR", "ChurnDate"]
    },
    "Customer Support": {
        "icon": "📞",
        "key_fields": ["CustomerID", "TicketID"],
        "fields": ["TicketID", "CustomerID", "IssueType", "CSAT"]
    },
    "Psychographic Data": {
        "icon": "🧠",
        "key_fields": ["customer_id"],
        "fields": [
            "persona_type", "motivation_factor", "brand_loyalty_score", "discount_affinity"
        ]
    },
    "Social/Sentiment Data": {
        "icon": "💬",
        "key_fields": ["customer_id"],
        "fields": [
            "social_mentions_count", "average_sentiment_score",
            "review_rating_avg", "last_review_date"
        ]
    },
    "Device / Tech Stack Data": {
        "icon": "📱",
        "key_fields": ["customer_id"],
        "fields": [
            "device_type", "app_version", "browser", "os_version"
        ]
    },
    "Economic / Environmental Data": {
        "icon": "🌍",
        "key_fields": ["location"],
        "fields": [
            "region_unemployment_rate", "region_inflation_rate",
            "festive_season_indicator", "climate_risk_zone"
        ]
    },
    "Cost Table": {
        "icon": "💸",
        "key_fields": ["Campaign_ID"],
        "fields": [
            "Campaign_ID", "Campaign_Name", "Channel", "Target_Segment", "Start_Date", "End_Date",
            "Campaign_Budget", "Impressions", "Clicks", "CTR (Click-Through Rate)", "Conversions",
            "Conversion_Rate", "Cost_Per_Click (CPC)", "Cost_Per_Conversion (CAC_Campaign_Level)",
            "Revenue_Generated", "ROI_Campaign_Level", "Creative_Type", "Campaign_Objective",
            "Landing_Page_URL", "Attribution_Model", "Touchpoints_Before_Conversion",
            "Avg_Time_to_Convert", "Device_Type", "Geo_Location"
        ]
    }
}



# --- Pre-defined CLV Analysis Content based on Combinations ---
CLV_ANALYSIS_CONTENT = {
    # START: Demographic Only Content
    frozenset({"Demographic"}): {
        "cltv_type": "Segment-based CLTV Estimation for understanding value by customer characteristics.",
        "outcome": """
- Segment-level predicted CLTV
- Prioritization of segments for acquisition/targeting
- Optional use in lookalike modeling for platforms like Meta or Google Ads
""",
        "explains": """
- Relative value of customer groups
- Geographic and demographic differences in predicted value
""",
        "does_not_explain": """
- Actual customer behavior
- Churn risk
- Purchase frequency or recency
- Engagement trends
""",
        "field_connections_note": "No transactional or behavioral data available for direct monetary or intent modeling.",
    },
    # END: Demographic Only Content

    # START: Transactional Only Content
    frozenset({"Transactional"}): {
        "cltv_type": "Historical CLTV estimation through revenue/cost aggregation and cohort modeling, focusing on past spend.",
        "outcome": """
- Individual CLTV per customer
- Cohort-level CLTV
- Input into churn models, customer scoring, retention initiatives
""",
        "explains": """
- Actual customer spend behavior (Recency, Frequency, Monetary value)
- Churn patterns through recency/frequency
- High-value vs low-value customers based on purchases
""",
        "does_not_explain": """
- Who the customer is (no demographic context)
- Why they purchased (no behavior or intent)
- External influences on loyalty or churn
""",
        "field_connections_note": "", # No specific note for this one
    },
    # END: Transactional Only Content

    # START: Behavioral Only Content
    frozenset({"Behavioral"}): {
        "cltv_type": "Engagement-based CLTV prediction using proxy scoring (e.g., engagement → intent → conversion value mapping).",
        "outcome": """
- Predicted value segments (high/low engagement)
- Behavioral cohorts
- Funnel drop-off insights
- CLTV proxy scores for retargeting
""",
        "explains": """
- Engagement quality (e.g., pages viewed, time on site)
- Intent indicators (e.g., repeated product visits, cart abandonment)
- Channel or campaign quality based on user interaction
""",
        "does_not_explain": """
- Actual spend or profitability
- Demographics or user identity (if anonymized)
- Direct purchase frequency/churn without transactional data
""",
        "field_connections_note": "",
    },
    # END: Behavioral Only Content
    
    frozenset({"Marketing Touchpoint"}): {
    "cltv_type": "Channel attribution and conversion touchpoint analysis for CLTV enrichment.",
    "outcome": """
- Identify high-performing channels or creatives
- Conversion-likelihood by touchpoint
- Assist scoring for retargeting or suppression
""",
    "explains": """
- Which channels assist conversions
- How often a user is touched before conversion
- Channel-level influence on customer journey
""",
    "does_not_explain": """
- Revenue or profitability
- Individual purchase behavior
- Demographic characteristics unless enriched
""",
    "field_connections_note": "Best used in combination with transactional data for revenue linkage."
},

frozenset({"Referral / Network Data"}): {
    "cltv_type": "Referral-based value modeling to understand network-driven acquisition.",
    "outcome": """
- Value of referred vs. organic users
- Virality or referral multiplier scores
- Reward optimization for refer-a-friend programs
""",
    "explains": """
- Influence of referral source on retention
- Spread pattern of new user acquisition
- Behavioral patterns of referred users
""",
    "does_not_explain": """
- Spend patterns without transactions
- Campaign ROI unless merged with cost data
- Identity traits beyond referral linkage
""",
    "field_connections_note": "Useful when paired with transactional or demographic data to compare referred vs. organic CLTV."
},

frozenset({"Subscription / Plan"}): {
    "cltv_type": "Subscription-based revenue continuity model for predictable CLTV forecasting.",
    "outcome": """
- Monthly Recurring Revenue (MRR) and churn rates
- Plan-wise CLTV segmentation
- Forecasting revenue continuity and retention risk
""",
    "explains": """
- Long-term value based on subscription status
- Influence of plan tiers on retention
- Customer base stability through churn rates
""",
    "does_not_explain": """
- Ad-hoc purchases or upsells
- Customer intent or motivations
- Identity context unless joined with user profiles
""",
    "field_connections_note": "Optimally paired with transactional and demographic data for complete view."
},

frozenset({"Customer Support"}): {
    "cltv_type": "Support interaction analysis to understand satisfaction impact on CLTV.",
    "outcome": """
- CSAT impact on retention and churn
- Support-heavy vs support-light customer segments
- Issue categories leading to churn
""",
    "explains": """
- Post-purchase service quality
- Relationship between support interactions and loyalty
- Impact of support responsiveness on CLTV
""",
    "does_not_explain": """
- Product selection or spend patterns
- Demographics or purchase motivations
- Cost of support unless integrated
""",
    "field_connections_note": "Value amplified when combined with transaction and product data."
},

frozenset({"Psychographic Data"}): {
    "cltv_type": "Persona-driven CLTV segmentation based on motivations and preferences.",
    "outcome": """
- CLTV estimates by persona type
- Price sensitivity segmentation
- Offers or message customization by affinity
""",
    "explains": """
- Discount-driven vs value-driven customer profiles
- Brand loyalty levels
- Strategic alignment of offerings to motivations
""",
    "does_not_explain": """
- Real spending or engagement
- Time-based retention metrics
- Marketing influence unless modeled with exposure
""",
    "field_connections_note": "Most effective with behavioral or transactional overlay."
},

frozenset({"Social/Sentiment Data"}): {
    "cltv_type": "Sentiment-enriched CLTV modifiers using public opinion and review behavior.",
    "outcome": """
- CLTV modifiers based on sentiment trends
- Segmenting promoters vs detractors
- Social-driven churn or loyalty forecasting
""",
    "explains": """
- Customer satisfaction indicators
- Word-of-mouth potential
- Online advocacy vs complaint trends
""",
    "does_not_explain": """
- Actual monetary value
- User identity or demographics
- Channel spend unless layered in
""",
    "field_connections_note": "Requires joins with user IDs for customer-level insights."
},

frozenset({"Device / Tech Stack Data"}): {
    "cltv_type": "Tech affinity modeling for CLTV influenced by device and platform behaviors.",
    "outcome": """
- Device-based value segmentation
- App/web usage trends by value tier
- Platform-specific performance optimization
""",
    "explains": """
- Preferences in tech ecosystem
- Device-wise engagement differences
- Conversion patterns across tech stacks
""",
    "does_not_explain": """
- Direct monetary contribution
- User intent or campaign response
- Identity resolution across sessions
""",
    "field_connections_note": "Supports UX optimization and attribution studies when linked to behavioral logs."
},

frozenset({"Economic / Environmental Data"}): {
    "cltv_type": "Contextual enrichment for CLTV using macroeconomic and environmental indicators.",
    "outcome": """
- Region-wise CLTV variation analysis
- External factor influence on churn or loyalty
- Strategic planning by location-specific risks or seasonality
""",
    "explains": """
- Impact of economic conditions on spending behavior
- Regional trends in customer performance
- Seasonality or climate effects on retention or acquisition
""",
    "does_not_explain": """
- Individual-level purchasing behavior
- Customer motivations or engagement
- Product or channel performance without other data
""",
    "field_connections_note": "Most effective when layered with demographic or transactional data for localized strategy modeling."
},

    # START: Cost Table Only Content
    frozenset({"Cost Table"}): {
        "cltv_type": "Cost-based CLTV analysis to understand margin impact and acquisition efficiency.",
        "outcome": """
- Customer-level or segment-level profitability insights
- Channel or campaign ROI comparison
- Informs CAC (Customer Acquisition Cost) and margin thresholds
""",
        "explains": """
- True profitability after accounting for cost to serve/acquire
- Variance in margins across customer types or channels
- Cost implications of retention strategies
""",
        "does_not_explain": """
- Customer engagement or behavior patterns
- Purchase frequency, recency, or monetary value
- Identity or demographic profile of customers
""",
        "field_connections_note": "Requires pairing with revenue or transactional data for net CLTV computation; standalone use only shows cost exposure, not value.",
    },
    # END: Cost Table Only Content

    frozenset({"Demographic", "Transactional"}): {
        "cltv_type": "Segment-aware historical CLTV modeling with actual transaction aggregation + demographic overlays",
        "outcome": """
- Per-customer and per-segment CLTV values
- Insights on which demographics drive high value
- Input for targeting, CAC planning, pricing strategies
""",
        "explains": """
- Actual purchase behavior
- Spend patterns across demographics
- Retention and lifetime trends by cohort
""",
        "does_not_explain": """
- Behavioral triggers or intent
- Campaign/channel performance
- In-session activity or engagement before purchase
""",
    },
    frozenset({"Demographic", "Behavioral"}): {
        "cltv_type": "Predictive modeling using behavioral engagement scores, segmented by demographics; estimate value per segment based on intent and assumed AOV",
        "outcome": """
- CLTV proxy scores at individual or segment level
- Insights into which demographic cohorts engage more deeply
- Behavioral personas with estimated value potential
""",
        "explains": """
- Who is engaging (demographics)
- How they engage (events, intent, funnel depth)
- Potential conversion value based on historic segment trends
""",
        "does_not_explain": """
- Actual spend (no transactions)
- True margin or purchase frequency
- Long-term retention (unless modeled via proxy)
""",
    },
    frozenset({"Transactional", "Behavioral"}): {
        "cltv_type": "Integrate behavioral signals with actual purchase history to model future purchase probability and value at a user level",
        "outcome": """
- Accurate user-level CLTV predictions
- Behavioral drivers of value
- Campaign prioritization, budget optimization
""",
        "explains": """
- What users buy (product, frequency)
- When they engage before/after purchase
- Why users might churn (based on drop-offs or inactivity)
""",
        "does_not_explain": """
- Who they are (no demographics)
- Geo-segmentation
- CAC-to-CLTV ratio (unless marketing spend is available)
""",
    },
    frozenset({"Demographic", "Transactional", "Behavioral"}): {
        "cltv_type": "End-to-end user-level CLTV modeling combining descriptive, behavioral, and financial data. Best suited for supervised prediction and advanced segmentation.",
        "outcome": """
- Highly accurate user-level CLTV predictions
- Segment-wise insights (age/gender/region vs behavior)
- Dynamic scoring for marketing, pricing, CRM use
- Business-case-ready view of revenue per cohort
""",
        "explains": """
- Who the user is
- How engaged they are
- What they’ve bought
- How much revenue they will likely bring
""",
        "does_not_explain": """
- Marketing cost (CAC) unless explicitly tracked
- Offline-to-online attribution (unless bridged via ID)
- Supply chain cost nuances (unless modeled separately)
""",
    },
    frozenset({"Transactional", "Order", "Audit Data"}): {
        "cltv_type": "Merge financial transaction info with product-level and operational/audit data to derive profit-based CLTV, factoring in returns, cancellations, fulfillment efficiency, and net margin",
        "outcome": """
- Ground-truth CLTV from net margin
- Operational inefficiency insights (return %, delivery failures)
- Attribution of profit loss to specific processes (e.g., delayed shipping)
- Targeted retention of profitable customers
""",
        "explains": """
- What products are profitable (net of costs, refunds, cancellations)
- Which customers churn due to operational pain points
- Which channels or warehouses drive poor margins
""",
        "does_not_explain": """
- - User intent or engagement (no behavioral/digital journey)
- Demographic segments or psychographic profiles
- Purchase motivations or product affinity
""",
    },
    frozenset({"Demographic", "Transactional", "Behavioral", "Order", "Audit Data"}): {
        "cltv_type": "Fully integrated predictive CLTV modeling using user attributes, purchase behavior, Browse sessions, order fulfillment experience, and profitability. Drives full-funnel analytics, customer scoring, and business prioritization ",
        "outcome": """
- Real-time, customer-level CLTV scores
- Clear ROI by segment, channel, cohort
- Actionable outputs for pricing, offers, acquisition & retention
- Identification of margin leakage and operational bottlenecks
""",
        "explains": """
- Who the user is
- How they behave
- What they buy
- How long they stay
- What value they generate over time
- Why profitability varies across fulfillment touchpoints
""",
        "does_not_explain": """
- Motivational drivers unless qualitative/voice-of-customer data is layered in
- External offline interactions unless unified via CRM/CDP
- CAC or marketing effectiveness unless paired with marketing spend data
""",
    },
    frozenset({"Marketing Touchpoint", "Cost Table"}): {
    "cltv_type": "Campaign Performance-Driven CLTV Estimation with Marketing Spend Efficiency Insights.",
    "outcome": """
- ROI-based customer segmentation
- Identification of high-CLTV campaigns and creative strategies
- Optimization of marketing spend based on conversion value
""",
    "explains": """
- Which campaigns contribute most to customer lifetime value
- Cost-per-conversion trends across channels
- CLTV uplift by segment, device, or creative
""",
    "does_not_explain": """
- Actual purchase behavior (without transactional data)
- Post-purchase customer journey or loyalty
- Demographic or behavioral nuances unless combined with other sources
""",
    "field_connections_note": "Connected via `campaign_id` between Marketing Touchpoint and Cost Table."
},
    frozenset({"Transactional", "Cost Table"}): {
        "cltv_type": "Spend Efficiency and Profitability-Based CLTV Estimation using Transaction Data and Campaign Costs.",
        "outcome": """
    - Customer-level CLTV linked to campaign ROI
    - Marginal cost per acquired customer
    - Profitability-adjusted segmentation and targeting
    """,
        "explains": """
    - How campaign cost impacts customer value over time
    - Efficiency of spend in acquiring high vs. low CLTV customers
    - CAC vs. LTV alignment
    """,
        "does_not_explain": """
    - User behavior or engagement intent
    - Non-purchase interactions like support or reviews
    - Demographic segmentation unless combined with such data
    """,
        "field_connections_note": "Connected indirectly via campaign attribution and customer acquisition mapping."
    },
    
    frozenset({
    "Transactional", "Demographic", "Behavioral", "Order", "Audit Data",
    "Marketing Touchpoint", "Referral / Network Data", "Subscription / Plan",
    "Customer Support", "Psychographic Data", "Social/Sentiment Data",
    "Device / Tech Stack Data", "Economic / Environmental Data", "Cost Table"
}): {
    "cltv_type": "Comprehensive, full-stack CLTV modeling leveraging every available signal—demographic, transactional, behavioral, operational, marketing, and environmental.",
    "outcome": """
- Hyper-personalized CLTV predictions at customer and segment level
- Profitability- and behavior-aware customer segmentation
- Unified view across acquisition, experience, retention, and revenue streams
""",
    "explains": """
- Who the customer is, how they behave, what they buy, and why they stay or churn
- How internal service, marketing, and operations impact lifetime value
- External economic and environmental influences on behavior and spend
""",
    "does_not_explain": """
- Rare edge-cases where offline data is not captured digitally
- Latent psychological factors unless modeled from proxy signals
- Non-attributable influence (e.g., word-of-mouth without digital trail)
""",
    "field_connections_note": "Requires robust customer ID mapping across systems and consistent data quality to maximize predictive performance."
},

    # Add a default/fallback entry for when no specific combination matches or for incomplete combinations
    frozenset(): { # When nothing is selected
        "cltv_type": "No data sources selected. Please choose data from the sidebar to begin analysis.",
        "outcome": "No outcomes can be derived without data.",
        "explains": "Cannot explain any CLTV aspects without data.",
        "does_not_explain": "All aspects of CLTV.",
        "field_connections_note": ""
    },
    "DEFAULT_ANALYSIS": { # For combinations not explicitly defined above
        "cltv_type": "With only this, CLTV cannot be calculated. This is an add-on that helps improve CLTV models or derive supporting insights.",
        "outcome": "Potential for deriving niche insights by combining diverse data types. Specific outcomes depend on the exact data and analytical methods applied.",
        "explains": "Ability to uncover unique correlations and dependencies between selected data points. May highlight new relationships for further investigation.",
        "does_not_explain": "Clear, pre-defined CLTV metrics without 'Transactional' data for monetary value or 'Demographic' data for identity context. Breadth of explanation depends heavily on data selected.",
        "field_connections_note": ""
    }

}

# --- SYNERGY ENGINE FOR ANALYSIS ---
def generate_cltv_analysis(selected_sources_list):
    s = frozenset(selected_sources_list) # Convert to frozenset for dictionary lookup

    if s in CLV_ANALYSIS_CONTENT:
        return CLV_ANALYSIS_CONTENT[s]
    elif not s: # If no sources are selected
        return CLV_ANALYSIS_CONTENT[frozenset()]
    else:
        # Fallback for undefined combinations
        return CLV_ANALYSIS_CONTENT["DEFAULT_ANALYSIS"]

# --- Session State & Helper Functions ---
if 'selected_sources' not in st.session_state:
    st.session_state.selected_sources = []

def format_option_label(source_name):
    """Formats the label for multiselect to include icons."""
    return f"{DATA_DEFINITIONS[source_name]['icon']} {source_name}"

def handle_select_unselect_all_buttons():
    """Handles the dynamic Select All / Unselect All button for the individual buttons."""
    all_source_names = list(DATA_DEFINITIONS.keys())
    
    if len(st.session_state.selected_sources) == len(all_source_names):
        # All are selected, so unselect all
        st.session_state.selected_sources = []
    else:
        # Not all are selected (or none are), so select all
        st.session_state.selected_sources = all_source_names
    st.rerun()

def clear_all_selections():
    """Clears all selected data sources."""
    st.session_state.selected_sources = []
    st.rerun()


# --- UI RENDERING ---

# ==========================
# SIDEBAR: DATA SELECTION FILTERS (BUTTONS)
# ==========================
with st.sidebar:
    st.title("Data Filters")
    st.header("Select Your Data Sources")
    st.write("Click buttons to select or deselect data sources for CLV analysis.")

    all_source_names = list(DATA_DEFINITIONS.keys())
    
    # Create buttons for each data source
    for source_name in all_source_names:
        is_selected = source_name in st.session_state.selected_sources
        button_type = "primary" if is_selected else "secondary"
        
        # Use a callback to update session state immediately
        if st.button(format_option_label(source_name), key=f"btn_{source_name}", type=button_type, use_container_width=True):
            if is_selected:
                st.session_state.selected_sources.remove(source_name)
            else:
                st.session_state.selected_sources.append(source_name)
            st.rerun() # Rerun to update button styles and main content

    st.markdown("---") # Separator 

    # Dynamic Select All / Unselect All button
    button_label = "Unselect All" if len(st.session_state.selected_sources) == len(all_source_names) else "Select All"
    if st.button(button_label, key="select_unselect_all_sidebar", use_container_width=True):
        handle_select_unselect_all_buttons()

    # Clear Selections button
    if st.button("Clear Selections", key="clear_selections_sidebar", use_container_width=True):
        clear_all_selections()


# ==========================
# MAIN CONTENT: ANALYSIS UI
# ==========================
st.title("CLV Potential Analysis")

selected = sorted(st.session_state.selected_sources)

# Generate analysis based on the selected individual sources
analysis = generate_cltv_analysis(selected)

if not selected: # Simplified check for no selection
    st.info("Select data sources from the sidebar to view the CLV analysis. Once selected, a detailed breakdown of CLV capabilities, outcomes, and limitations will appear here.")
else:
    # --- Section 1: The Selected Data & How It Connects ---
    st.subheader("The Selected Data & How It Connects")
    
    st.markdown("<h5>Your Selected Data Sources:</h5>", unsafe_allow_html=True)
    
    # Display the actual selected sources with enhanced styling
    selected_display_html = "".join([
        f"<span class='selected-source-item'><span class='icon'>{DATA_DEFINITIONS[s]['icon']}</span> {s}</span>" 
        for s in selected
    ])
    st.markdown(f"<div style='display: flex; flex-wrap: wrap; margin-bottom: 1.5rem;'>{selected_display_html}</div>", unsafe_allow_html=True)

    st.markdown("<h6>Available Fields & Connections:</h6>", unsafe_allow_html=True)
    
    # Dynamically gather all fields from the selected individual data sources
    all_fields = defaultdict(list)
    for source in selected:
        for field in DATA_DEFINITIONS[source]['fields']:
            all_fields[field].append(source)
    
    field_tags = ""
    # Highlight fields that appear in more than one selected source as 'connected'
    # And provide a note about them
    if selected:
        # Get a set of all unique fields from *all* selected sources
        all_unique_fields_in_selection = set()
        for source_name in selected:
            all_unique_fields_in_selection.update(DATA_DEFINITIONS[source_name]['fields'])

        # Determine which fields are common (present in more than one selected source)
        common_fields = {field for field, sources in all_fields.items() if len(sources) > 1}

        # Generate tags, applying appropriate styling
        for field in sorted(list(all_unique_fields_in_selection)): # Sort for consistent order
            if field in common_fields:
                field_tags += f"<span class='connected-field-tag'>{field}</span> "
            else:
                field_tags += f"<span class='field-tag'>{field}</span> "
    
    if field_tags:
        st.markdown(field_tags, unsafe_allow_html=True)
        # Add a note explaining the highlighting
        if len(selected) > 1: # Only show this note if multiple sources are selected, as common fields only make sense then
            st.markdown(
                "<p class='info-note'><i>Fields with a **blue background** are common across multiple selected data sources, indicating potential connection points.</i></p>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<p class='info-note'><i>Select more than one data source to see common fields highlighted.</i></p>", unsafe_allow_html=True)

    else:
        st.markdown("<p class='info-note'>No fields available from selected sources.</p>", unsafe_allow_html=True)


    # --- Section 2: CLTV Capabilities and Insights ---
    st.subheader("CLTV Capabilities and Insights")
    
    # What CLTV Can Be Calculated 

    # --- CLTV Type Heading ---
    st.markdown("<h5>What CLTV Can Be Calculated?</h5>", unsafe_allow_html=True)
    st.markdown(f"<p>{analysis['cltv_type']}</p>", unsafe_allow_html=True)

    # --- Outcomes Block ---
    st.markdown("""
    <div style='border: 1px solid #E5E7EB; border-radius: 8px; padding: 16px; background-color: #F9FAFB; margin-bottom: 24px;'>
        <h5>Outcomes:</h5>
        <div style='color:#4B5563; line-height:1.6;'>
            """ + analysis['outcome'] + """
    </div>
    """, unsafe_allow_html=True)

    # --- Can Explain Block (Green Border) ---
    st.markdown("""
    <div style='border: 1px solid #10B981; border-radius: 8px; padding: 16px; background-color: #ECFDF5; margin-bottom: 24px;'>
        <h5 style='color:#065F46;'>Can Explain:</h5>
        <div style='color:#065F46; line-height:1.6;'>
            """ + analysis['explains'] + """
    </div>
    """, unsafe_allow_html=True)

    # --- Cannot Explain Block (Red Border) ---
    st.markdown("""
    <div style='border: 1px solid #EF4444; border-radius: 8px; padding: 16px; background-color: #FEF2F2; margin-bottom: 24px;'>
        <h5 style='color:#991B1B;'>Cannot Explain:</h5>
        <div style='color:#991B1B; line-height:1.6;'>
            """ + analysis['does_not_explain'] + """
    </div>
    """, unsafe_allow_html=True)


    st.markdown("</div>", unsafe_allow_html=True) # Closing section-container for Section 2