import streamlit as st

st.set_page_config(
    page_title="CTI Toolbox",
    page_icon="🛡️",
    layout="wide"
)

# --- Pages ---
PAGES = {
    "🔧 Toolbox": "toolbox",
    "📚 About CTI": "about_cti"
}

selection = st.sidebar.radio("Navigate", list(PAGES.keys()))

# --- Custom CSS for animation and cards ---
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }
    .tool-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 102, 255, 0.2);
    }
    a {
        text-decoration: none;
        color: #2563eb;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .footer {
        margin-top: 4rem;
        text-align: center;
        color: gray;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Page 1: Toolbox ---
if selection == "🔧 Toolbox":
    st.markdown("<h1 class='fade-in' style='text-align: center;'>🛠️ CTI Toolbox</h1>", unsafe_allow_html=True)
    st.markdown("<p class='fade-in' style='text-align: center; color: gray;'>Collection of essential tools for Cyber Threat Intelligence</p>", unsafe_allow_html=True)

    # Search Input
    search = st.text_input("🔍 Search tools...", placeholder="Type to filter tools").lower()

    # Tool List
    tools = [
        {
            "name": "Urlscan.io",
            "url": "https://urlscan.io/",
            "description": "Scans and analyzes websites, recording domains, IPs, and resources.",
            "icon": "🔍",
            "category": "Analysis"
        },
        {
            "name": "Abuse.ch",
            "url": "https://abuse.ch/",
            "description": "Tracks malware and botnets through operational platforms.",
            "icon": "🧪",
            "category": "Malware"
        },
        {
            "name": "Talos Intelligence",
            "url": "https://talosintelligence.com/",
            "description": "Cisco’s Talos provides threat intel using global telemetry.",
            "icon": "🛰️",
            "category": "Threat Intel"
        },
        {
            "name": "PhishTool",
            "url": "https://app.phishtool.com/",
            "description": "Analyzes emails to uncover phishing IOCs and generate forensic reports.",
            "icon": "✉️",
            "category": "Phishing"
        }
    ]

    filtered = [t for t in tools if search in t["name"].lower() or search in t["description"].lower() or search in t["category"].lower()]

    cols = st.columns(2)
    for i, tool in enumerate(filtered):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="tool-card fade-in">
                    <span style='font-size: 1.5rem;'>{tool['icon']}</span>
                    <a href="{tool['url']}" target="_blank"> {tool['name']}</a>
                    <p style="color: #4b5563; margin-top: 0.5rem;">{tool['description']}</p>
                    <p style="color: #6b7280; font-size: 0.85rem;">Category: <strong>{tool['category']}</strong></p>
                </div>
            """, unsafe_allow_html=True)

# --- Page 2: About CTI ---
elif selection == "📚 About CTI":
    st.title("📚 About Cyber Threat Intelligence (CTI)")

    st.markdown("""
    **Cyber Threat Intelligence (CTI)** is the process of collecting, analyzing, and using information about potential or current attacks that threaten an organization’s digital assets.

    ### 🔍 Key Components of CTI:
    - **Indicators of Compromise (IOCs)**: Evidence of intrusion like IPs, hashes, domains
    - **Tactics, Techniques, and Procedures (TTPs)**: Behavior patterns of threat actors
    - **Threat Actors**: Profiles and motivations of attackers (e.g., nation-states, cybercriminals)

    ### 🧩 Types of CTI:
    - **Strategic**: High-level summaries for decision-makers
    - **Tactical**: Adversary behaviors and tools
    - **Operational**: Specific attack plans, indicators
    - **Technical**: Data on specific threats like malware or exploit kits

    ### ⚒️ Benefits:
    - Improved threat detection and response
    - Better defense posture and risk management
    - Insights for proactive threat hunting

    > CTI is crucial in modern cybersecurity to stay ahead of threats in a proactive and informed manner.
    """)

# --- Footer ---
st.markdown("""
    <div class="footer">
        © 2025 - CTI Toolbox | Developed by ELMORTAJI AYOUB
    </div>
""", unsafe_allow_html=True)
