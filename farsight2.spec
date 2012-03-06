%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define gst_ver 0.10.23
%define gst_plugins_base_ver 0.10.23
%define gst_plugins_good 0.10.7
%define gst_python 0.10.10

Name:           farsight2
Version:        0.0.16
Release:        1.1%{?dist}
Summary:        Libraries for videoconferencing

Group:          System Environment/Libraries
License:	LGPLv2+
URL:            http://farsight.freedesktop.org/wiki/
Source0:        http://farsight.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glib2-devel >= 2.14
BuildRequires:  gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_plugins_base_ver}
BuildRequires:	gstreamer-python-devel >= %{gst_python}
BuildRequires:	libnice-devel >= 0.0.9
BuildRequires:	gupnp-igd-devel
BuildRequires:	python-devel
BuildRequires:	pygobject2-devel

Requires:	gstreamer-plugins-good >= %{gst_plugins_good}


%description
%{name} is a collection of GStreamer modules and libraries for
videoconferencing.


%package   	python
Summary:	Python binding for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}


%description	python
Python bindings for %{name}.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires:       gstreamer-devel  >= %{gst_ver}
Requires:       gstreamer-plugins-base-devel >= %{gst_plugins_base_ver}
Requires:       pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
%configure								\
  --with-package-name='Fedora farsight2 package'			\
  --with-package-origin='http://download.fedora.redhat.com/fedora'	\
  --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}-0.0
%{_libdir}/%{name}-0.0/libmulticast-transmitter.so
%{_libdir}/%{name}-0.0/librawudp-transmitter.so
%{_libdir}/%{name}-0.0/libnice-transmitter.so
%{_libdir}/gstreamer-0.10/libfsfunnel.so
%{_libdir}/gstreamer-0.10/libfsrtpconference.so
%{_libdir}/gstreamer-0.10/libfsvideoanyrate.so
%{_libdir}/gstreamer-0.10/libfsrtcpfilter.so
%{_libdir}/gstreamer-0.10/libfsmsnconference.so


%files python
%defattr(-,root,root,-)
%{python_sitearch}/farsight.so


%files devel
%defattr(-,root,root,-)
%{_libdir}/libgstfarsight-0.10.so
%{_libdir}/pkgconfig/%{name}-0.10.pc
%{_includedir}/gstreamer-0.10/gst/farsight/
%{_datadir}/gtk-doc/html/%{name}-libs-0.10/
%{_datadir}/gtk-doc/html/%{name}-plugins-0.10/


%changelog
* Fri Dec 04 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.0.16-1.1
- Rebuilt for RHEL 6

* Tue Oct  6 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.16-1
- Update to 0.0.16.

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.0.15-2
- Rebuild for new gupnp

* Thu Sep  3 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.15-1
- Update to 0.0.15.

* Thu Aug 06 2009 Warren Togami <wtogami@redhat.com> - 0.0.14-1
- 0.0.14

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Warren Togami <wtogami@redhat.com> - 0.0.12-3
- rebuild

* Mon Jun 22 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.12-2
- Remove unnecessary requires on gst-plugins-farsight.

* Sat May 30 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.12-1
- Update to 0.0.12.

* Tue May 26 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.11-1
- Update to 0.0.11.

* Wed May 20 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.10-1
- Update to 0.0.10.

* Tue Apr  7 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.9-1
- Update to 0.0.9.

* Tue Mar 17 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.8-1
- Update to 0.0.8.
- Bump min version of gstreamer needed.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.7-2
- Add BR on gupnp-igd-devel, pygobject2-devel, and pygtk2-devel.

* Fri Jan  9 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.7-1
- Update to 0.0.7.

* Mon Jan  5 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.6-4
- Add BR on libnice-devel and build libnice transmitter.
- Set gstreamer package name & origin.

* Fri Jan 02 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.0.6-3
- Rebuild.

* Wed Dec 31 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.0.6-2
- Preserve time stamps.

* Tue Dec 16 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.0.6-1
- Initial Fedora spec.
