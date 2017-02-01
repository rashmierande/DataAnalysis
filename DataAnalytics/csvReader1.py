import unicodecsv
from datetime import datetime as dt

print("UnicodeCSV and DateTime is working!")

# Data CSV that is imported.
enrollments = "/Users/Rashmi/Desktop/Data Analysis/enrollments.csv"
daily_engagements = "/Users/Rashmi/Desktop/Data Analysis/daily_engagement.csv"
project_submissions = "/Users/Rashmi/Desktop/Data Analysis/project_submissions.csv"


def parse_date(date):
    """
    :param date: Will be the string date
    :return: Object Date
    """
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    """
    :param i: Will be accepting the string i when called
    :return: Will be returning a casted integer from string.
    """
    if i == '':
        return None
    else:
        return int(i)

def csv_reader(filename):
    """
    :param filename: Will be accepting the path of the csv file to be inserted.
    :return: A list of the data inside the csv.
    """
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


for enrollment in enrollments:
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['is_canceld'] = enrollment['is_canceled'] == 'True'

print (enrollments[0])