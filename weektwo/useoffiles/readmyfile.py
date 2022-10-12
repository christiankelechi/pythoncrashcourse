import pathlib

mytext=pathlib.Path("D:\\codeblazebackendcourse\\weektwo\\useoffiles\\pythoncourse.txt")
with mytext.open(mode='r',encoding='utf-8') as readme:
    print(readme.read())