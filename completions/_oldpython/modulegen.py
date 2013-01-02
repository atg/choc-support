import inspect

# These modules can put shit in the global scope (ie non-methods)
privileged_modulenames = [
    "__builtin__",
    "string",
    "math",
]
""" 
modulenames = [
    "__builtin__",
    # # "__future__",
    # "__main__",
    # "_winreg", # 469
    # "abc", # 128
    # "aifc", # 58
    # "anydbm", # 228
    # "argparse", # 2363
    # "array", # 220
    # "ast", # 40 
    # "asynchat", # 220
    # "asyncore", # 3500
    # "atexit", # 420
    # #"audioop", # 54
    # "base64", # 4000
    # "BaseHTTPServer", # 1066
    # "bdb", # 119
    # "binascii", # 2900
    # "binhex", # 25
    # "bisect", # 1200
    # "bsddb", # 388
    # "bz2", # 931
    # "calendar", # 240
    # "cgi", # 12900
    # #"CGIHTTPServer", # 87
    # "cgitb", # 1580
    # "chunk", # 70
    # "cmath", # 160
    # "cmd", # 320
    # "code",
    # "codecs",
    # "codeop",
    # "collections",
    # "colorsys",
    # "compileall",
    # "compiler.ast",
    # "compiler.visitor",
    # "ConfigParser",
    # "contextlib",
    # "Cookie",
    # "cookielib",
    # "copy",
    # "copy_reg",
    # "cPickle",
    # "cProfile",
    # "crypt",
    # "cStringIO", # 6900
    # "csv",
    # "ctypes",
    # "curses",
    # "curses.ascii",
    # "curses.panel",
    # "curses.textpad",
    # "datetime",
    # "dbhash",
    # "dbm",
    # "decimal",
    # "difflib",
    # "dis",
    # "distutils",
    # # "distutils.archive_util",
    # # "distutils.bcppcompiler",
    # # "distutils.ccompiler",
    # # "distutils.cmd",
    # # "distutils.command",
    # # "distutils.command.bdist",
    # # "distutils.command.bdist_dumb",
    # # "distutils.command.bdist_msi",
    # # "distutils.command.bdist_packager",
    # # "distutils.command.bdist_rpm",
    # # "distutils.command.bdist_wininst",
    # # "distutils.command.build",
    # # "distutils.command.build_clib",
    # # "distutils.command.build_ext",
    # # "distutils.command.build_py",
    # # "distutils.command.build_scripts",
    # # "distutils.command.check",
    # # "distutils.command.clean",
    # # "distutils.command.config",
    # # "distutils.command.install",
    # # "distutils.command.install_data",
    # # "distutils.command.install_headers",
    # # "distutils.command.install_lib",
    # # "distutils.command.install_scripts",
    # # "distutils.command.register",
    # # "distutils.command.sdist",
    # # "distutils.core",
    # # "distutils.cygwinccompiler",
    # # "distutils.debug",
    # # "distutils.dep_util",
    # # "distutils.dir_util",
    # # "distutils.dist",
    # # "distutils.emxccompiler",
    # # "distutils.errors",
    # # "distutils.extension",
    # # "distutils.fancy_getopt",
    # # "distutils.file_util",
    # # "distutils.filelist",
    # # "distutils.log",
    # # "distutils.msvccompiler",
    # # "distutils.spawn",
    # # "distutils.sysconfig",
    # # "distutils.text_file",
    # # "distutils.unixccompiler",
    # # "distutils.util",
    # # "distutils.version",
    # "doctest",
    # "DocXMLRPCServer",
    # "dumbdbm",
    # "dummy_thread",
    # "dummy_threading",
    # "email",
    # "email.charset",
    # "email.encoders",
    # "email.errors",
    # "email.generator",
    # "email.header",
    # "email.iterators",
    # "email.message",
    # "email.mime",
    # "email.parser",
    # "email.utils",
    # "encodings.idna",
    # "encodings.utf_8_sig",
    # "errno",
    # "exceptions",
    # "fcntl",
    # "filecmp",
    # "fileinput",
    # "findertools",
    # "fnmatch",
    # "formatter",
    # "fpectl",
    # "fractions",
    # "ftplib",
    # "functools",
    # "future_builtins",
    # "gc",
    # "gdbm",
    # "gensuitemodule",
    # "getopt",
    # "getpass",
    # "gettext",
    # "glob",
    # "grp",
    # "gzip",
    "hashlib",
    # "heapq",
    # "hmac",
    # "hotshot",
    # "hotshot.stats",
    # "htmlentitydefs",
    # "HTMLParser",
    # "httplib",
    # "imaplib",
    # "imghdr",
    # "imp",
    # "importlib",
    # "inspect",
    # "io",
    # "itertools",
    # "json",
    # "keyword",
    # "lib2to3",
    # "linecache",
    # "locale",
    # "logging",
    # "logging.config",
    # "logging.handlers",
    # "macpath",
    # "mailbox",
    # "mailcap",
    # "marshal",
    "math",
    # "mimetypes",
    # "MiniAEFrame",
    # "mmap",
    # "modulefinder",
    # # "msilib",
    # "msvcrt",
    # "multiprocessing",
    # "multiprocessing.connection",
    # "multiprocessing.dummy",
    # "multiprocessing.managers",
    # "multiprocessing.pool",
    # "multiprocessing.sharedctypes",
    # "netrc",
    # "nis",
    # "nntplib",
    # "numbers",
    # "operator",
    "os",
    "os.path",
    # "ossaudiodev",
    # "parser",
    # "pdb",
    # "pickle",
    # "pickletools",
    # "pipes",
    # "pkgutil",
    # "platform",
    # "plistlib",
    # "poplib",
    # "posix",
    # "pprint",
    # "profile",
    # "pstats",
    # "pty",
    # "pwd",
    # "py_compile",
    # "pyclbr",
    # "pydoc",
    # "Queue",
    # "quopri",
    # "random", # 6500
    # "re", # 140
    # "readline", # 440
    # "repr", # 50
    # "resource", # 100
    # "rlcompleter", 
    # "robotparser",
    # "runpy",
    # "sched",
    # "ScrolledText",
    # "select",
    # "shelve",
    # "shlex",
    # "shutil",
    # "signal",
    # "SimpleHTTPServer",
    # "SimpleXMLRPCServer",
    # "site",
    # "smtpd",
    # "smtplib",
    # "sndhdr",
    # "socket",
    # "SocketServer",
    # "spwd",
    # "sqlite3",
    # "ssl",
    # "stat",
    "string",
    # "StringIO",
    # "struct",
    "subprocess",
    # "sunau",
    # "symbol",
    # "symtable",
    "sys",
    # "sysconfig",
    # "syslog",
    # "tabnanny",
    # "tarfile",
    # "telnetlib",
    # "tempfile",
    # "termios",
    # "test",
    # "test.test_support",
    # "textwrap",
    # "thread",
    # "threading",
    # "time",
    # "timeit",
    # "Tix",
    # "Tkinter",
    # "token",
    # "tokenize",
    # "trace",
    # "traceback",
    # "ttk",
    # "tty",
    # "turtle",
    # "types",
    # "unicodedata",
    # "unittest",
    # "urllib",
    "urllib2",
    # "urlparse",
    # "UserDict",
    # "UserList",
    # "UserString",
    # "uu",
    # "uuid",
    # "warnings",
    # "wave",
    # "weakref",
    # "webbrowser",
    # "whichdb",
    # "winsound",
    # "wsgiref",
    # "wsgiref.handlers",
    # "wsgiref.headers",
    # "wsgiref.simple_server",
    # "wsgiref.util",
    # "wsgiref.validate",
    # "xdrlib",
    # "xml.dom",
    # "xml.dom.minidom",
    # "xml.dom.pulldom",
    # "xml.etree.ElementTree",
    # "xml.parsers.expat",
    # "xml.sax",
    # "xml.sax.handler",
    # "xml.sax.saxutils",
    # "xml.sax.xmlreader",
    # "xmlrpclib",
    # "zipfile",
    # "zipimport",
    # "zlib" # 2,551
    ]

"""

modulenames = [
    "__builtin__",
    # # "__future__",
    # "__main__",
    # "_winreg", # 469
    # "abc", # 128
    # "aifc", # 58
    # "anydbm", # 228
    # "argparse", # 2363
    # "array", # 220
    # "ast", # 40 
    # "asynchat", # 220
    # "asyncore", # 3500
    # "atexit", # 420
    # #"audioop", # 54
    # "base64", # 4000
    # "BaseHTTPServer", # 1066
    # "bdb", # 119
    # "binascii", # 2900
    # "binhex", # 25
    # "bisect", # 1200
    # "bsddb", # 388
    # "bz2", # 931
    # "calendar", # 240
    # "cgi", # 12900
    # #"CGIHTTPServer", # 87
    # "cgitb", # 1580
    # "chunk", # 70
    # "cmath", # 160
    # "cmd", # 320
    # "code",
    # "codecs",
    # "codeop",
    # "collections",
    # "colorsys",
    # "compileall",
    # "compiler.ast",
    # "compiler.visitor",
    # "ConfigParser",
    # "contextlib",
    # "Cookie",
    # "cookielib",
    # "copy",
    # "copy_reg",
    # "cPickle",
    # "cProfile",
    # "crypt",
    # "cStringIO", # 6900
    # "csv",
    # "ctypes",
    # "curses",
    # "curses.ascii",
    # "curses.panel",
    # "curses.textpad",
    # "datetime",
    # "dbhash",
    # "dbm",
    # "decimal",
    # "difflib",
    # "dis",
    # "distutils",
    # # "distutils.archive_util",
    # # "distutils.bcppcompiler",
    # # "distutils.ccompiler",
    # # "distutils.cmd",
    # # "distutils.command",
    # # "distutils.command.bdist",
    # # "distutils.command.bdist_dumb",
    # # "distutils.command.bdist_msi",
    # # "distutils.command.bdist_packager",
    # # "distutils.command.bdist_rpm",
    # # "distutils.command.bdist_wininst",
    # # "distutils.command.build",
    # # "distutils.command.build_clib",
    # # "distutils.command.build_ext",
    # # "distutils.command.build_py",
    # # "distutils.command.build_scripts",
    # # "distutils.command.check",
    # # "distutils.command.clean",
    # # "distutils.command.config",
    # # "distutils.command.install",
    # # "distutils.command.install_data",
    # # "distutils.command.install_headers",
    # # "distutils.command.install_lib",
    # # "distutils.command.install_scripts",
    # # "distutils.command.register",
    # # "distutils.command.sdist",
    # # "distutils.core",
    # # "distutils.cygwinccompiler",
    # # "distutils.debug",
    # # "distutils.dep_util",
    # # "distutils.dir_util",
    # # "distutils.dist",
    # # "distutils.emxccompiler",
    # # "distutils.errors",
    # # "distutils.extension",
    # # "distutils.fancy_getopt",
    # # "distutils.file_util",
    # # "distutils.filelist",
    # # "distutils.log",
    # # "distutils.msvccompiler",
    # # "distutils.spawn",
    # # "distutils.sysconfig",
    # # "distutils.text_file",
    # # "distutils.unixccompiler",
    # # "distutils.util",
    # # "distutils.version",
    # "doctest",
    # "DocXMLRPCServer",
    # "dumbdbm",
    # "dummy_thread",
    # "dummy_threading",
    # "email",
    # "email.charset",
    # "email.encoders",
    # "email.errors",
    # "email.generator",
    # "email.header",
    # "email.iterators",
    # "email.message",
    # "email.mime",
    # "email.parser",
    # "email.utils",
    # "encodings.idna",
    # "encodings.utf_8_sig",
    # "errno",
    # "exceptions",
    # "fcntl",
    # "filecmp",
    # "fileinput",
    # "findertools",
    # "fnmatch",
    # "formatter",
    # "fpectl",
    # "fractions",
    # "ftplib",
    # "functools",
    # "future_builtins",
    # "gc",
    # "gdbm",
    # "gensuitemodule",
    # "getopt",
    # "getpass",
    # "gettext",
    # "glob",
    # "grp",
    # "gzip",
    "hashlib",
    # "heapq",
    # "hmac",
    # "hotshot",
    # "hotshot.stats",
    # "htmlentitydefs",
    # "HTMLParser",
    # "httplib",
    # "imaplib",
    # "imghdr",
    # "imp",
    # "importlib",
    # "inspect",
    # "io",
    # "itertools",
    # "json",
    # "keyword",
    # "lib2to3",
    # "linecache",
    # "locale",
    # "logging",
    # "logging.config",
    # "logging.handlers",
    # "macpath",
    # "mailbox",
    # "mailcap",
    # "marshal",
    "math",
    # "mimetypes",
    # "MiniAEFrame",
    # "mmap",
    # "modulefinder",
    # # "msilib",
    # "msvcrt",
    # "multiprocessing",
    # "multiprocessing.connection",
    # "multiprocessing.dummy",
    # "multiprocessing.managers",
    # "multiprocessing.pool",
    # "multiprocessing.sharedctypes",
    # "netrc",
    # "nis",
    # "nntplib",
    # "numbers",
    # "operator",
    "os",
    "os.path",
    # "ossaudiodev",
    # "parser",
    # "pdb",
    # "pickle",
    # "pickletools",
    # "pipes",
    # "pkgutil",
    # "platform",
    # "plistlib",
    # "poplib",
    # "posix",
    # "pprint",
    # "profile",
    # "pstats",
    # "pty",
    # "pwd",
    # "py_compile",
    # "pyclbr",
    # "pydoc",
    # "Queue",
    # "quopri",
    # "random", # 6500
    # "re", # 140
    # "readline", # 440
    # "repr", # 50
    # "resource", # 100
    # "rlcompleter", 
    # "robotparser",
    # "runpy",
    # "sched",
    # "ScrolledText",
    # "select",
    # "shelve",
    # "shlex",
    "shutil",
    # "signal",
    # "SimpleHTTPServer",
    # "SimpleXMLRPCServer",
    # "site",
    # "smtpd",
    # "smtplib",
    # "sndhdr",
    # "socket",
    # "SocketServer",
    # "spwd",
    # "sqlite3",
    # "ssl",
    # "stat",
    "string",
    # "StringIO",
    # "struct",
    "subprocess",
    # "sunau",
    # "symbol",
    # "symtable",
    "sys",
    # "sysconfig",
    # "syslog",
    # "tabnanny",
    # "tarfile",
    # "telnetlib",
    # "tempfile",
    # "termios",
    # "test",
    # "test.test_support",
    # "textwrap",
    # "thread",
    # "threading",
    # "time",
    # "timeit",
    # "Tix",
    # "Tkinter",
    # "token",
    # "tokenize",
    # "trace",
    # "traceback",
    # "ttk",
    # "tty",
    # "turtle",
    # "types",
    # "unicodedata",
    # "unittest",
    # "urllib",
    "urllib2",
    # "urlparse",
    # "UserDict",
    # "UserList",
    # "UserString",
    # "uu",
    # "uuid",
    # "warnings",
    # "wave",
    # "weakref",
    # "webbrowser",
    # "whichdb",
    # "winsound",
    # "wsgiref",
    # "wsgiref.handlers",
    # "wsgiref.headers",
    # "wsgiref.simple_server",
    # "wsgiref.util",
    # "wsgiref.validate",
    # "xdrlib",
    # "xml.dom",
    # "xml.dom.minidom",
    # "xml.dom.pulldom",
    # "xml.etree.ElementTree",
    # "xml.parsers.expat",
    # "xml.sax",
    # "xml.sax.handler",
    # "xml.sax.saxutils",
    # "xml.sax.xmlreader",
    # "xmlrpclib",
    # "zipfile",
    # "zipimport",
    # "zlib" # 2,551
    ]

nn = []
funcs = []
methods = []
classes = []
modules = []

for m in modulenames:
    try:
        mm = __import__(m)
        #nn.extend(dir(mm))
        ismatchable = False
        if m not in ["__builtin__", "math"]:
            mp = m + "."
        else:
            mp = ""
            ismatchable = True
        
        for v in dir(mm):
            if v.startswith("_"):
                continue
            # Does this have documentation? If it doesn't, ignore it
            o = getattr(mm, v)
            d = inspect.getdoc(o)
            if d:
                # print("%s -- %o %o %o %o" % (v, inspect.ismethod(o), inspect.isfunction(o), inspect.isroutine(o), inspect.isbuiltin(o) ))
                if ismatchable and (inspect.isfunction(o) or inspect.isroutine(o)):
                    funcs.append(mp+v)
                elif ismatchable and inspect.ismethod(o):
                    funcs.append(mp+v)
                elif inspect.isclass(o):
                    if ismatchable: classes.append(mp+v)
                    for vv in dir(o):
                        if vv.startswith("_"):
                            continue
                        currentObject = getattr(o, vv)
                        if inspect.isfunction(currentObject) or inspect.isroutine(currentObject):
                            methods.append(vv)
                        elif inspect.ismethod(currentObject):
                            methods.append(vv)
                elif inspect.ismodule(o):
                    modules.append(v)
                
                nn.append(v)
    except Exception as e:
        pass


import json

def dumpto(t, oo):
    oo = sorted(set(oo))
    ooo = {
        'icon': t,
        'items': oo,
    }
    if t == 'method':
        ooo['prefix'] = '.'
    
    f = open("generated_" + t + ".json", "w+")
    f.write(json.dumps(ooo, sort_keys=True, indent=2))
    f.close()

dumpto('class', classes)
dumpto('function', funcs)
dumpto('method', methods)

#dumpto('modules', classes)

# funcs = open("genfunctions.txt")
#for v in methods:
#    print v
#funcs.write(v + "\n")


#for x in sorted(set(nn)):
#    print x
