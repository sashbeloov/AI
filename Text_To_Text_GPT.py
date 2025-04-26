import tiktoken

def analyze_tokenization(text):
    tokenizer = tiktoken.get_encoding("gpt2")
    tokens = tokenizer.encode(text)
    print(f"res: {tokens}")
    parts = [tokenizer.decode([t]) for t in tokens]

    print(f"Text: {text}")
    print(f"Tokens: {tokens}")
    print(f"Parts: {parts}")
    print(f"{'-'*30}")


analyze_tokenization("cryptocurrency")
analyze_tokenization("blockchain")
analyze_tokenization("unbelievable")

# tokenizer = tiktoken.get_encoding("gpt2")
#
# text1 = "Hello world"
# tokens1 = tokenizer.encode(text1)
# print(tokens1) # [15496, 995]
#
# text2 = "unbelievable"
# tokens2 = tokenizer.encode(text2)
# print(tokens2)  #[403, 6667, 11203, 540]