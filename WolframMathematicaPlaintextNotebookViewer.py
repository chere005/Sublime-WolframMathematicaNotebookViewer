import sublime, sublime_plugin, subprocess, os, sys

class NotebookviewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#Import Current Filepath as Plaintext
		path = str(self.view.file_name());

		if(path == "None"):
			sublime.error_message("File Not Saved")
			return

		settings = sublime.load_settings('WolframMathematicaPlaintextNotebookViewer.sublime-settings')
		wscriptpath = settings.get('wscriptpath')
		cmd = [wscriptpath, '-code', 'Quiet@Import[\"' + path + '\", {\"NB\", \"Plaintext\"}]']
		
		p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		out, error = p.communicate()
		out = out.decode('ascii')

		if(out == "$Failed\n"):
			sublime.error_message("Invalid Notebook")
		else:
			newView = self.view.window().new_file()
			newView.insert(edit, 0, out)