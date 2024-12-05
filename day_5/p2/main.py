def match_rules(rules, page):
    for a, b in rules:
        if not (a in page and b in page):
            continue
        if page.index(a) > page.index(b):
            return False
    return True

def bubble_sort_with_order(rules, page):
    n = len(page)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not match_rules(rules, [page[j], page[j + 1]]):
                page[j], page[j + 1] = page[j + 1], page[j]
    return page

def main():
    file=open("../input.txt",'r')
    rules, pages = [], []
    row = file.readlines()
    for line in row:
        if "|" in line:
            rules.append(line.rstrip().split('|'))
        else:
            pages.append(line.rstrip().split(','))
    pages_not_in_order = [bubble_sort_with_order(rules, i) for i in pages if not match_rules(rules, i)]
    print(pages_not_in_order)
    print(sum(int(x[len(x) // 2]) for x in pages_not_in_order))

if __name__ == "__main__":
    main()