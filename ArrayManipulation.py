#moblab api assignment: python rest api
'''
* GET: get a random string array in JSON form
* POST: takes in two integer arrays (JSON format)  as an input (array A and array B) and removes all items in array A that exists in array B. This should return the resulting array A in JSON form
* POST: takes in two string arrays (JSON format)  as an input (array A and array B) and returns an array of all shared items in JSON form
* POST: takes in one integer array (JSON format) as an input and returns a dictionary with the IQR (Q1,median,Q3) in JSON form
'''
import ArrayManipulationManager as manager
from flask import Flask, request, json, jsonify

app = Flask(__name__)

#GET Request
@app.route('/getrandomstringarray', methods=['GET'])
def GetRandomStringArray():
    rand = manager.getRandomStringArray()
    return (jsonify(rand))

#Error Handling
class BadInputRequest(Exception):
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload

@app.errorhandler(BadInputRequest)
def input_error(error):
    payload = dict(error.payload or ())
    payload['status'] = error.status
    payload['message'] = error.message
    return (json.dumps(payload)), 400

#POST Requests
@app.route('/findsameint', methods=['POST'])
def FindSameInt():
    #should only accept int
    json_data = request.get_data()
    array_a, array_b = __check_error(json.loads(json_data), int)

    result_array = manager.removeSharedIntegers(array_a, array_b)
    return (jsonify(result_array))

@app.route('/findsharedstr', methods=['POST'])
def FindSharedStr():
    json_data = request.get_data()
    array_a, array_b = __check_error(json.loads(json_data), str)

    matched_strings = manager.getSharedString(array_a, array_b)
    return (jsonify(list(set(matched_strings))))

@app.route('/calculateiqr', methods=['POST'])
def CalculateIqr():
    json_data = request.get_data()
    array_a = __check_error(json.loads(json_data))

    IQR = manager.Iqr(array_a)
    return (jsonify(IQR))

@app.route('/clearcache', methods=['GET'])
def ClearCache():
    if manager.clear_cache:
        return (jsonify('Cached cleared successfully.'))

def __check_error(data, datatype=None):
    if datatype is None:
        try:
                array_a = data["A"]
        except:
            raise BadInputRequest('Input Array A must be supplied')

        for i in array_a:
            if type(i) != int:
                raise BadInputRequest('Input Array A must be of type int')
        return array_a
    else:
        try:
            array_a, array_b = data["A"], data["B"]
        except:
            raise BadInputRequest('Input Array A and Array B must be supplied')
        
        for i in array_a:
            if type(i) != datatype:
                raise BadInputRequest('Input Array A must be of type {} '.format(datatype))
        for i in array_b:
            if type(i) != datatype:
                raise BadInputRequest('Input Array B must be of type {} '.format(datatype))
        
        return array_a, array_b

app.run(debug=True)