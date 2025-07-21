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

