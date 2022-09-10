with open("dataset_24465_4.txt", "r") as f:
    lines = f.readlines()
    lines.reverse()
    for item in lines:
        print(item.strip())