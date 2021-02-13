#Copyright [2020] [EXCISION LIMITED]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import streamlit as st
import pandas as pd
pd.options.display.max_colwidth = 1000000
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly
import plotly.express as px          
import plotly.graph_objects as go    
import plotly.figure_factory as ff
import io
import requests

#@st.cache(suppress_st_warning=True)

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Main                                                                                           #
# ::: Handles the navigation / routing and data loading / caching                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#

def main():    
    st.sidebar.subheader('Navigator')
    page = st.sidebar.radio('Go to:',
                            ["Registrar Toolkit",
                             "Excision Ltd Team",])

    if page ==   "Registrar Toolkit":       show_explore()
    elif page == "Excision Ltd Team":       show_the_app_team()

    st.sidebar.markdown('''**Contribute**''')
    st.sidebar.info("Contact Maria or Alastair to add useful info.")

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About the team                                                                                 #
# :::                                                                                             #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_the_app_team():
    st.title("App Design Team")
    st.markdown('''The team consists of a group of General Surgeons based in Edinburgh who are
                motivated to develop software to improve surgical **data systems**,
                **research** and **education**.''')
    st.markdown('''To meet these aims, a company called **Excision** was founded in 2020, and
                **SurgicalEps** Web App was the first major project.''',unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown('''**Contact details**''')
    st.sidebar.info('''Get in touch with any comments, queries or suggestions about this
                    App:surgicaleponyms@gmail.com''')
    
    st.subheader("App Developer")
    about1 = st.checkbox("Alastair Hayes")
    if about1:
        st.markdown('''Alastair is a Specialty Training Registrar in Edinburgh with interests
                    in Upper GI, Endocrine and Emergency General Surgery. His qualifications
                    include FRCSEd (Gen Surg) & PhD.''')
        st.markdown('''He is working to develop data science and software solutions for clinical
                    data systems, research and education in surgical practice.''')

    st.subheader("Associate App Developer")
    about2 = st.checkbox('''Anne Ewing''')
    if about2:
        st.markdown('''Anne is Specialty Training Registrar in Edinburgh with interests in Upper
                    GI, Hernias and Emergency General Surgery. She is passionate about surgical
                    teaching and outside work Anne is a competitive triathlete.''')

    st.subheader("Surgical Registrar ToolKit App - Coordinator")
    about2 = st.checkbox('''Maria Boland''')
    if about2:
        st.markdown('''Maria is awesome too...detail....:)....''')

    st.subheader("Acknowledgements")
    st.markdown('''[Google](https://www.google.com/search/howsearchworks/?fg=1),
                   [Mapbox](https://www.mapbox.com),
                   [Pandas](https://pandas.pydata.org), [Plotly](https://plotly.com/python/),
                   [PubMed&reg;](http://www.ncbi.nlm.nih.gov/pubmed),
                   [Streamlit](https://www.streamlit.io)''')

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Explorer                                                                                       #
# ::: Handles the navigation                                                                      #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def show_explore():
    st.write('''_# UNDER CONSTRUCTION # UNDER CONSTRUCTION # UNDER CONSTRUCTION #_''')
    st.markdown('''# RIE General Surgery Registrar ToolKit''')
    exp = st.radio('Go to:',
                                ["About",
                                 "Regional Hospitals",
                                 "UGI / General Surgery Dept at RIE",
                                 "Emergency Teams (ET1/ET2)",
                                 "Elective Work",
                                 "Shifts & Rotas",
                                 "Useful Info & Contact Numbers",
                                 ])
    
    if   exp == "About":                                exp_about()             #1
    elif exp == "Regional Hospitals":                   exp_Lothian()           #2
    elif exp == "UGI / General Surgery Dept at RIE":    exp_UGI()               #3
    elif exp == "Emergency Teams (ET1/ET2)":            exp_ET()                #4
    elif exp == "Elective Work":                        exp_Elective()          #5
    elif exp == "Shifts & Rotas":                       exp_Rotas()             #6
    elif exp == "Useful Info & Contact Numbers":        exp_Info()            #7
    elif exp == "Useful info for Edinburgh":            exp_OutWork()           #8
    elif exp == "Tips from ex-Fellows":                 exp_Tips()              #9 

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  About (1)                                                                                      #
# ::: Handles                                                                                     #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_about():
#Page
    st.markdown("---")
    st.subheader('Who is this App for?')
    st.write('''We designed this App to help visiting Fellows settle into the local Department of surgery and
                living in Edinburgh.''')
    st.subheader('How to use this App?')
    st.write('Select from options above to access different types of helpful information. Below is a summary of the different options.')
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Regional Hospitals:</span>
                   <span style="font-size:12pt;color:black;"> Maps and info from NHS Lothian and neighboring health boards
                   (eg. Fife, Borders, Forth Valley).</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">UGI / General Surgery Dept at RIE:</span>
                   <span style="font-size:12pt;color:black;"> Detail about our unit.</span>''',
                   unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Emergency Teams:</span>
                   <span style="font-size:12pt;color:black;"> How these work.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Elective:</span>
                   <span style="font-size:12pt;color:black;"> Days surgery, Cancer, Bariatrics, Benign Hiatal, Hernia work these work.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Rotas:</span>
                   <span style="font-size:12pt;color:black;"> How these work.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Useful info for work:</span>
                   <span style="font-size:12pt;color:black;"> Summary.</span>''',unsafe_allow_html=True)
    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Useful Information:</span>
                   <span style="font-size:12pt;color:black;"> GPs, School, Sports, Bars, Restaurants, Churches/Worship, Nightclubs, Guitar shops, Food shops, Renting.</span>''',unsafe_allow_html=True)

    

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Lothian (2)                                                                                    #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Lothian():
    st.markdown("---")
    st.subheader('''Regional Hospitals''')
    #st.write(' ')
    url = 'https://raw.githubusercontent.com/HayesAJ83/SurgicalRegToolKit/main/Lothian4python_Lite.csv'
    df1 = pd.read_csv(url, dtype={'PMID':str,'Year':int})
    df2 = df1.sort_values(by=['Place'],ascending=True)
    mapbox_access_token = 'pk.eyJ1IjoiYWpoYXllczgzIiwiYSI6ImNrY2pqM2lvMDB4Z24ydG8zdDl0NTYwbTUifQ.2DKVfTAaE77XAXMpDeq_Pg'
    site_lat = df2['Lat_A1']                          
    site_lon = df2['Long_A1']           
    text = df2['Place'].astype(str)
    locations_name = df2['Place']
    color= df2['Colour'].astype(str)

    types = st.selectbox('Select hospital:',
                     options=["Astley Ainslie Hospital",
                              "Borders General Hospital - BGH",
                              "Forth Valley Hospital",
                              "Royal Edinburgh Hospital",
                              "Royal Infirmary of Edinburgh - RIE",
                              "Spire Murrayfield",
                              "St. John's Hospital - SJH",
                              "Victoria Hospital - VHK",
                              "Western General Hospital - WGH",], index=4)
    
    figG3 = go.Figure()
    figG3.add_trace(go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers',
                marker=go.scattermapbox.Marker(size=12,color=color,opacity=0.8),
                text=text,hoverinfo='text',))

    if types == "Astley Ainslie Hospital":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.92982,lon=-3.19899),
                pitch=5,zoom=9.5,style='satellite-streets'))

    if types == "Borders General Hospital - BGH":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.59573,lon=-2.74245),
                pitch=5,zoom=7.0,style='satellite-streets'))

    if types == "Forth Valley Hospital":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=56.02526,lon=-3.84879),
                pitch=5,zoom=7.0,style='satellite-streets'))

    if types == "Royal Edinburgh Hospital":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.92760,lon=-3.21384),
                pitch=5,zoom=9.5,style='satellite-streets'))

    if types == "Royal Infirmary of Edinburgh - RIE":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.92137,lon=-3.13415),
                pitch=5,zoom=9.5,style='satellite-streets'))

    if types == "Spire Murrayfield":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.94431,lon=-3.26628),
                pitch=5,zoom=10,style='satellite-streets'))

    if types == "St. John's Hospital - SJH":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.89211,lon=-3.52319),
                pitch=5,zoom=8.5,style='satellite-streets'))
        
    if types == "Victoria Hospital - VHK":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=56.12519,lon=-3.15814),
                pitch=5,zoom=7,style='satellite-streets'))

    if types == "Western General Hospital - WGH":
        figG3.update_layout(
                autosize=True,hovermode='closest',showlegend=False,width=340,height=240,
                mapbox=dict(accesstoken=mapbox_access_token,bearing=0,center=dict(lat=55.9634,lon=-3.23521),
                pitch=5,zoom=10,style='satellite-streets'))
        

    figG3.update_layout(margin=dict(l=2, r=2, t=0, b=0))
    st.write(figG3)
    st.markdown('''<span style="font-size:10pt;color:black;">**Zoom** into map using **touchscreen**.</span>''', unsafe_allow_html=True)

    
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  UGI (3)                                                                                        #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_UGI():
    st.markdown("---")
    st.subheader("The UGI / General Surgery Dept")
    st.write('Department Overview')

    exp = st.radio('Topics:',#'Select',
                                ['Ward Rounds',                  
                                 'Day Surgery Unit',       
                                 'Operating Theatres',      
                                 'Secretaires',
                                 'Management team',
                                 'Morbidity & Mortality Meeting',
                                 ])

    if   exp == "Ward Rounds":                      in_wards()       #T1 # 
    elif exp == 'Day Surgery Unit':                 in_dsu()         #T2 #
    elif exp == "Operating Theatres":               in_th()          #T3 #
    elif exp == "Secretaries":                      in_secy()
    elif exp == "Management team":                  in_mx()
    elif exp == "Morbidity & Mortality Meeting":    in_mm()



def in_wards():
    st.markdown("---")
    st.write('* The team meets at ward 107 (Base A) to start the round. Ward 107 is on the first floor.')
    st.write('* The morning ward round is led by registrar and FY1, and normally directly supervised by consultants')
    st.write('* This starts at 8:00 am on Mondays, Tuesdays & Thursdays.')
    st.write('* The morning round begins a little later on Wednesdays, after the M&M meeting - approx 08:45 to 09:00 start.')
    st.write('* Starting at W107, we go to W106, and then onto critical care (W116 or W118)')
    st.write('* There is an FY1 dr on the rounds, their bleep number is **4583**')
    st.write('* There is an afternoon ward round')

#    st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Emergency Teams:</span>
#                   <span style="font-size:12pt;color:black;"> How these work.</span>''',unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  ET (4)                                                                                         #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_ET():
    st.markdown("---")
    st.subheader("Emergency Team") 
    ET = st.radio('Select component:',
                          options=['CEPOD - Theatre 17 or 13','ET1','ET2','Hot clinic',],index=1)

  

#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Elective (5)                                                                                   #
# ::: Handles                                                                                     #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Elective():
    st.markdown("---")
    st.subheader("Elective - UGI / General Surgery")
    Elective = st.radio('Select subspecialty:',
                          options=['Oesophagogastric Cancer',
                                   'Bariatrics',
                                   'Complex Hernia',
                                   'Benign Hiatal',
                                   'General Surgery',
                                   'Neck Endocrine',
                                   ],index=0)

    if   Elective == 'Oesophagogastric Cancer': elec_OG()
    elif Elective == 'Bariatrics':              elec_Bar()
    elif Elective == 'Complex Hernia':          elec_Hernia() 


def elec_OG():
    st.write('OG Cancer Multi-Disciplinary Meeting')
    st.write('OG Cancer clinic')
    st.write('OG Cancer team personel')
    st.write('OG Cancer Fellow')
    st.write('OG Cancer Theatre sessions')


def elec_Bar():
    st.write('Bariatrics Multi-Disciplinary Meeting')
    st.write('Bariatrics clinic')
    st.write('Bariatrics team personel')
    st.write('Bariatrics Theatre sessions')


def elec_Hernia():
    st.write('Hernia clinics')
    st.write('Hernia team personel')
    st.write('Hernia Fellow')
    st.write('Hernia Theatre sessions')
    




#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Rotas (6)                                                                                      #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Rotas():
    st.markdown("---")
    st.subheader("Shifts & Rotas - Link to latest version ")
    st.write('Elective day shifts')
    st.write('Clinics')
    
   




#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Useful Information (8)                                                                               #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def exp_Info():
    st.markdown("---")
    st.markdown('''### Useful Information''')
    Info = st.radio('',
                     options=['At Work',
                              'Outside Work',],index=0)

    if Info == 'At Work':        info_work()
    elif Info == 'Outside Work':   info_ed()


#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Outside Work (9)                                                                               #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def info_work():
    st.subheader("RIE tips")
    exp = st.radio('Topics:',#'Select',
                                ['Contact numbers & how to bleep',
                                 'The Wards',                  
                                 'In the Day Surgery Unit',       
                                 'Operating Theatres',      
                                 'Secretaires',
                                 'Management team details',
                                 ])

    if   exp == "The Wards":                                info_wards()       #T1 #
    elif exp == 'In the Day Surgery Unit':                  info_dsu()         #T2 #
    elif exp == "Operating Theatres":                       info_th()          #T3 #
    elif exp == "Secretaries":                              info_secy()
    elif exp == "Management team":                          info_mx()
    elif exp == "Contact numbers & how to bleep":           info_bleep()

def info_wards():
    st.markdown("---")
    st.write('''* The elective ward **FY1 bleep** for UGI ward rounds is **4583**. See 'making a bleep' topic above.''')
    st.write('''* **Ward 107**: This is where we prefer our elective patients to go who aren't suitable for day surgery or need critical care.''')
    st.write('''* **Ward 106**: This is where we prefer our emergency patients to go who can't stay in surgical obervation unit down on the ground floor.''')
    st.write('''* **Ward 116**: This is a high dependency unit, refered to as level 2 care, where usually non-intubated patients with organ support or complex acute issues, including monitored trauma patients, are cared for. Usual admission/discharge criteria have changed during pandemic, with some intubated patients being located here.''')
    st.write('''* **Ward 118**: This is the intensive therapy unit, refered to as level 3 care, where usually intubated patients are located.''') 
    st.write('''* **Ward 105**: This is the Vascular Surgical ward, occasionally we may have emergency admission patients here.''')

def info_bleep():
    st.markdown("---")
    st.subheader('Our Emergency Team')
    st.write('''* General Surgical Registrar Oncall at RIE: **5569 bleep**''')
    st.write('''* General Surgical ANP or FY2 Oncall at RIE: **2254 bleep**''')
    st.write('''* General Surgical ANP number: **07747473249**''')
    st.write('''* CEPOD Theatres co-ordinator phone: **07790826007**''')
    st.write('''* Anaesthetics Registrar Oncall: **2200 bleep**''')

    st.subheader('Emergency Contacts - RIE')
    st.write('''* Radiology Registrar Oncall: **tbc**''')
    st.write('''* Critical Care Registrar Oncall: **is this 2306 bleep?**''')
    
    st.write('''* Orthopaedics Registrar Oncall at RIE: **tbc**''')
    st.write('''* Cardiothoracics Registrar Oncall at RIE: **tbc**''')


    st.subheader('Emergency Contacts - WGH')
    st.write('''* Colorectal Registrar Oncall at WGH: **079 tbc**''')
    st.write('''* Colorectal FY2 Oncall at WGH: **tbc**''')
    
    st.subheader('Elective')
    st.write('''* The elective ward **FY1 bleep** for UGI ward rounds is **4583**. See 'making a bleep' topic above.''')

    
#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Outside Work (9)                                                                               #
# ::: Handles the                                                                                 #                                                                                              
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
def info_ed():
    st.subheader("Edinburgh Life")
    exp = st.radio('Select:',
                                ['Leisure',        # -
                                 'Medical Care',   # -
                                 'Child Care',     # -
                                 'Places of Worship',
                                 'Best Bars',
                                 ])

    if   exp == "Leisure":           out_leisure()       #T1 #- 
    elif exp == 'Medical Care':      out_medical()       #T2 #-
    elif exp == "Child Care":        out_child()         #T3 #-
    elif exp == "Places of Worship": out_worship()
    elif exp == "Best Bars":         out_bars()



#-------------------------------------------------------------------------------------------------#
#                                                                                                 #
#  Tips (9)                                                                                   #
# ::: Handles the                                                                                 #                                                                                              #
#                                                                                                 #
#-------------------------------------------------------------------------------------------------#
#def exp_Tips():
#    st.markdown("---")
#    st.subheader("Tips from our previous fellows")
#    exp = st.radio('Topics:',#'Select',
#                                ['Things I wish someone had told me',        # - ,
#                                 ])

#st.markdown('''<span style="font-size:12pt;color:black;font-weight:bold;">Tips & tricks:</span>
#                   <span style="font-size:12pt;color:black;">Barbora, Gustav, Adam, Maria, Matteo and others.</span>''',unsafe_allow_html=True)


#-------------------------------------------------------------------------------------------#


if __name__ == "__main__":
    main()
