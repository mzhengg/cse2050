def converter(p):
    p_start = p[0][0]
    p_end = p[len(p)-1][0]
    p_hourly = []
    k = 1
    for t in range(p_start, p_end+1):
        if t < p[k][0]:
            wage = p[k-1][1]
        else:
            k += 1
            wage = p[k-1][1]
        p_hourly.append((t, wage))
    return p_hourly
    
def merge_plannings(p1, p2):
    if len(p1) < 2 or len(p2) < 2: return
    L = []

    p1_hourly = converter(p1)
    p2_hourly = converter(p2)

    i, j = 0, 0
    wage = 0
    while i < len(p1_hourly) or j < len(p2_hourly):
        if i == len(p1_hourly) and j < len(p2_hourly):
            p2_time = p2_hourly[j][0]
            p2_wage = p2_hourly[j][1]

            if p2_wage != wage:
                L.append(p2_hourly[j])
                wage = p2_wage
            j += 1

        if i < len(p1_hourly) and j == len(p2_hourly):
            p1_time = p1_hourly[i][0]
            p1_wage = p1_hourly[i][1]

            if p1_wage != wage:
                L.append(p1_hourly[i])
                wage = p1_wage
            i += 1

        if i < len(p1_hourly) and j < len(p2_hourly):
            p1_time = p1_hourly[i][0]
            p1_wage = p1_hourly[i][1]
            p2_time = p2_hourly[j][0]
            p2_wage = p2_hourly[j][1]

            if p1_time < p2_time:
                if p1_wage > wage:
                    L.append(p1_hourly[i])
                    wage = p1_wage
                i += 1
                continue

            if p2_time < p1_time:
                if p2_wage > wage:
                    L.append(p2_hourly[j])
                    wage = p2_wage
                j += 1
                continue

            if p1_time == p2_time:
                if p1_wage > p2_wage and p1_wage != wage:
                    L.append(p1_hourly[i])
                    wage = p1_wage
                elif p2_wage > p1_wage and p2_wage != wage:
                    L.append(p2_hourly[j])
                    wage = p2_wage
                i += 1
                j += 1
                continue

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
        
if __name__ == '__main__':
    first_planning = [(2, 4), (5, 0), (6, 3), (10, 0)]
    second_planning = [(3, 5), (7, 0), (9, 2), (13, 0)]
    merged = [(2, 4), (3, 5), (7, 3), (10, 2), (13, 0)]
    res_merge = merge_plannings(first_planning, second_planning)
    assert(res_merge == merged)

    jobs_offers = [(2, 8, 3), (5, 7, 5)]
    optimal = [(2, 3), (5, 5), (7, 3), (8, 0)]
    res_planning = optimal_planning(jobs_offers)
    assert(res_planning == optimal)

    n = 50000
    many_jobs = [(2 * i, 2 * i + 1, i) for i in range(n)]
    long_planning = optimal_planning(many_jobs)