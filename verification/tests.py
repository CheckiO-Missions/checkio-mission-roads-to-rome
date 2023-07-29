"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(3, 3), []],
            "answer": 20,
        },
        {
            "input": [(3, 4), [(2, 2)]],
            "answer": 17,
        },
        {
            "input": [(10, 5), [(6, 1), (2, 3)]],
            "answer": 2063,
        },
    ],
    "Extra": [
        {
            "input": [(6, 8), [(4, 3), (7, 3), (7, 7), (1, 5)]],
            "answer": 1932,
        },
        {
            "input": [(10, 10), [(0, 1)]],
            "answer": 92378,
        },
        {
            "input": [(100, 100), [(0, 1), (1, 0)]],
            "answer": 0,
        },
        {
            "input": [(1, 3), [(0, 1)]],
            "answer": 1,
        },
        {
            "input": [(1, 3), [(0, 2)]],
            "answer": 2,
        },
        {
            "input": [(1, 3), [(1, 3)]],
            "answer": 0,
        },
        {
            "input": [(0, 0), []],
            "answer": 1,
        },
    ]
}
