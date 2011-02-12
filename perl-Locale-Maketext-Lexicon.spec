%define upstream_name	 Locale-Maketext-Lexicon
%define upstream_version 0.85

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module to use other catalog formats in Maketext
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(YAML)

BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Locale::Maketext::Lexicon is a module providing lexicon-handling backends, for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the Tie interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{perl_vendorlib}/Locale
%{_bindir}/*
%{_mandir}/*/*
