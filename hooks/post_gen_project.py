import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

author = "{{ cookiecutter.author }}"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository ...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'config', '--local', 'user.name', '"{{ cookiecutter.git_username }}"'])
subprocess.call(['git', 'config', '--local', 'user.email', '"{{ cookiecutter.git_email}}"'])
subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beggining of your project is defined now!\nBye {author}!{RESET_ALL}")
