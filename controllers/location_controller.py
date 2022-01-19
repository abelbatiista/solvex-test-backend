from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.location_model import Location

def get(id: int):
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM location WHERE user = ?'
        cursor.execute(query, [id])
        data = cursor.fetchall()
        list = []
        for _data in data:
            dictionary = dict(id=_data[0], user=_data[1], label=_data[2], adress=_data[3], street=_data[4],
                              number=_data[5], sector=_data[6], city=_data[7], province=_data[8],
                              country=_data[9], code=_data[10])
            list.append(dictionary)
        response = dict(ok=True, message='Successfully', locations=list, total=len(list))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def insert():
    try:
        location_details = request.get_json()
        location = Location(location_details['user'], location_details['label'], location_details['adress'],
                        location_details['street'], location_details['number'], location_details['sector'],
                        location_details['city'], location_details['province'], location_details['country'],
                        location_details['code'])
        database = get_database()
        cursor = database.cursor()
        query = '''
            INSERT INTO location(user, label, adress, street, number, sector, city, province, country, code) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(query, [location.user, location.label, location.adress, location.street, location.number,
                               location.sector, location.city, location.province, location.country, location.code])
        database.commit()
        dictionary = dict(id=location.id, user=location.user, label=location.label, adress=location.adress, street=location.street,
                          number=location.number, sector=location.sector, city=location.city, province=location.province,
                          country=location.country, code=location.code)
        response = dict(ok=True, message='Successfully', location=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)