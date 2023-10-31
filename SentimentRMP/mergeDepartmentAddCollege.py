import pandas as pd

def mergeColumns(csv1, csv2):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    merged_df = df1.merge(df2[['ID', 'Department']], left_on='InstructorID', right_on='ID', how='left')

    # Drop the 'ID' column, as it's no longer needed
    merged_df = merged_df.drop('ID_y', axis=1)

    df_list = merged_df.columns.tolist()
    df_list.insert(2, 'Department')
    merged_df = merged_df[df_list]

    merged_df = merged_df.to_csv('FinalTableWithDepartment.csv', index=False)

finalMapping = r"C:\Users\parki\Downloads\SentimentRMP\FinalTableRatings+Sentiment+Mapping.csv"
instructor = r"C:\Users\parki\Downloads\SentimentRMP\SentimentRMP\instructor.CSV"
# mergeColumns(finalMapping, instructor)

def addCollege(csv):
    df = pd.read_csv(csv)
    df['College'] = ''

    for index, row in df.iterrows():
        if row['Department'] in ['Art', 'Dance', 'Design', 'Film and Electronic Arts', 'Music or "Theatre Arts', 'Theater', 'Film', 'Music', 'Art History']:
             df.at[index, 'College'] = 'College of the Arts'
        if row['Department'] in ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management and Human Resource Management', 'Marketing', 'Human Resources Management']:
             df.at[index, 'College'] = 'College of Business'
        if row['Department'] in ['Advanced Studies in Education and Counseling', 'Educational Leadership', 'Liberal Studies', 'Single Subject Teacher Education', 'Teacher Education', 'Educational Psychology', 'Education']:
             df.at[index, 'College'] = 'College of Education'
        if row['Department'] in ['Biomedical Engineering', 'Chemical Engineering', 'Civil Engineering and Construction Engineering Management', 'Computer Engineering & Computer Science', 'Civil Engineering', 'Construction', 'Electrical Engineering', 'Mechanical Engineering', 'Mech. & Aerospace Engineering']:
             df.at[index, 'College'] = 'College of Engineering'
        if row['Department'] in ['Child Development', 'Child & Family Studies', 'Consumer Affairs', 'Criminal Justice', 'Health & Human Services', 'Family  Consumer Science', 'Fashion', 'Food Science', 'Gerontology', 'Health Care Administration', 'Health Science', 'Hospitality', 'Kinesiology', 'Military Science', 'Nursing', 'Nutrition', 'Physical Ed', 'Public Policy', 'Public Administration', 'Recreation', 'Social Work']:
             df.at[index, 'College'] = 'College of Health and Human Services'
        if row['Department'] in ['African Studies', 'African-American Studies', 'American Indian Studies', 'American Studies', 'Asian American Studies', 'Asian Studies', 'Anthropology', 'Chicano Studies', 'Chicano Latino Studies', 'Chinese', 'Classics', 'Communication', 'Communication Studies', 'Comparative Literature', 'Literature', 'Economics', 'English', 'Environmental Science', 'French', 'Geography', 'German', 'History', 'Human Development', 'International Studies', 'Italian', 'Japanese', 'Journalism', 'Linguistics', 'Philosophy', 'Political Science', 'Psychology', 'Religious Studies', 'Russian', 'Sociology', 'Spanish', 'Translation', "Women's Studies", 'Health Science/Womens, Gender & Sexuality Studies']:
             df.at[index, 'College'] = 'College of Liberal Arts'
        if row['Department'] in ['Biological Sciences', 'Chemistry', 'Biochemistry', 'Geology', 'Mathematics', 'Physics', 'Physics & Astronomy', 'Astronomy', 'Science Education']:
             df.at[index, 'College'] = 'College of Natural Sciences and Mathematics'



    df_list = df.columns.tolist()
    df_list.insert(3, 'College')
    df = df[df_list]

    df = df.to_csv('FinalTablewithDepartmentCollege.csv', index=False)
        
addCollege(r"C:\Users\parki\Downloads\SentimentRMP\FinalTableWithDepartment.csv")

