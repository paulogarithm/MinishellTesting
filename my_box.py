def get_longest(table: list[str]) -> str:
    max_len = -1
    res = ""
    for e in table: 
        if(len(e) <= max_len):
            continue
        max_len = len(e) 
        res = e
    return res


def box_that(name: str = "", table: list[str] = [], size: int = -1) -> str:
    longest = get_longest(table)
    char = ['─', '│', '┌', '┐', '└', '┘']
    longlen = len(longest) if len(longest) > size else size
    longlen = len(name) + 4 if longlen <= 0 else longlen

    name = f" {name} " if name != "" else char[0]
    end = len(name) * char[0]
    line = max(0, longlen - (len(name) - 2)) * char[0]

    box = ""
    box += f"{char[2]}{name}{line}{char[3]}\n"
    for text in table:
        text = text.ljust(max(longlen, len(name) - 2))
        box += f"{char[1]} {text} {char[1]}\n"
    box += f"{char[4]}{end}{line}{char[5]}\n"

    return box, longlen