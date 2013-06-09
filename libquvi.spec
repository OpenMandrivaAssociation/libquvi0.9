%define major	7
%define libname	%mklibname quvi %major
%define devname	%mklibname -d quvi

Summary:	Library for parsing flash media stream URLs with C API
Name:		libquvi
Version:	0.4.1
Release:	1
Group:		Networking/Other
License:	LGPLv2+
Url:		http://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libcurl) >= 7.18.2
BuildRequires:	pkgconfig(libquvi-scripts) >= 0.4.0
BuildRequires:	pkgconfig(lua) >= 5.1

%description
libquvi is a library for parsing video download links with C API.
It is written in C and intended to be a cross-platform library.

%package -n %{libname}
Summary:	Shared library files libquvi
Group:		Networking/Other
Requires:	libquvi-scripts >= 0.4.0

%description -n %{libname}
Shared library files libquvi.

%package -n %{devname}
Summary:	Files needed for building applications with libquvi
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	quvi-devel = %{version}-%{release}

%description -n %{devname}
Files needed for building applications with libquvi.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_mandir}/man3/*

