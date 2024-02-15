#!/usr/bin/python3
'''Maria and Ben are playing a game. Given a list of integers,
they are taking turns choosing a prime number from the list
and removing all its multiples. The player who
cannot choose a prime number anymore loses the game.
Maria always starts first. Write a function to determine
the winner of the game. If Maria wins, return "Maria";
if Ben wins, return "Ben"; if the game is a draw, return None.'''

def isWinner(x, nums):
    '''Returns the winner of the game.'''
    if x < 1 or not nums:
        return None

    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False

        for num in range(2, int(limit**0.5) + 1):
            if primes[num]:
                for multiple in range(num*num, limit+1, num):
                    primes[multiple] = False

        return primes

    def optimal_move(nums):
        for num in nums:
            if primes[num]:
                return num
        return None

    most_wins = 0
    winner = None

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        numbers = list(range(1, n + 1))
        current_player = "Maria"
        maria_wins = 0
        ben_wins = 0

        while numbers:
            prime_to_remove = optimal_move(numbers)
            if prime_to_remove is None:
                break

            multiples_to_remove = [num for num in numbers if num % prime_to_remove == 0]
            numbers = [num for num in numbers if num not in multiples_to_remove]

            if current_player == "Maria":
                maria_wins += 1
            else:
                ben_wins += 1

            current_player = "Ben" if current_player == "Maria" else "Maria"

        round_winner = "Maria" if maria_wins > ben_wins else "Ben"
        if round_winner == "Maria":
            most_wins += 1

    if most_wins == 0:
        return None
    return "Maria" if most_wins > x // 2 else "Ben"

# Example usage:
# print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
