import flask
import requests
import json
from collections import Counter

app = flask.Flask(__name__)

#DEBUG has vulnerability and therefor needs to be turned-off on production environment HTTPS CVE 
#app.config["DEBUG"] = True

@app.route('/nxt')
#@app.route('/')
def nxt():
    response = requests.post('http://aie.artiqox.com/nxt?requestType=getBlocks&firstIndex=0&lastIndex=99')
    results_g = response.json()
    Forgers = list(response)
    dic = results_g
    generatorRS = 'generatorRS'
    queue = []
    for i in range(100):
          result = dic['blocks'][i]['generatorRS']
          #print(result)
          queue.append(result)
          def_list = []
    def_list.append(Counter(queue))
    def_str1 = str(def_list)
    def_str = def_str1.replace('Counter', '')
    def_str = def_str.translate(str.maketrans({'{': '', '}': '', '[': '', ']': '', '(': '', ')': ''}))
    result = str()
    result = str('List of top AIE_WALLET that Forged in last 100 Blocks : ' + def_str)
    return result

if __name__ == '__main__':
   app.run(host='localhost')
