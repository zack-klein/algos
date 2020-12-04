class MovingAverage:
    def __init__(self, size: int):
        """
        We use a simple queue using Python built in lists.
        """
        self.size = size
        self.q = []

    def avg(self):
        return sum(self.q) / len(self.q)

    def next(self, val: int) -> float:

        if len(self.q) >= self.size:
            del self.q[0]

        self.q.append(val)

        return self.avg()
