from datetime import datetime, timedelta


def date_range(start_date: str, end_date: str) -> list:
    """
    Возвращает список дат за период от start_date до end_date.
    В случае неверного формата или при start_date > end_date возвращатеся пустой список
    :param start_date: начальная дата в формате YYYY-MM-DD
    :param end_date: начальная дата в формате YYYY-MM-DD
    :return: список дат за период от start_date до end_date
    """
    result_range = []
    date_format = "%Y-%m-%d"
    try:
        start_datetime = datetime.strptime(start_date, date_format)
        end_datetime = datetime.strptime(end_date, date_format)

        curent_datetime = start_datetime
        while curent_datetime <= end_datetime:
            result_range.append(curent_datetime.strftime(date_format))
            curent_datetime += timedelta(days=1)
    except:
        result_range = []
    return result_range


print(date_range("2022-01-01", "2022-01-03"))
print(date_range("2022-01-03", "2022-01-01"))
print(date_range("2022-02-30", "2022-02-31"))
