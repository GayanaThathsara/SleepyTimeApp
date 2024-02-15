
import datetime
from pytz import timezone
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sleepytime')
def sleepytime():
    input_time_str = request.args.get('input_time', '')
    input_time = datetime.datetime.strptime(input_time_str, '%H:%M').time()
    local_tz = timezone('Asia/Colombo')
    naive_time = datetime.datetime.combine(datetime.datetime.today(), input_time)
    local_time = local_tz.localize(naive_time, is_dst=None)
    utc_time = local_time.astimezone(timezone('UTC'))
    cycles = [(1.5, 'One Cycle'), (3, 'Two Cycles'), (4.5, 'Three Cycles'), (6, 'Four Cycles'), (7.5, 'Five Cycles'), (9, 'Six Cycles')]
    times = []
    for cycle in cycles:
        wake_up_time_utc = utc_time + datetime.timedelta(hours=cycle[0])
        wake_up_time_local = wake_up_time_utc.astimezone(local_tz)
        times.append((wake_up_time_local.strftime('%-I:%M %p'), cycle[1], cycle[0]))
    return jsonify(times)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
