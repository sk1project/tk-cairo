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
        self.widget_ctx.set_source_surface(self.buffer)
        self.widget_ctx.paint()

    def set_update(self, *args):
        if not self.flag is None:
            self.after_cancel(self.flag)
        self.flag = self.after(1, self.refresh)

    def init(self):
        print self._w
        print self.tk.interpaddr()

        self.widget_surface = _tkcairo.tk_surface_new(self._w, self.tk.interpaddr())
        self.buffer = cairo.ImageSurface(cairo.FORMAT_RGB24,
                                         self.winfo_width(), self.winfo_height())
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
        self.buffer_ctx.scale(1.0 / canvas.winfo_width(), 1.0 / canvas.winfo_height())


def draw(*args):
    canvas.buffer_ctx.set_source_rgba(0, 0, 0, 0.1)
    canvas.buffer_ctx.rectangle(0, 0, 100, 100)
    canvas.buffer_ctx.fill()
    canvas.refresh()


def redraw(*args):
    #	print canvas3.winfo_width(),canvas3.winfo_height()
    canvas3.buffer_ctx.set_source_rgb(1, 1, 1)
    canvas3.buffer_ctx.show_text('123')
    #	for cx, letter in enumerate('123'):
    #	    xbearing, ybearing, width, height, xadvance, yadvance = (canvas3.buffer_ctx.text_extents(letter))
    #	    canvas3.buffer_ctx.move_to(cx + 0.5 - xbearing - width / 2, 0.5 - ybearing - height / 2)
    #	    canvas3.buffer_ctx.show_text(letter)
    canvas3.refresh()


SIZE = 30

root = Tkinter.Tk()
canvas0 = tkCairoWidget(root, bg="white", width=700, height=50, borderwidth=1)
canvas0.pack(side="bottom", fill="x")

canvas1 = tkCairoWidget(root, bg="white", width=50, height=20, borderwidth=1)
canvas1.pack(side="left", fill="y")

canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")

canvas1 = tkCairoWidget(root, bg="white", width=50, height=20, borderwidth=1)
canvas1.pack(side="left", fill="y")

canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")

canvas1 = tkCairoWidget(root, bg="white", width=50, height=20, borderwidth=1)
canvas1.pack(side="left", fill="y")

canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")

canvas1 = tkCairoWidget(root, bg="white", width=50, height=20, borderwidth=1)
canvas1.pack(side="left", fill="y")

canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")

canvas1 = tkCairoWidget(root, bg="white", width=50, height=20, borderwidth=1)
canvas1.pack(side="left", fill="y")

canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")

canvas1 = tkCairoWidget(root, bg="white", width=50, height=20, borderwidth=1)
canvas1.pack(side="left", fill="y")

canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")
canvas = tkCairoWidget(canvas1, bg="white", width=50, height=50, borderwidth=1)
canvas.pack(side="bottom")

canvas3 = tkCairoWidget(root, bg="white", width=30, height=20, borderwidth=1)
canvas3.pack(side="right", fill="both", expand=1)

# button=Tkinter.Button(root,text="DRAW", command=draw)
# button.pack()
button = Tkinter.Button(canvas0, text="REDRAW", command=redraw)
button.pack(side="bottom")

root.geometry('%dx%d%+d%+d' % (700, 700, 700, 200))
root.mainloop()
