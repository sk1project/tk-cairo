/* _tkcairo - small module for Tk surface of Cairo library.
 *
 * Copyright (C) 2017 by Igor E.Novikov
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <Python.h>
#include <pycairo.h>
#include <cairo.h>
#include <tcl.h>
#include <tk.h>

/* ------------------------- XlibSurface ------------------------------- */
#ifdef CAIRO_HAS_XLIB_SURFACE
#include <cairo-xlib.h>

static Pycairo_CAPI_t *Pycairo_CAPI;

static PyObject *
tkSurfaceNew (PyObject *self, PyObject *args)
{

	PyObject * interpaddr;
	Tcl_Interp * interp;
	Tk_Window	tkwin;
	Display * display;
	Drawable drawable;
	char * name;
	int width, height;


	if (!PyArg_ParseTuple(args, "sO:TkwinSurface.__new__", &name, &interpaddr))
		return NULL;

	interp = (Tcl_Interp*)PyInt_AsLong(interpaddr);

	tkwin = Tk_NameToWindow(interp, name, (ClientData)Tk_MainWindow(interp));
	if (!tkwin)
	{
		PyErr_SetString(PyExc_ValueError, name);
		return NULL;
	}

	drawable = Tk_WindowId(tkwin);
	if (!drawable)
	{
		PyErr_SetString(PyExc_ValueError, name);
		return NULL;
	}


	display = Tk_Display(tkwin);

	width = Tk_Width(tkwin);
	height = Tk_Height(tkwin);

	Visual *visual = DefaultVisual(display, DefaultScreen(display));

    return PycairoSurface_FromSurface (
	       cairo_xlib_surface_create(display, drawable, visual, width, height), NULL);
}

#endif  /* CAIRO_HAS_XLIB_SURFACE */


static
PyMethodDef cairo_methods[] = {
	{"tk_surface_new", tkSurfaceNew, METH_VARARGS},
	{NULL, NULL}
};

void
init_tkcairo(void)
{
    Py_InitModule("_tkcairo", cairo_methods);
    Pycairo_IMPORT;
}