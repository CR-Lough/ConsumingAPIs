import pandas as pd
from cerberus import Validator
from datetime import date, timedelta, datetime
v = Validator()

def to_date(s):
    return datetime.strptime(s, '%m/%d/%Y')

def add_new(df:pd.DataFrame) -> pd.DataFrame:
    v = Validator()

    schema = {
        'status_id':{"type":  ['float','integer'],"min": 1,"max": 999,'empty': False},
        'user_id':{"type": "string","minlength": 1,"maxlength": 50,'empty': False},
        'status_text':{"type": "string","minlength": 1,"maxlength": 100,'empty': False}
    }

    while v.validate({'name':(name := input('What is the employee\'s name?   '))},schema) is False:
        print('\nError! The name must be between 1 and 50 characters long.\n')
        print(v.errors)
    while v.validate({'address':(address := input('What is the employee\'s address?   '))},schema) is False:
        print('\nError! The address must be between 1 and 100 characters long.\n')
        print(v.errors)
    while v.validate({'ssn':(int(ssn := input('What is the employee\'s ssn?   ')))},schema) is False:
        print('\nError! The ssn must be between 100-000-0000 and 999-999-9999.\n')
        print(v.errors)

    new_row = {'employee_id':len(df.index), 'name':name, 'address':address}
    #append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    return df

def validate_payload(payload: dict):
    """
    validate payload against a Cerberus schema
    :param payload: payload to be validated
    :return: nothing
    """
    schema = {
        'STATUS_ID':{"type": "string","minlength": 1,"maxlength": 50, 'empty': False},
        'USER_ID':{"type": "string","minlength": 1,"maxlength": 50,'empty': False},
        'STATUS_TEXT':{"type": "string","minlength": 1,"maxlength": 100,'empty': False}
    }

    v = Validator()
    v.validate(payload, schema)
