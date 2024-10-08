import requests
from datetime import datetime, date, timedelta

holidays2025 = [{'fecha': '2025-01-01'}, {'fecha': '2025-04-18'}, {'fecha': '2025-04-19'}, {'fecha': '2025-05-01'}, {'fecha': '2025-05-21'}, {'fecha': '2025-06-20'}, {'fecha': '2025-06-29'}, {'fecha': '2025-06-29'}, {'fecha': '2025-07-16'}, {'fecha': '2025-08-15'}, {'fecha': '2025-09-18'}, {'fecha': '2025-09-19'}, {'fecha': '2025-10-12'}, {'fecha': '2025-10-31'}, {'fecha': '2025-11-01'}, {'fecha': '2025-11-16'}, {'fecha': '2025-12-08'}, {'fecha': '2025-12-14'}, {'fecha': '2025-12-25'}] 
holidays2026 = [{'fecha': '2026-01-01'}, {'fecha': '2026--3 '}, {'fecha': '2026--4 '}, {'fecha': '2026-05-01'}, {'fecha': '2026-05-21'}, {'fecha': '2026-06-21'}, {'fecha': '2026-06-29'}, {'fecha': '2026-07-16'}, {'fecha': '2026-08-15'}, {'fecha': '2026-09-18'}, {'fecha': '2026-09-19'}, {'fecha': '2026-10-12'}, {'fecha': '2026-10-31'}, {'fecha': '2026-11-01'}, {'fecha': '2026-12-08'}, {'fecha': '2026-12-25'}]

def get_holidays(year):
    url = f"https://apis.digital.gob.cl/fl/feriados/{year}"
    
    try:
        headers = {
            'Host': 'apis.digital.gob.cl',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        
        holidays = response.json()  # Parse the JSON response
        return holidays
        # Print out the holidays
        # for holiday in holidays:
        #     print(f"Date: {holiday['fecha']}, Name: {holiday['nombre']}, Type: {holiday['tipo']}")
    
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else: {err}")

def parseDates(dates, year) -> list:
    aux_dates = dates
    if "error" in dates:
        if year == "2025":
            aux_dates = holidays2025
        elif year == "2026":
            aux_dates = holidays2026
    return [date['fecha'] for date in aux_dates]

def get_some_years() -> list:
    current_year = datetime.now().year
    return [str(current_year + i) for i in range(-3,4,1)]

def get_weekends(year) -> list:
    weekends = []
    start_date = date(int(year), 1, 1)
    end_date = date(int(year), 12, 31)
    delta = timedelta(days=1)
    while start_date <= end_date:
        if start_date.weekday() in (5, 6):  # 5 = Saturday, 6 = Sunday
            weekends.append(start_date.strftime("%Y-%m-%d"))
        start_date += delta
    return weekends

def getInvalidDates(year) -> list:
    return ["holidays"] + parseDates(get_holidays(year), year) + ["weekends"] + get_weekends(year)

def isInvalidDate(date, invalidDates) -> bool:
    return False if date in invalidDates else True

def turnAroundDate(date_string:str) -> str:
    if date_string.count('-') == 2:
        splitted_date = date_string.split(sep='-')
        return splitted_date[2] + '-' + splitted_date[1] + '-' + splitted_date[0]
    return date_string


if __name__ == '__main__':
    # Example usage
    year = 2024
    holidays = get_holidays(year)
    print(getInvalidDates(2024))
