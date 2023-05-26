def min_time(tasks):
    start_times = sorted(set(task[0] for task in tasks))
    end_times = sorted(set(task[1] for task in tasks))
    times = start_times + end_times
    times.sort()
    
    total_time = 0
    for i in range(len(times) - 1):
        start_time = times[i]
        end_time = times[i+1]
        duration = 0
        for task in tasks:
            if start_time < task[1] and end_time > task[0]:
                duration += min(end_time, task[1]) - max(start_time, task[0])
        if duration > 0:
            total_time += end_time - start_time
    
    return total_time



print(min_time([[2,3,1],[4,5,1],[1,5,2]]))