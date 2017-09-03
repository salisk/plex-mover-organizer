import curses
from curses import wrapper

class GuiWindow:
    stdscr = None
    window = None
    title = ""
    pointer = "-->"
    edges = "|**"
    footer = "Space = select, Enter = start, q = cancel"
    header = "Select files to copy"

    offset = 0
    height = 15
    width = 70
    select = 0

    def begin_window(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
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

    def render(self):
        self.window.clear()
        #Draw borders
        self.window.border(
            self.edges[0], self.edges[0],
            self.edges[1], self.edges[1],
            self.edges[2], self.edges[2],
            self.edges[2], self.edges[2]
        )
        #Footer + header draw
        self.window.addstr(self.height + 4, 5, " " + self.footer + " ")
        self.window.addstr(0, 7, " " + self.header + " ")

        #Total size
        size_sum = 0
        for item in self.items_all:
            if item["selected"] == True:
                size_sum += item["size"]
        self.window.addstr(0, 50, " Total Size: " + str(size_sum) + " ")

        pos = 0
        options = self.items_all[self.offset:self.offset + self.height + 1]
        for option in options:
            label = ""
            if(option["selected"] == True):
                label = "[x] "
            else:
                label = "[ ] "

            self.window.addstr(pos + 2, 4, label)

            if pos == self.select:
                self.window.addstr(pos + 2, 8, option["name"], curses.A_STANDOUT)
            else:
                self.window.addstr(pos + 2, 8, option["name"])

            self.window.addstr(pos + 2, 60, str(option["size"]))

            pos += 1

        self.window.refresh()

    def window_loop(self, stdscr):
        while 1:
            self.render()
            #Check for input
            c = stdscr.getch()

            if c == ord('q') or  c == ord('Q'):
                break

            if c == ord(' '):
                if self.items_all[self.select + self.offset]["selected"] == False:
                    self.items_all[self.select + self.offset]["selected"] = True
                else:
                    self.items_all[self.select + self.offset]["selected"] = False

            if c == ord('n') or c == ord('N'):
                for item in self.items_all:
                    item["selected"] = True
            if c == ord('m') or c == ord('M'):
                for item in self.items_all:
                    item["selected"] = False

            if c == curses.KEY_ENTER:

                break

            if c == curses.KEY_UP:
                self.select -= 1
            if c == curses.KEY_DOWN:
                self.select += 1

            #Check for bounds
            #Upper bounds
            if self.select < 0:
                self.select = 0
                if self.offset > 0:
                    self.offset -= 1
            #Lower bounds
            if self.select >= self.length:
                self.select -= 1
            if self.select > self.height:
                self.select = self.height
                self.offset += 1
                if self.offset + self.select >= self.length:
                    self.offset -= 1

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
                "selected": False,
            })
        self.length = len(self.items_all)

        self.begin_window()
        curses.wrapper(self.window_loop)
        self.stop_window()