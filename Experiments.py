# streamlit run "G:\My Drive\UConn\1-Subjects\Python\STAT476\CODE\StreamlitApp1Deploy\Experiments.py"
import streamlit as st
from streamlit import session_state as Static
def mainline():
    ConsoleClear()
    test4()
    return() # End of function: mainline.

def test4():
    st.markdown("""
    <embed src="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="400" height="400">
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
    try:     # This works regardless of Operating System prevailing.
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