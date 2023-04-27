def return_correct_form(data):
    text = []
    second = data.split('\n')[1:]
    for i in second:
        if "Name" in i:
            a = i.split()[2:]
            text.append(a)
        elif "Email" in i:
            a = i.split()[2:]
            text.append(a)
        elif "Gender" in i:
            a = i.split()[1:]
            text.append(a)
        elif "Date" in i:
            a = i.replace(',', ' ').split()[3:]
            text.append(a)
        elif "Mobile" in i:
            a = i.split()[1:]
            text.append(a)
        elif "Subjects" in i:
            b = i.split(',')
            qw = []
            for j in range(len(b)):
                if j == 0:
                    qw.append(*b[j].split()[1:])
                else:
                    qw.append(b[j].strip())
            text.append(qw)
        elif "Hobbies" in i:
            a = i.split()[1:]
            text.append(a)
        elif "Picture" in i:
            a = i.split()[1:]
            text.append(a)
        elif "Picture" in i:
            a = i.split()[1:]
            text.append(a)
        elif "Address" in i:
            a = [' '.join(i.split()[1:])]
            text.append(a)
        elif "State" in i:
            a = i.split()[3:]
            text.append(a)
    return text
