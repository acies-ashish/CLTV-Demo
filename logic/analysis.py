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
    
    frozenset({"Transactional", "Order"}): {
    "cltv_type": "Detailed transaction-level CLTV using both payment and product-order data to model net revenue, returns, and product-level profitability.",
    "outcome": """
- Net CLTV per customer accounting for returns or item-level behavior
- Insights into frequently purchased products or categories
- Better prediction of customer lifetime revenue and churn likelihood
""",
    "explains": """
- Product- and order-level contribution to lifetime value
- Impact of order cancellations or return behavior
- Purchasing cadence and preferences across SKUs
""",
    "does_not_explain": """
- User intent or funnel behavior
- Demographic segmentation or acquisition source
- Operational delays unless fulfillment logs are included
""",
    "field_connections_note": "Strongly tied via `order_id` or `transaction_id`; enables per-SKU analysis and revenue integrity checks."
},
    
    frozenset({"Transactional", "Order", "Audit Data"}): {
    "cltv_type": "Merge financial transaction info with product-level and operational/audit data to derive profit-based CLTV, factoring in returns, cancellations, fulfillment efficiency, and net margin.",
    "outcome": """
- Ground-truth CLTV from net margin
- Operational inefficiency insights (return %, delivery failures)
- Attribution of profit loss to specific processes (e.g., delayed shipping)
""",
    "explains": """
- What products are profitable (net of costs, refunds, cancellations)
- Which customers churn due to operational pain points
- Which channels or warehouses drive poor margins
""",
    "does_not_explain": """
- User intent or engagement (no behavioral/digital journey)
- Demographic segments or psychographic profiles
- Purchase motivations or product affinity
""",
    "field_connections_note": "Powerful for root-cause attribution of customer churn and margin leakage when order operations data is granular and clean."
},

frozenset({"Transactional", "Behavioral", "Demographic", "Cost Table"}): {
    "cltv_type": "Full-funnel CLTV modeling incorporating identity, intent, spend behavior, and acquisition cost—enabling profitability-optimized targeting and retention.",
    "outcome": """
- Customer-level profit-adjusted CLTV
- Audience prioritization by ROI, not just revenue
- Insights for acquisition targeting, messaging, and retention levers
""",
    "explains": """
- Who high-value customers are (demographics)
- How they behave before purchasing (behavioral signals)
- What they spend and what it costs to acquire/retain them
- Segment-wise cost-efficiency and retention ROI
""",
    "does_not_explain": """
- Fulfillment or post-purchase issues unless audit/order data included
- Channel-level granularity unless campaign linkage is present
- Long-term economic sensitivity unless external data is used
""",
    "field_connections_note": "Powerful for aligning CLTV with CAC at segment and channel level. Key joins: `customer_id`, `campaign_id`, and behavioral user identifiers."
},

frozenset({"Transactional", "Behavioral", "Demographic", "Audit Data"}): {
    "cltv_type": "Experience-aware CLTV modeling integrating customer identity, spend behavior, engagement signals, and operational friction points.",
    "outcome": """
- Customer-level CLTV estimates enhanced with service quality signals
- Segment-wise analysis of churn risk driven by operational breakdowns
- Early churn flagging based on behavioral and audit patterns
""",
    "explains": """
- Who your customers are and how they spend
- What behaviors precede loyalty or churn
- Where operational events (e.g., failed logins, payment errors) impact value
""",
    "does_not_explain": """
- Cost to acquire or retain users (no marketing/campaign data)
- Product-level profitability or returns (no order-level detail)
- Economic or seasonal influences (no macro data)
""",
    "field_connections_note": "Requires unified user identifiers across behavioral, transactional, and audit systems for full attribution."
},

frozenset({"Transactional", "Behavioral", "Demographic", "Order", "Cost Table"}): {
    "cltv_type": "Profit-adjusted, behavior-informed CLTV modeling using full purchase, identity, engagement, and cost-of-acquisition context.",
    "outcome": """
- Customer-level CLTV incorporating order details and acquisition cost
- Segment-level insights on profitable vs. unprofitable customers
- Behavioral drivers of high- or low-margin customer journeys
""",
    "explains": """
- Who the customer is and what they purchase
- How user engagement drives revenue and repeat behavior
- How cost impacts profitability at product, customer, and cohort levels
""",
    "does_not_explain": """
- Operational breakdowns or service friction (no audit/support data)
- External macroeconomic impact unless additional data is added
- Multi-touch attribution unless marketing journey data is included
""",
    "field_connections_note": "Enables margin-level CLTV modeling with links via `customer_id`, `order_id`, and `campaign_id` across data sources."
},

frozenset({"Transactional", "Order", "Cost Table"}): {
    "cltv_type": "Profit-based CLTV modeling combining purchase history, product-level order data, and acquisition/servicing cost.",
    "outcome": """
- Net CLTV per customer after accounting for order returns and cost
- SKU-level profitability insights by customer and segment
- Strategic view of high-cost vs high-value customers
""",
    "explains": """
- What customers purchase and how often
- The cost dynamics influencing overall customer profitability
- Product or category-level contribution to CLTV
""",
    "does_not_explain": """
- Why customers churn or engage (no behavioral data)
- Demographic or identity context (no user profile data)
- Service or operational experience (no audit/support data)
""",
    "field_connections_note": "Joins rely on `customer_id`, `order_id`, and `campaign_id` for linking transactional, order, and cost sources effectively."
},

frozenset({"Transactional", "Behavioral", "Demographic", "Audit Data", "Cost Table"}): {
    "cltv_type": "End-to-end profitability-aware CLTV modeling integrating spend patterns, intent signals, user identity, service quality, and acquisition cost.",
    "outcome": """
- Customer-level CLTV adjusted for cost, behavior, and post-purchase friction
- Segmented ROI models for acquisition and retention planning
- Identification of high-value yet support-heavy or cost-inefficient users
""",
    "explains": """
- Who your customers are, how they behave, and what they spend
- How operational friction (e.g., login issues, failed payments) affects churn
- What it costs to acquire and retain different customer types
""",
    "does_not_explain": """
- Specific order or item-level contribution to CLTV unless order data is included
- Environmental or regional macro factors unless external data is layered
- Multi-touch campaign attribution without marketing touchpoint data
""",
    "field_connections_note": "Requires robust linking across `customer_id`, `event_id`, and `campaign_id`. Suitable for supervised CLTV models, retention flagging, and experience optimization."
},

frozenset({"Transactional", "Behavioral", "Demographic", "Audit Data", "Cost Table", "Order"}): {
    "cltv_type": "Comprehensive CLTV and profitability modeling combining identity, engagement, transactions, order-level performance, cost efficiency, and operational friction.",
    "outcome": """
- Customer-level net CLTV adjusted for cost, returns, and support activity
- Identification of operational bottlenecks reducing lifetime value
- Segment-specific acquisition and retention ROI analysis
""",
    "explains": """
- Full customer value lifecycle from acquisition cost to fulfillment outcome
- Which users are high-spend but operationally expensive or support-heavy
- Behavior-to-order conversion patterns by demographic or cohort
""",
    "does_not_explain": """
- External or seasonal economic influences unless macro data is included
- Creative- or channel-level campaign attribution (unless touchpoint data added)
- Psychological drivers unless layered with psychographic data
""",
    "field_connections_note": "Ideal for mature organizations with granular logs across customer, product, marketing, and operations. Supports CLTV prediction, churn diagnostics, and CAC-to-LTV alignment."
},

frozenset({"Transactional", "Behavioral", "Demographic", "Order"}): {
    "cltv_type": "Holistic CLTV modeling integrating identity, intent signals, transaction history, and detailed order behavior for improved retention and revenue prediction.",
    "outcome": """
- Customer-level CLTV enriched with order-level detail
- Segment-level product preferences and behavioral profiles
- Purchase likelihood and churn forecasting using behavioral patterns
""",
    "explains": """
- Who buys what, how often, and in what context
- Patterns in repeat purchasing and product-level preferences
- Early signs of churn or loyalty through engagement and order gaps
""",
    "does_not_explain": """
- Marketing cost efficiency (no CAC without cost data)
- Operational disruptions (no support/audit insights)
- External influences unless combined with macro data
""",
    "field_connections_note": "Join via `customer_id`, `order_id`, and behavioral identifiers to connect transactions with engagement and order details for full-funnel modeling."
},

frozenset({"Order", "Cost Table"}): {
    "cltv_type": "Order-based profitability estimation through indirect matching of product/order behavior to campaign spend or category-level cost assumptions.",
    "outcome": """
- Approximate customer value against campaign/marketing cost
- Product or category performance by acquisition ROI
- Indirect CLTV benchmarking without full transaction granularity
""",
    "explains": """
- Patterns in repeat orders or return rates by segment
- Cost exposure per product line or campaign
- Revenue trends mapped to marketing efforts
""",
    "does_not_explain": """
- Actual payment value (if discounts/refunds not tracked)
- Net profit unless cost of goods sold or return impact is included
- Engagement behavior or user journey
""",
    "field_connections_note": "Useful when `order_id` or `product_id` can be mapped to campaign or cost exposure sources."
},

frozenset({"Order", "Audit Data", "Cost Table"}): {
    "cltv_type": "Operational CLTV framework integrating order actions, fulfillment performance, and marketing costs—used to detect value erosion from operational failures.",
    "outcome": """
- Net margin attribution by product, process, and campaign
- Identification of high-cost, low-efficiency customer segments
- Insights into refund, delay, and cancellation-driven churn
""",
    "explains": """
- Cost and operational drivers behind customer churn
- Which fulfillment or audit events lower LTV
- Campaigns that result in poor operational outcomes
""",
    "does_not_explain": """
- Who the customer is (no demographics)
- Why they convert or engage (no behavioral signals)
- Total spend unless paired with transaction data
""",
    "field_connections_note": "Ideal for fulfillment-heavy businesses; requires join logic on `order_id`, `event_id`, and campaign metadata."
},


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
def generate_cltv_analysis(selected_sources_list):
    """
    Looks up the CLV analysis block for the selected set of data sources.
    Falls back to DEFAULT_ANALYSIS if combination is unknown.
    """
    s = frozenset(selected_sources_list)

    if s in CLV_ANALYSIS_CONTENT:
        return CLV_ANALYSIS_CONTENT[s]
    elif not s:
        return CLV_ANALYSIS_CONTENT[frozenset()]
    else:
        return CLV_ANALYSIS_CONTENT.get("DEFAULT_ANALYSIS", {
            "cltv_type": "Unknown",
            "outcome": "Not available.",
            "explains": "Not available.",
            "does_not_explain": "Not available.",
            "field_connections_note": ""
        })