#!/usr/bin/python3
'''Maria and Ben are playing a game. Given a list of integers,
they are taking turns choosing a prime number from the list
and removing all its multiples. The player who
cannot choose a prime number anymore loses the game.
Maria always starts first. Write a function to determine
the winner of the game. If Maria wins, return "Maria";
if Ben wins, return "Ben"; if the game is a draw, return None.'''

def isWinner(x, nums):
    '''Returns the winner of the game 
    based on the list of integers'''
    def sieve_of_eratosthenes(limit):
        primes = []
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        for num in range(2, int(limit**0.5) + 1):
            if is_prime[num]:
                primes.append(num)
                for multiple in range(num*num, limit+1, num):
                    is_prime[multiple] = False

        for num in range(int(limit**0.5) + 1, limit + 1):
            if is_prime[num]:
                primes.append(num)

        return primes

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def optimal_move(nums):
        for num in nums:
            if is_prime(num):
                return num
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        numbers = list(range(1, n + 1))
        current_player = "Maria"

        while numbers:
            prime_to_remove = optimal_move(numbers)
            if prime_to_remove is None:
                break  # No prime number left to choose, the other player wins
            multiples_to_remove = [num for num in numbers if num % prime_to_remove == 0]
            numbers = [num for num in numbers if num not in multiples_to_remove]

            # Switch players
            current_player = "Ben" if current_player == "Maria" else "Maria"

        # Determine the winner based on the last move
        if current_player == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

