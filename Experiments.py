# streamlit run "G:\My Drive\UConn\1-Subjects\Python\STAT476\CODE\StreamlitApp1Deploy\Experiments.py"
import streamlit as st
from streamlit import session_state as Static
def mainline():
    ConsoleClear()
    test10()
    return() # End of function: mainline.

def test10():
    import plotly.express as px
    import random
    import pandas as pd

    x = list(range(0, 100))
    y1 = x
    y2 = [item ** 1.2 for item in x]
    y3 = [item * -1 for item in x]

    # Create an example Pandas dataframe for plotting etc
    # The values are meaningless.
    df= pd.DataFrame()
    i = -1
    for  xvalue in (x):
        i = i + 1
        newrow = {'x' : xvalue,
                  'y1':   y1[i],
                  'y2':   y2[i],
                  'y3':   y3[i],
                  'random1': random.random(),
                  'sum with a long name': y1[i] + y2[i],
                  'sum with a longer name': y1[i] + y2[i] + + y3[i],
                  'random2': random.randint(1,100) 
                }
        df = df.append(newrow, ignore_index=True)
    
    x_slider = st.slider(label="How old are you?",
                    key="mysliderval",
                    min_value= 1.0,
                    max_value=100.0,
                    step=0.5,
                    format=None,
                    help="A help tooltip string",
                    on_change=slider_onchange_event, 
                    )
    st.write("I'm ", x_slider, 'years old')
      
    Fig1 = px.line(df, 
       x="x", 
       y=["y1","y2","y3"],
       color_discrete_map={"x":"red","y1":"blue","y2":"green","y3":"orange"},
       template="simple_white"
       )
    Fig1.add_vline(x=x_slider, line_width=3, line_dash="dash", line_color="green")
    st.plotly_chart(Fig1, use_container_width=True)   # Plot!
    return()


def slider_onchange_event():
    #Fig1.add_vline(x=G.PrevInt,line_dash="dash", line_color="red")

    return()



def test9():

    import streamlit as st
    import plotly.figure_factory as ff
    import numpy as np
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    # Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
             hist_data, group_labels, bin_size=[.1, .25, .5])
    st.plotly_chart(fig, use_container_width=True)   # Plot!
    
    return()




def test8():
    import base64
    import requests
    # The non raw version will go to the file at github and show it in a simple pdf viewer without index.
    Link01 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf"

    page = requests.get(Link01)
    st.write (page.text)
    
    base64_pdf = base64.b64encode(page)
    pdf_display = f"<iframe src='data:application/pdf;base64,{base64_pdf}' width='700' height='1000' type='application/pdf'></iframe>"
    st.markdonw(pdf_display)
    return()





def test7():
    # Method 3: Open with webbrowser
    import webbrowser
    # This will pop up the pdf if googles pdf reader page. But no index or working links.
    Link01 = r"https://smallpdf.com/pdf-reader?url=https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf?raw=true"
    # This will pop up the pdf if googles pdf reader page. But no index or working links.
    Link01 = r"https://docs.google.com/viewer?url=https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf?raw=true"
    # The non raw version will go to the file at github and show it in a simple pdf viewer without index.
    Link01 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf"

    # The raw version will download the pdf automatically.
    Link01 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf?raw=true"

    webbrowser.open_new(Link01)
    return()


def test6():
    st.markdown("""
    <embed src="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="400" height="400">
    """, unsafe_allow_html=True)

    return()


def test5():
    from bokeh.models.widgets import Div
    import streamlit as st
    
    # if st.button('Go to Streamlit'):
    #     js = "window.open('https://www.streamlit.io/')"  # New tab or window
    #     #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    #     js = "window.open('https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/github.io/Resource_ProgramDocumentation.pdf/')" 
    #     html = '<img src onerror="{}">'.format(js)
    #     div = Div(text=html)
    #     st.bokeh_chart(div)
    import urllib.request
    import webbrowser
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    try:
        webbrowser.get(chrome_path).open('http://docs.python.org/')
    except urllib.error.URLError as e: 
        st.write(e.reason)
        
    st.markdown("<a href='https://sumanbogati.github.io/sample.pdf' target='_BLANK'>Click here to open the file</a> "   )
        
    # webbrowser.open('https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/github.io/Resource_ProgramDocumentation.pdf')
    st.write("hit")
    
    # import urllib.request
    # try:
    #    with urllib.request.urlopen('http://www.python.org/') as f:
    #       st.write(f.read().decode('utf-8'))
    # except urllib.error.URLError as e:
    #    st.write(e.reason)
    # st.write('i thik this is how u do it')
    return



def test4():
    # It's very easy to display Pdf in browser from Github static page, for that you need approach following process,

    # Make the static website/repository using your Github username, for example, if the username is sumanbogati then repository would be sumanbogati.github.io
    # Put the desired pdf in that repository
    # Now locate the Url of Pdf wherever you want
    # For example, to display pdf in Html web page
    
    # <embed src="https://sumanbogati.github.io/sample.pdf" type="application/pdf" />
    # This is an instant demo.
    
    
    
    #   https://stackoverflow.com/questions/30745981/opening-pdf-in-a-browser-with-github-pages
    # https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/github.io/Resource_ProgramDocumentation.pdf
    # e1 = "<embed src="https://sumanbogati.github.io/sample.pdf" type="application/pdf" />"
    # e2 = "https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/github.io/Resource_ProgramDocumentation.pdf" />"
    e3 = "https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/github.io/Resource_ProgramDocumentation.pdf"
    #src="https://docs.google.com/gview?url=https://sumanbogati.github.io/sample.pdf&embedded=true" style="width:600px; height:500px;" frameborder="0"></iframe>
    
    # st.markdown("""
    # <embed src="https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf" width="400" height="400">
    # """, unsafe_allow_html=True)
    
    e7 = """<embed
    src="http://infolab.stanford.edu/pub/papers/google.pdf#toolbar=0&navpanes=0&scrollbar=0"
    type="application/pdf"
    frameBorder="0"
    scrolling="auto"
    height="100%"
    width="100%"
    </embed>"""
    
    
    # st.markdown(e7, unsafe_allow_html=True)
    
    st.markdown("""
    <embed src="<embed src="https://sumanbogati.github.io/sample.pdf" type="application/pdf" />" width="400" height="400">
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <embed src="<embed src="https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/github.io/Resource_ProgramDocumentation.pdf" type="application/pdf" />" width="400" height="400">
    """, unsafe_allow_html=True)
   


    return()


def test3():
    tempstr = """Pretty printing python dictionarys is easy using streamlit.   
Even nested dictionaries.  \r
We use the st.dataframe feature."""
       
    Static['TextBox2'] = tempstr        
    title = st.text_area(
            key="TextBox2",   # Value will be placed in GUI['MsgText'].
            label="",
            height=1,
            max_chars=None,
            help="Watch here for instructions and error messages",
            on_change=None)
    st.write("Contents:  \r" + title)
    return()

def test2():
    ###########################################################################
    # DEMONSTRATE SHOWING A PYTHON DICTIONARY ON A STREAMLIT WEBPAGE.
    
    people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}, 
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}

    st.info("DEMONSTRATE SHOWING A PYTHON DICTIONARY ON A STREAMLIT WEBPAGE.")
    st.text("Pretty printing python dictionarys is easy using streamlit.  \n"
            "Even nested dictionaries.  \n"
            "We use the st.dataframe feature.")
    st.dataframe(people)
    return

def test1():
    # Show a post plot message.
    temptext = f"""
         ## Box Header.    
        {Text_MD01()}         
        More text.
        """
    st.info(temptext )
    st.markdown(Text_MD02() )
    
    # Create a popup message describing the plot.
    st.button("Plot Details 1",help=Text_MD01() + "  \r" + Text_MD02())
    st.button(":arrow_down: How To Enlarge or Save The Plot",help=Text_MD02() )
    st.write("👇  How to include icons in any text",help="help text here" )    
    
    # /r is line feed not \r] carriage return
    st.markdown("This is text that   \rgoes on and on.")  
  
    return()

def Text__MD01(TitleLength = "short"):
    # Build a text message in markdown for display in Streamlit.
    GRowsToGenerate = 149
    AFloatNumber = 679.4357234
  
    # Add at least 4 spaces after a line to start an unspaced new line.
    TextMD = f"""
    The Values You Entered A Listed Below:    
        Rows To Generate = {"{:d}".format(GRowsToGenerate)}.             
        AFloatNumber = {"{:.5f}".format(AFloatNumber)}.         
      """
    return(TextMD)   #  End of function: Title_Build

def Text_MD01():
    # Build a text message in markdown for display in Streamlit.
    GRowsToGenerate = 149
    AFloatNumber = 679.4357234
  
    # Add at least 4 spaces after a line to start an unspaced new line.
    TextMD = f"""The Values You Entered A Listed Below:            
        - Rows To Generate = {"{:d}".format(GRowsToGenerate)}.    
        - AFloatNumber = {"{:.5f}".format(AFloatNumber)}.    
      """
    return(TextMD)   #  End of function: Text__MD01
 
def Text_MD02():
    # Build a text message in markdown for display in Streamlit.
    # Add at least 4 spaces after a line to start an unspaced new line.
    TextMD = """To Enlarge or Save The Plot:                 
      - You can enlarge the plot using the View full screen icon:             
          - The icon is above and to the right of the plot.                  
      - You can save the plot to your computer                               
          - Right click on the plot, then use 'save image' or 'copy image'.   
         """    
    return(TextMD)   #  End of function: Text__MD02
 
 

 
 
def ConsoleClear():  # Clear all output in console.
    try:     # This works regardless of Operating System prevailin
        from IPython import get_ipython
        get_ipython().magic("clear")
        get_ipython().magic("reset -f")
    except:
        pass
    return()  # End of function: Console_Clear

def Title_Build_0(TitleLength = "short"):
    GRowsToGenerate = 145
    AFloatNumber = 678.4357234
    Title_1 = str(""+
                   "Rows To Generate = {:d}  \r".format(GRowsToGenerate)  +
                   "AFloatNumber = {:.5f}".format(AFloatNumber) + "."
                   ) 
    return(Title_1)   #  End of function: Title_Build

mainline()