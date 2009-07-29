#!/usr/bin/env python
#
# Setup script for sK1 0.9
#
# Copyright (C) 2007 Igor E. Novikov
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
#
# Usage: 
# --------------------------------------------------------------------------
#  to build package:   python setup.py build
#  to install package:   python setup.py install
# --------------------------------------------------------------------------
#  to create source distribution:   python setup.py sdist
# --------------------------------------------------------------------------
#  to create binary RPM distribution:  python setup.py bdist_rpm
#
#  to create deb package just use alien command (i.e. rpm2deb)
#
#  help on available distribution formats: python setup.py bdist --help-formats
#

from distutils.core import setup, Extension
import os, sys

if __name__ == "__main__":

	share_dirs=[]
	for item in ['GNU_LGPL_v2', 'COPYRIGHTS']:
		share_dirs.append(item)
 
	src_path='src/'
	
	tcl_include_path = "/usr/include/tcl8.5"
	tcl_ver=""
	if os.path.isdir(tcl_include_path): 
		tcl_include_dirs = [tcl_include_path]		
		tcl_ver="8.5"
	else: tcl_include_dirs = []

 	tkcairo_src=src_path
 	tkcairo_include_dirs=['/usr/include/cairo']
 	tkcairo_include_dirs.extend(tcl_include_dirs)
	tkcairo_module = Extension('tkCairo._cairo',
			define_macros = [('MAJOR_VERSION', '1'),
						('MINOR_VERSION', '8')],
			sources = [tkcairo_src+'cairomodule.c', tkcairo_src+'pycairo-context.c', tkcairo_src+'pycairo-font.c',
					 tkcairo_src+'pycairo-matrix.c', tkcairo_src+'pycairo-path.c', tkcairo_src+'pycairo-pattern.c',
					 tkcairo_src+'pycairo-surface.c'],
			include_dirs=tkcairo_include_dirs,
			libraries=['tk'+tcl_ver, 'tcl'+tcl_ver, 'cairo'])
			
	setup (name = 'tkcairo',
			version = '1.8.6',
			description = 'python&cairo binding for Tkinter widgets',
			author = 'Igor E. Novikov',
			author_email = 'igor.e.novikov@gmail.com',
			maintainer = 'Igor E. Novikov',
			maintainer_email = 'igor.e.novikov@gmail.com',
			license = 'LGPL v2',
			url = 'http://sk1project.org',
			download_url = 'http://sk1project.org/',
			long_description = '''tkcairo is apython&cairo binding for Tkinter widgets. sK1 Team (http://sk1project.org), copyright (c) 2009 by Igor E. Novikov.
			''',
		classifiers=[
			'Development Status :: 5 - Stable',
			'Environment :: Desktop',
			'Intended Audience :: End Users/Desktop',
			'License :: OSI Approved :: LGPL v2',
			'Operating System :: POSIX',
			'Operating System :: MacOS :: MacOS X',
			'Programming Language :: Python',
			'Programming Language :: C',
			"Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
			],

			packages = ['tkCairo'],
			
			package_dir = {'tkCairo': 'src'},

			ext_modules = [tkcairo_module])
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
