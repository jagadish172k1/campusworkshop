"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaadtu7avj5o48nft4g-a.oregon-postgres.render.com",
        database="todo_6ulr",
        user="todo_6ulr_user",
        password="u251on28wkm5wKWloHo9jzTCvyIXBne3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
