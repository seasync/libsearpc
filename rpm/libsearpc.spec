%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:		libsearpc
Version:	3.1
Release:	1%{?dist}
Summary:	libsearpc - Seafile's RPC framework

Group:		Libraries
License:	Apache 2.0
URL:		https://github.com/seasync/libsearpc
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot)

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	gobject-introspection-devel
BuildRequires:  libjansson-devel
BuildRequires:  python3-base

Requires:	libjansson
Requires:	gobject-introspection
Requires:	python3-base

%description
The RPC framework for Seafile

%prep
%setup -q -n %{name}-%{version}


%build
%autogen.sh
%configure --prefix=/usr PYTHON='/usr/bin/python3'
make %{?_smp_mflags}

%install
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %name -p /sbin/ldconfig

%postun -n %name -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/searpc-codegen.py
%{_libdir}/pkgconfig/libsearpc.pc
%{_libdir}/libsearpc.*
%{python3_sitearch}/*
%{_includedir}/searpc*
