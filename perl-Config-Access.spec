%include	/usr/lib/rpm/macros.perl
Summary:	Config-Access perl module
Summary(pl):	Modu³ perla Config-Access
Name:		perl-Config-Access
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Config/Config-Access-%{version}.tar.gz
BuildRequires:	rpm-perlprov
BuildRequires:	perl >= 5.005_03-13
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Config-Access perl module.

%description -l pl
Modu³ perla Config-Access.

%prep
%setup -q -n Config-Access-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Config/Access
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Config/Access.pm
%{perl_sitearch}/auto/Config/Access

%{_mandir}/man3/*
