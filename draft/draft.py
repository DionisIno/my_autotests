def return_correct_form(data):
    text1 = []
    second = data.split('\n')[1:]
    for i in second:
        if "Name" in i:
            a = i.split()[2:]
            text1.append(a)
        elif "Email" in i:
            a = i.split()[2:]
            text1.append(a)
        elif "Gender" in i:
            a = i.split()[1:]
            text1.append(a)
        elif "Date" in i:
            a = i.replace(',', ' ').split()[3:]
            text1.append(a)
        elif "Mobile" in i:
            a = i.split()[1:]
            text1.append(a)
        elif "Subjects" in i:
            b = i.split(',')
            qw = []
            for j in range(len(b)):
                if j == 0:
                    qw.append(*b[j].split()[1:])
                else:
                    qw.append(b[j].strip())
            text1.append(qw)
        elif "Hobbies" in i:
            a = i.split()[1:]
            text1.append(a)
        elif "Picture" in i:
            a = i.split()[1:]
            text1.append(a)
        elif "Picture" in i:
            a = i.split()[1:]
            text1.append(a)
        elif "Address" in i:
            a = [' '.join(i.split()[1:])]
            text1.append(a)
        elif "State" in i:
            a = i.split()[3:]
            text1.append(a)
    return text1


def convert_to_12h_format(time_24h):
    time_24h_parts = time_24h.split(':')
    hour = int(time_24h_parts[0])
    minute = time_24h_parts[1]
    am_pm = 'AM'
    if hour == 0:
        hour = 12
    elif hour >= 12:
        am_pm = 'PM'
        if hour > 12:
            hour -= 12
    return f"{hour}:{minute} {am_pm}"
