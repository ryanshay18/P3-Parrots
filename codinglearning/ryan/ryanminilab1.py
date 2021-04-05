
class ryanLab:
    def __init__(self, n):
        self._n = n
        self.primes = [2]
        a = 2

        while a < n:
            counter = 0

            for i in self.primes:
                if a % i == 0:
                    counter += 1

            if counter == 0:
                self.primes.append(a)
            else:
                counter = 0

            a = a + 1

    @property
    def get_n(self):
        return self._n

    @property
    def get_primes(self):
        return self.primes
