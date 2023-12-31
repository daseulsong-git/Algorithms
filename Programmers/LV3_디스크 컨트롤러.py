# https://school.programmers.co.kr/learn/courses/30/lessons/42627

def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x:x[1])

    while jobs :
        for i in range(0,len(jobs)):
            if start >= jobs[i][0] :
                start += jobs[i][1]
                answer += (start - jobs[i][0])
                jobs.pop(i)
                break

            if i == len(jobs)-1 :
                start += 1

    return answer // length