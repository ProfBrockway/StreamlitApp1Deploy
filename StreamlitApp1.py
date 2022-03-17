
r"""
EXAMPLE OF A MODULE "DOCSTRING"
   To run this app in a web browser undeployed on the development computer
   run the following command in the Anaconda console.
streamlit run "G:\My Drive\UConn\1-Subjects\Python\STAT476\CODE\StreamlitApp1Deploy\StreamlitApp1.py"
   
# This code is a template for creating a python app to run in a streamlit
# webpage.
# The webpage has a familiar "toolbar on left / plot and output on right"
# layout.

"""


import streamlit as st
from streamlit import session_state as S
   # Writing S.VarName'] is easier than  st.session_state['VarName'] 
import matplotlib as mpl  
import os
import pandas as pd
import numpy as np
import random
import openpyxl # Flagged as unused but required for excel behind the scenes.

# Plotly imports. Some may be flagged as unused, but import them anyway.
import scipy  # Used by plotly figure factory behind the scenes.
import plotly
import plotly.express as px 
import plotly.figure_factory as ff
import plotly.graph_objects as go


class Global_Variables():  # A class for creating all python global variables.
    
    ##########################################################################
    # +++ RESOURCES AND OTHER LINKS OR VARIABLES THAT MIGHT CHANGE.
    #   - The values for these variables are all initialized here.
    
    Debug = False
    
    #  DETAILS ABOUT THIS MODULE
    # RESOURCE LINKS Etc  Pictures/Videos/Files etc stored online.
    #   Where possible we base our resources in this apps repostitory
    #   at github. If github basing is not possible or inadequate
    #   we have to use another cloud storage site, eg Google drive.Youtube etc.
    
    # +++ DETAILS ABOUT THIS MODULE
    ThisModule_Project = "Demonstrate and Explore Streamlit and Python."
    ThisModule_Version = "7_00     2022 March 3, 10.29 am EST."  
    ThisModule_About = "This module has a done of demo code.. "  
    ThisModule_Author = "TB, UConn Math Dept."
    ThisModule_Purpose = ("My first Streamlit app.")
    ThisModule_Contact = "Contacts not supplied."
    ThisModule_Docstring = (__doc__)
    ThisModule_FullPath  = os.path.abspath(__file__)
    ThisModule_FileName = os.path.basename(ThisModule_FullPath)
    ThisModule_ProjectPath = os.path.dirname(ThisModule_FullPath)
    ThisModule_Docstring = (__doc__)
    
    
        #https://github.com/ProfBrockway/StreamlitApp1Deploy/raw/main/Resource_ProgramDocumentation.pdf
    # Program Help/Documentation.    
    # The raw version will download the pdf automatically.
    Link01 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf?raw=true"
    # This will pop up the pdf if googles pdf reader page. But no index or working links.
    Link01 = r"https://docs.google.com/viewer?url=https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf?raw=true"
    # This will pop up the pdf if googles pdf reader page. But no index or working links.
    Link01 = r"https://smallpdf.com/pdf-reader?url=https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf?raw=true"
    # The non raw version will go to the file at github and show it in a simple pdf viewer without index.
    Link01 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_ProgramDocumentation.pdf"
    # Where to report a bug..
    Link04 = r"https://www.ibm.com/us-en?ar=1"   
    # A picture stored at this projects repository at github. 
    # NOTE: MUST HAVE THE '?raw=true' SUFFIX to extract the pic from github.
    Link06 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_TigerMoth.jpg?raw=true"
    # This apps code page at Github.
    Link08 = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/0bc950a80603401a54dfb1c6ebe15bc83a362d6e/StreamlitApp1.py"
    # A test pdf online somewhere.
    Link10 = r"https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" 
    # A RAW url to a demonstration CSV file stored at Github.
    Link11 = r"https://raw.githubusercontent.com/ProfBrockway/StreamlitApp1Deploy/main/Resource_TestCSVFile.csv"
    # A url of a video on Youtube.
    Link20 = r"https://youtu.be/nsHl48Wnudc"
    # A url of a video NOT on Youtube. Just a random website.
    Link24 = r"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4"
    # A url of a video on google drive.
    Link30 = r"https://drive.google.com/file/d/18xDRuX9lTpEuSsjtJjFHz4TNnxfKAWdI/view?usp=sharing"
	# Name of downloaded table
    Link40 = "ScreeningTestDataFrame.csv"
    # +++ END OF RESOURCES AND OTHER LINKS OR VARIABLES THAT MIGHT CHANGE.
    ###########################################################################

    # +++ USERS INPUTS (Copied from input widgets and internalized)
    RowsToGenerate = None
    AFloatNumber = None
    ShowLine3 = None
    ShowInput = None
    ShowData = None
    
    # +++ SUNDRY GLOBAL VARIABLES
    Fig1 = None
    Plot1 = None
    Title_1 = None
    Title_2 = None
    Msg01 = "Please fill out the input boxes and click the 'Plot Now' button."
    Msg_Current = None

    
    # +++ DATA TO BE PLOTTED
    x = []
    y1 = None
    y2 = None
    y3 = None  
    
    # +++ A PANDAS DATAFRAME
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
    # Remember this app is rerun by streamlit every time the GUI is displayed.
    # So we have to keep track of the conversation state and preserve
    # or recreate variables appropriately.
    
    # Note: Console output from this program - like print("Whatever") - will
    # appear in the streamlit console NOT the usual python console.
    #    If this is too inconvenient, you can write debbuging information etc,
    #    to the streamlit webpage.
    ConsoleClear()  # Clear the internal IPyhon console.
    
    # If this the initial session create "Static/Persistent" variables
    # and do the "first load only" program initialization.
    if 'Dialog_State' not in S:
        if G.Debug: print("Debug: State=0 Initial load. Display count=1")   
        Perform_First_Load_Only_Initialization()
        S.Dialog_State = 1  # Upgrade state so we don't come back here.

    else:  # We are responding to a session reply from the user.
        S.Display_Count += 1  # Count of sessions.
        if G.Debug: 
           print("Debug: State=1. Display count=", S.Display_Count)  
        
        # Initalize variables for every run.
        #   Remember nothing outside the Streamlit static/persistant dictionary
        #   is preserved across sessions. So we perform the one time
        #   program initialization once then perform the "every run"
        #   intialization.
        Perform_EveryRun_Initialization()
        
        # Validate and internalize users'input.
        InputOK = Validate_And_Internalize_User_Input()
        if InputOK == True:
            # Process the users input and generate the data for plotting.
            Process_Users_Data()
            # Plot the data
            Right_Panel_Build()

        else: # There is an error in the users input. 
           st.error(G.Msg_Current) # Show the error in the right panel.

    
    # Having processed all input, we now insert the output into our GUI,
    # display the GUI and then wait for next user input.
    GUI_Build_And_Show()
    return()  # End of function: MainLine.

def Perform_First_Load_Only_Initialization():
    
    # Initalize variables etc.
    Perform_EveryRun_Initialization()
     
    # ++++ Set up a typical "About/Help" menu for the webpage.
    #  - The set_page_config command can only be used once per run.
    #  - The set_page_config command be the first Streamlit command used.
    #  - New line marker \n must be preceeded by at least two blanks to work.
    st.set_page_config  (
     page_title = "Webage Header. ", 
     
     page_icon = ":confused:",
     
     layout="centered", # or "wide".
        # 'wide' gives a bigger display. 'centered' gives a smaller display
        #  Remember that plots and tables etc on the streamlit webpage 
        #  can be "blownup" by the user clicking an "expand" icon.
        #  So don't worry if the normal view is too small.
     
     initial_sidebar_state="auto",
     
     # \r requires two preceeding spaces to work.
     menu_items={ # These appear as the webpage "about" menu items.
     'Get Help  ':  G.Link01,
     'Report a bug  ': G.Link04,
     'About': '  \rProgram: ' +  G.ThisModule_FileName 
            + '  \rProject:  ' + G.ThisModule_Project
            + '  \rProgram Purpose:  ' + G.ThisModule_Purpose 
            + '  \rAuthor:  ' +  G.ThisModule_Author   
            + '  \rContacts:  ' +  G.ThisModule_Contact
            +  '  \rVersion:  ' + G.ThisModule_Version               
               }
                      )

    
    # +++ CREATE PERSISTENT/STATIC VARIABLES.
    # https://docs.streamlit.io/library/api-reference/session-state
    # During the first load session, we create our "Persistent" variables.
    #  Persistent variables:
    #   - Are stored and created by streamlit in the streamlit
    #     'session state dictionary'
    #   - Are static (preserved) between sessions.
    #   - Are effectively global.
    #   - Have a python dictionary like syntax.
    #   - Are created using the streamlit "session_state" method.
    #      - Eg:  st.session_state['Display_Count'] = 0
    #      - In our case the st.session_State is abbreviated to Static.
    #          - from streamlit import session_state as Static
    #          - Eg: S.Input_SSN'] = 0
    #   - Can be "linked" to a streamlit widget via the widget key= parameter.
    #      - Using the key= parameter on any widget automatically
    #        creates a static variable in the 'session state dictionary'.
    #        But I prefer to declare them explicity as well.
    #      - Any change in the Static linked widget will automatically update 
    #      - the linked persistant variable.
    #      - Any change in linked persistant variable will automatically 
    #        update the linked widgets value in the Static dictionary.
    #      - The python type of linked variables are specifed by the
    #        linked widget's  "format=" parameter.
    #
    #      - Eg of a Linked persistent variable.
    #         In this initialization section:
    #              S.FirstName'] = "Fred"  # Create a persistant variable.
    #         In the Static creation code:
    #             st.number_input(label=:Enter first name", key="FirstName")
    #         Notice the key is the same as the persistent variable name.

    S.Dialog_State = 0    # Create session Dialog_State variable.
    S.Display_Count = 1   # A debugging Display_Count of sessions.

    # Persistant variables for the users input in the GUI
    S.MsgText = G.Msg01       # A text box for instructions & errors.
    S.RowsToGenerate = 100    # An integer variable.
    S.AFloatNumber = 123.678  # A float variable.

    # Persistant variables for checkboxes.
    S.ShowLine3 = False
    S.ShowInput = True
    S.ShowData = True
    
    S.UploadedFile = None
     
    return()  # End of function: Perform_First_Load_Only_Initialization
 
def Perform_EveryRun_Initialization():
    # Initalize variables for every run.
    #   Remember nothing is preserved across sessions, except variables in  
    #   the Static streamlit "session_state" dictionary in its
    #   static/persistant variables.
    #  
    #   On the first run we perform the one time program initialization.
    #   On subsequent runs we perform the "every run" intialization to 
    #   initialize or reinitialize anything not preserved across 
    #   the display/response dialog.
    # 
    # Alternatives to repeating initialization here are: 
    # (1) Save static/persistant variables in the streamlit "session_state".
    # (2) Make the initialization "static" using streamlit st.cache.
    #      - Use st.cache if the initialization is very time consuming.
    # (3) Initialize in our Global_Variables class (above)
    #     The Global_Variables class is run everytime the app is run.
    #     So it initializes every time streamlit reruns this app.
    #
    # However having an "Every Time" initialization function is good practice.
    # It may be neccessary to make the logic work.
    # Also its less vulnerable to the subtle misbehaviors of alternatives
    # (1) and (2).
 
    # No code needed here right now. All initialization done in 
    # class Global_Variables.
 
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
    # - The Streamlit input widgets perform validation for data type 
	#   and values ranges.
    #      - Eg: A widget can be set up to disallow a number input 
	#        that is not numeric.
    #      - So most of the following validations are duplicative.
    #        But I have left them in as belt and suspenders.
    
    Msg_Set("")    
     
    # Validate and internalize population.
    G.RowsToGenerate, InputOK = Validate_Integer(S.RowsToGenerate)
    if InputOK == False:
        Msg_Set("Error 1006:\n'Rows to Generate' must be an integer.") 
        return(False) 
    if (G.RowsToGenerate < 50):
        Msg_Set("Error 1008:\n'Rows To Generate' must be [50,150] but not 99.")  
        return (False)
    if S.RowsToGenerate == 99:
       Msg_Set("Error 1010:\n'Rows to Generate' is 99 which is not ok.")
       return(False)
    G.AFloatNumber, InputOK= Validate_Float(S.AFloatNumber)
    if G.AFloatNumber == 9:
       Msg_Set("Error 1012:\n'A FloatNumber' is exactly 9 which is not ok.")
       return(False)
    
    # Internalize checkbox options.
    G.ShowLine3 = S.ShowLine3 
    G.ShowInput = S.ShowInput 
    G.ShowData = S.ShowData 
    
    # If we fall through here the users input is all valid.
    Msg_Set(G.Msg01)    # The "Please enter test specs" message.
    return(True)  # End of function: Validate_And_Internalize_User_Input

def Process_Users_Data():
    # Process the users input and create the data to be plotted/output.
    G.x = list(range(0, G.RowsToGenerate))
    G.y1 = G.x
    G.y2 = [item ** 1.2 for item in G.x]
    G.y3 = [item * -1 for item in G.x]

    # Create an example Pandas dataframe for plotting etc
    # The values are meaningless.
    
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
    
    # Temporary code only.
    # csvfullpath = os.path.join(G.ThisModule_ProjectPath,"TestCSVFile.csv")   
    # G.DataTable.to_csv(csvfullpath)   
    
    # End for   
    return()  # End of function: Generate_Data_To_Be_Plotted
   
def Right_Panel_Build():  # Build the main panel on the right. Plot, pics etc.
      
    # +++ CREATE A MATPLOTLIB FIGURE. 
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
    G.Plot1.set_title(Title_Build("long"),fontsize=10,fontweight="bold" )
    G.Plot1.grid(visible=True, which='major', axis="both")
    G.Plot1.set_xlabel("A sample x axis. x=[0,100]")
    G.Plot1.set_ylabel("Y Values Value")

    # Put header(s) before the plot.
    st.subheader(" This Is The Static 'Output Display Panel' On The Right")
    if G.ShowInput == True:
        temptext = f"""
             ### The Values You Entered Are Listed Below.  \r
            {Title_Build()}  \r
            \r
            More Stuff:
            1. Blah blah.
            1. More Blah Blah.    
            1. HOW TO ENLARGE OR SAVE THE PLOT :
                1. You can enlarge the plot using the View fullscreen icon. The icon is above and to the right of the plot.
                2. You can save the plot to your computer. Right click on the plot, then use 'save image' or 'copy image'.
            1. Great stuff ! 
            """
        st.info(temptext )
        
        
    else:
        st.subheader("The Values You Entered Are Not Displayed.")
 
    # Show the plot on the streamlit webpage.
    st.pyplot(G.Fig1)  # st.write(G.Fig1) also Displays a Matplotlib figure.
     
    # +++ PROVE EXTERIOR HELPER FUNCTIONS WORK IN STREAMLIT
    st.info("PROVE EXTERIOR HELPER FUNCTIONS WORK IN STREAMLIT")
    from HelperFunctions import Exterior_Helper_Function1
    from HelperFunctions import Exterior_Helper_Function2   
    st.text(Exterior_Helper_Function1())
    st.text(Exterior_Helper_Function2()) 
        
   # +++ SHOW A PANDAS DATAFRAME IF USER REQUESTED IT.
    if G.ShowData == True:
       st.markdown("#### The Pandas Data Table You Requested Follows:")
       st.dataframe(data=G.DataTable, width=None, height=None)
       st.write("The data shown is just filler to demonstrate a Pandas " 
                      "dataframe.") 
       st.write("The dataframe display will automatically offer vertical "
                    "and horizontal scroll bars if required.")
       st.write("You can expand the datatable using the 'View fullscreen' "
                    "icon. The icon is above and to the right of the table.")       

       
   #  +++ ADD A "DOWNLOAD" DATAFRAME BUTTON.
       # - The dataframe is converted to a csv file.
       # - That file is downloaded to the browsers download location.
       #  - There is no "save as" menu. The file name is hard coded.
       DataFrame_CSV = G.DataTable.to_csv().encode('utf-8')
       st.markdown("#### Download The Pandas DataFrame As A CSV File.")
       helpstr = f"""You can save the data frame to your computer using this button.  \r
                    The file will be called {G.Link40}.   \r
                     The file will be saved in your browser's default 'download' location on your computer.
	             """
       st.download_button(label="⚙️ Download The DataFrame",  
            data=DataFrame_CSV, 
            file_name=G.Link40, 
            mime= "text/csv",
            key="DownloadCSV_Button", 
            help=helpstr, 
            on_click=None, 
            args=None,
            kwargs=None, 
            disabled=False)

       
       
    #  +++ SHOW FONT CHANGES IN TEXT USING HTML.
    MDText = StMarkdown(
        "This Demonstrates That We Can Format Text Using HTML.",
         fontsize=22,bold=True,color="blue")   
    st.markdown(MDText, unsafe_allow_html=True) 
  

    
    # +++ DEMONSTRATE SHOWING A PICTURE FROM THE APPS GITHUB REPOSITORY.
    #   We must get our picture (and other resources) from a web address 
    #   because streamlit does NOT have a full backend on its server from
    #   which server disk we might otherwise get resources.
    #   The obvious online repository for resources like pictures is the
    #   github repository for the project. Streamlit drives itself from
    #   the github repository. However github cannot as yet support some 
    #   resources. For example a pdf displayed at github does not support 
    #   pdf features like indexing or links. 
    # Also the video storage is very  limited at github. S
    # So we will be using other online sites to store web
    #   accessable resources. (Eg Youtube)
    # - How to user github to host media for display
    #     https://www.labnol.org/internet/free-file-hosting-github/29092/
    st.markdown("#### DEMONSTRATE SHOWING A PICTURE FROM THE APPS GITHUB REPOSITORY.")
    st.image(G.Link06, 
        caption="We used a github url address to get this picture from " 
       "  github.   \n"  
        "  NOTE: THE URL MUST HAVE THE '?raw=true' SUFFIX to extract the pic"
        "from github.")
    st.write("You can enlarge the picture by clicking the pop up symbol "
             "that appears when you mouse near the top right of the image.")
     
    # # +++ DEMONSTRATE DOWNLOADING A PICTURE USING A DOWNLOAD BUTTON.
    # with open(G.Link06, "rb") as file:
    #  btn = st.download_button(
    #          label="Download image",
    #          data=file,
    #          file_name="Resource_TigerMoth.jpg",
    #          mime="image/png"
    #        )
    
    
    

    # +++ DEMONSTRATE SHOWING A VIDEO FROM YOUTUBE.
    #  Github basing of videos does not allow raw address of large files.
    #  Google basing of videos  does not work because it downloads too slowly.
    #  So until I can figure out how to base videos at github we use Youtube.
    st.markdown("#### DEMONSTRATE SHOWING A VIDEO FROM YOUTUBE.")
    FullURL = G.Link20
    st.video(FullURL)
    
    # +++ DEMONSTRATE SHOWING A VIDEO FROM AN ONLINE SOURCE OTHER THAN YOUTUBE.
    #  Github basing of videos does not allow raw address of large files.
    #  Google basing of videos  does not work because it downloads too slowly.    
    st.markdown("#### DEMONSTRATE SHOWING A VIDEO AN ONLINE SOURCE OTHER THAN YOUTUBE.")
    st.write("The following video is just on a website somewhere.")
    st.video(G.Link24)
 
    # # +++ DEMONSTRATE SHOWING A VIDEO FROM GOOGLE DRIVE.
    # #  Github does not allow raw address of large files.
    # #  Google basing of videos  does not work because it downloads too slowly.    
    # st.subheader("DEMONSTRATE SHOWING A VIDEO FROM GOOGLE DRIVE.")
    # st.write("")
    # st.video(G.Link30)
    

    # +++ DEMONSTRATE EASY SHOWING A PYTHON DICTIONARY ON A STREAMLIT WEBPAGE.
    people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}, 
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
    
    st.info("DEMONSTRATE SHOWING A PYTHON DICTIONARY ON A STREAMLIT WEBPAGE.")
    st.text("Pretty printing python dictionarys is easy using streamlit.  \n"
            "Even nested dictionaries.  \n"
            "We use the st.dataframe feature.")
    st.dataframe(people)
    
    #  +++ SHOW A PLOT USING PLOTLY WHICH HAS GREAT INTERACTIVE CONTROLS 
    st.info("DEMONSTRATE A 'PLOTLY' PLOT WITH GREAT INTERACTIVE CONTROLS.")
    st.write("""See my program 'screening test' for a much better example 
             of using plotly graphs which are MUCH better than 
             matplotlib in screenlit because the plotly plots are
             interactive.              """)
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
        
    
    #  +++ SHOW A CLICKABLE WEBLINK ON OUR WEBPAGE Static.
    #   There are several ways to do this.
    st.markdown("### LINK TO THIS APPS CODE. (DOWNLOADABLE). ")
    st.markdown(" [Link To Source Code](%s)" % G.Link08)
    # Also works: st.write("[Link To The Source Code](%s)" % G.Link08)


    #  +++ SHOW A PDF AT GITHUB USING POP UP NEW WEB PAGE
    ###########################################################################
    # +++ MAKE THIS APPS DOCUMENTATION AVAILABLE.
    #   We  base the pdf file in the github repository for the project.
    #   The github using the github link to the address displays
    #   the pdf file in the primitive github pdf view which does not
    #   have basic features, especially the pdf document index.
    #   I have not been able to fix this problem so for now, the pdf
    #   is displayed and the user advised to download it a use a 
    #   proper pdf viewer.
    st.info("🟢 THIS APP'S DOCUMENTATION.")
       
    col1, col2 = st.columns(2)
    with col1:
        st.write(" [ Link To This App's Documentation.]"  "(%s)" % G.Link01)
   
    with col2: 
        # Here we use a trick to display a pop up help message.
        # We use an st.button and load its help parameter with our popup.
        # This works fine when the user hovers the mouse over the button.   
        # But when the user clicks the button (as is reasonable) the
        # app is rerun. This doesn't produce any errors but is obviously
        # inefficient. We have to live with this until we find a better
        # method for pop up messages.
        tempstr = ("""You can read this app's documentation at the
        provided link using a primitive pdf reader.  \r
        But by downloading the documentation PDF and viewing it 
        on your computer you will be able to navigate the document using 
        an index, search, etc.  \r
        You can also see the program documentation by using
        the menu in the top right of this webpage '≡' (3 horizontal lines) then
        select 'GET HELP'. """) 
        st.button(label="Help", key="ButtonH1", help=tempstr )
   
    # DEMONSTRATE HOW TO USE AN ICON
    # https://share.streamlit.io/streamlit/emoji-shortcodes
    # Just copy and paste the icon from the list. 
    # Not all of the :whatever: codes work so best avoid that method.
    st.write("✔️  ❌  How to include icons in any text",help="help text here" )    
    
    
    # +++ SHOW DEBUGGING INFORMATION.
    if G.Debug:
      st.subheader("Debugging Information Follows.")
      st.write(" The streamlit st.session_state persistant/static "
                    "variables follow.") 
      st.write(S)    #  Show all streamlit persistent variables.
                # st.write(G)  # ?v fix so this works For debugging. Show global variables.
    
    # +++ DEMONSTRATE AN EXPANDER
    st.subheader("DEMONSTRATE AN EXPANDER.")
    with st.expander("An expanding section that shows debugging information"):
        st.write(""" Write or display anything here. """)
        st.write("You can call any Streamlit command.")
        st.subheader("Debugging Information Follows.")
        st.write(" The streamlit st.session_state persistant/static "
                      "variables follow.") 
        st.write(S)    #  Show all streamlit persistent variables.
        # st.write(G)  # ?v fix so this works For  Show global variables.
          
        
    # +++ DEMONSTRATE A CONTAINER, ALLOWS GROUPING OF ITEMS
    st.subheader("DEMONSTRATE A CONTAINER.")     
    with st.container():
        st.write("This is inside the container")
        st.write(""" Inserts an invisible container into your app that
                 can be used to hold multiple elements. This allows you to,
                 for example, insert multiple elements into your
                 app out of order.""")
    st.write("This is outside the container")
   
   
    # +++ DEMONSTRATE COLUMN LAYOUT.  
    st.subheader("DEMONSTRATE COLUMN LAYOUT. ") 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        
    # +++ DEMONSTRATE HOW THE ST.TEXT FEATURE FORMATS TEXT..
    Anumber = 678.4325 
    helpstr = f"""
    This shows how st.text shows fixed width preformatted text.\r
      A number. {Anumber}    \r
      This will appear on a new line.   \r
      The will be on another line."""
    st.text(helpstr)    
        
    # +++ DEMONSTRATE A STREAMLIT 'INFO' Box.      
    st.info("ℹ️  This is a Streamlit 'info' box.")   
        
    # +++ DEMONSTRATE A STREAMLIT 'WARNING' Box.     
    st.warning("⚠️ This is a Streamlit 'warning' box.")   
     
    # +++ DEMONSTRATE A STREAMLIT 'ERROR' Box.      
    st.error("❌ This is a Streamlit 'error' box.")   
       
    # +++ DEMONSTRATE A STREAMLIT 'SUCCESS' Box.     
    st.success("✅	This is a Streamlit 'success' box.")   
        
    # +++ DEMONSTRATE A STREAMLIT 'EXCEPTION' Box.    
    st.exception("This is a Streamlit 'exception' box.")   
    
    
    # +++ DEMONSTRATE EMOJIS  
    # The emojis supported by streamlit
    #    https://share.streamlit.io/streamlit/emoji-shortcodes
    # Just include the emojis markdown code in any output.
    st.info("The demonstates how easy it is to include emojis in any text:  \n"
            "  \n'white_check_mark ' :white_check_mark: "
            "  \n'pushpin ' :pushpin: " )
              
    # DEMONSTRATE READING A CSV FILE FROM THE PROJECT'S GITHUB REPOSITORY.
    temptext = """
    ### DEMONSTRATE READING A CSV FILE FROM THE PROJECT'S GITHUB REPOSITORY.  \n 
          THIS ALLOWS YOU TO HAVE A DATABASE AVAILABLE TO THE DEPLOYED
          APP WITHOUT THE NEED OF A WEB HOSTING BACKEND.  \n
        How To:
        1. Add the csv file to the project's github repository.
        1. Get the files github RAW url.    
        1. Code:
            1. url = 'the.url.of.the.RAW.file.a.tGithub'
            2. df = pd.read_csv(url)
        1. Your Done ! 
        """
    st.info(temptext)    
    df2 = pd.read_csv(G.Link11)
    st.dataframe(data=df2, width=None, height=None)
    
    # +++ DEMONSTRATE A STREAMLIT FILE UPLOAD BUTTON.
    # https://pythonwife.com/file-upload-download-with-streamlit/     
    st.info("DEMONSTRATE A STREAMLIT FILE UPLOAD BUTTON")
    UploadedFiles = st.file_uploader("Upload a file why not", 
                    key="UploadedFile",  #?V Add to static dictionary
                    type="", # Let the user upload any file type
                    help = "Help text appears here.",
                    accept_multiple_files=True,
                    on_change = None, # Callback event 
                    args =(), # optional tuple of args to pass to the callback.
                    kwargs = (), # A doctionary of kwargs to pass to  callback.
                    )
    
    if st.button("Process The Files"):
        # List details of the files uploaded.
        if UploadedFiles is not None:
           # The UploadedFile class is a subclass of BytesIO, and therefore it is
           # "file-like". This means you can pass them anywhere where a file
           # is expected 
           i = 0
           for Uploaded_File in UploadedFiles:
    		   # Create a dictionary of the file details, which prints pretty.
               file_details = {"File Index In List Of Files":i, 
                               "Filename":Uploaded_File.name,
                               "FileType":Uploaded_File.type,
                               "FileSize":Uploaded_File.size,
                               "InteralID":Uploaded_File.id}
               st.write(file_details)
               i = i + 1


    
    # +++ DEMONSTRATE USING AN EXCEL FILE (Upload then make it a pandas dataframe.") 
    # https://towardsdatascience.com/how-to-work-with-excel-files-in-pandas-c584abb67bfb
    st.info("DEMONSTRATE USING AN EXCEL FILE BASED ONLINE IN THE GITHUB REPOSTIORY")
    st.write("Be sure that that remote url of the excel file includes the 'raw' suffix ?raw=true")
    st.write("For pandas to input an excel file you must install a pandas slave program xlrd. pip install xlrd  ")
    xPath = r"https://github.com/ProfBrockway/StreamlitApp1Deploy/blob/main/Resource_TestExcelFile.xlsx?raw=true"
    df_sheet = pd.read_excel(xPath, sheet_name=0)
    st.write("EXCEL FILE FOLLOWS:\n",df_sheet)
    
    

    ###########################################################################
    # +++ SHOW THIS APPS DOCSTRING
    #  Github basing of videos does not allow raw address of large files.
    #  Google basing of videos  does not work because it downloads too slowly.
    #  So until I can figure out how to base videos at github we use Youtube.
    st.info("🟢  THIS APP's DOCUMENT STRING FOLLOWS.")   
    st.text(G.ThisModule_Docstring)
    
    
    # # +++ DEMONSTRATE AN EMPTY CONTAINER. ALLOWS REMOVAL OF ITEMS
    # import time
    # st.subheader("DEMONSTRATE AN EMPTY CONTAINER.ALLOWS REMOVAL OF ITEMS.")     
    # with st.empty():
    #     for seconds in range(20):
    #         st.write(f"⏳ {seconds} seconds have passed")
    #         time.sleep(1)
    #     st.write("✔️ 1 minute over!")
       
        

    return  # End of function: Right_Panel_Build

def GUI_Build_And_Show():        # Build the GUI.
    # - Our GUI is a streamlit web page with widgets in a vertical toolbar 
    #   on the left and a plot and display area on the right.
    #
    # - !!!!! DON'T ADD A "value=" parameter to any input widget. !!!!!!
    #     The "val=" causes error messages about duplicate initialization.
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
        # Add a title to the toolbar on the left.
        MDText = StMarkdown("THIS IS THE TOOLBAR",
           color="green",bold=True,italic=True,fontsize=16,align="center")
        st.write(MDText, unsafe_allow_html=True)
        
		# Add a form submit button.
        # Every "form" must have exactly one form_submit_button.
        st.form_submit_button(
                    label='Plot Now',
                    on_click=PlotNowButton_Click_Event,
                    help="When you have entered the parameters  \r"
                    "for the calculations click  \r"
                    "this button to draw your plot.",
                    args=(),
                    kwargs=())
            
 
        st.warning("The demonstates how easy it is to include emojis in "
                " any text:  \n"
                "  \n'white_check_mark ' :white_check_mark: "
                "  \n'pushpin ' :pushpin: " )
        
        
        # Create a textbox for displaying instructions and error messages.
        st.text_area(
            key="MsgText",   # Value will be placed in S.MsgText'].
            label="INSTRUCTIONS",
            height=150,
            max_chars=None,
            help="Watch here for instructions and error messages",
            on_change=None)

        # Create input boxes in the toolbar for our user specifed variables.

        #  Have the user input an integer from a widget.
        st.number_input(
            key="RowsToGenerate", # Value  linked to S.RowsToGenerate'].
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
            key="AFloatNumber",  # Linked to placed in S.AFloatNumber'].
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
    FormattedText = TextString
    ErrStr = TextString[0:5].upper()  
    if ErrStr == "ERROR":
        FormattedText = f"❌ There is an error in your input.    \n{FormattedText}   \nPlease correct and try again."
    S.MsgText = FormattedText
    G.Msg_Current = FormattedText
    return()

def Title_Build(TitleLength = "short"):
    G.Title_1 = str(
                   "Rows To Generate = {:d}   \r".format(G.RowsToGenerate)  +
                   "AFloatNumber = {:.5f}".format(G.AFloatNumber) + "."
                   )
    return(G.Title_1)   #  End of function: Title_Build

def StMarkdown(TextToBeFormated="", color="black",
    fontsize=14,bold=False,italic=False,fontname="Courier",align="left" ):
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
                              "text-align: ",  align, ";",
                           "'"
                  ">",
                        weight + TextToBeFormated + weightend ,
                  "</p>"]
               )
    return(md)  # End of function: StMarkdown



MainLine()   # Start this program.


