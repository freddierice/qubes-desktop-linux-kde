# This is a meta package that makes installing all KDE components easy

%if 0%{?qubes_builder}
%define _sourcedir %(pwd)/qubes-kde-dom0
%define qubes_kde_dom0_version %(cat version)
%endif
%{!?version: %define version %(cat version)}


Name:    qubes-kde-dom0
Summary: Metapackage for installing all KDE components needed for Qubes Dom0
Version: %{qubes_kde_dom0_version}
Release: 3%{?dist}

License: GPL2
URL: http://qubes-os.org

BuildArch: noarch

Requires: qubes-desktop-linux-common
Requires: kde-filesystem
Requires: kde-settings
Requires: kde-settings-kdm
Requires: kdelibs >= %{version}
Requires: plasma-workspace
Requires: plasma-workspace-libs
#Requires: kde-workspace-wallpapers
Requires: kde-runtime >= %{version}
Requires: kde-runtime-libs >= %{version}
Requires: kde-runtime-flags >= %{version}
Requires: kde-baseapps >= %{version}
Requires: kdm
Requires: ksysguardd
Requires: oxygen-cursor-themes
Requires: oxygen-icon-theme

# other 3rd party packages that are useful in Dom0...

# The konsole really looks awful without those fonts:
Requires: dejavu-sans-mono-fonts
Requires: dejavu-sans-fonts

# This is for people who don't use NetVM (i.e. don't have VT-d hardware)
# This should be left to the user IMO
#Requires: knetworkmanager

# Qubes-customized menus
Requires: qubes-menus

# Custom Breeze style for Qubes
Requires: plasma-breeze-qubes

Source0: kfileplaces-bookmarks.xml
Source1: kickoffrc
source2: kscreensaverrc
Source3: plasma-org.kde.plasma.desktop-appletsrc

%description
%{summary}.

%install
install -D %{SOURCE0} %{buildroot}%{_sysconfdir}/skel/.kde/share/apps/kfileplaces/bookmarks.xml
install -D %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.kde/share/config/kickoffrc
install -D %{SOURCE2} %{buildroot}%{_sysconfdir}/skel/.kde/share/config/kscreensaverrc
install -D %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.config/plasma-org.kde.plasma.desktop-appletsrc

%files
%defattr (-,root,root,-)
%{_sysconfdir}/skel/.kde/share/apps/kfileplaces/bookmarks.xml
%{_sysconfdir}/skel/.kde/share/config/kickoffrc
%{_sysconfdir}/skel/.kde/share/config/kscreensaverrc
%{_sysconfdir}/skel/.config/plasma-org.kde.plasma.desktop-appletsrc

%changelog
* Mon May 24 2010 Joanna Rutkowska <joanna@invisiblethingslab.com>
- spec file adapted to Qubes OS (based on Fedora spec)
- based on the original spec from Fedora 12:

