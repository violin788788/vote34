


from flask import Flask, render_template
app=Flask(__name__)
#MP3S_FOLDER=os.path.join(os.path.dirname(__file__),'static','mp3s')
@app.route('/')
def index():
    #files=[f for f in os.listdir(MP3S_FOLDER) if f.endswith('.mp3')]
    return render_template('vote34.html')

