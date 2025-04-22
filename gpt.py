import re
text = "Hello, students! How are you?"
tokens = re.split(r'([,.?!]|\s)', text)
print(tokens)
tokens = [token for token in tokens if token.strip()]
print(tokens)

tex = ['hello', 'world', 'hello', 'students']
unique_words = sorted(list(set(tex)))

dictionary = {word:number for number, word in enumerate(unique_words)}
print(dictionary)


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1',text)
        return text

vocab = {'hello':0, 'students':1, 'world':2}
tokenizer = SimpleTokenizerV1(vocab)

text = "hello world"
numbers = tokenizer.encode(text)
print(numbers)

new_text = tokenizer.decode(numbers)
print(new_text)

import re
text = "Hello, students! How are you?"
tokens = re.split(r'([,.?!]|\s)', text)
print(tokens)
tokens = [token for token in tokens if token.strip()]
print(tokens)

tex = ['hello', 'world', 'hello', 'students']
unique_words = sorted(list(set(tex)))

dictionary = {word:number for number, word in enumerate(unique_words)}
print(dictionary)


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return preprocessed,ids

vocab = {'hello':0, 'students':1, 'world':2,"<|unk|>":3}
tokenizer = SimpleTokenizerV2(vocab)

text = "hello dear world"
new_text, number = tokenizer.encode(text)
print(new_text)
# print(number)

class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return preprocessed,ids

vocab = {'hello':0, 'students':1, 'world':2,"<|unk|>":3, "pizza":4, "<|endoftext|>":5}
tokenizer = SimpleTokenizerV2(vocab)

text1 = "hello dear students"
text2 = "I like pizza and hachapuri"
full_text = text1 + " <|endoftext|> " + text2

new_text, number = tokenizer.encode(full_text)
print(new_text)
print(number)