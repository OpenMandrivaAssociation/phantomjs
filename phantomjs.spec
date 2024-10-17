%define name phantomjs
%define version 1.7.0
%define release 1

Summary: Headless WebKit with JavaScript API
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: http://phantomjs.googlecode.com/files/%{name}-%{version}-source.zip
License: BSD
Group:	 System/Libraries
Url:	 https://phantomjs.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel

%description
PhantomJS is a headless WebKit scriptable with JavaScript or CoffeeScript. 
It is used by hundreds of developers and dozens of organizations
for web-related development workflow.

%prep
%setup -q -n %{name}-%{version}

%build
./build.sh

%install
%__rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{_bindir}
%__install -m 755 bin/phantomjs %{buildroot}%{_bindir}/phantomjs

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog CONTRIBUTING.md LICENSE.BSD README.md third-party.txt examples
%_bindir/phantomjs
