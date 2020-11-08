from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Howdy!'

@app.route('/tng', methods=['POST'])
def thanks():
    if request.method == 'POST':
        data = request.get_json()
        if 'req' in data and data['req'].lower() == 'thanks':
            return "Gig 'Em" 
        else:
            return "Thanks"

@app.route('/year', methods=['GET','POST'])
def year():
    whoop = {
        'freshman': 'Ayyyyyyy',
        'sophomore': 'Ay Ay Ay Ay Ay',
        'junior': 'Ay Ay Ay Whoop',
        'senior': 'Ay Whoop'
    }
    if request.method=='GET':
        return jsonify(whoop)
    elif request.method=='POST':
        data = request.get_json()
        if 'req' in data and data['req'].lower() in whoop:
            return whoop[data['req'].lower()]
        else:
            return jsonify(whoop)

@app.route('/war-hymn', methods=['GET','POST'])
def war_hymn():
    song = ('''Hullabaloo, Caneck! Caneck!
    Hullabaloo, Caneck! Caneck!
    Good-bye to texas university
    So long to the orange and the white
    Good luck to dear old Texas Aggies
    They are the boys that show the real old fight
    “The eyes of Texas are upon you . . .”
    That is the song they sing so well
    So good-bye to texas university
    We’re going to beat you all to Chig-gar-roo-gar-rem
    Chig-gar-roo-gar-rem
    Rough Tough! Real Stuff! Texas A&M!''').split(" ")

    space = " "
    if request.method=='GET':
        return space.join(song)
    elif request.method=='POST':
        data = request.get_json()
        if 'req' in data and data['req'] in song:
            i = song.index(data['req'])
            return space.join(song[i:])
        else:
            return space.join(song)


if __name__ == '__main__':
    app.run(port=3000)