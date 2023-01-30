#Turn your CV into code!
#Name: Viskha Ivonita
#E-Mail: viskha.ivonita@gmail.com
#Phone number: 0123456789
#list of education: Master German Literatur, Humboldt Universität Berlin; Bachelor German Literatur, Universitas Padjadjaran
#list of jobs: Customer Care, idealo GmbH, 2017-now; Retail Professional, Woma GmbH, 2014-2017
#list of skills: excellent communication skills, computer literacy, writing, creativity, empathy

name = 'Viskha Ivonita'
print(type(name))

email = 'viskha.ivonita@gmail.com'
print(type(email))

phonenumber = '+49 1234 56789'
print(type(phonenumber))
print(phonenumber)

list_of_education = ['Master German Literatur - Humboldt Universität zu Berlin', 'Bachelor German Literatur - Universitas Padjadjaran']
print(type(list_of_education))
# print(*list_of_education, sep=', ')
for hedu in list_of_education:
    print (hedu)

list_of_jobs = [
    { 'company': 'idealo GmbH', 'role': 'Customer Care', 'date': '2017 until now' },
    { 'company': 'Woma GmbH', 'role': 'retail professional', 'date': '2014 - 2017'}
]
print(type(list_of_jobs))


list_of_skills = ['excellent communication skills', 'computer literacy', 'writing', 'creativity', 'empathy']
print(type(list_of_skills))
# print(*list_of_skills, sep=', ')
for skill in list_of_skills:
    print(skill)



