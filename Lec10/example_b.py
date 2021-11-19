# Задача E. Староста

n_days = int(input())
total_set = set()

for day in range(n_days):
    m_students_in_this_day = int(input())
    set_students_in_ths_day = set()

    for _ in range(m_students_in_this_day):
        student = input()
        set_students_in_ths_day.add(student)
    
    if day == 0:
        total_set = total_set.union(set_students_in_ths_day)
    else:
        ...

# Дописать
