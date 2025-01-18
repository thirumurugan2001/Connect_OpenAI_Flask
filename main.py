from flask import Flask, request, jsonify
from controller import *
app = Flask(__name__)



# This Route is used to the connect the Azure Open AI gpt-4o and implement the 3th tier.
@app.route('/openAi', methods=['POST'])
def TranscribeSummary():
    try:
        data = request.get_json()
        response = AzureOpenAIController(data)
        return jsonify(response)
    except Exception as e:
        print(f"Error in Transcribe Summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            })
   
# This Route is used to the connect the Google Search API and implement the 3th tier..
@app.route('/google', methods=['POST'])
def generate_summary():
    try:
        data = request.get_json()
        response = googleSerpController(data)
        return jsonify(response)    
    except Exception as e:
        print(f"Error in generate_summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            })


if __name__ == "__main__":
    app.run(debug=True , port="8080",host="0.0.0.0")