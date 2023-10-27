from flask import Flask, render_template, jsonify

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengluru,KA,India',
    'Salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Backend Engineer',
    'Location': 'Pune,MH,India',
    'Salary': 'Rs. 7,00,000'
}, {
    'id': 3,
    'title': 'Buisness Analyst',
    'Location': 'Bengluru,KA,India',
    'Salary': 'Rs. 5,00,000'
}]

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
