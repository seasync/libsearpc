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

Requires:	libjansson
Requires:	gobject-introspection

%description
The RPC framework for Seafile

%prep
%setup -q -n %{name}-%{version}


%build
%autogen.sh
%configure
make %{?_smp_mflags}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %name -p /sbin/ldconfig

%postun -n %name -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libsearpc.pc
%{_libdir}/libsearpc.a
%{_libdir}/libsearpc.la
%{_libdir}/libsearpc.so
%{_libdir}/libsearpc.so.1
%{_libdir}/libsearpc.so.1.0.2
%{_includedir}/searpc-client.h
%{_includedir}/searpc-named-pipe-transport.h
%{_includedir}/searpc-server.h
%{_includedir}/searpc-utils.h
%{_includedir}/searpc.h
