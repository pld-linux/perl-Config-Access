%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	Access
Summary:	Config::Access - Perform simple access control
Name:		perl-Config-Access
Version:	0.02
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Config::Access module provides a method of authenticating arbitrary
client/service pairs in a way very similar to that provided by the TCP
wrappers by Wietse Venema <wietse@wzv.win.tue.nl> but not limited to
inetd services and IP/host names.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Config/Access.pm
%{_mandir}/man3/*
