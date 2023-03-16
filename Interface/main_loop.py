from Interface.process_commands import wait_for_valid_command


def main_loop():
    running = True
    print(f'Botter version 1.0 loaded!')
    print(f'Please copy the session id (number) from the answergarden link!')
    print(f'Now add content to be sent by using "add" <word>')
    print(f'Lastly use "count" <number> to set the number of submissions')
    print(f'Type "help" for further information')
    print(f'Have fun :)')

    while running:
        return_value = wait_for_valid_command()
        if return_value == 'exit':
            running = False
