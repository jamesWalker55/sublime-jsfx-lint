import re
from SublimeLinter.lint import Linter


class JSFXLint(Linter):
    cmd = ("jsfx-lint", "-")
    name = "jsfx-lint"
    regex = r"""^(?P<error_type>warning|error):\s+(?P<message>.*)$\n\s*-*>\s*(?P<path>[^:]*):(?P<line>\d+):(?P<col>\d+)\s+\((?P<code>[^)]*)\)$"""
    multiline = True
    re_flags = re.MULTILINE | re.UNICODE
    defaults = {"selector": "source.jesusonic"}
