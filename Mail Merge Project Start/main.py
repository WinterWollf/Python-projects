with open("Input/Letters/starting_letter.txt", mode='r') as letter:
    lines = letter.readlines()
    with open("Input/Names/invited_names.txt", mode='r') as guests_list:
        for name in guests_list:
            guest = name.strip()
            with open(f"Output/ReadyToSend/{guest}.txt", mode='w') as invitation:
                for line in lines:
                    invitation.write(line.replace("[name]", f"{guest}"))
