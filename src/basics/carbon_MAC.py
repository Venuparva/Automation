def __init__(self):
        try:
            import msvcrt
            self.impl = self.get_windows
            print self.impl
        except ImportError:
            try:
                import tty, sys, termios
                self.impl = self.get_unix
                print self.impl
            except ImportError:
                import Carbon, Carbon.Evt
                self.impl = self.get_carbon
                print self.impl
