# 错误处理
def main():
    try:
        configuration = open("config.txt")
    except FileNotFoundError as error:
        if error.errno == 2:
            print("Couldn't find the config.txt file!")
        elif error.errno == 13:
            print("Found config.txt but couldn't read it")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")


if __name__ == "__main__":
    main()
