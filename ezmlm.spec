Summary:	Qmail Mailing List Manager
Name:		ezmlm
Version:	0.53
Release:	2
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://cr.yp.to/software/%{name}-%{version}.tar.gz
Patch0:		ezmlm.patch
URL:		http://www.qmail.org/
Copyright:	Check with djb@koobera.math.uic.edu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	qmail

%description
Qmail Mailing List Manager

%description -l pl
Qmailowy mened¿er list dyskusyjnych.

%prep
%setup -q
%patch
echo "/usr/lib/ezmlm" > conf-bin

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_libdir}/ezmlm}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.5 $RPM_BUILD_ROOT%{_mandir}/man5
install ezmlm-list ezmlm-make ezmlm-sub ezmlm-unsub $RPM_BUILD_ROOT%{_bindir}
install ezmlm-manage ezmlm-reject ezmlm-return ezmlm-send ezmlm-warn \
	ezmlm-weed	$RPM_BUILD_ROOT%{_libdir}/ezmlm

gzip -9nf BLURB CHANGES README THANKS TODO VERSION \
	$RPM_BUILD_ROOT%{_mandir}/man{1,5}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BLURB,CHANGES,README,THANKS,TODO,VERSION}.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ezmlm
%attr(755,root,root) %{_libdir}/ezmlm/*
%{_mandir}/man1/*
%{_mandir}/man5/*
