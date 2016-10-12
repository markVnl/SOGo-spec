Name:           libwbxml
Version:        0.11.2
Release:        3%{?dist}
Summary:        Library and tools to parse, encode and handle WBXML documents
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://libwbxml.opensync.org/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake, expat-devel, perl
Obsoletes:      wbxml2 <= 0.9.3

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce
bandwidth in mobile communications.

%package devel
Group:         Development/Libraries
Summary:       Development files of %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
Provides:      wbxml2-devel = %{version}-%{release}
Obsoletes:     wbxml2-devel <= 0.9.3

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
# Upstream does not support in-source-directory building
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake ..
popd
make -C %{_target_platform} %{?_smp_mflags}

%install
make -C %{_target_platform} install/fast DESTDIR=$RPM_BUILD_ROOT
rm -r $RPM_BUILD_ROOT/usr/share/doc/%{name}

%check
cd %{_target_platform}
ctest

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS BUGS ChangeLog COPYING GNU-LGPL NEWS README References THANKS TODO
%{_bindir}/*
%{_libdir}/libwbxml2.so.*

%files devel
%{_datadir}/cmake/Modules/*
%{_includedir}/*
%{_libdir}/libwbxml2.so
%{_libdir}/pkgconfig/libwbxml2.pc

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Petr Pisar <ppisar@redhat.com> - 0.11.2-1
- 0.11.2 bump

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 0.11.1-1
- 0.11.1 bump
- The license is LGPLv2+ only for all the code

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 23 2011 Petr Pisar <ppisar@redhat.com> - 0.11.0-1
- 0.11.0 bump: This version breaks API
- Add GPLv2+ to license tag because of xml2wbxml_tool
- Remove explicit defattr spec code

* Thu Feb 10 2011 Petr Pisar <ppisar@redhat.com> - 0.10.9-3
- Correct devel dependency typo

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 08 2011 Petr Pisar <ppisar@redhat.com> - 0.10.9-1
- 0.10.9 bump
- Remove BuildRoot stuff
- Make devel subpackage ISA specific

* Tue Aug 10 2010 Petr Pisar <ppisar@redhat.com> - 0.10.8-1
- 0.10.8 import
- based on and obsoletes wbxml2-0.9.2-16
