import sublime, sublime_plugin, os, os.path, sys

class NotebookviewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#Import Current Filepath as Plaintext
		path = str(self.view.file_name());
		nbText = os.popen(mPath + 'wolframscript -code "Quiet@Import[\\"' + path + '\\", {\\"NB\\", \\"Plaintext\\"}]"').read()

		if(nbText != "$Failed\n"):
			self.view.window().new_file().insert(edit, 0, nbText)
		else:
			sublime.error_message("Invalid Notebook")