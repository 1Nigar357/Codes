def main():
    text = convert(input())
    print(text)


def convert(text):
    text = text.replace(":(", "🙁")
    text = text.replace(":)", "🙂")
    return text

main()