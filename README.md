README Instructions - Christina Chimienti
===========================================
ArrayManipulation REST API:
Written in Python using flask and numpy and deployed in AWS over an EC2 instance running over flask and a waitress WSGI server.
I've included here instructions, examples of use, and time complexity. And I have also included additional test cases in the file 
ArrayManipulationManagerTest.py.
AWS IP: http://18.222.67.139


*GET /getrandomstringarray
- Use: get a random string array in JSON form  
- Time Complexity: O(n)  

Returns:
    [
        "nwLBA",
        "olK",
        "3",
        "a",
        "Uj",
        "QsgmQ"
    ]

*POST /findsameint
- Use: takes in two integer arrays (JSON format) as an input (array A and array B) and removes all items in array A that exists in array B. This returns the resulting array A in JSON form  
- Time Complexity: O(n)
    - Used list.append() rather than list.remove() in program to improve time complexity

Example Body: 
    {
	    "A" : [10, 100, 20, 30, 50, 60],
	    "B" : [10, 100, 20]
    }

Returns:
    [
        30,
        50,
        60
    ]


*POST /findsharedstr
- Use: takes in two string arrays (JSON format) as an input (array A and array B) and returns an array of all shared items in JSON form  
- Time Complexity: O(n)  

Example Body: 
    {
	    "A" : ["green", "purple", "red", "blue"],
	    "B" : ["yellow", "blue", "green"]
    }

Returns:
    [
        "green",
        "blue"
    ]   


*POST /calculateiqr
- Use: takes in one integer array (JSON format) as an input and returns a dictionary with the IQR (Q1, Q3, median) in JSON form  
- Time Complexity: O(n log n)

Example Body:
    {
	    "A" : [1, 2, 3, 4]
    }   

Returns:
    {
        "Q1": 1,
        "Q3": 4,
        "median": 2.5
    }
  
  
Additional Request to clear built up cache:

*GET /clearcache
- Use: clears stored cache for each POST API
- returns 'Cached cleared successfully.' upon success