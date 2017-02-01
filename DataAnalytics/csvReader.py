import unicodecsv

enrollments_filename = '/Users/Rashmi/Desktop/Data Analysis/enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

def read_csv(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

# with open(enrollments_filename, 'rb') as f:
#     reader = unicodecsv.DictReader(f)
#     enrollments = list(reader)

### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.

engagement_filename = '/Users/Rashmi/Desktop/Data Analysis/daily_engagement.csv'
submissions_filename = '/Users/Rashmi/Desktop/Data Analysis/project_submissions.csv'

enrollments = read_csv(enrollments_filename)
daily_engagement  = read_csv(engagement_filename)
project_submissions = read_csv(submissions_filename)

# with open(engagement_filename,'rb') as f:
#     reader = unicodecsv.DictReader(f)
#     daily_engagement = list(reader)
# with open(submissions_filename,'rb') as f:
#     reader = unicodecsv.DictReader(f)
#     project_submissions = list(reader)

print (enrollments[0])
print (daily_engagement[0])
print (project_submissions[0])

