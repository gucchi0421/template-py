from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    hoge = ["hoge", "fuga"]

    for h in hoge:
        print(h)


if __name__ == "__main__":
    main()
