#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-aiosignal
Version  : 1.2.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/27/6b/a89fbcfae70cf53f066ec22591938296889d3cc58fec1e1c393b10e8d71d/aiosignal-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/27/6b/a89fbcfae70cf53f066ec22591938296889d3cc58fec1e1c393b10e8d71d/aiosignal-1.2.0.tar.gz
Summary  : aiosignal: a list of registered asynchronous callbacks
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-aiosignal-license = %{version}-%{release}
Requires: pypi-aiosignal-python = %{version}-%{release}
Requires: pypi-aiosignal-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(frozenlist)

%description
=========
aiosignal
=========
.. image:: https://github.com/aio-libs/aiosignal/workflows/CI/badge.svg
:target: https://github.com/aio-libs/aiosignal/actions?query=workflow%3ACI
:alt: GitHub status for master branch

%package license
Summary: license components for the pypi-aiosignal package.
Group: Default

%description license
license components for the pypi-aiosignal package.


%package python
Summary: python components for the pypi-aiosignal package.
Group: Default
Requires: pypi-aiosignal-python3 = %{version}-%{release}

%description python
python components for the pypi-aiosignal package.


%package python3
Summary: python3 components for the pypi-aiosignal package.
Group: Default
Requires: python3-core
Provides: pypi(aiosignal)
Requires: pypi(frozenlist)

%description python3
python3 components for the pypi-aiosignal package.


%prep
%setup -q -n aiosignal-1.2.0
cd %{_builddir}/aiosignal-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641398085
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-aiosignal
cp %{_builddir}/aiosignal-1.2.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-aiosignal/2da4a3eea24ffca0a87562a6bff54344c074a108
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-aiosignal/2da4a3eea24ffca0a87562a6bff54344c074a108

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*