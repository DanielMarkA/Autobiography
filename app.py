from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Daniel's Autobiography",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

ASSETS = Path(__file__).parent / "assets"

PROFILE = {
    "name": "Daniel Mark B. Aguilar | F1",
    "nickname": "Daniel",
    "initials": "YN",
    "headline": "Aspiring Software Engineer & Tech Enthusiast",
    "program": "BS Computer Science",
    "school": "Cebu Institute of Technology - University",
    "grad": "2026",
    "status": "Alive",
    "email": "danielaguilar4234@gmail.com",
    "phone": "+63 900 000 0000",
    "github": "https://github.com/DanielMarkA",
    "location": "Makati City, Philippines",
}

SKILLS = pd.DataFrame(
    {
        "Skill": [
            "C# / .NET",
            "ASP.NET Core",
            "Blazor",
            "Tailwind CSS",
            "SQL",
            "Git",
            "JavaScript",
        ],
        "Proficiency": [85, 80, 85, 75, 75, 80, 65],
        "Category": [
            "Language",
            "Backend",
            "Frontend",
            "Frontend",
            "Database",
            "Tools",
            "Frontend",
        ],
    }
)

TOOLS = {
    "Development": ["Visual Studio", "VS Code", "Git", "Docker"],
    "Frontend & Design": ["Blazor WebAssembly", "Tailwind CSS", "Figma"],
    "Database & Cloud": ["PostgreSQL", "Supabase", "SQL Server"],
}

PROJECTS = [
    {
        "name": "AcademIQ",
        "tag": "PRJ1",
        "image": "unnamed.png",
        "role": "Full-Stack Developer",
        "collaborators": "Solo",
        "description": "Architected and developed an academic management platform that streamlines course administration, assignment tracking, submission grading, and rubrics. Implemented a decoupled architecture using ASP.NET Core Web API for the backend and Blazor WebAssembly for an interactive client UI.",
        "stack": [".NET / C#", "ASP.NET Core API", "Blazor WebAssembly", "Tailwind CSS"],
        "outcome": "Live prototype / Web application solution"
    },
    {
        "name": "GatherTable",
        "tag": "PRJ2",
        "image": "unnamed.png",
        "role": "Full-Stack Developer",
        "collaborators": "Solo",
        "description": "Built a comprehensive dining event coordination platform allowing hosts to manage venue details, guest invitations, dietary matrices, group pre-orders, and cost-splitting calculations. Designed responsive UI layouts and backend coordination services.",
        "stack": [".NET / C#", "Blazor Server", "Tailwind CSS"],
        "outcome": "Live prototype"
    },
    {
        "name": "Ambussin",
        "tag": "PRJ3",
        "image": "unnamed.png",
        "role": "Contributor / Developer",
        "collaborators": "Open Source / Team",
        "description": "Contributed features, bug fixes, and system improvements to the Ambussin project codebase, collaborating with core maintainers to enhance stability and functionality.",
        "stack": ["Insert Technologies Used, e.g., C#", "Unity", "Git"],
        "outcome": "Active open-source contribution / Live project release"
    }
]

CHAPTERS = [
    {
        "title": "Origins & Early Spark",
        "period": "Early Years",
        "body": "Growing up in Poblacion, Argao, Cebu, my early curiosity for how things work laid the foundation for my passion. Living in a vibrant town inspired a strong drive to learn, explore technology, and build solutions from the ground up."
    },
    {
        "title": "Academic Journey",
        "period": "High School - College",
        "body": "Completed my high school education at Argao National High School under the TVL Agriculture track, where I developed practical problem-solving skills and discipline. I then transitioned into higher education at Cebu Institute of Technology – University (CIT-U), sharpening my technical foundation and technical expertise."
    },
    {
        "title": "Current Focus & Vision",
        "period": "Present",
        "body": "Currently focused on full-stack web development and active open-source contributions. I am continuously expanding my skillset in modern frameworks, collaborating on software projects, and aspiring to build scalable, high-impact digital solutions for real-world application."
    }
]

INTERNSHIP_TEXT = (
    "Currently seeking internship and junior engineering opportunities to apply my "
    "computer science foundation, problem-solving skills, and passion for software engineering."
)


CSS = """
<style>
:root {
    --bg: #07090e;
    --surface: #0e131f;
    --surface-hover: #141c2e;
    --accent: #38bdf8;
    --accent-glow: rgba(56, 189, 248, 0.15);
    --muted: #64748b;
    --text: #e2e8f0;
    --text-bright: #ffffff;
    --border: #1e293b;
    color-scheme: dark;
}

html, body, .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background-color: var(--bg);
    color: var(--text);
}

/* Hide default Streamlit header, sidebar, and controls */
[data-testid="stHeader"],
[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Offset page content so it starts below the floating navbar */
.block-container {
    padding-top: 5.5rem !important;
    padding-bottom: 4rem;
    max-width: 1100px;
}

/* Floating Fixed Top Navigation Bar */
div.st-key-top_nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999999;
    background: rgba(7, 9, 14, 0.85);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
    padding: 0.75rem max(1.5rem, calc(50vw - 550px));
}

/* Headings */
h1, h2, h3, h4 {
    color: var(--text-bright) !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}
h1 { font-size: 2.4rem !important; }

/* Custom Cards */
.glass-card {
    background-color: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.4rem;
    height: 100%;
    transition: all 0.2s ease;
}
.glass-card:hover {
    border-color: var(--accent);
    box-shadow: 0 4px 20px var(--accent-glow);
}
.card-accent {
    border-left: 3px solid var(--accent);
}

/* Chips and Badges */
.badge {
    display: inline-block;
    background-color: rgba(56, 189, 248, 0.08);
    color: var(--accent);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 999px;
    padding: 0.2rem 0.75rem;
    margin: 0.2rem 0.2rem 0.2rem 0;
    font-size: 0.8rem;
    font-weight: 500;
}

/* Empty State / Placeholder */
.empty-placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem 1.5rem;
    background-color: var(--surface);
    border: 1px dashed var(--border);
    border-radius: 12px;
    color: var(--muted);
    text-align: center;
}
.empty-placeholder h4 {
    color: var(--muted) !important;
    font-weight: 500 !important;
    margin-bottom: 0.4rem;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
}
[data-testid="stMetricValue"] {
    color: var(--accent) !important;
}

/* Button Styling */
.stButton button {
    border-radius: 8px;
    border: 1px solid var(--border);
    background-color: var(--surface);
    color: var(--text);
    transition: all 0.15s ease;
}
.stButton button:hover {
    border-color: var(--accent);
    color: var(--accent);
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def set_page(name: str) -> None:
    st.session_state.page = name


def empty_state(message: str = "Nothing to see here...") -> None:
    st.markdown(
        f"""
        <div class="empty-placeholder">
            <span style="font-size: 2rem; margin-bottom: 0.5rem;">📁</span>
            <h4>{message}</h4>
            <p style="font-size: 0.85rem; margin: 0;">Add items in <code>app.py</code> to display content.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def badges(items) -> str:
    return "".join(f'<span class="badge">{item}</span>' for item in items)


def show_image(filename: str, caption: str, label: str = "IMG") -> None:
    path = ASSETS / filename
    if not path.exists() and filename == "profile.jpg" and (ASSETS / "me.jpg").exists():
        path = ASSETS / "me.jpg" 
    if path.exists():
        st.image(str(path), caption=caption, width="stretch")
    else:
        st.markdown(
            f"""
            <div class="empty-placeholder" style="min-height: 220px;">
                <span style="font-size: 1.5rem; font-weight: bold; color: var(--accent);">{label}</span>
                <p style="font-size: 0.8rem; margin-top: 0.5rem;">[Image: {filename}]</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


NAV_ITEMS = ["Home", "Autobiography", "Skills", "Projects", "Contact"]

with st.container(key="top_nav"):
    nav_cols = st.columns([2.5, 1, 1.2, 1, 1, 1], vertical_alignment="center")

    with nav_cols[0]:
        st.markdown(
            f"<h3 style='margin:0; font-size:1.15rem; color: var(--accent) !important;'>"
            f"{PROFILE['name']}</h3>",
            unsafe_allow_html=True,
        )

    for i, item in enumerate(NAV_ITEMS):
        with nav_cols[i + 1]:
            is_active = st.session_state.page == item
            st.button(
                item,
                key=f"top_nav_{item}",
                on_click=set_page,
                args=(item,),
                type="primary" if is_active else "secondary",
                width="stretch",
            )


def page_home() -> None:
    col_text, col_img = st.columns([3, 2], vertical_alignment="center", gap="large")
    with col_text:
        st.caption(f"{PROFILE['program']} • {PROFILE['school']}")
        st.title(PROFILE["headline"])
        st.markdown(
            f"<p style='font-size: 1.1rem; color: var(--muted); margin-bottom: 1.2rem;'>"
            f"Welcome to my digital portfolio and personal archive. Based in {PROFILE['location']}."
            f"</p>",
            unsafe_allow_html=True,
        )
        st.markdown(badges([PROFILE["status"], f"Class of {PROFILE['grad']}"]), unsafe_allow_html=True)
        st.write("")
        st.button("Explore My Work →", on_click=set_page, args=("Projects",), type="primary")

    with col_img:
        show_image("profile.jpg", PROFILE["name"], PROFILE["initials"])

    st.write("---")

    m1, m2, m3 = st.columns(3)
    m1.metric("Status", PROFILE["status"])
    m2.metric("Projects", len(PROJECTS))
    m3.metric("Skills", len(SKILLS) if not SKILLS.empty else 0)

    st.write("")
    st.subheader("Objective")
    st.markdown(
        f'<div class="glass-card card-accent"><p style="margin:0; font-size:1.05rem;">{INTERNSHIP_TEXT}</p></div>',
        unsafe_allow_html=True,
    )


def page_autobiography() -> None:
    st.title("Autobiography")
    st.caption("Milestones, lessons, and personal reflections.")
    st.write("---")

    if not CHAPTERS:
        empty_state("Nothing to see here... No chapters added yet.")
        return

    chapter_titles = [c["title"] for c in CHAPTERS]
    view = st.radio("Select Chapter", ["All"] + chapter_titles, horizontal=True)

    selected = CHAPTERS if view == "All" else [c for c in CHAPTERS if c["title"] == view]

    for ch in selected:
        st.markdown(
            f"""
            <div class="glass-card card-accent" style="margin-bottom: 1.2rem;">
                <span class="badge">{ch['period']}</span>
                <h3 style="margin: 0.4rem 0 0.8rem 0;">{ch['title']}</h3>
                <p style="line-height: 1.7; color: var(--text);">{ch['body']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def page_skills() -> None:
    st.title("Skills & Technologies")
    st.caption("Technical toolset and continuous learning.")
    st.write("---")

    if SKILLS.empty:
        empty_state("Nothing to see here... No skills have been configured.")
        return

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("Proficiencies")
        st.dataframe(
            SKILLS,
            hide_index=True,
            width="stretch",
            column_config={
                "Proficiency": st.column_config.ProgressColumn(
                    "Proficiency", min_value=0, max_value=100, format="%d%%"
                )
            },
        )

    with col2:
        st.subheader("Proficiency Chart")
        st.bar_chart(SKILLS.set_index("Skill")["Proficiency"], color="#38bdf8")

    st.write("")
    st.subheader("Tools & Frameworks")
    if not TOOLS:
        empty_state("No tools listed yet.")
    else:
        cols = st.columns(len(TOOLS))
        for col, (cat, items) in zip(cols, TOOLS.items()):
            with col:
                st.markdown(
                    f'<div class="glass-card"><h4>{cat}</h4>{badges(items)}</div>',
                    unsafe_allow_html=True,
                )


def page_projects() -> None:
    st.title("Projects")
    st.caption("Selected personal and collaborative work.")
    st.write("---")

    if not PROJECTS:
        empty_state("Nothing to see here... Projects are currently in development.")
        return

    for idx, p in enumerate(PROJECTS):
        with st.container():
            col_img, col_info = st.columns([1, 2], gap="large")
            with col_img:
                show_image(p["image"], p["name"], p["tag"])
            with col_info:
                st.markdown(
                    f"""
                    <div style="font-size: 0.75rem; letter-spacing: 2px; color: var(--accent);">PROJECT 0{idx+1}</div>
                    <h3 style="margin: 0.2rem 0 0.6rem 0;">{p['name']}</h3>
                    <p style="color: var(--text);">{p['description']}</p>
                    <div class="glass-card" style="padding: 0.8rem 1.2rem; margin: 0.8rem 0;">
                        <div><b>Role:</b> {p['role']}</div>
                        <div><b>Collaborators:</b> {p['collaborators']}</div>
                        <div><b>Outcome:</b> {p['outcome']}</div>
                    </div>
                    <div>{badges(p['stack'])}</div>
                    """,
                    unsafe_allow_html=True,
                )
            st.write("---")


def page_contact() -> None:
    st.title("Contact & Inquiries")
    st.caption("Leave a message or connect through my socials.")
    st.write("---")

    col_form, col_info = st.columns([3, 2], gap="large")

    with col_form:
        st.subheader("Send a Message")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.selectbox(
                "Reason",
                ["Internship Opportunity", "Collaboration", "General Feedback", "Other"],
            )
            msg = st.text_area("Message", height=130)
            submitted = st.form_submit_button("Send Message", type="primary")

        if submitted:
            if not name.strip() or not email.strip() or not msg.strip():
                st.error("Please fill out all required fields.")
            else:
                st.success(f"Thank you, {name}! Your message has been received.")

    with col_info:
        st.subheader("Direct Reach")
        st.markdown(
            f"""
            <div class="glass-card" style="display: flex; flex-direction: column; gap: 0.8rem;">
                <div><b style="color:var(--muted)">Email:</b><br>{PROFILE['email']}</div>
                <div><b style="color:var(--muted)">Phone:</b><br>{PROFILE['phone']}</div>
                <div><b style="color:var(--muted)">Location:</b><br>{PROFILE['location']}</div>
                <div><b style="color:var(--muted)">GitHub:</b><br><a href="{PROFILE['github']}" target="_blank">{PROFILE['github']}</a></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


ROUTES = {
    "Home": page_home,
    "Autobiography": page_autobiography,
    "Skills": page_skills,
    "Projects": page_projects,
    "Contact": page_contact,
}

ROUTES.get(st.session_state.page, page_home)()