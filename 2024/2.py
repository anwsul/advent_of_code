reports=[]
with open('./2.txt', 'r') as input:
    for line in input:
        reports.append(list(map(int, line.split())))


def calculate_safe_reports(reports):
    columns = len(reports)
    unsafe_count = 0

    for report in reports:
        _len = len(report)
        old_diff = 0

        for i in range(_len - 1):
            diff = report[i] - report[i+1]

            if diff == 0 or abs(diff) > 3 or diff * old_diff < 0:
                unsafe_count += 1
                break
            
            old_diff = diff
        
    safe_count = columns - unsafe_count
    print(safe_count)


def calculate_safe_reports_with_tolerance(reports):
    safe_count = 0

    for report in reports:
        safe_count += is_safe_report(report)
        
    print(safe_count)


def is_safe_report(report, tolerance_count=0):
    _len = len(report)    
    old_diff = 0

    for i in range(_len - 1):
        diff = report[i] - report[i+1]

        if diff == 0 or abs(diff) > 3 or diff * old_diff < 0:
            if tolerance_count != 0: 
                return False

            safe = False
            # check by removing the prev item in the report
            if i - 1 >= 0:
                new_report = report[:]
                new_report.pop(i - 1)
                safe = safe or is_safe_report(new_report, tolerance_count=1)
            
            if not safe:
                # check by removing the current item in the report
                new_report = report[:]
                new_report.pop(i)
                safe = safe or is_safe_report(new_report, tolerance_count=1)

            # check by removing the next item in the report
            if i + 1 < _len and not safe:
                new_report = report[:]
                new_report.pop(i + 1)
                safe = safe or is_safe_report(new_report, tolerance_count=1)
            
            return safe

        old_diff = diff
    
    return True


calculate_safe_reports(reports)
calculate_safe_reports_with_tolerance(reports)