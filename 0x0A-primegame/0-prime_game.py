#!/usr/bin/python3
"""
Task 0: Prime Game
"""


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    """
    def sieve(max_n):
        """
        generates all primes up to the maximum number in nums
        returns a list of primes and a boolean list indicating
        if an index is a prime
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        p = 2
        while p * p <= max_n:
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [i for i in range(max_n + 1) if is_prime[i]]
        return primes, is_prime

    def play_game(n, primes, is_prime):
        """
        simulates one round of the game
        """
        primes_set = set(primes)
        remaining = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while remaining:
            move_made = False
            for prime in primes:
                if prime in remaining:
                    multiples = set(range(prime, n + 1, prime))
                    remaining -= multiples
                    move_made = True
                    break
            if not move_made:
                return 1 - turn  # return the other player as the winner
            turn = 1 - turn  # switch turns

    max_n = max(nums)
    primes, is_prime = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes, is_prime)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
