# TODO Напишите функцию find_common_participants
def find_common_participants(first_list: str, second_list: str, separator=',') -> list:
    first_list = first_list.split(separator)
    second_list = second_list.split(separator)

    common_participants = list(set(first_list).intersection(second_list))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
