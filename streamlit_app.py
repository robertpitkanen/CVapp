# Import libraries
import json
import streamlit as st
import streamlit.components.v1 as components

# Graphs
import plotly.graph_objects as go

# Libraries for ChatGPT
import openai

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
# GDOCS_PATH = 'https://docs.google.com/spreadsheets/u/1/d/1xuY4upIooEeszZ_lCmeNx24eSFWe0rHe9ZdqH2xqVNk/pubhtml' # example url
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

⚡ Fun Fact: Ich habe mir Japanisch mit Anime und Videospielen beigebracht. 
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
    with open("pictures/CV_Robert.pdf", "rb") as file:
        btn1 = st.download_button(
            label="Lade mein Lebenslauf herunter",
            data=file,
            file_name="CV_Robert.pdf",
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
✅ Öffentliches Reden \n
✅ Kreatives Denken \n
✅ Problemlösung \n
✅ Brain Storming 
    """
    )

st.sidebar.divider()

# Timeline UI sections
#data = 'Data'
code = 'HTML Code'
line = 'Visualization'
about = 'About'
view = st.sidebar.radio("View My Timeline", (line, about), index=0) # code

if view == line:
    # render html
    components.html(htmlcode, height=TL_HEIGHT,)

# elif view == data:
    # st.subheader(data)
    # json_parsed = json.loads(json_text)
    # st.write(f"{len(json_parsed['events'])} events")

    # show json
    # st.json(json_text)

# elif view == code:
    # st.subheader(code)
    # st.markdown(htmlcode, unsafe_allow_html=False)

elif view == about:
    st.subheader(about)
    st.markdown('This Streamlit + TimelineJS demo is created by [Rob van Zoest](https://www.linkedin.com/in/robvanzoest/) from [innerdoc.com](https://www.innerdoc.com/).')
    st.markdown('The code is available on [github.com/innerdoc](https://github.com/innerdoc/nlp-history-timeline).')
    st.markdown('With the help of [Streamlit](https://streamlit.io) and [TimelineJS](http://timeline.knightlab.com/) it became a demo timeline about the history of Natural Language Processing!')


# Adding white space between timeline and images
st.markdown('###')

# Chat

# Function to load the API key from a YAML file
# Load your OpenAI API key
OPENAI_API_KEY = ""

# Create an OpenAI client instance with your API key
openai.api_key = OPENAI_API_KEY

dataframe_context = """
Hi there! 👋 I'm Robert, a 9th-grader at Schule Oberägeri with a passion for app development 📱.

Here's a quick overview of me:

* **Skills & Interests:**
    * Aspiring app developer (starting an internship at Lonza AG in August!)
    * Enjoy volleyball 🏐, playing guitar 🎸, anime, manga, and everything Japanese 🇯🇵
    * Fluent in English 🇬🇧, German 🇩🇪, and Swiss German 🇨🇭 (learning French 🇫🇷 too!)
* **Academic Achievements:**
    * Strong grades in math (4.5 average), Informatik (5.5+ average), and English, German, and Science (5+ average)
    * High scores on the Multicheck Test (95% berufsspezifische Fähigkeiten, 88% Potenzial, 77% Schulwissen)
* **Experience:**
    * Completed Schnupperlehre (internships) in app development (Applikationentwicklung) at several companies (Lonza AG, Landis + Gyr AG, Roche AG, Business Systems Integration AG, Exanic AG)
    * Explored platform development at Roche AG
* **Community Involvement:**
    * Actively volunteer at the local youth center in Ägeri, organizing events, helping out, and connecting with people 🤝
"""

# Define the relevant topics
relevant_topics = ["skills", "experience", "interests", "academic achievements", "internship", "app development", "volleyball", "guitar", "anime", "manga", "languages"]

# Function to check if a question is relevant
def is_relevant_question(question, topics):
    question = question.lower()
    return any(topic in question for topic in topics)

# Function to query OpenAI's GPT model
def query_gpt(question, dataframe_context):
    prompt = f"{dataframe_context}\n\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Robert, a 9th-grader at Schule Oberägeri. Answer only questions related to your skills, experience, interests, or academic achievements. If a question is unrelated, respond with 'I'm sorry, I can only answer questions related to my skills, experience, interests, or academic achievements.'"},
            {"role": "user", "content": question}
        ],
        temperature=0
    )
    return response.choices[0].message['content']

# Chat history stored in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat UI in the main page
st.markdown("""
#### Chat with Robert - Future App Developer 📱

Ask me anything about my skills, experience, interests, or academic achievements.

**Here's how to get the most out of our chat:**

* **Ask specific questions:**
    * "What programming languages do you know?"
    * "What are your favorite anime or manga?"
* **Be clear and concise:** This will help me provide accurate and relevant answers. 
* **My responses are based on my personal knowledge and experience:** I'll do my best to answer all your questions!

**Example Questions:**

* "What did you learn during your internships?"
* "What was your favorite Schnupperlehre experience?"

Ready to chat? Ask away! 
""")

def add_to_chat(author, message):
    # Prepend the new message to the beginning of the chat history
    st.session_state.chat_history.insert(0, f"{author}: {message}")

user_message = st.text_input("Your question:", key="user_query")

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    # Handling the chat interaction
    if st.button("Ask"):
        if user_message:
            # Add user message to chat
            add_to_chat("You", user_message)
            if is_relevant_question(user_message, relevant_topics):
                # Use the general summary for every query
                response = query_gpt(user_message, dataframe_context)
            else:
                response = "I'm sorry, I can only answer questions related to my skills, experience, interests, or academic achievements."
            add_to_chat("Bot", response)
        else:
            st.warning("Please enter a question.")
with col2:
    # Optionally, you might want to clear the chat
    if st.button("Clear"):
        st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    st.text(chat)
     
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
    st.image('pictures/292ded60-c52c-44c6-bead-7719989f9e1f.jpg')
