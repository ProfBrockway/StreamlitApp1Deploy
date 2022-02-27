
# CODE TO CHANGE FONT IN ST.TEXT WIDGET. DOES NOT WORK
# THERE IS NO WAY SAFE OR OTHERWISE TO SET THE FONT OF ST.TEXT WIDGET.
# ONLY RAW TEXT SHOW ON THE WEBPAGE (NOT IN A WIDGET) CAN HAVE ITS FONT
# CHANGED.  BOTTOM LINE STICK TO USING SAFE BUILTIN MARKDOWN EVEN IF
# ITS NOT THE COLOR OR WHATEVER YOU WANT.
def Msg_Set(TextString):
    ErrStr  =  TextString[0:5].upper()  
    if ErrStr == "ERROR":
        FormattedText = StMarkdown(TextString,color="red")  
    else:
        FormattedText = StMarkdown(TextString,color="black")  
    GUI['MsgText'] = FormattedText
    return(FormattedText)

##################################################################
    # Compact the streamlit layouts a little. ?V
    padding = 0
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
            padding-right: {padding}rem;
            padding-left: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)

#####################################################################


# SHOW A PDF FILE STORED ON A WEB PAGE DISK.
#   - This only works if the pdf is already in a web page.
#   - This only works locally. Acessing even a temp file on a users
#     computer is not permitted.
# To display a pdf from online resource we have to download it as
# file then read it back in. We use the python "tempfile" object
# so that the user doesn't get any junk file on the host computer.
# Tempfile works on all operating system and doesn't need a
# path supplied. It uses the default temp file facility of the opeerating
# systems.
import urllib.request  # For getting a pdf file online.
import base64    # For showing PDFs.
import tempfile  # For manipulating and showing a PDF file in streamlit.
st.subheader("Here is a pdf. THIS ONLY WORKS LOCALLY.")
st.caption("Be sure to use the PDF toolbar and index to navigate around "
           "the document.")
# Set the URL of the PDF. (Stored in the cloud somewhere).
PDF_URL = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
PDF_URL = G.Link01
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
    

######################################################################
    
    # Show the PDF file embedded in our webpage.
    # only works if the pdf is already in a webpage
    # If you try to get a file from (say) google it doesnt' work.
    st.subheader("Here A PDF Embedded In this web page PDF.")
    st.markdown("<embed src='https://drive.google.com/viewerng/viewer?embedded=true&url="
       + "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf' "  
       + "width='400' height='400'>" , unsafe_allow_html=True) 





#  ++++++++++++++++++++++++++ OLD CODE ++++++++++++++++++++++++++++++++++++++++
     # The following is obsolete since i use online sources for pdfs.
     # To display a pdf from online resource we have to download it as
     # file then read it back in. We use the python "tempfile" object
     # so that the user doesn't get any junk file on the host computer.
     # Tempfile works on all operating system and doesn't need a
     # path supplied. It uses the default temp file facility of the opeerating
     # systems.

    # PDF imports
    # import urllib.request  # For getting a pdf file online.
    # import base64    # For showing PDFs.
    # import tempfile  # For manipulating and showing a PDF file in streamlit.
    # PDF_Object = urllib.request.urlopen(G.Link10)    
    # # Store the PDF in a temp file so we can read it into 
    # TempPDFFile = tempfile.TemporaryFile()
    # TempPDFFile.write(PDF_Object.read())
    # TempPDFFile.seek(0) # Reposition at front of the temporary file.
    # # Convert the PDF file to a base64 byte stream for HTML. 
    # PDF_Base64 = base64.b64encode(TempPDFFile.read()).decode('utf-8')
    # TempPDFFile.close()
    #     # Parse To HTML Embed Tag
    # PDF_HTML = f"""<embed src='data:application/pdf;base64,{PDF_Base64}' 
    #                   width='1000' height='1000' type='application/pdf'>"""
    
    # pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>
    
    # pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])

    

# Also you could use Google's pdf viewer in this way:
# st.markdown("""
#            <embed src="https://drive.google.com/viewerng/
#             viewer?embedded=true&url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="400" height="400">
#            """, unsafe_allow_html=True)
    
    
    
    # st.markdown("""
    #            <embed src="https://drive.google.com/viewerng/
    #             viewer?embedded=true&url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="400" height="400">
    #            """, unsafe_allow_html=True)

        # st.markdown("<embed src='" 
        #             + G.Link02 
        #             + "' width='400' height='400'> ", unsafe_allow_html=True)

        # st.markdown("""
        #             <embed src="https://drive.google.com/file/d/1ADswqmBPZaEzwrhzu_mTk5HY_qHv2Mhw/view?usp=sharing" width="400" height="400">
        #             """, unsafe_allow_html=True)

        # st.markdown("""
        #             <embed src="https://drive.google.com/viewerng/
        #             viewer?embedded=true&url=https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" width="400" height="400">
        #             """, unsafe_allow_html=True)
    
    # other ideas
    # https://stackoverflow.com/questions/38491722/reading-a-github-file-using-python-returns-html-tags
    # https://www.codegrepper.com/code-examples/python/python+get+github+file+content
    # https://github.com/streamlit/example-app-pdf-report
    
    
    
    #######################################################################
    # ?V  Possible Bug when deploying matplotlib streamlit apps
      # https://docs.streamlit.io/streamlit-cloud/troubleshooting#limitations-and-known-issues
      #     from matplotlib.backends.backend_agg import RendererAgg
      # https://docs.streamlit.io/library/api-reference/charts/st.pyplot
      # _lock = RendererAgg.lock
      # with _lock:
      #   fig.title('This is a figure)')
      #   fig.plot([1,20,3,40])
      #   st.pyplot(fig)
