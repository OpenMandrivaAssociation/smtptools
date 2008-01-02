Summary:	Tools for the Simple Mail Transfer Protocol
Name:		smtptools
Version:	0.2.3
Release:	%mkrel 3
License:	GPL
Group:		Networking/Mail
URL:		http://www.ohse.de/uwe/software/smtptools.html
Source0:	ftp://ftp.ohse.de/uwe/releases/%{name}-%{version}.tar.bz2
Patch0:		smtptools-0.2.3-no_usmtpd.diff
Patch1:		smtptools-0.2.3-resolv.diff
BuildRequires:	libtool
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This collection of commands contains tools to send and receive
messsages with SMTP.

* smtpblast can be used to send messages to remote hosts without
  having to deal with the local mail system.

* tomaildir writes a single message from a file or stdin to a
  maildir.

* maildirblast can send the contents of a maildir through smtp.
  It may either use a relay host or MX records. See the
  manualpage.

This package does not provide the usmtpd server (replacement for
the qmail-smtpd) as it would imply qmail is required.

%prep

%setup -q
%patch0 -p0
%patch1 -p0

%build
rm -f configure
libtoolize --force --copy; aclocal-1.7; autoheader; automake-1.7 --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall

# remove the usmtpd as it would imply qmail is really needed...
rm -rf %{buildroot}%{_sbindir}
rm -f %{buildroot}%{_mandir}/man1/usmtpd.1

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README README.cvs README.smtpblast README.tomaildir
%{_bindir}/*
%{_mandir}/man1/*


