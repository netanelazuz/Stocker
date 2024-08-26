# this project goal is to give the user as much information on a stock he is interested in: 
# such as: current value (live), latest news related, market value, buyers - sellers ratio, graph of current status
# this will be done as the program takes a market ticker as an input and the rest is done by itself.
# features for the future: *a few tabs to enable multiple stocks status. **buy/sell reccomendation by technical analysis.

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

#home page route
@app.route("/")
@app.route("/home")
def index():
    #Go to home page as default
    return render_template('index.html')
        

@app.route('/search', methods=['GET'])
def search():
    # Get the search query from the form
    ticker = request.args.get('search')

    # If the ticker is not empty, redirect to the dashboard
    if ticker:
        return redirect(url_for('dashboard', ticker=ticker))
    
    # If the ticker is empty, redirect back to the homepage (or handle as needed)
    return redirect(url_for('index'))

  
@app.route("/dashboard/")
def dashboard():
    ticker = request.args.get('ticker')
    return render_template("dashboard.html", ticker= ticker)

if __name__ == "__main__":
    app.run(debug=True)
