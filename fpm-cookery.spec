#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	A tool for building software packages with fpm
Name:		fpm-cookery
Version:	0.29.0
Release:	0.1
License:	BSD
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	bd210d6acb6a0519f8d940200917eefe
URL:		https://github.com/bernd/fpm-cookery
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-rake
BuildRequires:	ruby-rspec < 4
BuildRequires:	ruby-rspec >= 3.0
%endif
Requires:	fpm < 2
Requires:	fpm >= 1.1
Requires:	ruby-addressable
Requires:	ruby-facter
Requires:	ruby-puppet < 4
Requires:	ruby-puppet >= 3.4
Requires:	ruby-systemu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool for building software packages with fpm.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fpm-cook
%{ruby_vendorlibdir}/fpm/cookery
%{ruby_specdir}/%{name}-%{version}.gemspec
