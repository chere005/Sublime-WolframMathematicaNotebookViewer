# Sublime-WolframMathematicaNotebookViewer
A Sublime Text 2/3 plugin that opens a new page, and prints the plaintext of the currently opened notebook.

A local Mathematica installation must be present, and added to the system's PATH environment variable:

Default Windows:
Add the following under PATH in "Environment Variables". Should be easy to search for in Win7+.
"%ProgramFiles%\Wolfram Research\Mathematica\11.1\"
Modify the above directory if your installation is located somewhere else.

Default OSX:
Append the following to ~/.bash_profile:
export PATH="$PATH:/Applications/Mathematica.app/Contents/MacOS/"
Modify the above directory if your installation is located somewhere else.
