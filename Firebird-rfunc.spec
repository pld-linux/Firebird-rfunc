%define		pname	rfunc
%define		subver	rc1
Summary:	rFunc - UDF Library for InterBase/Firebird server
Name:		Firebird-rfunc
Version:	2.1.3.1
Release:	0.%{subver}.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/rfunc/%{pname}-%{version}-RC1-unix.tar.gz
# Source0-md5:	8105d437b058defb82d83aac9b665b6d
Patch0:		%{name}-makefile.patch
URL:		http://rfunc.sourceforge.net/
BuildRequires:	Firebird-devel
BuildRequires:	libuuid-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ibdir	%{_libdir}/interbase

%description
rFunc is a UDF Library for InterBase/Firebird server. The library
represents a set of user's (UDF) string, bit, numerical functions, and
also for operation with dates&time and BLOBs.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} -C source \
	CC="%{__cc}" \
	LIBDIR="%{_libdir}" \
	USERCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{ibdir}/UDF
install source/rfunc $RPM_BUILD_ROOT%{ibdir}/UDF/rfunc.so
install sql/rfunc6.sql $RPM_BUILD_ROOT%{ibdir}/UDF/rfunc.sql

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/rfunc* doc/*.css doc/img
%lang(ru) %doc doc/rus
%attr(755,root,root) %{ibdir}/UDF/rfunc.so
%{ibdir}/UDF/rfunc.sql
