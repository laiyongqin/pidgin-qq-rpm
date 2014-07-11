Name:       lwqq
Version:	0.3.1
Release:	1
License:	GPLv3
Summary:	A Linux WebQQ Client
URL:	http://github.com/mathslinux/lwqq
Group:	Internet/Instant Messenger
Source:	%{name}-3.0.tar.bz2
BuildRequires:	cmake
BuildRequires:	gtk3-devel
BuildRequires:	libev-devel
BuildRequires:	sqlite-devel
BuildRequires:	libcurl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This Project is based on kernelhcy's gtkqq project, i rewrite the qq
library to impove its stability.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n %{name}-3.0
sed -i 's| lib| %{_lib}|' lib/CMakeLists.txt

%build
%cmake
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.so.*
%{_libdir}/pkgconfig/*.pc

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.a

%changelog
* Mon Nov 11 2013 Huaren Zhong <huaren.zhong@gmail.com> - 0.2
- Rebuild for Fedora
* Fri Jul 11 2014 Stanislav Hanzhin-Tsvetkov <hanzhin.stas@gmail.com> - 0.3.1
- Update version to 0.3.1
