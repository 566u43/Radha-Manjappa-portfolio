
import streamlit as st

st.set_page_config(
    page_title="Radha Portfolio",
    page_icon="💻",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

body {
    background-color: #070b1a;
}

.stApp {

    background:
    radial-gradient(circle at 20% 20%,
    rgba(255,215,0,0.18), transparent 25%),

    radial-gradient(circle at 80% 15%,
    rgba(255,200,0,0.15), transparent 20%),

    radial-gradient(circle at 70% 80%,
    rgba(255,215,0,0.12), transparent 25%),

    linear-gradient(
    135deg,
    #4fd1c5 0%,
    #38b2ac 35%,
    #319795 70%,
    #2c7a7b 100%
);

    background-size: 200% 200%;

    animation: gradientMove 15s ease infinite;
}
@keyframes gradientMove {

    0% { background-position: 0% 50%; }

    50% { background-position: 100% 50%; }

    100% { background-position: 0% 50%; }
}


.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* REMOVE STREAMLIT STYLE */

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
            
            .greeting-bar {

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.20);

    border-radius: 25px;

    padding: 20px;

    text-align: center;

    margin-bottom: 25px;

    box-shadow:
    0px 8px 20px rgba(0,0,0,0.15);
}

.greeting-bar h2 {

    color: white;

    margin: 0;
}

.greeting-bar p {

    color: rgba(255,255,255,0.85);

    margin-top: 8px;

    font-size: 16px;
}

/* PROFILE CARD */

.profile-card {

    background: rgba(255,255,255,0.10);

    backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.18);

    border-radius: 30px;

    padding: 25px;

    color: white;

    box-shadow:
    0px 8px 32px rgba(0,0,0,0.25);
}


/* SKILLS */

.skill:hover {
    background: #6C63FF;
    transform: scale(1.05);
    font-weight: bold;
}

/* CONTENT */

.content-box {

    background: rgba(255,255,255,0.90);

    backdrop-filter: blur(18px);

    border-radius: 25px;

    padding: 35px;

    color: #111828;

    border: 1px solid rgba(255,255,255,0.30);

    box-shadow:
    0px 8px 32px rgba(31,38,135,0.10);
}




/* BUTTON STYLE */

/* Normal buttons + Download button */

div.stButton > button,
div.stDownloadButton > button {

    width: 100%;
    height: 60px;

    background: rgba(255,255,255,0.15);

    color: white;

    border: 1px solid rgba(255,255,255,0.25);

    border-radius: 15px;

    font-size: 17px;

    font-weight: 600;

    backdrop-filter: blur(10px);
}

div.stButton > button:hover,
div.stDownloadButton > button:hover {

    background: #2563eb;

    color: white;

    border: none;
}

/* SERVICE CARD */

.service-card {

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.25);

    border-radius: 25px;

    padding: 25px;

    color: white;

    box-shadow:
    0px 8px 32px rgba(0,0,0,0.20);

    transition: 0.3s;
}

.service-card:hover {

    transform: translateY(-5px);

    background: rgba(255,255,255,0.18);
}

.main-glass {

    background: rgba(255,255,255,0.10);

    backdrop-filter: blur(20px);

    border: 1px solid rgba(255,255,255,0.18);

    border-radius: 30px;

    padding: 30px;

    box-shadow:
    0px 8px 32px rgba(0,0,0,0.25);

    margin-top: 20px;
}


h1,h2,h3,h4 {
    color: white;
}

p {
    color: #F3F4F6;
}

label {
    color: purple;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================

if "page" not in st.session_state:
    st.session_state.page = "About Me"

# =========================
# VISITOR LOGIN
# =========================




# =========================
# TOP GREETING
# =========================

from datetime import datetime

hour = datetime.now().hour

if hour < 12:
    greeting = " Good Morning 👋"
elif hour < 17:
    greeting = " Good Afternoon 👋"
else:
    greeting = " Good Evening 👋"



st.markdown(f"""
<div style="
background: rgba(255,255,255,0.15);
padding:20px;
border-radius:25px;
text-align:center;
font-size:32px;
font-weight:700;
margin-bottom:30px;
backdrop-filter: blur(18px);
border:1px solid rgba(255,255,255,0.25);
color:white;
box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
">
{greeting} 
</div>
""", unsafe_allow_html=True)
# =========================
# MAIN LAYOUT
# =========================

left, center, nav = st.columns([1.2, 4, 0.7])

# =========================
# LEFT PANEL
# =========================

with left:

    st.image("assets/profile.jpg", width=220)

    st.markdown("## Radha M")
    st.markdown("### Python Developer & Data Analyst")
    st.markdown("📍 Bangalore, India")
    st.markdown("📧 radhamlakshmi@gmail.com")

    st.markdown("### Connect")

    st.markdown("""
<a href="https://github.com/566u43" target="_blank">
    <button style="
        width:100%;
        height:55px;
        background:#2563eb;
        color:white;
        border:none;
        border-radius:12px;
        font-size:16px;
        cursor:pointer;">
        💻 GitHub
    </button>
</a>

<br><br>

<a href="https://www.linkedin.com/in/radha-manjappa-7a7260236" target="_blank">
    <button style="
        width:100%;
        height:55px;
        background:#0A66C2;
        color:white;
        border:none;
        border-radius:12px;
        font-size:16px;
        cursor:pointer;">
        🔗 LinkedIn
    </button>
</a>
""", unsafe_allow_html=True)
    st.markdown("---")

    with open("assets/Radha Manjappa Resume.pdf", "rb") as pdf_file:
     st.download_button(
        label="📄 Download Resume",
        data=pdf_file,
        file_name="Radha_M_Resume.pdf",
        mime="application/pdf",
        use_container_width=True
    )  


# =========================
# CENTER PANEL
# =========================

with center:

    if st.session_state.page == "About Me":

        st.header("About Me")

        st.markdown("""
##  Hello, I'm Radha M

Python Developer and Data Analyst passionate about building interactive dashboards, business insights, and data-driven solutions.

I work with Python, SQL, Power BI, Excel, Pandas, Streamlit, and Data Analytics.
""")

        st.header("What I Do")

        s1, s2, s3 = st.columns(3)

        with s1:
            st.markdown("""
            <div class="service-card">
            <h3>📊 Data Analytics</h3>
            <p>Analyze business data using Python, Pandas, SQL and Excel.</p>
            </div>
            """, unsafe_allow_html=True)

        with s2:
            st.markdown("""
            <div class="service-card">
            <h3>📈 Dashboards</h3>
            <p>Create Power BI dashboards and visual analytics solutions.</p>
            </div>
            """, unsafe_allow_html=True)

        with s3:
            st.markdown("""
            <div class="service-card">
            <h3>💻 Web Apps</h3>
            <p>Build interactive web applications using Streamlit.</p>
            </div>
            """, unsafe_allow_html=True)

            
    # =====================
    # SKILLS
    # =====================

    elif st.session_state.page == "Skills":
        
        

        st.header("🛠  Technical Skills")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Programming")
            st.write("✔ Python")
            st.write("✔ SQL")
            

            st.subheader("Data Analytics")
            st.write("✔ Power BI")
            st.write("✔ Excel")
            st.write("✔ Pandas")
            st.write("✔ NumPy")

        with col2:
            st.subheader("Web Development")
            st.write("✔ Streamlit")
            st.write("✔ HTML")
            st.write("✔ CSS")

            st.subheader("Tools")
            st.write("✔ Git & GitHub")
            st.write("✔ VS Code")
            st.write("✔ Jupyter Notebook")

            if st.button("⬅ Back to Home"):
                st.session_state.page = "About Me"

    # =====================
    # PROJECTS
    # =====================
    elif st.session_state.page == "Projects":

        st.header("📂 Projects")
        if st.button("⬅ Back to Home"):
            st.session_state.page = "About Me"

        st.subheader("📊 Retail Profit Analysis")

        st.write("""
        • Analyzed retail sales data using Python and SQL.\n
        • Built Power BI dashboards.\n
        • Identified profitable products and business insights.
        """)

        st.subheader("📈 Sales Dashboard")

        st.write("""
        • Interactive Power BI Dashboard.\n
        • KPI Tracking.\n
        • Sales Trend Analysis
        """)

        st.subheader("💻 Portfolio Website")

        st.write("""
        • Developed using Streamlit\n
        • Responsive Glassmorphism UI\n
        • Resume Download\n
        • Navigation Menu
        """)

    # =====================
    # EXPERIENCE
    # =====================
    elif st.session_state.page == "Experience":

        st.header("💼 Experience")
        if st.button("⬅ Back to Home"):
            st.session_state.page = "About Me"

        st.subheader("Data Management Intern")

        st.write("""
        **Mevi Technologies**

        • Managed business datasets

        • Cleaned and validated data

        • Created reports using Excel

        • Supported analytics team
        """)

        st.subheader("Data Management Analyst")

        st.write("""
        **Machanas Startup**

        • Data Entry

        • Report Generation

        • Database Management

        • Documentation
        """)

   

    # =====================
    # CERTIFICATIONS
    # =====================

    elif st.session_state.page == "Certifications":

        st.header("🏆 Certifications")

        if st.button("⬅ Back to Home"):
            st.session_state.page = "About Me"


        st.write("🏅 IBM Data Analytics")

        st.write("🏅 PwC Power BI Job Simulation")

        st.write("🏅 Python Programming")

        st.write("🏅 SQL for Data Analysis")

    # =====================
    # EDUCATION
    # =====================

    elif st.session_state.page == "Education":

        st.header("🎓 Education")

        if st.button("⬅ Back to Home"):
            st.session_state.page = "About Me"

        st.markdown("""
### 🎓 Master of Computer Applications (MCA)

🏫 **St. Francis College**  
📅 **2021 – 2023**  
🎯 **CGPA:** **7.6 / 10**

---

### 🎓 Bachelor of Computer Science (BSc)

🏫 **St. Anne's College for Womens**  
📅 **2018 – 2021**  
🎯 **CGPA:** **8.0 / 10**
""")

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# RIGHT NAVIGATION PANEL
# =========================

with nav:

    st.markdown("### Explore")

    if st.button("🛠 Skills"):
        st.session_state.page = "Skills"

    if st.button("📂 Projects"):
        st.session_state.page = "Projects"

    if st.button("💼 Experience"):
        st.session_state.page = "Experience"

    if st.button("🏆 Certifications"):
        st.session_state.page = "Certifications"

    if st.button("🎓 Education"):
        st.session_state.page = "Education"
