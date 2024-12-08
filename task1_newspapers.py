from datetime import datetime as dt


def parse_newspapers_date(newspapers: dict) -> dict:
    """
    Для каждой газеты из списка определяется формат указанной даты для перевода в объект datetime
    :param newspapers:
    :return: словарь с газетами и их датами типа datetime
    """
    parsed_newspapers = {}
    for name, date in newspapers.items():
        format = ""
        if name == "The Moscow Times":
            format = "%A, %B %d, %Y"
        elif name == "The Guardian":
            format = "%A, %m.%d.%y"
        elif name == "Daily News":
            format = "%A, %d %B %Y"
        if format:
            parsed_newspapers[name] = dt.strptime(date, format)
    return parsed_newspapers


newspapers = {
    "The Moscow Times": "Wednesday, October 2, 2002",
    "The Guardian": "Friday, 11.10.13",
    "Daily News": "Thursday, 18 August 1977"
}
for newspaper in parse_newspapers_date(newspapers).items():
    print(newspaper)
