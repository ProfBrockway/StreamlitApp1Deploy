
# https://docs.streamlit.io/knowledge-base/tutorials/databases/public-gsheet
# https://share.streamlit.io/streamlit/example-app-bug-report/main
import streamlit as st
from streamlit import session_state as S

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
# !!!!!!!!!! Make plotly plot appear in spyder environment !!!!!!!!!!
import plotly.io as pio
pio.renderers.default= "browser" # "browser" will be interactive. "svg" will not


Glink= "https://docs.google.com/spreadsheets/d/1g7vE0sf6nDpWM-ga3rIqWfLy1-ra7lxH4jPqdcWDBNs/edit?usp=sharing"

