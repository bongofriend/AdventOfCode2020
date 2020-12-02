from os import path

class PasswordPolicy():
    _policy: str
    _password: str
    _char: str

    def __init__(self, policy: str, password: str, char: str):
        self._policy = policy
        self._password = password
        self._char = char
    
    def is_policy_valid_problem_1(self) -> bool:
        [lower, upper] = map(lambda x: int(x), self._policy.split('-'))
        char_occurence = self._password.count(self._char)
        return char_occurence <= upper and char_occurence >= lower
    
    def is_policy_valid_problem_2(self) -> bool:
        [first, second] = map(lambda x: int(x), self._policy.split('-'))
        return bool(self._password[first-1] == self._char) ^ bool(self._password[second-1] == self._char)


def line_to_password_policy(line: str) -> PasswordPolicy:
    [policy, char, password] = [x.strip() for x in line.split(' ')]
    return PasswordPolicy(policy, password, char.replace(':', ''))

def problem_1() -> int:
    cur_dir = path.dirname(path.abspath(__file__))
    with open(path.join(cur_dir, 'passwords.txt'), 'r') as f:
        lines = f.readlines()
        passwords = list(map(line_to_password_policy, lines))
        return len(list(filter(lambda p: p.is_policy_valid_problem_1(), passwords)))

def problem_2() -> int:
    cur_dir = path.dirname(path.abspath(__file__))
    with open(path.join(cur_dir, 'passwords.txt'), 'r') as f:
        lines = f.readlines()
        passwords = list(map(line_to_password_policy, lines))
        return len(list(filter(lambda p: p.is_policy_valid_problem_2(), passwords)))

print(f'Solution for Problem 1: {problem_1()}')
print(f'Solution for Problem 2: {problem_2()}')

