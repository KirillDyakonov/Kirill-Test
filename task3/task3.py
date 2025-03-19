import json
import sys

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

values = json.load(open(values_file))
tests = json.load(open(tests_file))

values_dict = {}
for item in values['values']:
    values_dict[item['id']] = item['value']


def fill_values(test):
    if isinstance(test, dict):
        if 'id' in test and test['id'] in values_dict:
            test['value'] = values_dict[test['id']]

        if 'values' in test:
            for sub_test in test['values']:
                fill_values(sub_test)

for test in tests['tests']:
    fill_values(test)

json.dump(tests, open(report_file, 'w'), indent=4)