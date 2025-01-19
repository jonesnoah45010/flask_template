from flask import Flask, render_template, jsonify, request




app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
	info = 'Hello, this is info that has been inserted into the HTML of this page from the Flask backend!!!!'
	return render_template("index.html",info = info)



@app.route('/render_form', methods=['GET', 'POST'])
def render_form():
	return render_template("form.html")

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
	data = request.get_json()
	print("I just recieved " + str(data))
	message = data["message"]
	send_back = {}
	send_back["response"] = message + " was recieved"
	return jsonify(send_back), 200




if __name__ == '__main__':
	app.run(debug=True,  host='0.0.0.0', port = 5002)







