Summary:	Poly/ML compiler and runtime system
Summary(pl):	Poly/ML kompilator i ¶rodowisko wykonania
Name:		polyml
Version:	4.1.3
Release:	1
License:	Cambridge University Technical Services Limited
Group:		Development/Languages
Source0:	http://www.lfcs.informatics.ed.ac.uk/software/polyml/source/%{name}-driver-%{version}.tar.gz
# Source0-md5:	814cea1cfb376d4bb3977f78bad3d5eb
Source1:	http://www.lfcs.informatics.ed.ac.uk/software/polyml/dbases/%{name}-%{version}.i386.tar.gz
# Source1-md5:	4309deffef425ef2052a2bfd37539f31
Source2:	http://www.lfcs.informatics.ed.ac.uk/software/polyml/dbases/%{name}-%{version}.ppc.tar.gz
# Source2-md5:	7f9f0911ce15a146cc002ac55efc34c2
Source3:	http://www.lfcs.informatics.ed.ac.uk/software/polyml/dbases/%{name}-%{version}.sparc.tar.gz
# Source3-md5:	8a9ebd594f8c13cd45184db7ec3687dd
Patch0:		%{name}-opt.patch
URL:		http://www.polyml.org/
BuildRequires:	lesstif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} ppc sparc sparc64

%description
Poly/ML is a full implementation of Standard ML available as
open-source. This release supports the ML97 version of the language
and the Standard Basis Library.

%description -l pl
Poly/ML jest pe³n± implementacj± Standard ML dostêpn± jako
open-source. To wydanie wspiera wersjê ML97 jêzyka oraz bibliotekê
standardow± (Standard Basis Library).

%define		_dbver		%(echo %{version} | tr -d .)

%prep
%setup -q -c
%patch0 -p1

%ifarch %{ix86}
tar -zxf %{SOURCE1}
%endif
%ifarch ppc
tar -zxf %{SOURCE2}
%endif
%ifarch sparc sparc64
tar -zxf %{SOURCE3}
%endif

%build
cd driver
# it is not autoconf's configure script!, takes no parameters
./configure
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	DEFAULT_POLYPATH='\".:%{_libdir}/poly\"'
cd -

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/poly

install driver/poly $RPM_BUILD_ROOT%{_bindir}/poly
install DB%{_dbver}Release $RPM_BUILD_ROOT%{_libdir}/poly

cd $RPM_BUILD_ROOT%{_libdir}/poly
ln -s DB%{_dbver}Release ML_dbase
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc driver/LICENCE
%attr(755,root,root) %{_bindir}/poly
%dir %{_libdir}/poly
%attr(444,root,root) %{_libdir}/poly/*
