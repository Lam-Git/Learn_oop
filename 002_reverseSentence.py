class ReverseSentence:
    def __init__(
        self, sentence="Hello World, everything will be just fine."
    ):  # (objects)
        self.sentence = sentence

    def reverse(self):
        return " ".join(self.sentence.split(" ")[::-1])


if __name__ == "__main__":
    sentence = input("Please write your sentence: ")
    reverse_sentence = ReverseSentence(sentence)  # setting up the variable
    print(
        "The reversed sentence is: ", reverse_sentence.reverse()
    )  # this code take the instance method and the second instance

