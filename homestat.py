#!/usr/bin/env python3

from collections import Counter
import operator

female_name = ('Анна', 'Алиса', 'Полина', 'Татьяна',
               'Юлия', 'Кристина', 'Мария', 'Ольга',
               'Ксения', 'Надежда', 'Елена')
male_name = ('Дмитрий', 'Кирилл', 'Алехандро',
             'Виктор', 'Александр', 'Сергей',
             'Андрей')


def name_gender(full_name):
    surname = full_name.split()[0]
    name = full_name.split()[1]

    if name in female_name:
        return name, 'female'
    elif (surname[-1:] == 'а' or surname[-2:] == 'ая') and\
            name not in male_name:
        return name, 'female'

    return name, 'male'


def get_all_data(stat):
    all_data = []

    for year, data in stat.items():
        all_data += data

    return all_data


def sorted_data(data):
    return sorted(dict(Counter(data)).items(),
                  key=operator.itemgetter(1),
                  reverse=True)


def calc_stat(data):
    res = []
    sort_data = sorted_data(data)

    for info, count in sort_data:
        res.append((info[0], count))

    return res


def calc_stat_by_gender(data, gender):
    res = []
    sort_data = sorted_data(data)

    for info, count in sort_data:
        if info[1] == gender:
            res.append((info[0], count))

    return res


def make_stat(filename):
    """
    Функция вычисляет статистику по именам за каждый год с учётом пола.
    """
    with open(filename, 'r', encoding='windows-1251') as file:
        lines = file.readlines()

    dictionary = {}
    year = ''

    for line in lines:
        begin_name = line.find('/>') + 2
        end_name = line.find('</a')
        begin_year = line.find('<h3>') + 4
        end_year = line.find('</h3>')

        if begin_year != -1 and end_year != -1:
            year = line[begin_year:end_year]
            dictionary[year] = []
            continue

        if begin_name != -1 and end_name != -1 and \
                year != '':
            name = line[begin_name:end_name]
            dictionary[year].append(name_gender(name))

    return dictionary


def extract_years(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список годов,
    упорядоченный по возрастанию.
    """
    years = list(stat.keys())
    years.sort()

    return years


def extract_general(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для всех имён.
    Список должен быть отсортирован по убыванию количества.
    """
    all_data = get_all_data(stat)

    return calc_stat(all_data)


def extract_general_male(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён мальчиков.
    Список должен быть отсортирован по убыванию количества.
    """
    all_data = get_all_data(stat)

    return calc_stat_by_gender(all_data, 'male')


def extract_general_female(stat):
    """
    Функция принимает на вход вычисленную статистику и выдаёт список tuple'ов
    (имя, количество) общей статистики для имён девочек.
    Список должен быть отсортирован по убыванию количества.
    """
    all_data = get_all_data(stat)

    return calc_stat_by_gender(all_data, 'female')


def extract_year(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    return calc_stat(stat[year])


def extract_year_male(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён мальчиков в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    return calc_stat_by_gender(stat[year], 'male')


def extract_year_female(stat, year):
    """
    Функция принимает на вход вычисленную статистику и год.
    Результат — список tuple'ов (имя, количество) общей статистики для всех
    имён девочек в указанном году.
    Список должен быть отсортирован по убыванию количества.
    """
    return calc_stat_by_gender(stat[year], 'female')


if __name__ == '__main__':
    pass
