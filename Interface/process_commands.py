from Interface.command_lookup import command_list


def get_user_input():
    user_input = input()
    user_input.strip()
    if user_input.isspace():
        return 'NULL'
    return user_input


def process(line):
    cmd, *args = line.split()
    try:
        return command_list[cmd](*args)
    except Exception:
        return False


def wait_for_valid_command():
    user_input = get_user_input()

    while process(user_input) == False:
        print(f'\"{user_input}\" is not a valid command!')
        user_input = get_user_input()

    return user_input