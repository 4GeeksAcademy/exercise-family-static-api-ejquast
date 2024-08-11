"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

initial_data = [{
    "first_name" : "John",
    "last_name" : "Jackson",
    "age" : "33",
    "lucky_numbers" : [7, 13, 22]
},{
    "first_name" : "Jane",
    "last_name" : "Jackson",
    "age" : "35",
    "lucky_numbers" : [10, 14, 3]
},{
    "first_name" : "Jimmy",
    "last_name" : "Jackson",
    "age" : "5",
    "lucky_numbers" : [1]
}]

for members_data in initial_data:
    jackson_family.add_member(members_data)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

def get_all_members(self):
    return self._members

@app.route('/member/<int:id>', methods=['GET'])
def find_member(id):
    member = jackson_family.get_member(id)
    return jsonify(member), 200

def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

@app.route('/member', methods=['POST'])
def add_member():
    ## You have to implement this method
    ## Append the member to the list of _members
    member_request_body = request.get_json(force=True)
    print("Incoming request with the following body", member_request_body)
    member_request_body = jackson_family.add_member(member_request_body)
    return jsonify(member_request_body), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    ## You have to implement this method
    ## Loop the list and delete the member with the given id
    member = jackson_family.get_member(id)
 
    if member:
        jackson_family.delete_member(id)
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
