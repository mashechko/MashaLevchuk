class Matrix:
    def __init__(self, n=None, m=None, a=None, b=None):
        if not n:
            self.data = [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        else:
            import random
            data = []
            for _ in range(n):
                line = []
                for _ in range(m):
                    line.append(random.randint(a, b))
                data.append(line)
            self.data = data

    def __str__(self):
        pass