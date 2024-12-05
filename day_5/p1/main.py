def match_rules(rules, page):
    print(page)
    for a, b in rules:
        if not (a in page and b in page):
            continue
        if page.index(a) > page.index(b):
            return False
    return True

def main():
    file=open("../input.txt",'r')
    rules, pages = [], []
    row = file.readlines()
    for line in row:
        if "|" in line:
            rules.append(line.rstrip().split('|'))
        else:
            pages.append(line.rstrip().split(','))
    pages_in_order = [i for i in pages if match_rules(rules, i)]
    print(sum(int(x[len(x) // 2]) for x in pages_in_order))

if __name__ == "__main__":
    main()