# class BytePairEncoder:


text = """Vibe coding is an approach to producing software by using artificial intelligence (AI), where a person describes a problem in a few natural language sentences as a prompt to a large language model (LLM) tuned for coding. The LLM generates software based on the description, shifting the programmer's role from manual coding to guiding, testing, and refining the AI-generated source code.[1][2][3]

Advocates of vibe coding say that it allows even amateur programmers to produce software without the extensive training and skills required for software engineering.[4] Critics point out a lack of accountability and increased risk of introducing security vulnerabilities in the resulting software. The term was introduced by Andrej Karpathy in February 2025[2][4][1] and listed in the Merriam-Webster Dictionary the following month as a "slang & trending" term.[5]

Definition
Computer scientist Andrej Karpathy, a co-founder of OpenAI and former AI leader at Tesla, introduced the term vibe coding in February 2025. The concept refers to a coding approach that relies on LLMs, allowing programmers to generate working code by providing natural language descriptions rather than manually writing it.[1][2][4]

Karpathy described his approach as conversational, using voice commands while AI generates the actual code. "It's not really coding - I just see things, say things, run things, and copy-paste things, and it mostly works."[4] Karpathy acknowledged that vibe coding has limitations, noting that AI tools are not always able to fix or understand bugs, requiring him to experiment with unrelated changes until the problems are resolved.[2] He concluded that he found the technique "not too bad for throwaway weekend projects" and described it as "quite amusing".

The concept of vibe coding elaborates on Karpathy's claim from 2023 that "the hottest new programming language is English", meaning that the capabilities of LLMs were such that humans would no longer need to learn specific programming languages to command computers.[6]

A key part of the definition of vibe coding is that the user accepts code without full understanding.[1] Programmer Simon Willison said: "If an LLM wrote every line of your code, but you've reviewed, tested, and understood it all, that's not vibe coding in my book—that's using an LLM as a typing assistant."[1]
"""

print(len(text.split(" ")))

tokens = text.encode('utf-8')

ids = list(map(int, tokens))


def frequency_pair(ids):
    count = {}
    for i in range(len(ids)):
        if i < len(ids) - 1:
            pair = (ids[i], ids[i + 1])
            count[pair] = count.get(pair, 0) + 1

    return count

print(ids)
freq = frequency_pair(ids)

top_pair = max(freq, key=freq.get)

print(top_pair)

def merge(ids, pair, idx):
    new_ids = []
    i = 0
    while i < len(ids):
        a, b = pair
        if i < len(ids) - 1 and ids[i] == a and ids[i+1] == b:
            new_ids.append(idx)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids




vocab_size = 353
num_merges = vocab_size - 256
ids = list(tokens)


merges = {}
for i in range(num_merges):
    freq = frequency_pair(ids)

    top_pair = max(freq, key=freq.get)

    idx = 256 + i
    print(f"Merging: {top_pair} -> {idx}")
    ids = merge(ids, top_pair, idx)
    merges[top_pair] = idx


print(merges)


print(len(tokens))
print(len(ids))

print(len(tokens) / len(ids))


vocab = {idx: bytes([idx]) for idx in range(256)}
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]


print(vocab)

def decode(ids):
    token = b"".join(vocab[idx] for idx in ids)
    text = token.decode("utf-8", errors="replace")

    return text

def encode(text):
    tokens = list(text.encode("utf-8"))
    while len(tokens) >= 2:
        freq = frequency_pair(tokens)
        pair = min(freq, key=lambda p: merges.get(p, float('inf')))
        if pair not in merges:
            break 
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)

    return tokens
        

print(decode(ids))
print(decode(encode("help")))

text2 = decode(encode(text))
print(text == text2)