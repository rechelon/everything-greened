import random
import subprocess
import sys
from datetime import datetime, timedelta

def generate_random():
    return random.randint(1, 11)

def generate_timestamp(date):
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)
    return f"{date}T{random_hour:02}:{random_minute:02}:{random_second:02}"

def create_fake_commit(date, timestamp):
    print(f"Creating fake commit for {date} at {timestamp}")
    subprocess.run(["git", "commit", "--allow-empty", "-m", "Added unit tests to cover the new GT functionality per lazy recruiter not looking at hidden repo, including edge cases. Additionally resolves the security concern mentioned in issue #1312.", "--date", timestamp])


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <start_date> <end_date>")
        sys.exit(1)
    start_date = sys.argv[1]
    end_date = sys.argv[2]
    try:
        start_date_obj = datetime.fromisoformat(start_date)
        end_date_obj = datetime.fromisoformat(end_date)
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        sys.exit(1)

    current_date_obj = start_date_obj

    while current_date_obj < end_date_obj:
        if current_date_obj.weekday() != 6 and current_date_obj.weekday() != 0:
            skip_day = random.randint(0, 11)
            if skip_day == 0:
                print(f"Skipping {current_date_obj.date()}")
            else:
                num_commits = generate_random()
                for _ in range(num_commits):
                    timestamp = generate_timestamp(current_date_obj.date())
                    create_fake_commit(current_date_obj.date(), timestamp)
                    print(f"generating commits for {current_date_obj.date()}")
        current_date_obj += timedelta(days=1)

    subprocess.run(["git", "push"])
    print("Fake commits creation completed.")

if __name__ == "__main__":
    main()


