from os import path

import sublime, sublime_plugin


class PythonPackageToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        pckg = []
        if path.basename(filename) != '__init__.py':
            pckg.append(path.splitext(path.basename(filename))[0])
        while filename != path.dirname(filename):
            filename = path.dirname(filename)
            if not path.exists(path.join(filename, '__init__.py')):
                break
            pckg.append(path.basename(filename))

        sublime.set_clipboard('.'.join(reversed(pckg)))
        sublime.status_message('Copied python package')

    def is_enabled(self):
        filename = self.view.file_name()
        return filename and path.splitext(filename)[1] == '.py'

    def is_visible(self):
        return self.is_enabled()
