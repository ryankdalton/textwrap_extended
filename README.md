# textwrap_extended
Extends the Python Standard Library "textwrap" library.  Adds a minimum line length and intelligently handles the last line of text.

This code was originally designed to enhance the "wordwrap()" function in QGIS. Because both the QGIS wordwrap() and Python textwrap.fill()
functions only consider maximum line length, you often get a small bit of text "leftover" on a line all by itself, because it was the only
word not to fit on the previous line.

This function is particularly helpful for shorter string lengths (less than 30 characters) because it can intelligently "even out" the
length of the last line by combining it with the last word of the previous line.

Example usage:

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print textwrap_extended(string, 8, 24)

QGIS implementation:
For QGIS users who weant to add this function to their labeling expressions, a couple simple changes will need to be made:
1) Open the Layer Properties dialog
2) Click on the "Labels" tab
3) Open the "Label with" expression dialog
4) On the Expression Dialog, click on the "Function Editor" tab
5) Click the "+" button in the lower-left corner to create a new custom function item
6) Paste the following code, followed by the code in the function:

    from qgis.core import *
    from qgis.gui import *

    @qgsfunction(args='auto', group='Custom')        
    def textwrap_extended (string, minlength, maxlength, feature, parent):
      <function code>

These changes will be all that is needed for you to start using this function in QGIS.
