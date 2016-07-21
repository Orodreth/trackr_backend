from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, user):
        error = ""

        if len(user["name"]) < 1:
            error = "Name cannot be blank!"
        elif len(user["pwd"]) < 8:
            error = "Password should be at least 8 characters!"
        elif user["pwd"] != user["pwd_confirm"]:
            error = "Confirm password is not match with Password!"

        sql = "select * from users where name = :name"
        data = {
            "name": user["name"]
        }
        result = self.db.query_db(sql, data)
        if len(result) > 0:
            error = "This user name has already been used!"

        if len(error) != 0:
            return { "status": "Fail", "error": error }

        pwd = self.bcrypt.generate_password_hash(user["pwd"])
        sql = "insert into users(name, password, created_at, updated_at) " \
            "values(:name, :password, NOW(), NOW())"
        data = {
            "name": user["name"],
            "password": pwd
        }
        
        user_id = self.db.query_db(sql, data)

        return { "status": "Success" }


    def login_user(self, info):
        sql = "select * from users where name = :name"
        data = {
            "name": info["name"]
        }
        result = self.db.query_db(sql, data)

        error = ""

        if result == None or len(result) == 0:
            error = "Invalid user name!"
            return { "status": "Fail", "error": error }

        if self.bcrypt.check_password_hash(result[0]["password"], info["pwd"]):
            return { "status": "Success" }

        error = "Invalid password!"

        return { "status": "Fail", "error": error }


    def create_record(self, info):
        sql = "select id from users where name = :name"
        data = {
            "name": info["name"]
        }
        id = self.db.get_one(sql, data)["id"]

        sql = "insert into records(title, memo, latitude, longitude, created_at, updated_at, user_id) " \
            "values(:title, :memo, :latitude, :longitude, NOW(), NOW(), :id)"
        data = {
            "title": info["title"],
            "memo": info["memo"],
            "latitude": info["latitude"],
            "longitude": info["longitude"],
            "id": id
        }
        self.db.query_db(sql, data)

        return { "status": "Success" }

    def get_all_records_by_user_name(self, name): 
        sql = "select id, title, memo, latitude, longitude from records where user_id in (select id from users where name = :name)"
        data = {
            "name": name
        }
        return self.db.query_db(sql, data)

    def delete_record_by_id(self, id):
        sql = "delete from records where id = :id"
        data = {
            "id": id
        }
        self.db.query_db(sql, data)

        return { "status": "Success" }