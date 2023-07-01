__builtin__	The module that provides the built-in namespace.
__future__	Future statement definitions
__main__	The environment where the top-level script is run.
_winreg (Windows)	Routines and objects for manipulating the Windows registry.
==========
a	
abc	Abstract base classes according to PEP 3119.
aepack (Mac)	Deprecated: Conversion between Python variables and AppleEvent data containers.
aetools (Mac)	Deprecated: Basic support for sending Apple Events
aetypes (Mac)	Deprecated: Python representation of the Apple Event Object Model.
aifc	Read and write audio files in AIFF or AIFC format.
AL (IRIX)	Deprecated: Constants used with the al module.
al (IRIX)	Deprecated: Audio functions on the SGI.
anydbm	Generic interface to DBM-style database modules.
applesingle (Mac)	Deprecated: Rudimentary decoder for AppleSingle format files.
argparse	Command-line option and argument parsing library.
array	Space efficient arrays of uniformly typed numeric values.
ast	Abstract Syntax Tree classes and manipulation.
asynchat	Support for asynchronous command/response protocols.
asyncore	A base class for developing asynchronous socket handling services.
atexit	Register and execute cleanup functions.
audioop	Manipulate raw audio data.
autoGIL (Mac)	Deprecated: Global Interpreter Lock handling in event loops.
==========
base64	RFC 3548: Base16, Base32, Base64 Data Encodings
BaseHTTPServer	Basic HTTP server (base class for SimpleHTTPServer and CGIHTTPServer).
Bastion	Deprecated: Providing restricted access to objects.
bdb	Debugger framework.
binascii	Tools for converting between binary and various ASCII-encoded binary representations.
binhex	Encode and decode files in binhex4 format.
bisect	Array bisection algorithms for binary searching.
bsddb	Interface to Berkeley DB database library
buildtools (Mac)	Deprecated: Helper module for BuildApplet, BuildApplication and macfreeze.
bz2	Interface to compression and decompression routines compatible with bzip2.
==========
calendar	Functions for working with calendars, including some emulation of the Unix cal program.
-	Carbon	- mainly for Apple MAC os events,These are a set of modules that provide interfaces to various legacy Mac OS toolboxes
        Carbon.AE - Apple Events
        Carbon.AH - These modules all live in a package called Carbon. Despite that name they are not all part of the Carbon framework: CF is really in the CoreFoundation framework and Qt is in the QuickTime framework. The normal use pattern is
        Carbon.App - Appearance manager
        Note : Most of the OS X APIs that these modules use are deprecated or removed in recent versions of OS X. Many are not available when Python is executing in 64-bit mode. The Carbon modules have been removed in Python 3. You should avoid using them in Python 2.
cd (IRIX)	Deprecated: Interface to the CD-ROM on Silicon Graphics systems.
cfmfile (Mac)	Deprecated: Code Fragment Resource module.
cgi	Helpers for running Python scripts via the Common Gateway Interface.
CGIHTTPServer	This module provides a request handler for HTTP servers which can run CGI scripts.
cgitb	Configurable traceback handler for CGI scripts.
chunk	Module to read IFF chunks.
cmath	Mathematical functions for complex numbers.
cmd	Build line-oriented command interpreters.
code	Facilities to implement read-eval-print loops.
codecs	Encode and decode data and streams.
codeop	Compile (possibly incomplete) Python code.
collections	High-performance datatypes
ColorPicker (Mac)	Deprecated: Interface to the standard color selection dialog.
colorsys	Conversion functions between RGB and other color systems.
commands (Unix)	Deprecated: Utility functions for running external commands.
compileall	Tools for byte-compiling all Python source files in a directory tree.
-	compiler	Deprecated: Python code compiler written in Python.
            compiler.ast	
    compiler.visitor	
ConfigParser	Configuration file parser.
contextlib	Utilities for with-statement contexts.
Cookie	Support for HTTP state management (cookies).
cookielib	Classes for automatic handling of HTTP cookies.
copy	Shallow and deep copy operations.
copy_reg	Register pickle support functions.
cPickle	Faster version of pickle, but not subclassable.
cProfile	
crypt (Unix)	The crypt() function used to check Unix passwords.
cStringIO	Faster version of StringIO, but not subclassable.
csv	Write and read tabular data to and from delimited files.
ctypes	A foreign function library for Python.
-	curses (Unix)	An interface to the curses library, providing portable terminal handling.
==========
datetime	Basic date and time types.
dbhash	DBM-style interface to the BSD database library.
dbm (Unix)	The standard "database" interface, based on ndbm.
decimal	Implementation of the General Decimal Arithmetic Specification.
DEVICE (IRIX)	Deprecated: Constants used with the gl module.
difflib	Helpers for computing differences between objects.
dircache	Deprecated: Return directory listing, with cache mechanism.
dis	Disassembler for Python bytecode.
-	distutils	Support for building and installing Python modules into an existing Python installation.
           distutils.archive_util	Utility functions for creating archive files (tarballs, zip files, ...)
    distutils.bcppcompiler	
    distutils.ccompiler	Abstract CCompiler class
    distutils.cmd	This module provides the abstract base class Command. This class is subclassed by the modules in the distutils.command subpackage.
    distutils.command	This subpackage contains one module for each standard Distutils command.
    distutils.command.bdist	Build a binary installer for a package
    distutils.command.bdist_dumb	Build a "dumb" installer - a simple archive of files
    distutils.command.bdist_msi	Build a binary distribution as a Windows MSI file
    distutils.command.bdist_packager	Abstract base class for packagers
    distutils.command.bdist_rpm	Build a binary distribution as a Redhat RPM and SRPM
    distutils.command.bdist_wininst	Build a Windows installer
    distutils.command.build	Build all files of a package
    distutils.command.build_clib	Build any C libraries in a package
    distutils.command.build_ext	Build any extensions in a package
    distutils.command.build_py	Build the .py/.pyc files of a package
    distutils.command.build_scripts	Build the scripts of a package
    distutils.command.check	Check the metadata of a package
    distutils.command.clean	Clean a package build area
    distutils.command.config	Perform package configuration
    distutils.command.install	Install a package
    distutils.command.install_data	Install data files from a package
    distutils.command.install_headers	Install C/C++ header files from a package
    distutils.command.install_lib	Install library files from a package
    distutils.command.install_scripts	Install script files from a package
    distutils.command.register	Register a module with the Python Package Index
    distutils.command.sdist	Build a source distribution
    distutils.core	The core Distutils functionality
    distutils.cygwinccompiler	
    distutils.debug	Provides the debug flag for distutils
    distutils.dep_util	Utility functions for simple dependency checking
    distutils.dir_util	Utility functions for operating on directories and directory trees
    distutils.dist	Provides the Distribution class, which represents the module distribution being built/installed/distributed
    distutils.emxccompiler	OS/2 EMX Compiler support
    distutils.errors	Provides standard distutils exceptions
    distutils.extension	Provides the Extension class, used to describe C/C++ extension modules in setup scripts
    distutils.fancy_getopt	Additional getopt functionality
    distutils.file_util	Utility functions for operating on single files
    distutils.filelist	The FileList class, used for poking about the file system and building lists of files.
    distutils.log	A simple logging mechanism, 282-style
    distutils.msvccompiler	Microsoft Compiler
    distutils.spawn	Provides the spawn() function
    distutils.sysconfig	Low-level access to configuration information of the Python interpreter.
    distutils.text_file	provides the TextFile class, a simple interface to text files
    distutils.unixccompiler	UNIX C Compiler
    distutils.util	Miscellaneous other utility functions
    distutils.version	implements classes that represent module version numbers.
dl (Unix)	Deprecated: Call C functions in shared objects.
doctest	Test pieces of code within docstrings.
DocXMLRPCServer	Self-documenting XML-RPC server implementation.
dumbdbm	Portable implementation of the simple DBM interface.
dummy_thread	Drop-in replacement for the thread module.
dummy_threading	Drop-in replacement for the threading module.
==========
EasyDialogs (Mac)	Deprecated: Basic Macintosh dialogs.
-	email	Package supporting the parsing, manipulating, and generating email messages, including MIME documents.
    	    email.charset	Character Sets
    email.encoders	Encoders for email message payloads.
    email.errors	The exception classes used by the email package.
    email.generator	Generate flat text email messages from a message structure.
    email.header	Representing non-ASCII headers
    email.iterators	Iterate over a message object tree.
    email.message	The base class representing email messages.
    email.mime	Build MIME messages.
    email.parser	Parse flat text email messages to produce a message object structure.
    email.utils	Miscellaneous email package utilities.
-	encodings	
ensurepip	Bootstrapping the ``pip`` installer into an existing Python installation or virtual environment.
errno	Standard errno system symbols.
exceptions	Standard exception classes.
==========
fcntl (Unix)	The fcntl() and ioctl() system calls.
filecmp	Compare files efficiently.
fileinput	Loop over standard input or a list of files.
findertools (Mac)	Wrappers around the finder's Apple Events interface.
FL (IRIX)	Deprecated: Constants used with the fl module.
fl (IRIX)	Deprecated: FORMS library for applications with graphical user interfaces.
flp (IRIX)	Deprecated: Functions for loading stored FORMS designs.
fm (IRIX)	Deprecated: Font Manager interface for SGI workstations.
fnmatch	Unix shell style filename pattern matching.
formatter	Generic output formatter and device interface.
fpectl (Unix)	Provide control for floating point exception handling.
fpformat	Deprecated: General floating point formatting functions.
fractions	Rational numbers.
FrameWork (Mac)	Deprecated: Interactive application framework.
ftplib	FTP protocol client (requires sockets).
functools	Higher-order functions and operations on callable objects.
future_builtins	
==========
gc	Interface to the cycle-detecting garbage collector.
gdbm (Unix)	GNU's reinterpretation of dbm.
gensuitemodule (Mac)	Create a stub package from an OSA dictionary
getopt	Portable parser for command line options; support both short and long option names.
getpass	Portable reading of passwords and retrieval of the userid.
gettext	Multilingual internationalization services.
gl (IRIX)	Deprecated: Functions from the Silicon Graphics Graphics Library.
GL (IRIX)	Deprecated: Constants used with the gl module.
glob	Unix shell style pathname pattern expansion.
grp (Unix)	The group database (getgrnam() and friends).
gzip	Interfaces for gzip compression and decompression using file objects.
==========
hashlib	Secure hash and message digest algorithms.
heapq	Heap queue algorithm (a.k.a. priority queue).
hmac	Keyed-Hashing for Message Authentication (HMAC) implementation
-	hotshot	High performance logging profiler, mostly written in C.
htmlentitydefs	Definitions of HTML general entities.
htmllib	Deprecated: A parser for HTML documents.
HTMLParser	A simple parser that can handle HTML and XHTML.
httplib	HTTP and HTTPS protocol client (requires sockets).
==========
ic (Mac)	Deprecated: Access to the Mac OS X Internet Config.
icopen (Mac)	Deprecated: Internet Config replacement for open().
imageop	Deprecated: Manipulate raw image data.
imaplib	IMAP4 protocol client (requires sockets).
imgfile (IRIX)	Deprecated: Support for SGI imglib files.
imghdr	Determine the type of image contained in a file or byte stream.
imp	Access the implementation of the import statement.
importlib	Convenience wrappers for __import__
imputil	Deprecated: Manage and augment the import process.
inspect	Extract information and source code from live objects.
io	Core tools for working with streams.
itertools	Functions creating iterators for efficient looping.
==========
jpeg (IRIX)	Deprecated: Read and write image files in compressed JPEG format.
json	Encode and decode the JSON format.
==========
keyword	Test whether a string is a keyword in Python.
==========
lib2to3	the 2to3 library
linecache	This module provides random access to individual lines from text files.
locale	Internationalization services.
-	logging	Flexible event logging system for applications.
==========
macerrors (Mac)	Deprecated: Constant definitions for many Mac OS error codes.
MacOS (Mac)	Deprecated: Access to Mac OS-specific interpreter features.
macostools (Mac)	Deprecated: Convenience routines for file manipulation.
macpath	Mac OS 9 path manipulation functions.
macresource (Mac)	Deprecated: Locate script resources.
mailbox	Manipulate mailboxes in various formats
mailcap	Mailcap file handling.
marshal	Convert Python objects to streams of bytes and back (with different constraints).
math	Mathematical functions (sin() etc.).
md5	Deprecated: RSA's MD5 message digest algorithm.
mhlib	Deprecated: Manipulate MH mailboxes from Python.
mimetools	Deprecated: Tools for parsing MIME-style message bodies.
mimetypes	Mapping of filename extensions to MIME types.
MimeWriter	Deprecated: Write MIME format files.
mimify	Deprecated: Mimification and unmimification of mail messages.
MiniAEFrame (Mac)	Support to act as an Open Scripting Architecture (OSA) server ("Apple Events").
mmap	Interface to memory-mapped files for Unix and Windows.
modulefinder	Find modules used by a script.
msilib (Windows)	Creation of Microsoft Installer files, and CAB files.
msvcrt (Windows)	Miscellaneous useful routines from the MS VC++ runtime.
multifile	Deprecated: Support for reading files which contain distinct parts, such as some MIME data.
-	multiprocessing	Process-based "threading" interface.
mutex	Deprecated: Lock and queue for mutual exclusion.
==========
Nav (Mac)	Deprecated: Interface to Navigation Services.
netrc	Loading of .netrc files.
new	Deprecated: Interface to the creation of runtime implementation objects.
nis (Unix)	Interface to Sun's NIS (Yellow Pages) library.
nntplib	NNTP protocol client (requires sockets).
numbers	Numeric abstract base classes (Complex, Real, Integral, etc.).
==========
operator	Functions corresponding to the standard operators.
optparse	Deprecated: Command-line option parsing library.
-	os	Miscellaneous operating system interfaces.
ossaudiodev (Linux, FreeBSD)	Access to OSS-compatible audio devices.
==========
parser	Access parse trees for Python source code.
pdb	The Python debugger for interactive interpreters.
pickle	Convert Python objects to streams of bytes and back.
pickletools	Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.
pipes (Unix)	A Python interface to Unix shell pipelines.
PixMapWrapper (Mac)	Deprecated: Wrapper for PixMap objects.
pkgutil	Utilities for the import system.
platform	Retrieves as much platform identifying data as possible.
plistlib	Generate and parse Mac OS X plist files.
popen2	Deprecated: Subprocesses with accessible standard I/O streams.
poplib	POP3 protocol client (requires sockets).
posix (Unix)	The most common POSIX system calls (normally used via module os).
posixfile (Unix)	Deprecated: A file-like object with support for locking.
pprint	Data pretty printer.
profile	Python source profiler.
pstats	Statistics object for use with the profiler.
pty (Linux)	Pseudo-Terminal Handling for Linux.
pwd (Unix)	The password database (getpwnam() and friends).
py_compile	Generate byte-code files from Python source files.
pyclbr	Supports information extraction for a Python class browser.
pydoc	Documentation generator and online help system.
==========
Queue	A synchronized queue class.
quopri	Encode and decode files using the MIME quoted-printable encoding.
==========
random	Generate pseudo-random numbers with various common distributions.
re	Regular expression operations.
readline (Unix)	GNU readline support for Python.
resource (Unix)	An interface to provide resource usage information on the current process.
rexec	Deprecated: Basic restricted execution framework.
rfc822	Deprecated: Parse 2822 style mail messages.
rlcompleter	Python identifier completion, suitable for the GNU readline library.
robotparser	Loads a robots.txt file and answers questions about fetchability of other URLs.
runpy	Locate and run Python modules without importing them first.
==========
sched	General purpose event scheduler.
ScrolledText (Tk)	Text widget with a vertical scroll bar.
select	Wait for I/O completion on multiple streams.
sets	Deprecated: Implementation of sets of unique elements.
sgmllib	Deprecated: Only as much of an SGML parser as needed to parse HTML.
sha	Deprecated: NIST's secure hash algorithm, SHA.
shelve	Python object persistence.
shlex	Simple lexical analysis for Unix shell-like languages.
shutil	High-level file operations, including copying.
signal	Set handlers for asynchronous events.
SimpleHTTPServer	This module provides a basic request handler for HTTP servers.
SimpleXMLRPCServer	Basic XML-RPC server implementation.
site	Module responsible for site-specific configuration.
smtpd	A SMTP server implementation in Python.
smtplib	SMTP protocol client (requires sockets).
sndhdr	Determine type of a sound file.
socket	Low-level networking interface.
SocketServer	A framework for network servers.
spwd (Unix)	The shadow password database (getspnam() and friends).
sqlite3	A DB-API 2.0 implementation using SQLite 3.x.
ssl	TLS/SSL wrapper for socket objects
stat	Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().
statvfs	Deprecated: Constants for interpreting the result of os.statvfs().
string	Common string operations.
StringIO	Read and write strings as if they were files.
stringprep	String preparation, as per RFC 3453
struct	Interpret strings as packed binary data.
subprocess	Subprocess management.
sunau	Provide an interface to the Sun AU sound format.
sunaudiodev (SunOS)	Deprecated: Access to Sun audio hardware.
SUNAUDIODEV (SunOS)	Deprecated: Constants for use with sunaudiodev.
symbol	Constants representing internal nodes of the parse tree.
symtable	Interface to the compiler's internal symbol tables.
sys	Access system-specific parameters and functions.
sysconfig	Python's configuration information
syslog (Unix)	An interface to the Unix syslog library routines.
==========
tabnanny	Tool for detecting white space related problems in Python source files in a directory tree.
tarfile	Read and write tar-format archive files.
telnetlib	Telnet client class.
tempfile	Generate temporary files and directories.
termios (Unix)	POSIX style tty control.
-	test	Regression tests package containing the testing suite for Python.
textwrap	Text wrapping and filling
thread	Create multiple threads of control within one interpreter.
threading	Higher-level threading interface.
time	Time access and conversions.
timeit	Measure the execution time of small code snippets.
Tix	Tk Extension Widgets for Tkinter
Tkinter	Interface to Tcl/Tk for graphical user interfaces
token	Constants representing terminal nodes of the parse tree.
tokenize	Lexical scanner for Python source code.
trace	Trace or track Python statement execution.
traceback	Print or retrieve a stack traceback.
ttk	Tk themed widget set
tty (Unix)	Utility functions that perform common terminal control operations.
turtle	Turtle graphics for Tk
types	Names for built-in types.
==========
unicodedata	Access the Unicode Database.
unittest	Unit testing framework for Python.
urllib	Open an arbitrary network resource by URL (requires sockets).
urllib2	Next generation URL opening library.
urlparse	Parse URLs into or assemble them from components.
user	Deprecated: A standard way to reference user-specific modules.
UserDict	Class wrapper for dictionary objects.
UserList	Class wrapper for list objects.
UserString	Class wrapper for string objects.
uu	Encode and decode files in uuencode format.
uuid	UUID objects (universally unique identifiers) according to RFC 4122
==========
videoreader (Mac)	Deprecated: Read QuickTime movies frame by frame for further processing.
W (Mac)	Deprecated: Widgets for the Mac, built on top of FrameWork.
warnings	Issue warning messages and control their disposition.
wave	Provide an interface to the WAV sound format.
weakref	Support for weak references and weak dictionaries.
webbrowser	Easy-to-use controller for Web browsers.
whichdb	Guess which DBM-style module created a given database.
winsound (Windows)	Access to the sound-playing machinery for Windows.
-	wsgiref	WSGI Utilities and Reference Implementation.
xdrlib	Encoders and decoders for the External Data Representation (XDR).
-	xml	Package containing XML processing modules
xmlrpclib	XML-RPC client access.
==========
zipfile	Read and write ZIP-format archive files.
zipimport	support for importing Python modules from ZIP archives.
zlib	Low-level interface to compression and decompression routines compatible with gzip.
