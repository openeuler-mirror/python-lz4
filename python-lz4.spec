%global _empty_manifest_terminate_build 0
Name:           python-lz4
Version:        3.1.3
Release:        2
Summary:        LZ4 Bindings for Python
License:        BSD and Zlib
URL:            https://github.com/python-lz4/python-lz4
Source0:        https://files.pythonhosted.org/packages/d9/c5/080234f5b6b698f56339edf7715d9256eca4eb3d35b36893227c399e69f9/lz4-3.1.3.tar.gz

%description
LZ4 Bindings for Python

%package -n python3-lz4
Summary:        LZ4 Bindings for Python
Provides:       python-lz4
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-bootstrap-theme
BuildRequires:  python3-flake8
BuildRequires:  python3-pkgconfig
BuildRequires:  python3-setuptools_scm
# Tests running requires
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
# General requires
Requires:       python3-sphinx
Requires:       python3-sphinx-bootstrap-theme
Requires:       python3-flake8
# Tests running requires
Requires:       python3-pytest
Requires:       python3-psutil
Requires:       python3-pytest-cov
%description -n python3-lz4
LZ4 Bindings for Python

%package help
Summary:        LZ4 Bindings for Python
Provides:       python3-lz4-doc
%description help
LZ4 Bindings for Python

%prep
%autosetup -n lz4-%{version}

%build
%py3_build


%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py test

%files -n python3-lz4 -f filelist.lst
%dir %{python3_sitearch}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Dec 03 2021 huangtianhua <huangtianhua@huawei.com> - 3.1.3-2
- Correct files include dir of python3_sitearch macro

* Thu Aug 19 2021 OpenStack_SIG <openstack@openeuler.org> - 3.1.3-1
- Package Spec generate
