"""
This one was fun!

https://leetcode.com/problems/bulls-and-cows/submissions/
"""


def getHint(self, secret: str, guess: str) -> str:

    bulls = 0
    secret_wout_bulls = ""
    guess_wout_bulls = ""

    for i, letter in enumerate(secret):
        if secret[i] == guess[i]:
            bulls += 1

        else:
            secret_wout_bulls += letter
            guess_wout_bulls += guess[i]

    cows = 0

    for i, letter in enumerate(guess_wout_bulls):

        if letter in secret_wout_bulls:
            cows += 1
            secret_wout_bulls = secret_wout_bulls.replace(letter, "", 1)

    return f"{bulls}A{cows}B"
