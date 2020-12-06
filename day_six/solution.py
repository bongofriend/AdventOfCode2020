from os import path

def count_answers_part_1(answers: list) -> int:
    count = 0
    current_answers = set()
    for l in answers:
        if l == "":
            count += len(current_answers)
            current_answers.clear()
        for a in l:
            current_answers.add(a)
    if len(current_answers) > 0:
        count += len(current_answers)
    return count

def count_answers_part_2(answers: list) -> int:
    group_member_count = 0
    current_answers = dict()
    count = 0
    for l in answers:
        if l == "":
            count += count_group_answers(current_answers, group_member_count)
            group_member_count = 0
            current_answers.clear()
        else:
            group_member_count += 1
            for a in l:
                if a in current_answers.keys():
                    current_answers[a] = current_answers[a] + 1
                else:
                    current_answers[a] = 1
    if len(current_answers) > 0:
        count += count_group_answers(current_answers, group_member_count)
    return count

def count_group_answers(answers: dict, member_count: int) -> int:
    count = 0
    for value in answers.values():
        if value == member_count:
            count += 1
    return count
       

current_dir = path.dirname(path.abspath(__file__))
with open(path.join(current_dir, "answers.txt"), "r") as f:
    answers = [l.rstrip() for l in f.readlines()]
    print(count_group_answers_part_1(answers))
    print(count_answers_part_2(answers))
