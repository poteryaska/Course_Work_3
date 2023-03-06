import json
from datetime import datetime

def load_data():
    '''Чтение файла со списком операций'''
    with open('operations.json', 'r', encoding='utf-8') as f:
        raw_json = f.read()
        operations = json.loads(raw_json)
    return operations


def get_executed_operation(operations):
    ''':return данные по исполненным("EXECUTED") операциям'''
    data = []
    for i in operations:
        if "state" in i and i["state"] == "EXECUTED":
            data.append(i)
    return data


def get_last_five_operations(data, last_days=5):
    ''':return сортированные по дате пять последних операций'''
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:last_days]

def get_total_information(data):
    ''':return список операций с данными в необходимом формате'''
    total_information = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = i["description"]
        if "from" in i:
            sender = i["from"].split()
            sender_card = sender.pop()
            payment_system = ''.join(sender)
            sender_account = f'{sender_card[:4]} {sender_card[4:6]}** **** {sender_card[-4:]}'
        else:
            payment_system = 'Aноним'
            sender_account = ''
        bene = i["to"].split()
        beneficiary_acc = bene.pop()
        bene_name = ''.join(bene)
        beneficiary_account = f'**{beneficiary_acc[-4:]}'
        amount = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
        total_information.append(f'{date} {description}\n{payment_system} {sender_account} -> {bene_name} {beneficiary_account}\n{amount}\n')
    return total_information




