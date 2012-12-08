%define upstream_name	 Locale-Maketext-Lexicon
%define upstream_version 0.86

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl module to use other catalog formats in Maketext
License:	MIT
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(YAML)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
Locale::Maketext::Lexicon is a module providing lexicon-handling backends, for
Locale::Maketext to read from other localization formats, such as PO files,
MO files, or from databases via the Tie interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.860.0-5mdv2012.0
+ Revision: 765393
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.860.0-4
+ Revision: 763909
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.860.0-3
+ Revision: 667223
- mass rebuild

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.860.0-2
+ Revision: 640744
- rebuild to obsolete old packages

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.860.0-1
+ Revision: 638485
- update to new version 0.86

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.850.0-1
+ Revision: 637368
- update to new version 0.85

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.840.0-1mdv2011.0
+ Revision: 625274
- update to new version 0.84

* Sat Dec 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.830.0-1mdv2011.0
+ Revision: 622842
- update to new version 0.83

* Sat Sep 04 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.820.0-2mdv2011.0
+ Revision: 575951
- extract deps from meta.yml

* Sun Apr 18 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.820.0-1mdv2011.0
+ Revision: 536188
- update to 0.82

* Fri Apr 09 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.800.0-1mdv2010.1
+ Revision: 533391
- update to 0.80

* Wed Mar 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.790.0-1mdv2010.1
+ Revision: 513797
- update to 0.79

* Wed Feb 24 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.780.0-1mdv2010.1
+ Revision: 510521
- update to 0.78

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.770.0-1mdv2010.0
+ Revision: 403393
- rebuild using %%perl_convert_version

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.77-1mdv2009.1
+ Revision: 324508
- update to new version 0.77

* Tue Dec 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.76-1mdv2009.1
+ Revision: 314752
- update to new version 0.76

* Wed Nov 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2009.1
+ Revision: 307066
- update to new version 0.75

* Sun Nov 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.74-1mdv2009.1
+ Revision: 305986
- update to new version 0.74

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.73-1mdv2009.1
+ Revision: 299389
- update to new version 0.73

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-1mdv2009.1
+ Revision: 292557
- update to new version 0.71

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2009.0
+ Revision: 277951
- update to new version 0.68

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.67-1mdv2009.0
+ Revision: 270390
- update to new version 0.67

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.66-4mdv2009.0
+ Revision: 257646
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.66-3mdv2009.0
+ Revision: 245701
- rebuild

* Wed Feb 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdv2008.1
+ Revision: 166954
- update to new version 0.66

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.65-1mdv2008.1
+ Revision: 138047
- update to new version 0.65

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 0.64-1mdv2008.0
+ Revision: 44517
- new release


* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.62-1mdv2007.0
- New version 0.62

* Thu May 04 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.61-2mdk
- Fix license

* Tue May 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.61-1mdk
- New release 0.61

* Thu Apr 13 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.60-1mdk
- new release

* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.56-1mdk
- New release 0.56

* Wed Mar 22 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.55-1mdk
- 0.55

* Thu Mar 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.54-1mdk
- 0.54

* Mon Dec 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.53-1mdk
- 0.53

* Mon Nov 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.50-1mdk
- 0.50

* Mon Jun 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.49-2mdk 
- don't ship useless empty dirs
- spec cleanup
- make test in %%check

* Fri Apr 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.49-1mdk
- 0.49

* Mon Mar 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.48-1mdk
- 0.48

* Fri Feb 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.47-1mdk
- 0.47

* Thu Dec 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.46-1mdk
- New version 0.46
- Drop patch 0, upstreamed (although titi's new option was renamed from
  export_all to allow_empty)

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.45-2mdk
- fix buildrequires in a backward compatible way

* Tue Dec 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.45-1mdk
- 0.45
- Adapt patch 0 to new version

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.44-4mdk 
- rebuild

* Thu Oct 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.44-3mdk
- actually apply patch 0 ...

* Tue Oct 12 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.44-2mdk
- patch 0: add support for export_all

* Mon Oct 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.44-1mdk
- New version 0.44 ; remove MANIFEST, add Changes and README in docs

* Mon Aug 30 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.42-1mdk
- New version

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.38-2mdk 
- rebuild

* Wed Apr 28 2004 Michael Scherer <misc@mandrake.org> 0.38-1mdk
- New release 0.38

* Fri Apr 02 2004 Michael Scherer <misc@mandrake.org> 0.36-1mdk 
- First MandrakeSoft Package

