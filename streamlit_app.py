# Import libraries
import json
import streamlit as st
import streamlit.components.v1 as components

# Graphs
import plotly.graph_objects as go


# set page layout to wide
try:
    st.set_page_config(layout="wide")
except:
    st.beta_set_page_config(layout="wide")


# parameters for Timeline
CDN_LOCAL = False
CDN_PATH = 'https://cdn.knightlab.com/libs/timeline3/latest'
CSS_PATH = 'timeline3/css/timeline.css'
JS_PATH = 'timeline3/js/timeline.js'

SOURCE_TYPE = 'json' # json or gdocs
JSON_PATH = 'timeline_nlp.json' # example json

# Timeline height
TL_HEIGHT = 500 # px

# Toast message
st.toast('Hallo 👋 Willkommen zu mein Interaktives Lebenslauf')

# Heading title & image
st.title("ROBERT PITKÄNEN")
st.header("Zukünftiger Applikationsentwickler ")
st.image("pictures/MeAndMyFamily.jpg")

# About me block
st.markdown(
    """ 
    #### Hallo 👋 Mein Name ist Robert Pitkänen 

Hallo 👋 Mein Name ist Robert Pitkänen 

🏫 9. Klässler der Schule Oberägeri | Zukünftiger Applikationsentwickler 💻 

🏐 Volleyball-Enthusiast & Gitarre spieler 🎸 

📖 Interessiere mich für Anime, Manga, Videospiele 

🌱 Ich beginne diesen August mein Applikationsentwickler Lehre bei der Lonza AG! 

🤝 Freiwillige Arbeit im Jugendzentrum: Veranstaltungen organisieren, in der Kiosk helfen usw. 

🗣️ Ich spreche fliessend Englisch, Deutsch und Schweizerdeutsch. Ich lerne auch Französisch!  
    """
    )

# Adding white space
st.markdown('###')

# Using Tabs

tab1, tab2, tab3, tab4 = st.tabs(["🧑‍💻 Schnupperlehre", "📈 Multicheck Results", "🧑‍🎓 Kurse", "🙋‍♂️ Freiwilligenarbeit"])

tab1.write(
        """
        #### :blue[Schnupperlehre für Applikationentwicklung]
        **Lonza AG**, Februar 2024 \n
        **Landis + Gyr AG**, Januar 2024\n
        **Roche AG**, Juni 2023\n
        **Business Systems Integration AG**, April 2023\n
        **Exanic AG**, März 2023

        #### :blue[Schnupperlehre für Plavormentwicklung]
        **Roche AG**, Juni 2023
        """
        )

# Create a bar chart for Multicheck Results
multicheck_fig = go.Figure(go.Bar(
                x=[77, 88, 95],
                y=['Schulwissen', 'Potenzial', 'Berufsspezifische Fähigkeiten'],
                orientation="h"
            ))

multicheck_fig.update_layout(
    title={
        "text": "Multicheck ICT Informatiker/in EFZ Applikationsentwicklung",
        'y':0.85,
        'x':0.6,
        "xanchor": "center",
        "yanchor": "top"
    })

    # Display the bar chart
tab2.plotly_chart(multicheck_fig)

tab3.write(
        """
        #### :blue[Kurse]
        **Work smarter with Microsoft Excel**, February 2024 \n
        **CS50&#39;s Understanding Technology**, Februar 2023 \n
        **Power Searching with Google**, Januar 2023\n
        **Scratch**, September 2022\n
        **Unity from Zero to Proficiency (Foundations)**, März 2022 
        """
        )

tab4.write(
        """
        #### :blue[Volunteering]
        **Arbeiten bei der Kioskteam**, Jugendarbeit Aegrital, 2023 - jetzt \n
        **Junior-coach**, Midnight sports Aegeri, 2023 - jetzt \n
        **Waffeln verkauft im Auto Kino**, Jugendarbeit Aegerital, 2022 
        """
        )

# Adding white space between previous text and buttons
st.markdown('##')

# Layout with columns
col1, col2, col3 = st.columns([1, 1, 2])

# Buttons to download my CV and contact me
with col1:
    with open("pictures/Lebenslauf_Robert_Pitkanen.pdf", "rb") as file:
        btn1 = st.download_button(
            label="Lade mein Lebenslauf herunter",
            data=file,
            file_name="Lebenslauf_Robert_Pitkanen.pdf",
            mime="file/pdf"
          )
with col2:  
    btn2 = st.link_button(
            "Kontaktieren Sie mich ",
            "mailto:robertpitkanen@gmail.com"
          )

    
# load timeline data
json_text = ''
if SOURCE_TYPE == 'json':
    with open(JSON_PATH, "r") as f:
        json_text = f.read()
        source_param = 'timeline_json'
        source_block = f'var {source_param} = {json_text};'
elif SOURCE_TYPE == 'gdocs':
    source_param = f'"{GDOCS_PATH}"'
    source_block = ''


# load timeline css + js
if CDN_LOCAL:
    with open(CSS_PATH, "r") as f:
        css_text = f.read()
        css_block = f'<head><style>{css_text}</style></head>'

    with open(JS_PATH, "r") as f:
        js_text = f.read()
        js_block  = f'<script type="text/javascript">{js_text}</script>'
else:
    css_block = f'<link title="timeline-styles" rel="stylesheet" href="{CDN_PATH}/css/timeline.css">'
    js_block  = f'<script src="{CDN_PATH}/js/timeline.js"></script>'


# write html block
htmlcode = css_block + ''' 
''' + js_block + '''

    <div id='timeline-embed' style="width: 95%; height: '''+str(TL_HEIGHT)+'''px; margin: 1px;"></div>

    <script type="text/javascript">
        var additionalOptions = {
            start_at_end: false, is_embed:true,
        }
        '''+source_block+'''
        timeline = new TL.Timeline('timeline-embed', '''+source_param+''', additionalOptions);
    </script>'''

# Sidebar

# Contact me
st.sidebar.header("Kontaktieren Sie mich")
st.sidebar.markdown(
    """ 
    📧 robertpitkanen@gmail.com \n
    ☎️ +41 78 834 8688 \n
    🚀 github.com/robertpitkanen
    """
    )

st.sidebar.divider()

# Education
st.sidebar.header("Ausbildung")
st.sidebar.markdown(
    """ 
    **Sekundarschule**, Schule Oberägeri, Schweiz \n
    **Primarschule (4-6 Klasse)**, Schule Oberägeri, Schweiz\n
    **Primarschule (1-3 Klasse)**, Haapsalu Linnaalgkool, Estland
    """
    )

st.sidebar.divider()

# Languages
st.sidebar.header("Sprachen")
st.sidebar.markdown(
    """ 
    🇨🇭 Schweizerdeutsch \n
    🇩🇪 Deutsch\n
    🇬🇧 Englisch\n
    🇫🇷 Französisch\n
    🇪🇪 Estnisch
    """
    )

st.sidebar.divider()

# Personal Skills
st.sidebar.header("Persönliche Fähigkeiten ")
st.sidebar.markdown(
    """ 
✅ Teamfähig \n
✅ Selbstsicherheit \n
✅ Schnell lernend \n 
    """
    )

st.sidebar.divider()

# Timeline UI sections
code = 'HTML Code'
line = 'Visualisierung'
about = 'Über Timeline'
view = st.sidebar.radio("Timeline", (line, about), index=0) # code

if view == line:
    # render html
    components.html(htmlcode, height=TL_HEIGHT,)

elif view == about:
    st.subheader(about)
    st.markdown('This Streamlit + TimelineJS demo is created by [Rob van Zoest](https://www.linkedin.com/in/robvanzoest/). The code is available on [github.com/innerdoc](https://github.com/innerdoc/nlp-history-timeline).')

# Adding white space between timeline and images
st.markdown('###')
     
# Adding white space between timeline and images
st.markdown('###')

# Image Gallery

col1, col2, col3 = st.columns(3)

with col1:
    st.image('pictures/IMG_6187.jpg')
    st.image('pictures/IMG_4183.jpg')


with col2:
    st.image('pictures/IMG_0235.jpg')
    st.image('pictures/IMG_7305.jpg')

with col3:
    st.image('pictures/IMG_3389.jpg')
    # st.image('pictures/robert_orlando.jpg')
