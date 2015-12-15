%define	oname libquvi
%define major %{version}
%define api 0.9
%define libname %mklibname quvi %{major}
%define devname %mklibname -d quvi %{api}

%define _disable_rebuild_configure 1

Summary:	Library for parsing flash media stream URLs with C API
Name:		libquvi%{api}
Version:	0.9.4
Release:	17
Group:		Networking/Other
License:	AGPL
Url:		http://quvi.sourceforge.net/
Source0:	http://downloads.sourceforge.net/quvi/%{oname}-%{version}.tar.xz
Patch0:		libquvi-0.9.1-headers-reinstall.patch
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libcurl) >= 7.18.2
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libquvi-scripts-0.9)
BuildRequires:	pkgconfig(lua) >= 5.1

%description
libquvi is a library for parsing video download links with C API.
It is written in C and intended to be a cross-platform library.

%package -n %{libname}
Summary:	Shared library files libquvi
Group:		Networking/Other
Requires:	libquvi-scripts%{api} >= 0.9

%description -n %{libname}
Shared library files libquvi.

%package -n %{devname}
Summary:	Files needed for building applications with libquvi
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	quvi%{api}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d quvi} >= 0.9

%description -n %{devname}
Files needed for building applications with libquvi.

%prep
%setup -q -n %{oname}-%{version}
%apply_patches
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man3/libquvi.3  %{buildroot}%{_mandir}/man3/libquvi0.9.3
%files -n %{libname}
%{_libdir}/%{oname}-%{api}-%{major}.so

%files -n %{devname}
%{_libdir}/%{oname}-%{api}.so
%{_libdir}/pkgconfig/%{oname}-%{api}.pc
%{_includedir}/quvi-%{api}
%{_mandir}/man3/*
%{_mandir}/man7/*
