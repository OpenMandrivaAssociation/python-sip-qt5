Summary:	Tool for creating Python bindings for Qt
Name:		python-sip-qt5
Version:	12.7.1
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt5_sip/PyQt5_sip-%{version}.tar.gz
#Patch0:		sip-4.19.10-destdir.patch
#Patch1:		sip-4.19.10-py2.patch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-sip >= 1:5.0.0

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files -f %{name}.list

#------------------------------------------------------------
%prep
%autosetup -p1 -n PyQt5_sip-%{version}

%build
%setup_compile_flags

export LDFLAGS="%{ldflags} -lpython3.8"

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
