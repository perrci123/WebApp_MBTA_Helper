from flask import Flask, render_template, request

from src.mbta_helper import find_stop_near

app = Flask(__name__) #COPY

app.config['DEBUG'] = True #THIS

app.secret_key = "Some secret string here" #FOR WEBSITE CODE

@app.route('/', methods=['GET', 'POST'])
@app.route('/mbta/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        location = request.form['a']
        stop, dist = find_stop_near(location)
        if stop:
            return render_template('MBTA_result.html', a=location,
                                   s=stop, d=dist)
        else:
            return render_template('MBTA_form.html')
    return render_template('MBTA_form.html')

if __name__ == '__main__':
    app.run()
