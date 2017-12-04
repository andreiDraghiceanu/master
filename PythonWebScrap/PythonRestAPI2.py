from flask import Flask, render_template, request, jsonify
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'Javascript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})


@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode
