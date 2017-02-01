import unicodecsv
from datetime import datetime as dt
from collections import defaultdict
import numpy as np

print("UnicodeCSV and DateTime is working!")

# Data CSV that is imported.
enrollments = "/Users/Rashmi/Desktop/Data Analysis/enrollments.csv"
daily_engagements = "/Users/Rashmi/Desktop/Data Analysis/daily_engagement.csv"
project_submissions = "/Users/Rashmi/Desktop/Data Analysis/project_submissions.csv"

def csv_reader(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days <7 and time_delta.days >= 0


enrollments = csv_reader(enrollments)
daily_engagements  = csv_reader(daily_engagements)
project_submissions = csv_reader(project_submissions)


for engagement_record in daily_engagements:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

print("the new key val is ", daily_engagements[0]['account_key'])


len(enrollments)
unique_enrolled_students = get_unique_students(enrollments)
len(unique_enrolled_students)
len(daily_engagements)
unique_engagement_students = get_unique_students(daily_engagements)
len(unique_engagement_students)
len(project_submissions)
unique_project_submitters = get_unique_students(project_submissions)
len(unique_project_submitters)

for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        print ("enrollement is ",enrollment)
        break

num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students and enrollment['join_date']!= enrollment['cancel_date']:
        num_problem_students +=1
        print (enrollment)

print ("problem students num is     ",num_problem_students)

udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']=='True':
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagements = remove_udacity_accounts(daily_engagements)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print(len(non_udacity_enrollments))
print(len(non_udacity_engagements))
print(len(non_udacity_submissions))

paid_students = {}
for enrollment in non_udacity_enrollments:
    if  not enrollment['is_canceled'] : #or int(enrollment['days_to_cancel']) > 7
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
           paid_students[account_key] = enrollment_date
print("paid student is ",len(paid_students))

def remove_free_trial_cancels(data):
    new_data=[]
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagements = remove_free_trial_cancels(non_udacity_engagements)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print (len(paid_enrollments))
print(len(paid_engagements))
print(len(paid_submissions))

paid_engagement_in_first_week =[]
for engagement_record in paid_engagements:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']
    if within_one_week(join_date,engagement_record):
        paid_engagement_in_first_week.append(engagement_record)

print("first week",len(paid_engagement_in_first_week))

engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)

total_minutes_by_Account ={}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_Account[account_key] = total_minutes

total_minutes =  total_minutes_by_Account.values()
# print("Mean ",np.mean(total_minutes))
# print("Standard deviation ",np.std(total_minutes))
# print("Minimum ", np.min(total_minutes))
# print("Maximum ",np.maximum(total_minutes))

student_with_max_minutes = None
max_minutes = 0
for student, total_minutes in total_minutes_by_Account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes  = student

print(max_minutes)

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        print (engagement_record)