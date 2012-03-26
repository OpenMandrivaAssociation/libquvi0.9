%define major 7
%define libname %mklibname quvi %major
%define develname %mklibname -d quvi

Name:           libquvi
Version:        0.4.1
Release:        1
Summary:        Library for parsing flash media stream URLs with C API
Group:          Networking/Other
License:        LGPLv2+
URL:            http://quvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/quvi/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(libcurl) >= 7.18.2
BuildRequires: pkgconfig(libquvi-scripts) >= 0.4.0
BuildRequires: pkgconfig(lua) >= 5.1

%description
libquvi is a library for parsing video download links with C API.
It is written in C and intended to be a cross-platform library.

%package -n %libname
Summary: Shared library files libquvi
Group: Networking/Other
Requires: libquvi-scripts >= 0.4.0

%description -n %libname
Shared library files libquvi.

%package -n %develname
Summary: Files needed for building applications with libquvi
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: quvi-devel = %{version}-%{release}

%description -n %develname
Files needed for building applications with libquvi.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
rm -f %buildroot%{_libdir}/*.la

%files -n %libname
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %develname
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_mandir}/man3/*
