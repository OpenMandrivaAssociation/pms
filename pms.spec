%define debug_package %{nil}

Summary:	Password Management System
Name:		pms
Version:	0.94
Release: 	9
License:	GPL
Group:		File tools
URL:		http://passwordms.sourceforge.net
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}.install.patch.bz2
BuildRequires:	ncurses-devel
BuildRequires:	cdk-devel


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
install -d %{buildroot}%{_bindir}/
%makeinstall

%files
%{_bindir}/*
%defattr(644,root,root,755)
%doc README NOTES TODO
