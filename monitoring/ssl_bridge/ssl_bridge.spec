Name:         ssl_bridge
Source0:      %{name}-%{version}.tar.gz
Version:      1.9.1
Release:      1%{?dist}
Summary:      SSL bridge
# This src.rpm is cannonical upstream
# You can obtain it using this set of commands
# git clone git://git.fedorahosted.org/git/spacewalk.git/
# cd monitoring/ssl_bridge
# make srpm
URL:          https://fedorahosted.org/spacewalk
BuildArch:    noarch
Requires:     perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Group:        Development/Libraries
License:      GPLv2
Buildroot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:     nocpulse-common

%description
NOCpulse provides application, network, systems and transaction monitoring,
coupled with a comprehensive reporting system including availability,
historical and trending reports in an easy-to-use browser interface.

This package provides an authenticating relay between an SSL client and an 
unencrypted server.

%prep
%setup -q


%build
#Nothing to build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 ssl_bridge.pl $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(-,root,root,-)
{_bindir}/ssl_bridge.pl

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Sep 11 2008 Miroslav Suchý <msuchy@redhat.com> 1.9.1-1
- removing logrotate, it is hadled by nocpulse-common 
- clean up spec to comply with Fedora

* Thu Jun 19 2008 Miroslav Suchy <msuchy@redhat.com>
- migrating nocpulse home dir (BZ 202614)

* Mon Jun 16 2008 Milan Zazrivec <mzazrivec@redhat.com> 1.9.0-5
- cvs.dist import
