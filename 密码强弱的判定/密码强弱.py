class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath

    def write_filepath(self, line):
        f = open(self.filepath, 'a')
        f.write(line)
        f.close()

    def read_filepath(self):
        f = open(self.filepath, 'r')
        lines = f.readline()
        f.close()
        return lines


class PasswordTool:
    def __init__(self, password):
        self.password = password

    def fun(self):
        tri = False
        for c in self.password:
            if c.isnumeric():
                tri = True
                break
        return tri

    def fun2(self):
        tri = False
        for c in self.password:
            if c.isalpha():
                tri = True
                break
        return tri


def main():
    number = 5
    filepath = 'password__book1.0.txt'
    while number > 0:
        password = input('请输入密码：')
        long = len(password)
        string__thin = 0
        password__tool = PasswordTool(password)

        if long >= 8:
            string__thin += 1
        else:
            print('密码长度不够')

        if password__tool.fun():
            string__thin += 1
        else:
            print('密码缺少数字')

        if password__tool.fun2():
            string__thin += 1
        else:
            print('密码缺少字母')

        if string__thin >= 3:
            qiangdu = '强'
        else:
            qiangdu = '弱'

        file__toll = FileTool(filepath)
        line = '密码：{}，强度：{}\n'.format(password, qiangdu)
        file__toll.write_filepath(line)

        if string__thin >= 3:
            print('此密码可以使用')
            break
        else:
            print('此密码强度不够')
            number -= 1
    if number == 0:
        print('尝试次数过多，密码设置失败')
    line = file__toll.read_filepath()
    print(line)


if __name__ == '__main__':
    main()