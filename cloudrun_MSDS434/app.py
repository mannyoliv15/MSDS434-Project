from flask import Flask, jsonify, render_template, request, make_response
import transformers


app = Flask(__name__)


# create a python dictionary for your models d = {<key>: <value>, <key>: <value>, ..., <key>: <value>}
dictOfModels = {"General Text" : transformers.pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english"), "Twitter": transformers.pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")}
# create a list of keys to use them in the select part of the html code
listOfKeys = []
for key in dictOfModels :
        listOfKeys.append(key)

def get_prediction(message,model):
    # inference
    results = model(message)  
    return results

@app.route('/', methods=['GET'])
def get():
    # in the select we will have each key of the list in option
    return render_template("home.html", len = len(listOfKeys), listOfKeys = listOfKeys)

@app.route('/', methods=['POST'])
def predict():
    message = request.form['message']
    # choice of the model
    results = get_prediction(message, dictOfModels[request.form.get("model_choice")])
    print(f'User selected model : {request.form.get("model_choice")}')
    my_prediction = f'The feeling of this text is {results[0]["label"]} with probability of {results[0]["score"]*100}%.'
    return render_template('result.html', text = f'{message}', prediction = my_prediction)

if __name__ == '__main__':
    # starting app
    app.run(debug=True)