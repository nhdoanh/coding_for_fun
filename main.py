import os


def find_sum(str1, str2):
    # Make sure l2 > l1
    if len(str1) > len(str2):
        str1, str2 = str2, str1

    # số dư
    result = ""

    # length
    l1 = len(str1)
    l2 = len(str2)

    str1 = str1[::-1]
    str2 = str2[::-1]

    carry = 0
    for i in range(l1):
        digit1 = int(str1[i])
        digit2 = int(str2[i])
        temp = (digit1 + digit2) + carry

        carry = int(temp / 10)
        temp %= 10
        result += str(temp)

    for i in range(l1, l2):
        digit = int(str2[i])
        temp = digit + carry
        carry = int(temp / 10)
        result += str(temp % 10)

        if(carry != 0):
            result += str(carry)

    result = result[::-1]

    return result


def main():
    FOLDER_READER = "/data"
    result = "0"
    for filename in os.listdir(os.getcwd() + FOLDER_READER):
        with open(os.path.join(os.getcwd() + FOLDER_READER, filename), 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                result = find_sum(result, line)

    f = open(os.path.join(os.getcwd() + FOLDER_READER, "result.txt"), 'w')
    f.write(result)

    f.close()


if __name__ == "__main__":
    main()
