import pandas as pd

url = "https://drive.google.com/file/d/1aE_7AUXf824C6G6JUdypORJwoi5S8Qze/view?usp=sharing"
url = "https://raw.githubusercontent.com/ProfBrockway/StreamlitApp1Deploy/main/TestCSVFile.csv"
df = pd.read_csv(url)
print(df.head())