#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (C) 2009-2017 by Igor E. Novikov
#
# This library is covered by GNU Library General Public License.
# For more info see COPYRIGHTS file in sK1 root directory.


import Tkinter
import cairo
import _tkcairo

#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (C) 2009-2017 by Igor E. Novikov
#
# This library is covered by GNU Library General Public License.
# For more info see COPYRIGHTS file in sK1 root directory.


import Tkinter
import cairo
import _tkcairo


class tkCairoWidget(Tkinter.Frame):
    buffer = None
    buffer_ctx = None
    widget_surface = None
    widget_ctx = None
    flag = None

    def __init__(self, master, **kw):
        Tkinter.Frame.__init__(self, master, **kw)
        self.tk.call(self._w, "configure", "-background", "")
        self.bind("<Visibility>", self.set_update)
        self.bind("<Expose>", self.set_update)
        self.bind("<Configure>", self.reinit)
        self.bind("<Property>", self.reinit)


    def refresh(self):
        if self.widget_ctx is None:
            self.init()
        self.draw()
        # print 'test1'
        # self.widget_ctx.set_source_surface(self.buffer)
        # print 'test2'
        # self.widget_ctx.paint()
        # print 'test3'

    def set_update(self, *args):
        if not self.flag is None:
            self.after_cancel(self.flag)
        self.flag = self.after(1, self.refresh)


    def init(self):
        print self._w
        print self.tk.interpaddr()

        self.widget_surface = _tkcairo.tk_surface_new(self._w, self.tk.interpaddr())
        print 'here', self.widget_surface
        if not self.widget_surface: return
        self.buffer = cairo.ImageSurface(cairo.FORMAT_RGB24,
                                         self.winfo_width(), self.winfo_height())
        self.widget_ctx = cairo.Context(self.widget_surface)
        print 'here', self.widget_ctx
        self.buffer_ctx = cairo.Context(self.buffer)
        print 'here', self.buffer_ctx


    def reinit(self, *arg):
        self.init()
        self.draw()


    def clear(self):
        self.widget_ctx.set_source_rgb(1, 1, 1)
        self.widget_ctx.rectangle(0, 0, self.winfo_width(), self.winfo_height())
        self.widget_ctx.fill()


    def draw(self):
        self.clear()

root = Tkinter.Tk()
canvas0 = tkCairoWidget(root, bg="white", width=700, height=500, borderwidth=1)
canvas0.pack(side="top", fill="both")

button = Tkinter.Button(root, text="REDRAW", command=canvas0.refresh)
button.pack(side="bottom")

root.geometry('%dx%d%+d%+d' % (700, 700, 700, 200))
root.mainloop()