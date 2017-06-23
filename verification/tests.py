"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[]],
            "answer": True
        },{
            "input": [[[]]],
            "answer": True
        },{
            "input": [[[],[]]],
            "answer": True
        },{
            "input": [[1]],
            "answer": False
        },{
            "input": [[[],[1]]],
            "answer": False
        }
    ],
    "Extra": [
        {
            "input": [[[[[]]]]],
            "answer": True
        },{
            "input": [[[1],[1]]],
            "answer": False
        }
    ]
}