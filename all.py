from email import contentmanager
from pickle import NONE
import faker


fake = faker.Faker()

DUMMY_DATA_NUMBER = 100;
TABLE_NAME = "researchers";
TABLE_COLUMNS = ["id", "first_name", "last_name","sex","birthdate","org_name","works_since","age"]
content_researchers = "";
content_org = "";
content_rc= "";
content_uni="";
content_c="";
content_phone = "";

def get_initials(fullname):
  xs = (fullname)
  name_list = xs.split()

  initials = ""

  for name in name_list:  # go through each name
    initials += name[0].upper()  # append the initial

  return initials

# for organization with phone, research center, company and uni

for _ in range(30):
        
    name_org= fake.unique.company()
    initials= get_initials(name_org)
    postal_code=  fake.postcode()
    street=fake.street_name()
    city= fake.city()
    phone= fake.random_number(10)
    
    content_org += f'INSERT INTO {"organization"} ({",".join(["name","initials","postal_code","street","city"])}) VALUES ("{name_org}","{initials}","{postal_code}","{street}","{city}");\n'
    content_phone += f'INSERT INTO {"phone"} ({",".join(["name","phone"])}) VALUES ("{name_org}","{phone}");\n'
  # for research center
    if _%3==0 :
         name_rc = name_org
         budget_from_edu_rc= fake.random_number(7)
         budget_from_priv= fake.random_number(7)
    
         content_rc += f'INSERT INTO {"research_center"} ({",".join(["name","budget_from_edu","budget_from_priv"])}) VALUES ("{name_rc}","{budget_from_edu_rc}","{budget_from_priv}");\n'
  # for uni   
    elif _%3==1:  
        name_uni=name_org
        budget_from_edu_uni= fake.random_number(7)
        content_uni += f'INSERT INTO {"university"} ({",".join(["name","budget_from_edu","budget_from_priv"])}) VALUES ("{name_uni}","{budget_from_edu_uni}");\n'
  # for company
    else:
        name_comp=name_org
        equity= fake.random_number(7)
        content_c += f'INSERT INTO {"company"} ({",".join(["name","equity"])}) VALUES ("{name_comp}","{equity}");\n'

content_worksfor="";

#for scientific field

content_sf = "";

for _ in range(8):
    
    name = fake.unique.random_element(elements=('Physical science', 'Mathematics','Chemical sciences', 'Earth and related Environmental sciences','Biological science,', 'Nano-technology','Medical engineering', 'Electrical engineering'))
    
    content_sf += f'INSERT INTO {"scientific field"} ({",".join("name")}) VALUES ("{name}");\n'


#for project and deliverable and field that describes

content_ftd="";
content_project = "";
content_deliverable="";
for _ in range(50):
    
    title_project = fake.unique.catch_phrase()
    amount=  fake.random_number(8)
    summary= fake.paragraph(nb_sentences=2)
    start_date= fake.date()
    end_date= fake.date_between()
    name=fake.name()
    evaluated_from= fake.random_number(5)
    grade=fake.random_number(2)
    date_of_eval=fake.date_this_year()

    title_deliverable=fake.bs()
    summary= fake.paragraph(nb_sentences=2)
    
    due_date=fake.future_date()
    exec = fake.first_name()
    field= fake.random_element(elements=('Physical science', 'Mathematics','Chemical sciences', 'Earth and related Environmental sciences','Biological science,', 'Nano-technology','Medical engineering', 'Electrical engineering'))

    
    content_project += f'INSERT INTO {"project"} ({",".join(["title","amount","summary","start_date","end_date","duration","name","evaluated_from","from_org","grade","date_of_eval", "exec"])}) VALUES ("{title_project}","{amount}","{summary}","{start_date}","{end_date}","","PROG","{evaluated_from}","ORG","{grade}","{date_of_eval}","{exec}");\n'
    content_deliverable += f'INSERT INTO {"deliverable"} ({",".join(["title","summary","title_project","due_date"])}) VALUES ("{title_deliverable}","{summary}","{title_project}","{due_date}");\n'
    content_ftd += f'INSERT INTO {"fieldthatdescribes"} ({",".join(["name","title"])}) VALUES ("{field}","");\n'

# for researchers ands works for
for _ in range(100):
    sex =fake.random_element(elements=('M', 'F'))
    id = fake.unique.random_number(3)
    first_name= fake.first_name_male() if sex=="M" else fake.first_name_female()
    last_name = fake.last_name()
    
    birthdate= fake.date_of_birth(None,25,65)
    works_since= fake.date_between()
    content_researchers += f'INSERT INTO {"researchers"} ({",".join( ["id", "first_name", "last_name","sex","birthdate","name","works_since","age"])}) VALUES ("{id}","{first_name}", "{last_name}", "{sex}","{birthdate}","{name_org}" ,"{works_since}","" );\n'
    content_worksfor += f'INSERT INTO {"worksfor"} ({",".join( ["title", "id"])}) VALUES ("","{id}" );\n'



#for program
content_program = "";

for _ in range(30):
    
    name_program = fake.name()
    address_program= fake.address()
    
    
    content_program += f'INSERT INTO {"program"} ({",".join(["name","address"])}) VALUES ("{name_program}","{address_program}");\n'

with open(f"dummy_data.txt", 'w') as f:
    f.write(content_researchers)
    f.write(content_org)
    f.write(content_phone)
    f.write(content_rc)
    f.write(content_uni)
    f.write(content_c)
    f.write(content_sf)
    f.write(content_project)
    f.write(content_deliverable)
    f.write(content_program)
    f.write(content_worksfor)
    f.write(content_ftd)