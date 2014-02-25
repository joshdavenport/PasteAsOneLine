import sublime, sublime_plugin

class PasteAsOneLineCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# get contents of the clipboard
		clipboard = sublime.get_clipboard()
		# store original clipboard
		original_clipboard = clipboard
		# set the clipboard to the new onelined content
		sublime.set_clipboard(self.merge_lines(clipboard))

		s = sublime.load_settings("ClipboardHistory.sublime-settings")

		if s.get('paste_and_indent'):
			self.view.run_command('paste_and_indent')
		else:
			self.view.run_command('paste')

		#return the original clipboard
		sublime.set_clipboard(original_clipboard)

	def merge_lines(self, mergee):
		mergee = mergee.replace('\n', ' ')
		mergee = mergee.replace('\r', ' ')
		mergee = mergee.replace('\t', '')
		mergee = mergee.replace('   ', ' ')
		mergee = mergee.replace('  ', ' ')
		mergee = mergee.replace('  ', ' ')
		return mergee