"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Trackr(Controller):
    def __init__(self, action):
        super(Trackr, self).__init__(action)
        self.load_model('User')
   

    def index(self):
        return self.load_view('index.html')


    def register(self):
        user = {
            "name": request.form["name"],
            "pwd": request.form["password"],
            "pwd_confirm": request.form["confirm_password"],
        }

        result = self.models["User"].create_user(user)

        return jsonify(rst = result)


    def login(self):
        info = {
            "name": request.form["name"],
            "pwd": request.form["password"]
        }

        result = self.models["User"].login_user(info)

        return jsonify(rst = result)

    def createRecord(self): 
    	info = {
    		"name": request.form["name"],
    		"title": request.form["title"],
            "memo": request.form["memo"],
            "latitude": request.form["latitude"],
            "longitude": request.form["longitude"],
    	}

    	result = self.models["User"].create_record(info)

    	return jsonify(rst = result)

    def getAllRecords(self):
    	name = request.form["name"]
    	result = self.models["User"].get_all_records_by_user_name(name)
    	return jsonify(rst = result)


    def deleteRecord(self):
    	id = request.form["id"]
    	result = self.models["User"].delete_record_by_id(id)
    	return jsonify(rst = result)