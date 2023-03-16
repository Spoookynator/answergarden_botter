import random
from Globals import settings
from web_agent import fill_out
from tqdm import tqdm
import os.path
import concurrent.futures
from concurrent.futures import as_completed


def c_help():
    print(f'List of available commands: ')
    print(f'| help')
    print(f'| exit')
    print(f'| content <word> <word> ... - replace word list with')
    print(f'| add <word> <word> ... - add to word list')
    print(f'| id <session_id>')
    print(f'| settings')
    print(f'| random <min> <max>')
    print(f'| count <number>')
    print(f'| start')
    print(f'| import <path to file>')


def c_exit():
    print('Exiting Program...')


def c_set_content(*args):

    content = ""
    for i in range(len(args)):
        content += args[i]
        if i != len(args) - 1:
            content += " "

    if 20 < len(content) < 41:
        print("Warning| content length is over 20, some answergardens may not accept this answer!")
    elif len(content) > 40:
        print("Error| content over 40 chars longs, no answergarden will accept. Please choose another phrase!")
        return
    settings.content = content
    print(f'Content to search set to "{content}"')


def c_contents(*args):
    content = ""
    for i in range(len(args)):
        content += args[i]
        if i != len(args) - 1:
            content += " "

    if 20 < len(content) < 41:
        print("Warning| content length is over 20, some answergardens may not accept this answer!")
    elif len(content) > 40:
        print("Error| content over 40 chars longs, no answergarden will accept. Please choose another phrase!")
        return
    if settings.contents[0] == 'NULL':
        settings.contents = [content]
        print(f'Content to search set to "{content}"')
    else:
        settings.contents.append(content)
        print(f'Added "{content}" to contents')


def c_random(minimum, maximum):

    random_int = random.randint(int(minimum), int(maximum))
    settings.number_of_answers = random_int
    print(f'Random number of answers set to {random_int}')


def c_session_id(user_id):
    settings.session_id = user_id
    print(f'Session ID set to {user_id}')


def c_current_settings():
    print(f'Current word: {settings.contents}')
    print(f'Current number of answers: {settings.number_of_answers}')
    print(f'Current constant base-URL: {settings.BASE_URL}')
    print(f'Current session id: {settings.session_id}')


def c_start():

    base_url = settings.BASE_URL
    session_id = settings.session_id
    contents = settings.contents
    count = settings.number_of_answers

    threads = min(len(contents), 30)
    if contents[0] == 'NULL' or session_id == 'NULL':
        print('Please fill out all details')
        return

    with tqdm(total=len(contents) * count, colour='white') as progress_bar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(thread_start, content, count, session_id, base_url, progress_bar) for content in contents]

            # as_completed makes sure the bar only updates once the thread closes
            # for future in as_completed(futures):
            #    progress_bar.update(1)


def thread_start(content, count, session_id, base_url, progress_bar):
    for i in range(count):
        fill_out(content, session_id, base_url)
        progress_bar.update(1)


def c_submissions(number):
    settings.number_of_answers = int(number)
    print(f'Set number of answers to {number}')


def c_import(filepath):
    if os.path.exists(filepath):
        answer = input("This will overwrite all currently selected content. Continue (Y)es (N)o")
        if answer == 'Y' or answer == 'y':
            with open(filepath, "r") as r:
                settings.contents = r.read().splitlines()
                print('Saved!')
        else:
            print('Aborted!')
    else:
        print(f'File at "{filepath}" not found!')
