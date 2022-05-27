import faker


fake = faker.Faker()

DUMMY_DATA_NUMBER = 30;
TABLE_NAME = "executive";
TABLE_COLUMNS = ["name"]
content = "";



for _ in range(DUMMY_DATA_NUMBER):
    
    name = fake.unique.first_name()
    
    content += f'INSERT INTO {TABLE_NAME} ({",".join(TABLE_COLUMNS)}) VALUES ("{name}");\n'

with open(f"dummy_data_{TABLE_NAME}.txt", 'w') as f:
    f.write(content)