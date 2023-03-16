from Interface.commands import *


command_list = {
    'help': c_help,
    'exit': c_exit,
    'content': c_set_content,
    'add': c_contents,
    'random': c_random,
    'settings': c_current_settings,
    'id': c_session_id,
    'start': c_start,
    'count': c_submissions,
    'import': c_import

}
