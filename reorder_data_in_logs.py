"""
https://leetcode.com/problems/reorder-data-in-log-files/submissions/
"""

# Builds two arrays, messes with one, then concats them. Time complexity is
# n x 2.
def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    digit_logs = []
    letter_logs = []

    for i, log in enumerate(logs):
        split_log = log.split(" ", 1)
        log_type = split_log[0]
        log_content = split_log[1]

        try:
            int(log_content[0])
            can_be_int = True
        except Exception:
            can_be_int = False

        if not can_be_int:
            letter_logs.append(log_content + " " + log_type)

        else:
            digit_logs.append(log)

    # Now we have a list where the log is on backwards...
    sorted_letter_logs = []
    for log in sorted(letter_logs):
        split_log = log.rsplit(" ", 1)
        log_type = split_log[1]
        log_content = split_log[0]
        sorted_letter_logs.append(log_type + " " + log_content)

    return sorted_letter_logs + digit_logs
