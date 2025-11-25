"""
Birthday Calculator - 
Supports multiple date/time formats and Jalali conversion.
"""

from datetime import datetime
import jdatetime
class BirthdayCalculator:
    def __init__(self, user_input:str):
        """Initialize with user input string and parse birth date/time."""
        parsed_date = self._parse_input(user_input)
        self.birth_datetime = parsed_date
        self.now = datetime.now()

    def _parse_input(self,user_input) -> datetime:
        """Parse various date/time formats into datetime object."""
        cleaned = user_input.strip()
        formats = [
        "%Y-%m-%d",           # 2025-04-05
        "%Y/%m/%d",           # 2025/04/05
        "%d/%m/%Y",           # 05/04/2025
        "%d-%m-%Y",           # 05-04-2025
        "%Y-%m-%d %H:%M",     # 2025-04-05 14:30
        "%Y/%m/%d %H:%M",     # 2025/04/05 14:30
        "%d/%m/%Y %H:%M",     # 05/04/2025 14:30
        ]

        for fmt in formats:
            try:
                parsed_date = datetime.strptime(cleaned,fmt)
                return parsed_date
            except ValueError:
                continue

        raise ValueError(
            "Unable to parse date. "
        "Please use formats like: YYYY/MM/DD, DD/MM/YYYY, or with time (HH:MM)"
        )

    def _lived_seconds(self) -> int:
        """Return total seconds lived since birth."""
        age_delta = self.now - self.birth_datetime
        return int(age_delta.total_seconds())

    def _days_and_minutes_to_next_birthday(self):
        """Calculate days and remaining minutes until next Gregorian birthday."""
        today = self.now.date()
        current_year =today.year
        this_year_birthday = self.birth_datetime.replace(current_year)

        if this_year_birthday.date()<today:
            next_birthday = this_year_birthday.replace(year= current_year+1)
        else:
            next_birthday = this_year_birthday

        delta = next_birthday - self.now
        days = delta.days
        total_seconds_left = delta.total_seconds()
        total_minutes = int(total_seconds_left // 60)
        minutes_only = total_minutes - (days*24*60)
        return days,minutes_only
    
    def _to_jalali(self) -> str:
        """Convert Gregorian birth date to Jalali (Persian) calendar format."""
        jalali_date = jdatetime.date.fromgregorian(date= self.birth_datetime.date())
        return jalali_date.strftime("%Y/%m/%d")
    
    def _days_and_minutes_to_next_jalali_birthday(self):
        """Calculate days until next birthday in Jalali calendar.
        Handles leap year edge cases (Esfand 30 → 29).
        """
        today = jdatetime.date.today()
        jalali_birthday = jdatetime.date.fromgregorian(date=self.birth_datetime.date())

        try:
            next_jbirthday = jalali_birthday.replace(year=today.year)
        except ValueError:
            next_jbirthday = jalali_birthday.replace(year=today.year, day=29)

        if next_jbirthday < today:
            try:
                next_jbirthday = jalali_birthday.replace(year=today.year + 1)
            except ValueError:
                next_jbirthday = jalali_birthday.replace(year=today.year + 1 , day=29)

        delta = next_jbirthday - today
        return delta.days

    def celebrate(self) -> None:
        """Display all birthday information in a beautiful format."""
        seconds = self._lived_seconds()
        days , minutes = self._days_and_minutes_to_next_birthday()
        jalali = self._to_jalali()
        jalali_days = self._days_and_minutes_to_next_jalali_birthday()
        print(f"""
        ✨ Your Birthday Information✨
--------------------------------------------------
Birth Date (Gregorian)  : {self.birth_datetime.strftime('%Y/%m/%d %H:%M')}
Birth Date (Jalali)     : {jalali}
You have lived          : {seconds:,}
Next birthday in        : {days} days and {minutes:,} minutes:))
Next Jalali birthday in : {jalali_days} days :))
HAPPY BIRTHDAY IN ADVANCE :))))✨
""")
        
# ___________________testing_________________

if __name__ == "__main__":
    try:
        birth = input("Enter your gregorian birth date (e.g., 1374/05/24 14:30): ")
        calc = BirthdayCalculator(birth)
        calc.celebrate()
    except ValueError as e:
        print(f"Error: {e}")






































# import datetime
# import pytz
# print("time of now")

# value = datetime.datetime(year=2020, month=2, day=2)
# print(value)

# iran = pytz.timezone('asia/tehran')
# irant = datetime.datetime.now(iran)
# print('iran', irant.strftime('%Y.%m.%d %H:%M:%S'))

# us = pytz.timezone('America/New_York')
# ust = irant.astimezone(us)
# print('America', ust.strftime('%Y.%m.%d %H:%M:%S'))



