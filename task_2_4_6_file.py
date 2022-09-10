import os
import os.path

if __name__ == '__main__':
    resultlist = []
    for current_dir, dirs, files in os.walk('./main'):
        print(current_dir, dirs, files)
        for item in files:
            if item.find(".py") >= 0:
                s = current_dir.replace('./', '')
                resultlist.append(s + '\n')
                print(current_dir)
                break
    resultlist.sort()
    with open("2.4.6_result.txt", "w") as f:
        f.writelines(resultlist)