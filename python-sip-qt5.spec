Summary:	Tool for creating Python bindings for Qt
Name:		python-sip-qt5
Version:	12.9.0
Release:	2
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt5_sip/PyQt5_sip-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-sip 
# FIXME why is this not autodetected?
Provides:	python3.11dist(pyqt5-sip) = %{version}
Provides:	python3dist(pyqt5-sip) = %{version}

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files -f %{name}.list

%prep
%autosetup -p1 -n PyQt5_sip-%{version}
# Some c files are pre-built with an outdated (and incompatible with
# python 3.11) version of cython -- rebuild them
cd sip-qt5
cython _quoting_c.pyx
# Not sure if this is a bug in cython or in python itself -- PyFrameObject
# is being used, but the header defining it isn't pulled in.
# Either way it's easily fixable by doing something not very nice -- patching
# precompiled code
sed -i -e '/#include "Python.h"/a#include "internal/pycore_frame.h"' _quoting_c.c

%build
%set_build_flags
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

python setup.py \
	build

%install
python setup.py \
	install \
	--root="%{buildroot}" \
	--record="%{name}.list"

%check
python setup.py \
	check
