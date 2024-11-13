from utilz import capitalize_words, truncate


text = "hello world"

capitalized_text = capitalize_words(text)

print(capitalized_text)  # Output: "Hello World"


short_text = truncate(text, length=5)

print(short_text)  # Output: "hello..."
