
**Учебный проект по автоматизации тестирования API на языке Python на примере тестирования нескольких методов  [Telegram Bot API](https://core.telegram.org/bots/api#replyparameters)**

В проекте использовались библиотеки: pytest, requests, allure, logging, jsonschema

**Цель учебной работы** -  использовать знания и навыки, полученные в процессе изучения основ автотестирования, а именно:          
- базовые навыки программирования (структуры языка, типы данных, модули, переменные окружения и т.п.)
- знания теории REST API (HTTP-методы, структура запроса и ответа, коды статусов ответа)
- принципы ООП (наследование, полиморфизм, абстракция, инкапсуляция)
- работа с фреймворком pytest (запуск тестов, обработка исключений, параллелизация, фикстуры, конфигурационный файл conftest)
- работа с библиотекой requests (работа с HTTP-запросами)
- работа с IDE PyCharm
- работа с библиотекой для репорта отчётов (Allure Report)
- логирование с помощью библиотеки logging (прикрепление логов к отчёту Allure)
- валидация JSON-схем с помощью библиотеки jsonschema

**Структура проекта**        
За основу взята идея создания объектов под каждый endpoint, по аналогии с паттерном Page Object для тестирования UI, когда для каждой страницы создаётся свой объект     
- папка endpoints, в ней хранится файл с описанием класса-родителя для всех endpoints, содержащего методы, общие для всех endpoints
методы каждого из классов инкапсулируют логику тестовых проверок, благодаря чему тесты выглядят человекочитаемо
- папка tests с тестами
- папка json_schemas с json-схемами для каждого метода
- файл logger с методом для логирвания
- конфигурационный файл conftest для фикстур
- файлы с переменными окружения (секретными токенами и id)


