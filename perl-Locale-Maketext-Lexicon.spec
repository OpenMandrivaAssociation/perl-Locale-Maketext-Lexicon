%define modname	Locale-Maketext-Lexicon
%define modver	1.00

Summary:	Perl module to use other catalog formats in Maketext
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Locale/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel

%description
Locale::Maketext::Lexicon is a module providing lexicon-handling backends, for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the Tie interface.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{perl_vendorlib}/Locale
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

