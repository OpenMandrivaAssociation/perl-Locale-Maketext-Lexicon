%define module	Locale-Maketext-Lexicon
%define name	perl-%{module}
%define version 0.66
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Development/Perl
Summary:	Perl module to use other catalog formats in Maketext
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Locale/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Locale::Maketext::Lexicon is a module providing lexicon-handling backends, for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the Tie interface.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%__make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Locale
%{_bindir}/*
%{_mandir}/*/*

