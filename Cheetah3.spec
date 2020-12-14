#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Cheetah3
Version  : 3.2.6
Release  : 13
URL      : https://files.pythonhosted.org/packages/ee/6f/29c6d74d8536dede06815eeaebfad53699e3f3df0fb22b7a9801a893b426/Cheetah3-3.2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/ee/6f/29c6d74d8536dede06815eeaebfad53699e3f3df0fb22b7a9801a893b426/Cheetah3-3.2.6.tar.gz
Summary  : Cheetah is a template engine and code generation tool
Group    : Development/Tools
License  : MIT
Requires: Cheetah3-bin = %{version}-%{release}
Requires: Cheetah3-license = %{version}-%{release}
Requires: Cheetah3-python = %{version}-%{release}
Requires: Cheetah3-python3 = %{version}-%{release}
Requires: Markdown
BuildRequires : Markdown
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
It can be used standalone or combined with other tools and frameworks. Web
        development is its principle use, but Cheetah is very flexible and
        is also being used to generate C++ game code, Java, sql, form emails
        and even Python code.
        
        It's a fork of the original CheetahTemplate library.
        
        Documentation
        ================================================================================
        For a high-level introduction to Cheetah please refer to the User's Guide

%package bin
Summary: bin components for the Cheetah3 package.
Group: Binaries
Requires: Cheetah3-license = %{version}-%{release}

%description bin
bin components for the Cheetah3 package.


%package license
Summary: license components for the Cheetah3 package.
Group: Default

%description license
license components for the Cheetah3 package.


%package python
Summary: python components for the Cheetah3 package.
Group: Default
Requires: Cheetah3-python3 = %{version}-%{release}
Provides: cheetah3-python

%description python
python components for the Cheetah3 package.


%package python3
Summary: python3 components for the Cheetah3 package.
Group: Default
Requires: python3-core
Provides: pypi(cheetah3)

%description python3
python3 components for the Cheetah3 package.


%prep
%setup -q -n Cheetah3-3.2.6
cd %{_builddir}/Cheetah3-3.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601997591
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Cheetah3
cp %{_builddir}/Cheetah3-3.2.6/LICENSE %{buildroot}/usr/share/package-licenses/Cheetah3/a7186cce21fd72616b0fde6964715d4c16ea0c19
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cheetah
/usr/bin/cheetah-analyze
/usr/bin/cheetah-compile

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Cheetah3/a7186cce21fd72616b0fde6964715d4c16ea0c19

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
