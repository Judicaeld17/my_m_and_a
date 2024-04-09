def clean_gender(x):
    if x == "0" or x=="M":
        x="Male"
    elif x=="1" or x=="F":
        x="Female"
    return x  
def check_string_column(column_data):
    dirty_value={}
    for index,value in column_data.items():
        if not isinstance(value,str) or not value.isalpha():
            dirty_value[index]=value
    if dirty_value:
        return dirty_value,f'This column contains {len(dirty_value)} dirty values'
    else: 
        return "Column is clean"
def check_numerical_column(column_data):
    dirty_value={}
    for index,value in column_data.items():
        if not isinstance(value,(int)):
            dirty_value[index]=value
    if dirty_value:
        return dirty_value,f'This column contains {len(dirty_value)} dirty values'
    else: 
        return "Column is clean"
def clean_name(name):
    if isinstance(name,str):
        return name.replace("\\","").replace('"',"").title()
def clean_city(city):
    if isinstance(city,str):
        return city.replace("-"," ").replace("_"," ").title()
def clean_age(age):
    if isinstance(age,str):
        return age.replace("yo","").replace("year","").replace("years","").replace("s","").replace("integer_","").replace('"',"")
def clean_gender_tab3(x):
    if x == "string_Male" or x=="boolean_0" or x=="character_M":
        x="Male"
    elif x=="string_Female" or x=="boolean_1":
        x="Female"
    return x
def replace_string_(column_data):
    if isinstance(column_data,str):
        return column_data.replace("string_","")
    
    