%global __python %{python3}
%define underscore() %(echo %1 | sed 's/-/_/g')

Summary:       ARGO probe that checks if 3DBionotes web application is working as expected
Name:          argo-probe-3dbionotes
Version:       0.1.0
Release:       1%{?dist}
Source0:       %{name}-%{version}.tar.gz
License:       ASL 2.0
Group:         Development/System
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:        %{_prefix}
BuildArch:     noarch

BuildRequires: python3-devel
Requires: python36-requests

%description
ARGO probe that checks if 3DBionotes web application is working as expected

%prep
%setup -q

%build
%{py3_build}

%install
%{py3_install "--record=INSTALLED_FILES" }

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{_libexecdir}/argo/probes/webodv/*.py[o,c]
