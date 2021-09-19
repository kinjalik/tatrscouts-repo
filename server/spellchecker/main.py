import json

from tatdistrsem import TatSpellCheck

tst=TatSpellCheck()

from flask import Flask

app = Flask(__name__)



@app.route("/spellcheck/<text>")
def hello_world(text):
    spr=tst.spellcheck(text)
    data_set = {"word_index":spr[0], "word_string": spr[1]}
    json_dump = json.dumps(data_set)
    return json_dump