# This code is a template for a python app to run in a streamlit webpage.
# The webpage has a familiar "toolbar on left / plot and output on right"
#  layout.

# To run this app in a web browser undeployed on the development computer
# rub the following command in the Anaconda console.
# streamlit run "G:\My Drive\UConn\1-Subjects\Python\STAT476\CODE\StreamlitApp1\StreamlitApp1.py"
   

import streamlit as st
from streamlit import session_state as GUI
   # Writing GUI['VarName'] is easier than writing st.session_state['VarName'] 
import matplotlib as mpl  # We are using Matplotlib objects.
import os
import pandas as pd
import numpy as np
import random
from PIL import Image  # For getting and displaying images in streamlit.



# PDF imports
import urllib.request  # For getting a pdf file online.
import base64    # For showing PDFs.
import tempfile  # For manipulating and showing a PDF file in streamlit.
  

class Global_Variables():  # A class for creating all python global variables.

    # USERS INPUTS (Copied from input widgets and internalized)
    RowsToGenerate = None
    AFloatNumber = None
    ShowLine3 = None
    ShowInput = None
    ShowData = None
    
    # SUNDRY GLOBAL VARIABLES
    Fig1 = None
    Plot1 = None
    Msg01 = "Fill out the input boxes and click the 'Plot Now' button."
    Debug = False
    ThisModule_Version = "7.0"
    ThisModule_FullPath  = None
    ThisModule_FileName = None
    ThisModule_ProjectPath = None
    Title_1 = None
    Title_2 = None
    
    
    # DATA TO BE PLOTTED
    x = []
    y1 = None
    y2 = None
    y3 = None  
    
    # A Pandas Dataframe

    DataTable = pd.DataFrame(
    columns=["x",
             "y1",
             "y2",
             "y3",
             "random1",
             "sum with a long name",
             "sum with a longer name",
             "random2"]
                           )
    
# End of Global Variables
G = Global_Variables()    # Instantiate our global variables.

def MainLine():
    # Remember this app is rerun every time the GUI is displayed.
    # So we have to keep track of the conversation state and preserve
    # or recreate variables.
    
    # Note: Console output from this program - like print("Whatever") - will
    # appear in the streamlit console NOT the usual python console.
    #    If this is too inconvenient, you can write debbuging information etc,
    #    to the streamlit webpage.
    ConsoleClear()  # Clear the internal IPyhon console.
    
    G.Debug = False  # Trace and dump some important variables.

    # If this the initial session create "Static/Persistent" variables.
    if 'Dialog_State' not in GUI:
        if G.Debug: print("Debug: First Display. Display count=1")   
        Perform_Program_Initialization()
        GUI['Dialog_State'] = 1  # Upgrade state so we don't come back here.

    else:  # We are responding to a session reply from the user.
        GUI['Display_Count'] += 1  # Count of sessions.
        if G.Debug: 
           print("Debug: Input received. Display count=", GUI['Display_Count'])  
        
        # Initalize variables for every run.
        #   Remember nothing outside the GUI static/persistant dictionary
        #   is preserved across sessions. So we perform the one time
        #   program initialization once then perform the "every run"
        #   intialization.
        Perform_EveryRun_Initialization()
        # Validate and internalize users'input.
        InputOK = Validate_And_Internalize_User_Input()
        if InputOK == True:
            # Process the users input and generate the data for plotting
            Process_Users_Data()
            # Plot the data
            Plot_Build()
        else:
            # There is an error in the users input. 
            # A message describing the error is already set.
            pass
    # Having prepared all output, we now insert the output into our GUI.
    # display the GUI and wait for next user input.
    GUI_Build_And_Show()
    return()  # End of function: MainLine.

def Perform_Program_Initialization():

    # During the first load session, we create our "Persistent" variables.
    #  Persistent variables:
    #   - Are stored and created by streamlit.
    #   - Are static (preserved) between sessions.
    #   - Are effectively global.
    #   - Have a python dictionary like syntax.
    #   - Are created using the streamlit "session_state" method.
    #       - Eg:  st.session_state['Display_Count'] = 0
    #       - In our case the st.session_State is abbreviated at import to GUI.
    #          - Eg: GUI['Input_SSN'] = 0
    #   - Can be "linked" to a streamlit widget via the widget key= parameter.
    #      - Any change in the GUI linked widget will automatically update 
    #      - the linked persistant variable.
    #      - Any change in linked persistant variable will automatically 
    #        update the linked widgets value in th GUI.
    #      - The python type of linked variables are specifed by the
    #        linked widget's  "format=" parameter.
    #
    #      - Eg of a Linked persistent variable.
    #         In this initialization section:
    #              GUI['FirstName'] = "Fred"  # Create a persistant variable.
    #         In the GUI creation code:
    #             st.number_input(label=:Enter first name", key="FirstName")
    #         Notice the key is the same as the persistent variable name.

    GUI['Dialog_State'] = 0    # Create session Dialog_State variable.
    GUI['Display_Count'] = 1   # A debugging Display_Count of sessions.

    # Persistant variables for the users input in the GUI
    GUI['MsgText'] = G.Msg01           # A text box for instructions & errors.
    GUI['RowsToGenerate'] = 100        # An integer variable.
    GUI['AFloatNumber'] = 123.678               # A float variable.

    # Persistant variables for checkboxes.
    GUI['ShowLine3'] = False
    GUI['ShowInput'] = True
    GUI['ShowData'] = True

    Paths_Get()  # Get the current file names, paths, versions etc.

    # Set up some basic properties of the GUI.
      #  - The set_page_config command can only be used once per run.
      #  - New line marker \n must be preceeded by at least two blanks to work.
    st.set_page_config  (
        page_title="Web Page Header. Version: " +  G.ThisModule_Version,
        page_icon=None,
        layout="centered", # or "wide".
           # 'wide' gives a bigger display. 'centered' gives a smaller display
           #  Remember that plots and tables etc on the streamlit webpage 
           #  can be "blownup" by the user clicking an "expand" icon
           # so don't worry if the normal view is too small.
        initial_sidebar_state="auto",
        menu_items={ # These appear as the webpage "about" menu items.
                   'Get Help': 'https://www.extremelycoolapp.com/help',
                   'Report a bug': 'https://www.extremelycoolapp.com/bug',
                   'About': 'Produced by  Spring 2021.  \n ' +
                       'Author: Fred Bloggs    \n' +
                       'Program Purpose:  To test streamlit' +
                        G.ThisModule_FileName +'  \n' +
                       "Version: " + G.ThisModule_Version 
                   }
                        )

    return()  # End of function: Perform_Program_Initialization
 
def Perform_EveryRun_Initialization():
    # Initalize variables for every run.
    #   Remember nothing is preserved across sessions, except variables in  
    #   the GUI streamlit "session_state" and its static/persistant variables.
    #  
    #   So on the first run we perform the one time program initialization.
    #   On subsequent runs we perform the "every run" intialization.
    #    So here we initialize anything not preserved across display/response.
    # 
    # Alternatives to repeating initialization here are: :
    # (1) Save static/persistant variables in the streamlit "session_state".
    # (2) Make the initialization "static" using steamlit st.cache.
    #      - Usefull if the initialization is very time consuming.
    # However having an "Every Time" initialization function is good practice
    # and less vulnerable to the subtle misbehaviors of the alternatives.
        
    Paths_Get()  # Get the current file names, paths, versions etc.
    return()
    
def Validate_And_Internalize_User_Input():
    # - This function validates the users input.
    # - This function also internalizes the users input.
    #     -Internalization isolates the data processing from the GUI.
    #     -Internalization is achieved by transfering the input values
    #      from the streamlit persistant session_state dictionary to 
    #      regular python variables in our global variable class.
    #    - We are using streamlit for our GUI but that may be replaced.
    #      Also streamlit has some nasty bugs we don't want complicating
    #      the data processing code.
    #
    # - The GUI performs validation for data type and values ranges.
    #      - Eg: The GUI won't allow a number input that is not numeric.
    #      - So most of the following validations are duplicative.
    #        But I have left them in as belt and suspenders.
    
    Msg_Set("")    
     
    # Validate and internalize population.
    G.RowsToGenerate, InputOK = Validate_Integer(GUI['RowsToGenerate'])
    if InputOK == False:
        Msg_Set("Error 1006: Rows to Generate must be an integer.") 
        return(False) 
    if (G.RowsToGenerate < 50):
        Msg_Set("Error 1008: Rows To Generate  must be [50,150] but not 99.")  
        return (False)
    if GUI['RowsToGenerate'] == 99:
       Msg_Set("Rows to Generate is exactly 99 which is not ok.")
       return(False)
    
    G.AFloatNumber, InputOK= Validate_Float(GUI['AFloatNumber'])
    if G.AFloatNumber == 9:
       Msg_Set("AFloatNumber is exactly 9 which is not ok.")
       return(False)
    
    # Internalize checkbox options.
    G.ShowLine3 = GUI['ShowLine3']  
    G.ShowInput = GUI['ShowInput']  
    G.ShowData = GUI['ShowData'] 
    
    # If we fall through here the users input is all valid.
    Msg_Set(G.Msg01)    # The "Please enter test specs" message.
    return(True)  # End of function: Validate_And_Internalize_User_Input

def Process_Users_Data():
    # Process the users input and create the data to be plotted/output.
    G.x = list(range(0, G.RowsToGenerate))
    G.y1 = G.x
    G.y2 = [item ** 1.2 for item in G.x]
    G.y3 = [item * -1 for item in G.x]

    # Create an example Pandas dataframe to show how easily streamlit 
    # shows it on the webpage. The values are meaningless.
    
    i = -1
    for  xvalue in (G.x):
       i = i + 1
       newrow = {'x' : xvalue,
                 'y1':   G.y1[i],
                 'y2':   G.y2[i],
                 'y3':   G.y3[i],
                 'random1': random.random(),
                 'sum with a long name': G.y1[i] + G.y2[i],
                 'sum with a longer name': G.y1[i] + G.y2[i] + + G.y3[i],
                 'random2': random.randint(1,100) 
               }
       G.DataTable = G.DataTable.append(newrow, ignore_index=True)
    # End for   
    return()  # End of function: Generate_Data_To_Be_Plotted
   
def Plot_Build():
    #  Possible Bug when deploying matplotlib streamlit apps
    # https://docs.streamlit.io/streamlit-cloud/troubleshooting#limitations-and-known-issues
    #     from matplotlib.backends.backend_agg import RendererAgg
    # https://docs.streamlit.io/library/api-reference/charts/st.pyplot
    # _lock = RendererAgg.lock
    # with _lock:
    #   fig.title('This is a figure)')
    #   fig.plot([1,20,3,40])
    #   st.pyplot(fig)

    

    # Create a Matplotlib figure.
    G.Fig1 = mpl.figure.Figure()
    
    # Create a plot object within the main figure with multiple lines.
    G.Plot1 = G.Fig1.add_subplot(111)
    G.Plot1.clear()  # Clear any current plot in G.Plot1. Just to be sure.

    # Add two lines to the plot
    G.Plot1.plot(G.x, G.y1, label="Y = X", color="red")
    G.Plot1.plot(G.x, G.y2, label="Y = X**2", color="blue")

    # The following shows how the plot can be modified by users requests.
    if G.ShowLine3 == True:
        G.Plot1.plot(G.x, G.y3, label="Y = - X", color="green")
        
    # Prettyfy the plot.    
    G.Plot1.minorticks_on()
    G.Plot1.legend(loc="best", fontsize=14, prop={"weight": "bold"})
    G.Plot1.set_title("Matplotlib Plot Title.", fontsize=10, fontweight="bold")
    G.Plot1.grid(visible=True, which='major', axis="both")
    G.Plot1.set_xlabel("A sample x axis. x=[0,100]")
    G.Plot1.set_ylabel("Y Values Value")

    # Show the plot on the streamlit webpage.
    st.subheader(" This Is The GUI 'Output Display Panel' On The Right")
    st.pyplot(G.Fig1)  # st.write(G.Fig1) also Displays a Matplotlib figure.
    st.caption("You can enlarge the plot using the 'View fullscreen' "
                  "icon. The icon is above and to the right of the plot.")
    st.caption("You can save the plot to your computer. Right click on "
                  "the plot, then use 'save image' or 'copy image'.")
    # Show how checkbox or other user requests can be used to
    # conditionally show data or text or any output after the plot appears.
    if G.ShowInput == True:
        st.subheader("The Values You Entered Are Listed Below.")
        st.write(Title_Build())
    else:
        st.subheader("The Values You Entered Are Not Displayed.")
        
   # Show the Pandas dataframe if user requested it. 
    if G.ShowData == True:
       st.subheader("The Pandas Data Table You Requested Follows:")
       st.dataframe(data=G.DataTable, width=None, height=None)
       st.caption("The data is just filler to demonstrate the Pandas' " 
                  "dataframes.") 
       st.caption("The dataframe display will automatically offer vertical "
                  "and horizontal scroll bars if required.")
       st.caption("You can expand the datatable using the 'View fullscreen' "
                  "icon. The icon is above and to the right of the table.")       

       
       # Add a "download" dataframe button.
       #   - The dataframe is converted to a csv file.
       #   - The csv file is downloaded to the browsers default download
       #     location.
       #   - There is no "save as" menu. The file name is hard coded.
       DataFrame_CSV = G.DataTable.to_csv().encode('utf-8')
       st.subheader("Download The Pandas DataFrame As A CSV File.")
       st.download_button(label="Download The DataFrame", 
                           data=DataFrame_CSV, 
                           file_name="DataFrame.csv", 
                           mime= "text/csv",
                           key='download-csv', 
                           help=None, 
                           on_click=None, 
                           args=None,
                           kwargs=None, 
                           disabled=False)
       st.caption("You can save the data frame to your computer using the "
                  "above button.") 
       st.caption("The file will be called 'DataFrame.csv'")
       st.caption("The file will be saved in your browser's default download "
                  "location on your computer.")
       
    # Demonstrate that we can control text appearance using HTML.
    md = StMarkdown("This Demonstrates That We Can Format Text Using HTML.",
                    fontsize=22,bold=True,color="blue")   
    st.write(md)
  
    # ?V How to user github to host media for display
    #   https://www.labnol.org/internet/free-file-hosting-github/29092/
    
    # Show a picture.
    # Get a picture from our pc. Not usable without a web backend.
    # FullPath = os.path.join(G.ThisModule_ProjectPath, "TigerMoth.jpg")
    # st.subheader("We Can Display And Save Any Image Or Audio/Visual Media")
    # MyImage = Image.open(FullPath)
    # st.image(MyImage, caption='Sunrise by the mountains')
    
    st.subheader(" We can display a picture from a web address (Github)")
    st.image("https://raw.githubusercontent.com/ProfBrockway/OSExperiments/main/TigerMoth.jpg")
    
    
    # Show a video
    FullPath = os.path.join(G.ThisModule_ProjectPath, "TestVideo.mp4")
    video_file = open(FullPath, 'rb')
    video_bytes = video_file.read()
    st.subheader("We Can Display Any Movie, So The Page Is Self Documenting.")
    st.video(video_bytes)
    
    # Plot a chart using native streamlit plotting functions.  
    chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
                           
    st.subheader("Plot A Chart Using Native Streamlit Plotting Functions.")
    st.line_chart(chart_data)
    
    # Show a clickable weblink on our webpage GUI.
    myurl = "https://github.com/ProfBrockway/ScreeningTests"
    st.subheader("Link To This Apps Code.")
    st.markdown("     [Link To Source Code](%s)" % myurl)
    
    # Show a PDF
    # To display a pdf from online resource we have to download it as
    # file then read it back in. We use the python "tempfile" object
    # so that the user doesn't get any junk file on the host computer.
    # Tempfile works on all operating system and doesn't need a
    # path supplied. It uses the default temp file facility of the opeerating
    # systems.
    st.subheader("Here Is The Program Documentation As A PDF.")
    st.caption("Be sure to use the PDF toolbar and index to navigate around "
               "the document.")

    # Set the URL of the PDF. (Stored in the cloud somewhere).
    PDF_URL = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    # Retrieve the PDF object from its web page.
    PDF_Object = urllib.request.urlopen(PDF_URL)    
    # Store the PDF in a temp file so we can read it into 
    TempPDFFile = tempfile.TemporaryFile()
    TempPDFFile.write(PDF_Object.read())
    TempPDFFile.seek(0) # Reposition at front of the temporary file.
    # Convert the PDF file to a base64 byte stream for HTML. 
    PDF_Base64 = base64.b64encode(TempPDFFile.read()).decode('utf-8')
    TempPDFFile.close()
        # Parse To HTML Embed Tag
    PDF_HTML = f"""<embed src='data:application/pdf;base64,{PDF_Base64}' 
                      width='1000' height='1000' type='application/pdf'>"""
    # Render with Streamlit Markdown
    st.markdown(PDF_HTML, unsafe_allow_html=True)
    
 
    
    
    # Show debugging information.
    if G.Debug:
        st.subheader("Debugging Information Follows.")
        st.caption(" The streamlit st.session_state persistant/static "
                   "variables follow.") 
        st.write(GUI)    #  Show all streamlit persistent variables.
        
        # st.write(G)  # ?v fix so this works For debugging. Show global variables.


    return  # End of function: Plot_Build

def GUI_Build_And_Show():        # Build the GUI.
    # - Our GUI is a streamlit web page with widgets in a vertical toolbar 
    #   on the left and a plot and display area on the right.
    #
    # - !!!!! DON"T ADD A "value=" parameter to any input widget. !!!!!!
    #      The "val=" causes error messages about duplicate initialization.
    #
    #  - Widget values are stored in "linked" streamlit persistent variables.
    #     The value input/output to/from each widget is stored in/retrieved 
    #     from a streamlit "linked" persistant variable linked to the 
    #     widget's by the widgets "key=" parameter. See elsewhere in this
    #     program for an explanation of "linked" static variables.
   
    # - We now make the sidebar a single form with a single submit button.
    #    With st.form and its form_submit_button, this app only reruns
    #    when you hit the form submit button, NOT at each widget interaction.
    #    https://blog.streamlit.io/introducing-submit-button-and-forms/
    Form1 = st.sidebar.form(key="Form1", clear_on_submit=False)

    with Form1:
        StMarkdown("THIS IS THE TOOLBAR",
                    color="green",bold=True,italic=True,fontsize=16)
 
        # Create a textbox for displaying instructions and error messages.
        st.text_area(
            key="MsgText",   # Value will be placed in GUI['MsgText'].
            label="",
            height=None,
            max_chars=None,
            help=None,
            on_change=None)

        # Create input boxes in the toolbar for our user specifed variables.

        #  Have the user input an integer from a widget.
        st.number_input(
            key="RowsToGenerate", # Value will linked to GUI['RowsToGenerate'].
            label="Table Rows To Generate",
            min_value=1,       # Be sure all values for this variable are
            max_value=1000,    # specified as integers.
            step=None,         # else streamlit throws an error. 
            format="%i",       # Make this variable an integer.
            help="Enter the RowsToGenerate.\nValue [50,150] but not 99",
            on_change=None,
            args=None,
            kwargs=None,
            disabled=False)

        #  Have the user input a float number from a widget.
        st.number_input(
            key="AFloatNumber",  # Value will be placed in GUI['AFloatNumber'].
            label="A float number",
            min_value=0.00,         # Always add a number after the point
            max_value=80000000.0,   # since the variable is a float. 
            step=100.0,            # else streamlit throws an error. 
            format="%f",            # Make this variable a float.
            help="Enter any number.\nValue 99 NOT permitted.",
            on_change=None)

        # Add checkboxes for selecting the lines to be shown on plot.
        st.checkbox(key="ShowLine3", label="Show the Line_3 in plot.")
        st.checkbox(key="ShowInput", label="Show The Variables I Input.")
        st.checkbox(key="ShowData", label="Show The Pandas Data Frame.")
        
        # Add a form submit button.
        #   Every "form" block must have exactly one form_submit_button
        st.form_submit_button(
            label='Plot Now',
            on_click=PlotNowButton_Click_Event,
            help="Click this button to draw your plot.",
            args=(),
            kwargs=())
    # End of 'with form'.
    

    return()  # End of function: GUI_Build_And_Show

def PlotNowButton_Click_Event():
    # Not used.
    # This function is Included to demonstrate that streamlit widgets have a
    # typical "callback" event option.
    return()  # End of function: PlotNowButton_Click_Event

def ConsoleClear():  # Clear all output in console.
    try:     # This works regardless of Operating System prevailing.
        from IPython import get_ipython
        get_ipython().magic("clear")
        get_ipython().magic("reset -f")
    except:
        pass
    return()  # End of function: Console_Clear

def Validate_Float(TextString):
    try:
        tempvar = float(TextString)
    except:
        return (0,False)
    else:
        return(tempvar,True)

def Validate_Integer(TextString):
    try:
        tempvar = int(TextString)
    except:
        return (0,False)
    else:
        return(tempvar,True)

def Msg_Set(TextString):
    GUI['MsgText'] = TextString
    return()

def Paths_Get():
    # Get the current paths and file names of this app.
    #   https://docs.python.org/3/library/os.path.html
    G.ThisModule_FullPath = os.path.abspath(__file__)
    G.ThisModule_FileName = os.path.basename(G.ThisModule_FullPath)
    G.ThisModule_ProjectPath = os.path.dirname(G.ThisModule_FullPath)
    return()  # End of function Paths_Get

def Title_Build(TitleLength = "short"):
    G.Title_1 = str(
                   "You entered the following values:  \n" +
                   "Rows To Generate = {:d}  \n".format(G.RowsToGenerate)  +
                   "AFloatNumber = {:.5f}".format(G.AFloatNumber) + "."
                   )
    return(G.Title_1)   #  End of function: Title_Build

def StMarkdown(TextToBeFormated="", color="black",
                                     fontsize=14,
                                     bold=False,
                                     italic=False,
                                     fontname="Courier"):
    # Set a particular font for display as html markdown text.
    weight = ""    
    weightend = ""
    if bold:
        weight = "<strong>"    
        weightend = "</strong>" 
    if italic:
        weight = "<em>"    
        weightend = "</em>"  
    if bold and italic:
        weight = "<em><strong>"    
        weightend = "</em></strong>"
        
    fs = str(fontsize).strip() + "px"
    md = " ".join(
                  ["<p",
                      "style='",
                              "font-family:", fontname, ";",
                              "color:", color, ";",
                              "font-size: ",  fs, ";",
                           "'"
                  ">",
                        weight + TextToBeFormated + weightend ,
                  "</p>"]
               )
    if G.Debug: print(md) # ?V
    st.markdown(md, unsafe_allow_html=True)
    return(md)

MainLine()   # Start this program.
