from CrunchAPI import Test

test = Test()

info = {'testName': 'name1111', 'testDescription': 'descr2', 'question': 'qst', 'options': ['pick 1', 'pick 2', 'pick 3', 'pick 4', 'pick 5'], 'selectedOption': 3}
print(test.addTest(info))