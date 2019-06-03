import sys

def sp2tab(line, sp):
    """ convert an indent of spaces to \t strings 
    ex.) python main.py -sp2tab 4
        --> an indenct of 4 spaces to 1 r"\t" string.
    """
    cnt = 0
    spaces = sp
    while line.startswith(spaces):
        cnt += 1
        spaces += sp 
    return line.replace(sp, r"\t", cnt)


def tab2sp(line, spaces):
    """ convert an indent of tab to spaces 
    ex.) python main.py -tab2sp 4
        --> an indenct of tab to 4 spaces
    """
    cnt = 0
    tabs = "\t"
    while line.startswith(tabs):
        cnt += 1
        tabs += "\t"
    return line.replace("\t", spaces, cnt)


def convert(s, options):
    """ convert all texts to json format strings """
    is_sp2tab = False
    is_tab2sp = False

    for i, op in enumerate(options):
        if op == "-sp2tab":
            # convert tab to spaces
            is_sp2tab = True
            sp_num = int(options[i+1])
        if op == "-tab2sp":
            # convert spaces to tab
            is_tab2sp = True
            sp_num = int(options[i+1])

    # Convert
    ans = ""
    if is_sp2tab or is_tab2sp:
        spaces = " " * sp_num
    
    for line in s.splitlines():
        if is_sp2tab:
            line = sp2tab(line, spaces)
        elif is_tab2sp:
            line = tab2sp(line, spaces)
        else:
            line = line.replace("\t", r"\t")
        line = line.replace("\"", r"\"")
        ans += "\"" + line + "\",\n"
    return ans


if __name__ == "__main__":
    args = sys.argv
    file_name = args[1]
    options = args[2:]  # Option arguments if exists.

    # Read an input file.
    f = open(file_name, "r", encoding="utf-8")
    s = f.read()
    f.close()

    # Convert
    ans = convert(s, options)
    
    # Write into an output file.
    f = open("output.json", "w", encoding="utf-8")
    f.write(ans)
    f.close()
