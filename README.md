
# Answergarden Botter

This is a small program I wrote that can autonomously submit any amount of words to the answergarden.

## How to install

1. Download the [Answergarden Botter.exe](https://github.com/Spoookynator/answergarden_botter/tree/main/dist) file in the dist directory
1. Create a new directory on your local machine. You can give it any name you want!
1. Now put the .exe into this folder and that's it!

---

## Note: You might need to add a firewall exception to let the program send outbound information!

- On Windows type "firewall" into the search bar
- Go to `Advanced Settings`
- Now right click the tab `Outbound Rules` and press `New Rule`
- Choose `Program` then click `Next`.
- Now paste the path to the .exe into the field and click `Next`.
- Finally choose `Allow Connection` and you're done!

---

## How to use

Just open the executable and type `help` to get a list of all commands.

---

What you need:

- The id of the session
- At least one word to be submitted

---

- type `id <number>` to select the session ID. You will find at the end of the link: `https://answergarden.ch/<number>`.
- type `content <word/sentence>` to set the word/sentence to be spammed. Be careful, this will replace all other stored words/sentences!
- type `add <word/sentence>` to add a word/sentence to the list.
- type `count <number>` to set the number of times the word/sentence is to be spammed.
- type `start` to start the program

---

You can also import words/sentences from a file. This file needs to be formatted with no header and one word/sentence per line.

Use `import <path to file>` to import this file. This will replace all other stored words/sentences.

---

# List of all commands

- `help` displays list of commands and information about them.
- `exit` exits the program
- `id <session id>` set the session id of the answergarden
- `content <word/sentence>` set the content to be spammed, will replace all currently stored contents
- `add <word/sentence>` adds content to list
- `count <number>` set number of times words should be spammed
- `random <min> <max>` chooses a random number of times the word will be spammed
- `import <path to file>` will import words/sentences from file. File has to have no hader and one word/sentence per line.
- `settings` displays currently selected ID, words, and count
