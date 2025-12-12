Summary:	Tool for creating Python bindings for Qt
Name:		python-sip-qt5
Version:	12.17.2
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/p/pyqt5_sip/pyqt5_sip-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-sip >= 6.5.0
# FIXME why is this not autodetected?
#Provides:	python%{py_ver}dist(pyqt5-sip) = %{version}
#Provides:	python%{pyver}dist(pyqt5-sip) = %{version}

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%{py_platsitedir}/PyQt5
%{py_platsitedir}/pyqt5_sip-%{version}.dist-info

%build -p
%set_build_flags
export LDFLAGS="%{build_ldflags} -lpython%{pyver}"
