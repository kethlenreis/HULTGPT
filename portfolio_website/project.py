import os
from flask import Flask, render_template

app = Flask(__name__)

#  store image URLs and subtitles
images = [
    ('https://i.imgur.com/Vkw2Uel.jpg', 'President of the Hult Connect Club'),
    ('https://i.imgur.com/HAdUR2A.jpg', 'Business Writing Certificate'),
    ('https://i.imgur.com/lcp3uLD.jpg', 'Python for Everybody Certificate'),
    ('https://i.imgur.com/8aZ8pwS.jpg', 'Volunteer Koman Breast Cancer Corp.'),
    
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', images=images)

@app.route('/contact')
def contact():
    return render_template('contact.html')  

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()