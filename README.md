# Daniel Mark B. Aguilar — Autobiography & Interactive Portfolio

An interactive, personal autobiography and software engineering portfolio web application built with **Streamlit**, **Pandas**, and **NumPy** for **CSIT 349 (Applied Artificial Intelligence)** at **Cebu Institute of Technology – University (CIT-U)**.

---

## Overview

This web application serves as a living academic dossier and portfolio for **Daniel Mark B. Aguilar**, a BS Computer Science student at CIT-U. It highlights his technical origins, academic progression, software engineering proficiencies, and showcased projects (.NET/C#, Blazor, ASP.NET Core, and open-source contributions).

The interface is built with a bespoke **floating glassmorphic top navigation bar**, completely replacing the default collapsible sidebar for a seamless, modern web experience.

---

## Features & Sections

- **Floating Glassmorphic Top Navigation:** Fixed, blurred backdrop navbar (`Home`, `Autobiography`, `Skills`, `Projects`, `Contact`) that remains easily accessible as you scroll through content.
- **Home & Hero Section:** 
  - Executive introduction, student status badges, and academic metrics.
  - Personal portrait display rendered from `assets/me.jpg`.
  - Professional objective and internship outlook callout.
- **Autobiography:** 
  - Chronological story chapters covering *Origins & Early Spark* (Argao, Cebu), *Academic Journey* (Argao National High School TVL Agriculture track to CIT-U BSCS), and *Current Focus & Vision*.
  - Built-in graceful empty-state handling for milestones.
- **Skills Matrix & Tools:** 
  - Quantitative proficiency ratings across languages and frameworks (C#/.NET, ASP.NET Core, Blazor, SQL, Tailwind CSS, Git).
  - Categorized toolchain registers (Visual Studio, Docker, Supabase, PostgreSQL, Figma).
- **Featured Projects Showcase:** 
  - **AcademIQ:** Decoupled academic management web platform built with ASP.NET Core API and Blazor WebAssembly.
  - **GatherTable:** Event dining coordination and dietary matrix platform using Blazor Server and Tailwind CSS.
  - **Ambussin:** Open-source gameplay and systems contributions (C#, Unity, Git).
  - High-resolution project previews dynamically loaded from `assets/unnamed.png`.
- **Transmission & Contact Portal:** 
  - Fully reactive contact and feedback form that validates input and returns a real-time confirmation message.
  - Direct communication links (Institutional email, GitHub profile, and location).

---

## Tech Stack & Dependencies

- **Language:** Python 3.10+
- **Core Framework:** [Streamlit](https://streamlit.io/) (v1.30.0+)
- **Data Handling:** [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
- **Frontend / Styling:** Bespoke CSS3 (Glassmorphism, custom sticky positioning, CSS variables)
- **Primary Color Palette:** Deep Obsidian (`#07090E`), Slate Surface (`#0E131F`), Electric Sky Accent (`#38BDF8`), Soft Gray Text (`#E2E8F0`).

---

## Getting Started

### 1. Clone or Open the Repository
```bash
git clone https://github.com/DanielMarkA/portfolio-streamlit.git
cd portfolio-streamlit
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

The application will launch automatically in your default browser at `http://localhost:8501`.