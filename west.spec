Summary:	Tools for building and working with the Zephyr RTOS
Name:		west
Version:	1.5.0
Release:	1
Group:		Development
License:	Apache 2.0
Url:		https://pypi.org/project/west/
Source0:	https://files.pythonhosted.org/packages/source/w/west/west-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pykwalify)
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Tools for building and working with the Zephyr RTOS

%files
%{_bindir}/west
%{py_puresitedir}/west
%{py_puresitedir}/west*.*-info

#------------------------------------------------------------
%prep
%autosetup -p1

%build
%set_build_flags

export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%{__python} setup.py \
	install \
	--root="%{buildroot}" --skip-build --optimize=1
