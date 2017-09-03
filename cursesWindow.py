import curses
from curses import wrapper

class GuiWindow:
    stdscr = None
    window = None
    title = ""
    pointer = "-->"
    edges = "|-+"

    height = 15
    width = 60

    def begin_window(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.window = curses.newwin(
            5 + self.height,
            self.width,
            2,
            4
        )

    def stop_window(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def redraw(self):
        self.window.clear()
        self.window.border(
            self.edges[0], self.edges[0],
            self.edges[1], self.edges[1],
            self.edges[2], self.edges[2],
            self.edges[2], self.edges[2]
        )

    def window_loop(self, stdscr):
        while 1:
            self.redraw()

    def __init__(
        self,
        items,
        title = 'Select'
    ):
        self.title = title
        self.items_all = []

        for item, memory in items:
            self.items_all.append({
                "name": item,
                "size": memory,
                "selected": False
            })
        self.length = len(self.items_all)

        self.begin_window()
        curses.wrapper(self.window_loop)
        self.stop_window()