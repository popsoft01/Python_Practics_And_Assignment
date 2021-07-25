import random


def article_function(article):
    return random.randint(0, len(article)-1)


# class sentence:
#     pass

art = ["the ", "a ", "one ", "some ", "any"]
print(article_function(art))
