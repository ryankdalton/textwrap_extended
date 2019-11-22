def textwrap_extended (string, minlength, maxlength):
    """Extends the Python Standard Library "textwrap" library.  Adds a minimum line length and intelligently handles the last line of text."""
    import textwrap

    lines = textwrap.wrap(string, maxlength)
    newlines = list(lines)

    index = 0
    for l in lines:
        if len(l) < minlength and index > 0:
            prelist = lines[index-1].split(" ")
            postlist = l.split(" ")
            

            lastword = prelist[-1]
            prelist.remove(lastword)
            postlist.insert(0,lastword)


            if len( " ".join(prelist) ) >= minlength:
                newlines[index-1] = " ".join(prelist)
                newlines[index] = " ".join(postlist)
        
        index += 1

    wraptext = "\n".join(newlines)
    return wraptext



x = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print textwrap_extended(x, 8, 24)
