Summary:	Qmail Mailing List Manager
Summary(pl):	Zarz�dca list dyskusyjnych dla qmaila
Name:		ezmlm
Version:	0.53
Release:	2
License:	Check with djb@koobera.math.uic.edu
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://cr.yp.to/software/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
URL:		http://www.qmail.org/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qmail Mailing List Manager.

%description -l pl
Qmailowy mened�er list dyskusyjnych.

%prep
%setup -q
%patch
echo "/usr/lib/ezmlm" > conf-bin

%build
cat > auto-ccld.sh <<EOF
#!/bin/sh
CC='%{__cc} %{rpmcflags}'
LD='%{__cc} %{rpmldflags}'
EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_libdir}/ezmlm}

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.5 $RPM_BUILD_ROOT%{_mandir}/man5
install ezmlm-list ezmlm-make ezmlm-sub ezmlm-unsub $RPM_BUILD_ROOT%{_bindir}
install ezmlm-manage ezmlm-reject ezmlm-return ezmlm-send ezmlm-warn \
	ezmlm-weed	$RPM_BUILD_ROOT%{_libdir}/ezmlm

gzip -9nf BLURB CHANGES README THANKS TODO VERSION

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