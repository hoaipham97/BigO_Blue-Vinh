import pandas as pd
import xlrd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials
from oauth2client.client import GoogleCredentials, OAuth2Credentials
from oauth2client.client import flow_from_clientsecrets
from oauth2client import GOOGLE_TOKEN_URI
from google.oauth2 import service_account


token_uri = GOOGLE_TOKEN_URI

scope = [
    'https://www.googleapis.com/auth/spreadsheets.readonly'
    # 'https://www.googleapis.com/auth/drive',
    # 'https://www.googleapis.com/auth/drive.file'
]

gCreds = OAuth2Credentials( 
    access_token = None,
    token_expiry = None,
    user_agent = None,
    client_id = "764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com",
    client_secret="", 
    refresh_token="", 
    token_uri = GOOGLE_TOKEN_URI
).scopes.add('https://www.googleapis.com/auth/spreadsheets.readonly')

client = gspread.Client(auth=gCreds)
PATH_FILE = 'account.xlsx'
SHEET_NAME = 'Sheet1'
client.open(PATH_FILE)
def read_excel():
    excel_data_df = pd.read_excel(PATH_FILE, sheet_name=SHEET_NAME, engine='openpyxl')
    excel_data_df.columns =['account', 'project_id']
    excel_data_df.dropna(thresh=1)
    # print(excel_data_df)
    list_accounts = []
    for index, row in excel_data_df.iterrows():
        if(pd.isnull(row['account']) == False & pd.isnull(row['project_id'])==False):
            each_account = [row['account'],row['project_id']]
            list_accounts.append(each_account)
    return list_accounts

if __name__ == '__main__':
    list_accouts = read_excel()
    print(list_accouts)
