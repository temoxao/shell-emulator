import os
username = os.environ["USER"]
hostname = os.uname().nodename
prompt = f"{username}@{hostname}:~$ "
while True:
    command = input(prompt)
    parts = command.split()
    expanded_parts = [os.path.expandvars(part) for part in parts]
    if len(expanded_parts) != 0 and expanded_parts[0] == "ls":
        print(*expanded_parts)
    if len(expanded_parts) != 0 and expanded_parts[0] == "cd":
        print(*expanded_parts)
    if len(expanded_parts) != 0 and expanded_parts[0] == "exit":
        break
    if len(expanded_parts) != 0 and expanded_parts[0] not in ["ls", "cd", "exit"]:
        print(f"Unknown command: {expanded_parts[0]}")
