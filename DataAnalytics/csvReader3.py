
import unicodecsv

enrollments_filename = '/Users/Rashmi/Desktop/Data Analysis/enrollments.csv'
daily_engagements = "/Users/Rashmi/Desktop/Data Analysis/daily_engagement.csv"
project_submissions = "/Users/Rashmi/Desktop/Data Analysis/project_submissions.csv"


def read_csv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)




enrollments = read_csv(enrollments_filename)
daily_engagement  = read_csv(daily_engagements)
project_submissions = read_csv(project_submissions)



udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)



def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagements = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)
print (len(non_udacity_enrollments))
print (len(non_udacity_engagements))
print (len(non_udacity_submissions))


paid_student = {}
for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] >7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if account_key not in paid_student or enrollment_date > paid_student[account_key]:
           paid_student[account_key] = enrollment_date
len(paid_student)