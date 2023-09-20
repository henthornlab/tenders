from flask import Flask, request, render_template_string
import logging
import datetime

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.INFO)

app = Flask(__name__)


@app.route('/')
def home():

    logging.info("New request for / from %s", request.remote_addr)
    logging.info("Request.args is %s", request.args)
    date = request.args.get('date')
    if date == None:
        today = datetime.date.today()
        date = today.strftime("%m-%d-%Y")

    template = create_response(date)
    return render_template_string(template)


def tenders_percentage(date):
    # Create a datetime object from the string
    try:
        dt = datetime.datetime.strptime(date, '%m-%d-%Y').date()
        # Chances are good on Thursdays
        if dt.weekday() == 3:
            # And they seem to be served once a month on the 2nd week
            if (dt.isocalendar().week % 4 - 1) == 0:
                return '''<b>very good!!</b>
                    <br><img src="https://raw.githubusercontent.com/henthornlab/assets/main/chicken.gif" alt="dancing tenders">
                    <br><br>'''
            else:
                return '''better than average.<br><br>'''
        else:
            return 'not very high. Sorry.'
    except:
        return '<i>ERROR<br>Cannot calculate percentage because date is not in correct month-day-year format. (e.g. 12-23-2023)</i>'

def create_response(date):
    return '''
        <!DOCTYPE html>
        <html>
          <head><title>Chicken Tenders Calculator</title></head>
          <body>
            <h1>Welcome to the CTPC -- The Chicken Tenders Probability Calculator</h1>
            <h3>The likelihood of chicken tenders being served on ''' + date + ''' 
            is ''' + tenders_percentage(date) + '''</h3>

            To check another date, include a ?date query with the URL.
            <br><a href="/?date=09-14-2023">Example query for 09-14-2023</a>
            <br><a href="/?date=09-15-2023">Example query for 09-15-2023</a>
            <br><a href="/?date=09-21-2023">Example query for 09-21-2023</a>
            <br><br>     
          </body>
        </html>'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
