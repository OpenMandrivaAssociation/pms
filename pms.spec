Summary:	Password Management System
Name:		pms
Version:	0.94
Release: 	%mkrel 7
License:	GPL
Group:		File tools
URL:		http://passwordms.sourceforge.net
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}.install.patch.bz2
BuildRequires:	ncurses-devel libcdk-devel
BuildRoot:	%{_tmppath}/%{name}-root-%{version}

%description
The Password Management System is a simple password manager for the
console which uses blowfish for encryption and CDK for the interface.
It was written for sysadmins who must handle user logins for many computers. 

%prep
%setup -q
%patch0 -p0

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%_bindir/
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/*
%defattr(644,root,root,755)
%doc README NOTES TODO



%changelog
* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.94-7mdv2009.0
+ Revision: 259111
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.94-6mdv2009.0
+ Revision: 247035
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.94-4mdv2008.1
+ Revision: 125371
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import pms


* Thu Jul 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.94-4mdk
- rebuild

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.94-3mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.94-2mdk
- rebuild

* Wed Oct 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.94-1mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Changed BuildRequires
	- Updated install patch
	- 0.94
	- Updated URL

* Thu Jun 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.93b-1mdk
- fix group typo
- fix permissions on doc files
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
        - Initial release
