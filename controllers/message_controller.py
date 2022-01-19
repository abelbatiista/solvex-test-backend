from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.message_model import Message

app = Flask(__name__)

def insert(message: Message):
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO message(from_id, to_id, message, date) VALUES (?, ?, ?, ?)'
        cursor.execute(query, [message.frm, message.to, message.message, message.date])
        database.commit()
    except(Exception):
        pass