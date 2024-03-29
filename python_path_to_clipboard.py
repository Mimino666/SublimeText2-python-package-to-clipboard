from os import path

import sublime
import sublime_plugin


SETTINGS_FILE = 'Python Path to Clipboard.sublime-settings'


class PythonPathToClipboardCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        pckg = []
        if self._base_filename(filename) != '__init__':
            pckg.append(self._base_filename(filename))

        pckg_path = path.dirname(filename)
        while self._is_package(pckg_path):
            pckg.append(path.basename(pckg_path))
            pckg_path, old_path = path.dirname(pckg_path), pckg_path
            if pckg_path == old_path:
                break

        sublime.set_clipboard('.'.join(reversed(pckg)))
        sublime.status_message('Copied python import path')

    def is_enabled(self):
        return self._is_current_python_file()

    def is_visible(self):
        return self._is_current_python_file()

    def _is_current_python_file(self):
        '''True, if current file if a python file.'''

        filename = self.view.file_name()
        extensions = self._get_python_extensions()
        return (filename and
                extensions and
                path.splitext(filename)[1] in extensions)

    def _get_python_extensions(self, default=None):
        settings = sublime.load_settings(SETTINGS_FILE)
        return settings.get('python_extensions', default)

    def _base_filename(self, filename):
        return path.splitext(path.basename(filename))[0]

    def _is_package(self, pckg_path):
        for ext in self._get_python_extensions(['.py']):
            filename = path.join(pckg_path, '__init__' + ext)
            if path.exists(filename):
                return True

        return False
