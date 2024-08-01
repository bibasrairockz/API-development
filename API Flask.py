from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route("/")
def home():
    return "Home "

@app.route("/get-user/<user_id>")
def get_user_with_id(user_id):
    user_data= {
    "user_id": user_id,
    "name": "Bibas",
    "email": "bibasrai@yahoo.com"
    }

    extra= request.args.get("extra")

    if extra:
        user_data['extra']= extra
    
    return jsonify(user_data), 1000


if __name__=="__main__":
    app.run(debug= True, port= 9000)

