"""
https://leetcode.com/problems/logger-rate-limiter/
"""


class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp,
        otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.messages:
            self.messages[message] = [timestamp]
            return True

        else:
            previous_timestamps = self.messages[message]
            max_allowed_timestamp = timestamp - 10
            max_timestamp = max(previous_timestamps)

            if max_timestamp > max_allowed_timestamp:
                return False

            previous_timestamps.append(timestamp)

            return True
