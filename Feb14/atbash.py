def atbash(given):
    decode = given.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                             "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA")

    answer = given.translate(decode)
    return print(answer)


atbash("apple")
atbash("Hello world!")
atbash("Christmas is the 25th of December")
