from  flask import Flask, render_template # import the flask structure and render_template to connect back to front end

app = Flask(__name__, template_folder='templates', static_folder='static') # look into this folder "." (not a separate template folder) for the html

@app.route('/') # sort of needed to lauch app. when someone visits the url for this page, run the bellow
def home(): # function "home" we call towards the end
    return render_template('index.html') # connects to the index.html file

@app.route('/narr') #when someone visits the url for this second page, run the bellow
def narr(): 
    return render_template('narr.html')

if __name__ == '__main__': # if this file matches main(?)
    app.run(debug=True, port=8000)