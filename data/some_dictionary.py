simple_dictionary = {
    'city': 'San Francisco',
    2: 'Neato',
    'name': 'Carmen',
    1: 'Wow',
    'age': 39,
    'height': 74,
}

another_dict = {
    "widget": {
        "debug": "on",
        "window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 500,
            "height": 500
        },
        "image": {
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
        }
    }
}

"""
Missing key is an exception in Python (vs. nil in Ruby); use .get()
No particular order by default (but there is OrderedDict)
Common operations:
​.keys(), .values(), .items(), .get()
"""
