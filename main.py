ENTRY = "My alarm rang at 6 AM Saturday, chirpy as a coworker who doesn't know the office burned down."

assert 1 <= len(ENTRY) <= 200


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
