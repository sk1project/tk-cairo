#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (C) 2009-2017 by Igor E. Novikov
#
# This library is covered by GNU Library General Public License.
# For more info see COPYRIGHTS file in sK1 root directory.


import Tkinter
import cairo
import _tkcairo

# !/usr/bin/env python

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
        self.bind("<Visibility>", self.refresh)
        self.bind("<Expose>", self.refresh)
        self.bind("<Configure>", self.refresh)
        self.bind("<Property>", self.refresh)

    def refresh(self, *args):
        self.init()
        if not self.buffer or not self.widget_surface:return
        self.draw()
        self.widget_ctx.set_source_surface(self.buffer)
        self.widget_ctx.paint()

    def set_update(self, *args):
        if not self.flag is None:
            self.after_cancel(self.flag)
        self.flag = self.after(1, self.refresh)

    def init(self):
        self.widget_surface = _tkcairo.tk_surface_new(self._w, self.tk.interpaddr())
        if not self.widget_surface: return
        w, h = self.winfo_width(), self.winfo_height()
        if not w or not h: return
        self.buffer = cairo.ImageSurface(cairo.FORMAT_RGB24, w, h)
        self.widget_ctx = cairo.Context(self.widget_surface)
        self.buffer_ctx = cairo.Context(self.buffer)

    def reinit(self, *arg):
        self.init()
        self.draw()

    def clear(self):
        self.buffer_ctx.set_source_rgb(1, 1, 1)
        self.buffer_ctx.rectangle(0, 0, self.winfo_width(), self.winfo_height())
        self.buffer_ctx.fill()

    def draw(self):
        self.clear()

        self.buffer_ctx.scale(self.winfo_width() / 1.0, self.winfo_height() / 1.0)

        pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
        pat.add_color_stop_rgba(1, 1, 1, 0, 1)
        pat.add_color_stop_rgba(0, 0, 0, 1, 1)

        self.buffer_ctx.rectangle(0, 0, 1, 1)
        self.buffer_ctx.set_source(pat)
        self.buffer_ctx.fill()

        pat = cairo.RadialGradient(0.45, 0.4, 0.1,
                                   0.4, 0.4, 0.5)
        pat.add_color_stop_rgba(0, 1, 0, 1, 1)
        pat.add_color_stop_rgba(1, 0, 1, 0, 1)

        self.buffer_ctx.set_source(pat)
        self.buffer_ctx.arc(0.5, 0.5, 0.3, 0, 2 * 3.14)
        self.buffer_ctx.fill()
        self.buffer_ctx.scale(1.0 / self.winfo_width(), 1.0 / self.winfo_height())


root = Tkinter.Tk()
canvas0 = tkCairoWidget(root, bg="white", width=700, height=500, borderwidth=1)
canvas0.pack(side="top", fill="both")

button = Tkinter.Button(root, text="REDRAW", command=canvas0.refresh)
button.pack(side="bottom")

root.geometry('%dx%d%+d%+d' % (700, 700, 700, 200))
root.mainloop()
