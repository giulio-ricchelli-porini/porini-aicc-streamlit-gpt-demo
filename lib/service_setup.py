import openai
import pyodbc

from configs import AZURE_OPENAI_SERVICE, OPENAI_API_KEY, SQL_SERVER_NAME, SQL_SB_NAME, SQL_USERNAME, SQL_PASSWORD


def openai_setup():
    openai.api_type = "azure"
    openai.api_base = f"https://{AZURE_OPENAI_SERVICE}.openai.azure.com"
    openai.api_version = "2022-12-01"
    openai.api_key = OPENAI_API_KEY


def setup_sql_connection():
    connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={SQL_SERVER_NAME};Database={SQL_SB_NAME};Uid={SQL_USERNAME};Pwd={SQL_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    connection = pyodbc.connect(connection_string)
    connection.cursor()
