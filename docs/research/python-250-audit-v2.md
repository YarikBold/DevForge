# Аудит 250 Python-заданий

Проверено заданий: 250. Источник: `src/course.json` и прикреплённый список ID.

## Сводка

| Статус | Количество |
|---|---:|
| KEEP | 2 |
| REWORK | 244 |
| MOVE | 0 |
| REPLACE | 0 |
| UNSUPPORTED | 4 |

## Правила аудита

- `KEEP`: конкретное условие, проверяемые данные и поддерживаемый тип задания.
- `REWORK`: идея полезна, но есть шаблонные тесты, неполный контракт или несоответствие условия.
- `MOVE`: требуется переставить по уровню сложности.
- `REPLACE`: смысл задания нужно заменить новым.
- `UNSUPPORTED`: нужен отдельный тип интерфейса или runner.

## Все задания

| ID | Тема | Тип | Сложность | Статус | Проблемы |
|---|---|---|---|---|---|
| `python-intro-01` | Введение в программирование и Python | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-intro-02` | Введение в программирование и Python | `predict_output` | `easy` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner |
| `python-intro-03` | Введение в программирование и Python | `debug` | `easy` | **REWORK** | неполные тестовые данные |
| `python-intro-04` | Введение в программирование и Python | `debug` | `easy` | **REWORK** | неполные тестовые данные |
| `python-intro-05` | Введение в программирование и Python | `fill_blanks` | `easy` | **REWORK** | неполные тестовые данные |
| `python-intro-06` | Введение в программирование и Python | `choice` | `easy` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner |
| `python-intro-07` | Введение в программирование и Python | `match` | `medium` | **UNSUPPORTED** | тип требует отдельного интерфейса/runner |
| `python-intro-08` | Введение в программирование и Python | `debug` | `medium` | **REWORK** | неполные тестовые данные |
| `python-intro-09` | Введение в программирование и Python | `write_program` | `medium` | **REWORK** | неполные тестовые данные |
| `python-intro-10` | Введение в программирование и Python | `hidden_tests` | `hard` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-types-01` | Переменные и типы данных | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-types-02` | Переменные и типы данных | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-types-03` | Переменные и типы данных | `debug` | `easy` | **REWORK** | неполные тестовые данные |
| `python-types-04` | Переменные и типы данных | `predict_output` | `easy` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner |
| `python-types-05` | Переменные и типы данных | `predict_output` | `medium` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner |
| `python-types-06` | Переменные и типы данных | `fill_blanks` | `medium` | **REWORK** | неполные тестовые данные |
| `python-types-07` | Переменные и типы данных | `match` | `medium` | **UNSUPPORTED** | тип требует отдельного интерфейса/runner |
| `python-types-08` | Переменные и типы данных | `pytest` | `hard` | **REWORK** | тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-types-09` | Переменные и типы данных | `refactor` | `hard` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-types-10` | Переменные и типы данных | `hidden_tests` | `hard` | **REWORK** | тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-io-ops-01` | Ввод, вывод и операции | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-io-ops-02` | Ввод, вывод и операции | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-io-ops-03` | Ввод, вывод и операции | `write_program` | `easy` | **KEEP** | не обнаружено |
| `python-io-ops-04` | Ввод, вывод и операции | `debug` | `medium` | **REWORK** | неполные тестовые данные |
| `python-io-ops-05` | Ввод, вывод и операции | `predict_output` | `medium` | **REWORK** | неполные тестовые данные; тип требует отдельного интерфейса/runner |
| `python-io-ops-06` | Ввод, вывод и операции | `fill_blanks` | `medium` | **REWORK** | неполные тестовые данные |
| `python-io-ops-07` | Ввод, вывод и операции | `match` | `medium` | **UNSUPPORTED** | тип требует отдельного интерфейса/runner |
| `python-io-ops-08` | Ввод, вывод и операции | `pytest` | `hard` | **REWORK** | тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-io-ops-09` | Ввод, вывод и операции | `refactor` | `hard` | **REWORK** | тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-io-ops-10` | Ввод, вывод и операции | `hidden_tests` | `hard` | **REWORK** | тип требует отдельного интерфейса/runner; сложность слишком рано |
| `python-conditions-01` | Условия и логические выражения | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-conditions-02` | Условия и логические выражения | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-conditions-03` | Условия и логические выражения | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-conditions-04` | Условия и логические выражения | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-conditions-05` | Условия и логические выражения | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-conditions-06` | Условия и логические выражения | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-conditions-07` | Условия и логические выражения | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-conditions-08` | Условия и логические выражения | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-conditions-09` | Условия и логические выражения | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-conditions-10` | Условия и логические выражения | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-loops-01` | Циклы for и while | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-loops-02` | Циклы for и while | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-loops-03` | Циклы for и while | `write_program` | `easy` | **REWORK** | неполные тестовые данные |
| `python-loops-04` | Циклы for и while | `write_program` | `medium` | **KEEP** | не обнаружено |
| `python-loops-05` | Циклы for и while | `write_program` | `medium` | **REWORK** | неполные тестовые данные |
| `python-loops-06` | Циклы for и while | `debug` | `medium` | **REWORK** | неполные тестовые данные |
| `python-loops-07` | Циклы for и while | `write_program` | `medium` | **REWORK** | неполные тестовые данные |
| `python-loops-08` | Циклы for и while | `write_program` | `hard` | **REWORK** | неполные тестовые данные |
| `python-loops-09` | Циклы for и while | `debug` | `hard` | **REWORK** | неполные тестовые данные |
| `python-loops-10` | Циклы for и while | `hidden_tests` | `hard` | **UNSUPPORTED** | тип требует отдельного интерфейса/runner |
| `python-strings-01` | Строки | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-strings-02` | Строки | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-strings-03` | Строки | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-strings-04` | Строки | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-strings-05` | Строки | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-strings-06` | Строки | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-strings-07` | Строки | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-strings-08` | Строки | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-strings-09` | Строки | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-strings-10` | Строки | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-lists-tuples-01` | Списки и кортежи | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-lists-tuples-02` | Списки и кортежи | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-lists-tuples-03` | Списки и кортежи | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-lists-tuples-04` | Списки и кортежи | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-lists-tuples-05` | Списки и кортежи | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-lists-tuples-06` | Списки и кортежи | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-lists-tuples-07` | Списки и кортежи | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-lists-tuples-08` | Списки и кортежи | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-lists-tuples-09` | Списки и кортежи | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-lists-tuples-10` | Списки и кортежи | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-dicts-sets-01` | Словари и множества | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-dicts-sets-02` | Словари и множества | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-dicts-sets-03` | Словари и множества | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-dicts-sets-04` | Словари и множества | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-dicts-sets-05` | Словари и множества | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-dicts-sets-06` | Словари и множества | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-dicts-sets-07` | Словари и множества | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-dicts-sets-08` | Словари и множества | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-dicts-sets-09` | Словари и множества | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-dicts-sets-10` | Словари и множества | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-functions-01` | Функции | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-functions-02` | Функции | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-functions-03` | Функции | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-functions-04` | Функции | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-functions-05` | Функции | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-functions-06` | Функции | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-functions-07` | Функции | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-functions-08` | Функции | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-functions-09` | Функции | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-functions-10` | Функции | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-scope-01` | Области видимости | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-scope-02` | Области видимости | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-scope-03` | Области видимости | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-scope-04` | Области видимости | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-scope-05` | Области видимости | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-scope-06` | Области видимости | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-scope-07` | Области видимости | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-scope-08` | Области видимости | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-scope-09` | Области видимости | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-scope-10` | Области видимости | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-files-01` | Работа с файлами | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-files-02` | Работа с файлами | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-files-03` | Работа с файлами | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-files-04` | Работа с файлами | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-files-05` | Работа с файлами | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-files-06` | Работа с файлами | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-files-07` | Работа с файлами | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-files-08` | Работа с файлами | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-files-09` | Работа с файлами | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-files-10` | Работа с файлами | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-exceptions-01` | Обработка исключений | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-exceptions-02` | Обработка исключений | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-exceptions-03` | Обработка исключений | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-exceptions-04` | Обработка исключений | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-exceptions-05` | Обработка исключений | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-exceptions-06` | Обработка исключений | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-exceptions-07` | Обработка исключений | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-exceptions-08` | Обработка исключений | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-exceptions-09` | Обработка исключений | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-exceptions-10` | Обработка исключений | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-packages-01` | Модули, пакеты и виртуальные окружения | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-packages-02` | Модули, пакеты и виртуальные окружения | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-packages-03` | Модули, пакеты и виртуальные окружения | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-packages-04` | Модули, пакеты и виртуальные окружения | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-packages-05` | Модули, пакеты и виртуальные окружения | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-packages-06` | Модули, пакеты и виртуальные окружения | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-packages-07` | Модули, пакеты и виртуальные окружения | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-packages-08` | Модули, пакеты и виртуальные окружения | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-packages-09` | Модули, пакеты и виртуальные окружения | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-packages-10` | Модули, пакеты и виртуальные окружения | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-oop-01` | Объектно-ориентированное программирование | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-oop-02` | Объектно-ориентированное программирование | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-oop-03` | Объектно-ориентированное программирование | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-oop-04` | Объектно-ориентированное программирование | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-oop-05` | Объектно-ориентированное программирование | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-oop-06` | Объектно-ориентированное программирование | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-oop-07` | Объектно-ориентированное программирование | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-oop-08` | Объектно-ориентированное программирование | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-oop-09` | Объектно-ориентированное программирование | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-oop-10` | Объектно-ориентированное программирование | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-iterators-01` | Итераторы и генераторы | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-iterators-02` | Итераторы и генераторы | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-iterators-03` | Итераторы и генераторы | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-iterators-04` | Итераторы и генераторы | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-iterators-05` | Итераторы и генераторы | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-iterators-06` | Итераторы и генераторы | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-iterators-07` | Итераторы и генераторы | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-iterators-08` | Итераторы и генераторы | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-iterators-09` | Итераторы и генераторы | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-iterators-10` | Итераторы и генераторы | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-algorithms-01` | Алгоритмы и структуры данных | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-algorithms-02` | Алгоритмы и структуры данных | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-algorithms-03` | Алгоритмы и структуры данных | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-algorithms-04` | Алгоритмы и структуры данных | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-algorithms-05` | Алгоритмы и структуры данных | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-algorithms-06` | Алгоритмы и структуры данных | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-algorithms-07` | Алгоритмы и структуры данных | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-algorithms-08` | Алгоритмы и структуры данных | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-algorithms-09` | Алгоритмы и структуры данных | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-algorithms-10` | Алгоритмы и структуры данных | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-api-01` | JSON и HTTP API | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-api-02` | JSON и HTTP API | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-api-03` | JSON и HTTP API | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-api-04` | JSON и HTTP API | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-api-05` | JSON и HTTP API | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-api-06` | JSON и HTTP API | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-api-07` | JSON и HTTP API | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-api-08` | JSON и HTTP API | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-api-09` | JSON и HTTP API | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-api-10` | JSON и HTTP API | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-sql-01` | SQL в Python | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-sql-02` | SQL в Python | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-sql-03` | SQL в Python | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-sql-04` | SQL в Python | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-sql-05` | SQL в Python | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-sql-06` | SQL в Python | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-sql-07` | SQL в Python | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-sql-08` | SQL в Python | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-sql-09` | SQL в Python | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-sql-10` | SQL в Python | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-testing-01` | Автоматизированное тестирование | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-testing-02` | Автоматизированное тестирование | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-testing-03` | Автоматизированное тестирование | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-testing-04` | Автоматизированное тестирование | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-testing-05` | Автоматизированное тестирование | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-testing-06` | Автоматизированное тестирование | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-testing-07` | Автоматизированное тестирование | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-testing-08` | Автоматизированное тестирование | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-testing-09` | Автоматизированное тестирование | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-testing-10` | Автоматизированное тестирование | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-debugging-01` | Отладка и логирование | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-debugging-02` | Отладка и логирование | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-debugging-03` | Отладка и логирование | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-debugging-04` | Отладка и логирование | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-debugging-05` | Отладка и логирование | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-debugging-06` | Отладка и логирование | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-debugging-07` | Отладка и логирование | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-debugging-08` | Отладка и логирование | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-debugging-09` | Отладка и логирование | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-debugging-10` | Отладка и логирование | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-typing-01` | Типизация и качество кода | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-typing-02` | Типизация и качество кода | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-typing-03` | Типизация и качество кода | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-typing-04` | Типизация и качество кода | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-typing-05` | Типизация и качество кода | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-typing-06` | Типизация и качество кода | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-typing-07` | Типизация и качество кода | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-typing-08` | Типизация и качество кода | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-typing-09` | Типизация и качество кода | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-typing-10` | Типизация и качество кода | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-architecture-01` | Архитектура программ | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-architecture-02` | Архитектура программ | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-architecture-03` | Архитектура программ | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-architecture-04` | Архитектура программ | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-architecture-05` | Архитектура программ | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-architecture-06` | Архитектура программ | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-architecture-07` | Архитектура программ | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-architecture-08` | Архитектура программ | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-architecture-09` | Архитектура программ | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-architecture-10` | Архитектура программ | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-git-01` | Git в Python-проектах | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-git-02` | Git в Python-проектах | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-git-03` | Git в Python-проектах | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-git-04` | Git в Python-проектах | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-git-05` | Git в Python-проектах | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-git-06` | Git в Python-проектах | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-git-07` | Git в Python-проектах | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-git-08` | Git в Python-проектах | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-git-09` | Git в Python-проектах | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-git-10` | Git в Python-проектах | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-apps-01` | Практическая разработка приложений | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-apps-02` | Практическая разработка приложений | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-apps-03` | Практическая разработка приложений | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-apps-04` | Практическая разработка приложений | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-apps-05` | Практическая разработка приложений | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-apps-06` | Практическая разработка приложений | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-apps-07` | Практическая разработка приложений | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-apps-08` | Практическая разработка приложений | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-apps-09` | Практическая разработка приложений | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-apps-10` | Практическая разработка приложений | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-final-01` | Итоговый проект | `code` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-final-02` | Итоговый проект | `debug` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-final-03` | Итоговый проект | `predict` | `easy` | **REWORK** | шаблонные формулировки/тесты |
| `python-final-04` | Итоговый проект | `choice` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-final-05` | Итоговый проект | `fill` | `medium` | **REWORK** | шаблонные формулировки/тесты |
| `python-final-06` | Итоговый проект | `match` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-final-07` | Итоговый проект | `traceback` | `medium` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-final-08` | Итоговый проект | `test` | `hard` | **REWORK** | шаблонные формулировки/тесты |
| `python-final-09` | Итоговый проект | `refactor` | `hard` | **REWORK** | шаблонные формулировки/тесты; тип требует отдельного интерфейса/runner |
| `python-final-10` | Итоговый проект | `hidden-tests` | `hard` | **REWORK** | шаблонные формулировки/тесты |

