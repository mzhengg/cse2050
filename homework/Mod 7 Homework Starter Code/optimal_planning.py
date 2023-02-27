def merge_plannings(p1, p2):
    L = []

    i, j = 0, 0
    p1_salary = 0
    p2_salary = 0
    cur_salary = 0

    while i < len(p1) and j < len(p2):
        if p1[i][0] < p2[j][0]:
            p1_salary = p1[i][1]
            max_salary = max(p1_salary, p2_salary)
            if max_salary != cur_salary:
                L.append((p1[i][0], max_salary))
                cur_salary = max_salary
            i += 1
        else:
            p2_salary = p2[j][1]
            max_salary = max(p1_salary, p2_salary)
            if max_salary != cur_salary:
                L.append((p2[j][0], max_salary))
                cur_salary = max_salary
            j += 1

    L += p1[i:] + p2[j:]
    return L

def optimal_planning(jobs):
    if len(jobs) == 0:
        return
    if len(jobs) == 1:
        start = jobs[0][0]
        end = jobs[0][1]
        wage = jobs[0][2]
        return [(start, wage), (end, 0)]
    
    middle = len(jobs) // 2
    left = optimal_planning(jobs[:middle])
    right = optimal_planning(jobs[middle:])

    return merge_plannings(left, right)



