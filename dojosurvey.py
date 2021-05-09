from flask import Flask,render_template, request
app = Flask (__name__)

@app.route('/')
def survey_form():

    return render_template('dojosurvey.html')

@app.route('/result', methods=['POST'])
def result():

    return render_template('result.html', 
    full_name = request.form['full_name'],
    locations = request.form['locations'],
    languages = request.form['languages'],
    comment = request.form['comment'] 
    )



if __name__ == "__main__":
    app.run(debug = True)
