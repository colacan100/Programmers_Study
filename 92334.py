def solution(id_list, report, k):
    report = set(report)
    answer_dict = {ans:0 for ans in id_list}
    report_dict = {rep:0 for rep in id_list}

    for i in report:
        report_dict[i.split()[1]] += 1

    for j in report:
        if report_dict[j.split()[1]] >= k :
            answer_dict[j.split()[0]] += 1

    answer = list(answer_dict.values())
    print(answer)
    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)