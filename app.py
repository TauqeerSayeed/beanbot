from flask import Flask, render_template, request, redirect
import webbrowser
import time

app = Flask(__name__)
channel_created = False  # To track if the channel is created

@app.route('/', methods=['GET', 'POST'])
def index():
    global channel_created

    if request.method == 'POST':
        url = request.form['url']

        webbrowser.open(url)

        # Wait for user input
        time.sleep(1)

    return render_template('index.html')

@app.route('/open-channel', methods=['POST'])
def open_channel():
    global channel_created

    if request.form.get('create_channel'):
        # User has clicked the "Channel Created" button
        channel_created = True

    if channel_created:
        # Channel is created, proceed to open the given channel
        channel_link = "https://www.youtube.com/@sahilstudio01"  # Replace with your channel link
        webbrowser.open(channel_link)

    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)
