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

    template = '''
    <!DOCTYPE html>
    <html>
      <head>
        <title>Chicken Tenders Calculator</title>
      </head>
      <body>
        <h1>Welcome to the CTPC -- The Chicken Tenders Probability Calculator</h1>
        <h3>Percent likelihood of chicken tenders being served on ''' + date + ''' 
        is ''' + tenders_percentage(date) + '''!</h3>

        To check another date, include a ?date query with the URL.
        <br><a href="/?date=01-11-2023">Example query for 01-11-2023</a> 
      </body>
    </html>'''

    return render_template_string(template)


def tenders_percentage(date):
    # Create a datetime object from the string
    try:
        dt = datetime.datetime.strptime(date, '%m-%d-%Y').date()
        # Find the day of the week. There's the 50% chance of tenders on Wednesdays
        if dt.weekday() == 2:
            return '50%'
        else:
            return '0%'
    except:
        return '<i>ERROR<br>Cannot calculate percentage because date is not in correct month-day-year format. (e.g. 12-23-2023)</i>'


if __name__ == '__main__':
    with open('flag.txt') as f:
        flag = f.read()

    app.run()
