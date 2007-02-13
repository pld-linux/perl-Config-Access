%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	Access
Summary:	Config::Access - perform simple access control
Summary(pl.UTF-8):	Config::Access - wykonywanie prostej kontroli dostępu
Name:		perl-Config-Access
Version:	0.02
Release:	11
License:	free
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8d90b7c317ce3144410b26a34fad026e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Config::Access module provides a method of authenticating
arbitrary client/service pairs in a way very similar to that provided
by the TCP wrappers by Wietse Venema <wietse@wzv.win.tue.nl> but not
limited to inetd services and IP/host names.

%description -l pl.UTF-8
Moduł Config::Access udostępnia metodę do autoryzacji dowolnej pary
klient/usługa w sposób bardzo podobny do udostępnianego przez TCP
wrappers autorstwa Wietse Venemy, ale nie ograniczony do usług inetd
ani nazwy/IP komputera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Config/Access.pm
%{_mandir}/man3/*
