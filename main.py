from utils import *

def main():
    '''Запускаем все функции по порядку:
    чтение файла,
    фильтр по исполненным операциям,
    сортировка по дате и выборка последних пяти операций,
    создание списка операций в необходимом формате для вывода.
    '''
    data = load_data()
    data = get_executed_operation(data)
    data = get_last_five_operations(data)
    data = get_total_information(data)
    '''Вывод самих операций с необходимыми данными'''
    for operation in data:
        print(operation)

if __name__ == '__main__':
    main()