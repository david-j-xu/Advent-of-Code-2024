with open("input.txt") as f:
    reports = [list(map(int, line[:-1].split(" "))) for line in f.readlines()]                
    safe = 0
    for report in reports:
        diffs = []
        for i in range(len(report) - 1):
            diffs.append(report[i] - report[i + 1])
        good = (all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])) and all([abs(diff) <= 3 for diff in diffs])
        safe += 1 if good else 0
            
    print(safe)

    safe = 0
    for report in reports:
        diffs = []
        for i in range(len(report) - 1):
            diffs.append(report[i] - report[i + 1])
        good = (all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])) and all([abs(diff) <= 3 for diff in diffs])
        if not good:
            for i in range(len(report)):
                new_report = report[0:i] + report[i + 1:]
                diffs = []
                for i in range(len(new_report) - 1):
                    diffs.append(new_report[i] - new_report[i + 1])
                if (all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])) and all([abs(diff) <= 3 for diff in diffs]):
                    good = True
        if good:
            safe += 1
    print(safe)