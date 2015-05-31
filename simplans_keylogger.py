import sublime, sublime_plugin
import time as t
import os

class SaveFiles(object):

	def new_file_history(self):
		s = sublime.load_settings("LogUserAction.sublime-settings")
		hist_file_name = s.get("history_file")
		get_date = t.localtime(t.time())
		time_date = "%d-%d-%d, %d:%d" %(get_date[2], get_date[1], get_date[0], get_date[3], get_date[4])
		full_path = os.path.join(sublime.packages_path(), hist_file_name)
		# file open
		with open(full_path, "a+") as f:
			f.write("\n\n Date: " + time_date + "\n\n")
			f.write( "New Window Created.\n\n")
			f.write("\n\n====================================================")
			f.close()

	def open_file_history(self, file_name):
		s = sublime.load_settings("LogUserAction.sublime-settings")
		hist_file_name = s.get("history_file")
		get_date = t.localtime(t.time())
		time_date = "%d-%d-%d, %d:%d" %(get_date[2], get_date[1], get_date[0], get_date[3], get_date[4])
		full_path = os.path.join(sublime.packages_path(), hist_file_name)
		# file open
		with open(full_path, "a+") as f:
			f.write("\n\n Date: " + time_date + "\n\n")
			f.write( "File Opened: " + file_name + "\n\n")
			f.write("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			f.close()

	def key_strokes_history(self, file_name, get_it):
		s = sublime.load_settings("LogUserAction.sublime-settings")
		hist_file_name = s.get("history_file")
		get_date = t.localtime(t.time())
		time_date = "%d-%d-%d, %d:%d" %(get_date[2], get_date[1], get_date[0], get_date[3], get_date[4])
		full_path = os.path.join(sublime.packages_path(), hist_file_name)
		# file open
		with open(full_path, "a+") as f:
			f.write("\n\n Date: " + time_date + "\n\n")
			f.write( "File Name: " + str(file_name) + "\n\n")
			# for get_one in get_it:

			f.write("Content: \n" + get_it)
			f.write("\n\n*******************************************************")
			f.close()


class LogUserActionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		"""
			opened file content which save to history
		"""
		file_name = self.view.file_name()
		SaveFiles().open_file_history(file_name)

		
class LogUserTestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")


# class LogUserKeyloggerCommand(sublime_plugin.TextCommand):
# 	def run(self, edit):
# 		file_name = self.view.file_name()
# 		# get_it = [] 
# 		# if self.view.window().active_view():
# 		get_it = self.view.substr(self.view.line(self.view.sel()[0].begin()))
# 			# get_it.append(content)
# 		# get_it = " ".join(get_it)
# 		SaveFiles().key_strokes_history(file_name, get_it)


class LogUserOpenCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.open_file("history.txt")



class LogListener(sublime_plugin.EventListener):
	def __init__(self):
		self.file_name = ""
		self.get_it = ""
		self.lis = []

	def on_new(self, view):
		SaveFiles().new_file_history()

	def on_load(self, view):
		view.run_command("log_user_action")

	def on_modified(self, view):
		self.file_name = view.file_name()
		keylogger = view.substr(view.line(view.sel()[0].begin()))
		self.lis.append(keylogger)
		self.get_it = " ".join(self.lis)

	def on_pre_save(self, view):
	# 	view.run_command("log_user_keylogger")
		SaveFiles().key_strokes_history(self.file_name, self.get_it)
		self.lis = []