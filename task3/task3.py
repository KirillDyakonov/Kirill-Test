import json

def load_json(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        return json.load(f)

def update_tests(tests, values_dict):

    for test in tests:
        if isinstance(test, dict):
            test_id = test.get('id')
            if test_id in values_dict:
                test['value'] = values_dict[test_id]
        if 'values' in test:
            update_tests(test['values'], values_dict)

    return tests

def save_json(data, file_path):
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def main():
    values_file = input("Введите путь к файлу values.json: ").strip()
    tests_file = input("Введите путь к файлу tests.json: ").strip()
    report_file = input("Введите путь к файлу report.json (куда сохранить результат): ").strip()

    try:
        values = load_json(values_file)
        tests = load_json(tests_file)

        report = update_tests(tests, values)

        save_json(report, report_file)

        print(f"Файл {report_file} успешно заполнен!")
    except FileNotFoundError:
        print("Ошибка: Один из файлов не найден. Проверьте путь.")
    except json.JSONDecodeError:
        print("Ошибка: Некорректный JSON в одном из файлов.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()