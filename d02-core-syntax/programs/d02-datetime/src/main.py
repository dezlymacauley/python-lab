# Importing the `datetime` class from the `datetime` module
from datetime import datetime

def main():
    
    #__________________________________________________________________________
  
    # EXAMPLE: 1 => Declaring a `datetime`

    start_time: datetime = datetime(
        year=2026, month=10, day=21, hour=22, minute=30, second=20
    )

    print(f"start_time: {start_time}")
    # start_time: 2026-10-21 22:30:20
    #__________________________________________________________________________
  
    # EXAMPLE: 2 => Accessing the fields of the datetime class

    print(f"year: {start_time.year}")
    print(f"month: {start_time.month}")
    print(f"day: {start_time.day}")
    print(f"hour: {start_time.hour}")
    print(f"minute: {start_time.minute}")
    print(f"second: {start_time.second}")
    #__________________________________________________________________________

if __name__ == "__main__":
    main()
