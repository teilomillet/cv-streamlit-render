from pathlib import Path

import streamlit as st
from PIL import Image

# -- Path settings --------------------------------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Teïlo_Millet.pdf"
profile_pic = current_dir / "assets" / "profile-pic(1).png"



# -- General Settings --------------------------------
PAGE_TITLE = "Teïlo Millet"
PAGE_ICON = ":wave:"
NAME = "Teïlo Millet"
Description = """
📊 Junior Data Analyst, aspiring Data Applications Builder, assisting enterprises by supporting data-driven decision-making
"""
EMAIL = " teilomillet@proton.me"
SOCIAL_MEDIA = {
    "LinkedIn": "http://linkedin.com/in/teilomillet",
    "Github": "http://github.com/teilomillet",
    "Twitter": "http://twitter.com/disteilo"
}

PROJECTS = {
    "Here will be all the project": "github.com/teilomillet/ici",
    "🚀 Improve decision-making": "github.com/teilomillet/ici",
    "💰 Sales": "github.com/teilomillet/ici",
    "🚚 Transport": "github.com/teilomillet/ici",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Title
st.title("Yo")


# -- Load CSS, PDF & PROFIL PIC --------------------------------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# -- HERO SECTION --------------------------------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(Description)
    st.download_button(
        label="📝 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime="applications/octet-stream",
    )
st.write("📨", EMAIL)



# -- SOCIAL LINKS --------------------------------
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATION --------------------------------
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
"""
- ✅ Ici on ecrit son experience et ses qualifications,
- ✅ genre bla
- ✅ blablablabla
"""
)

# --- SKILLS -----------------------------------------
st.write("#")
st.subheader("Skills")
st.write(
"""
- 👨‍💻 Ici on décrit ses skills,
- 📈 genre bla
- 📊 blablablabla
- 🗂 blablallallad
"""
)

# --- PROJECTS & ACCOMPLISHMENTS --------------------------------
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Work History --------------------------------
st.write("#")
st.subheader("Work History")
st.write("---")

#--- Job 1 --------------
st.write("📊", "Job 1")
st.write("DATE - To DATE")
st.write(
"""
- Resume 1
- Resume 230
"""
)
st.write("---")
#--- Job 2 --------------
st.write("📊", "Job 2")
st.write("DATE - To DATE")
st.write(
"""
- Resume 30
- Resume 44
"""
)
