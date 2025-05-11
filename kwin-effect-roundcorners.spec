Summary:        KDE KWin effect to round the corners of windows
Name:           kwin-effect-roundcorners
Version:        0.7.2
Release:        1
License:        GPL-3.0
URL:            https://github.com/matinlotfali/KDE-Rounded-Corners
Source0:        https://github.com/matinlotfali/KDE-Rounded-Corners/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem: cmake
# Cmake places files in {_libdir} but plugins require to be in {_qtdir}
BuildOption: -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR=%{_qtdir}

# Build requirements
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KWin)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6QmlAssetDownloader)
BuildRequires:  pkgconfig(Qt6QmlCore)
BuildRequires:  pkgconfig(Qt6QmlNetwork)
BuildRequires:  appstream
BuildRequires:  vulkan-headers
BuildRequires:  qt6-qtbase-theme-gtk3

%description
KDE Rounded Corners is a desktop effect for KWin that smoothly rounds
the corners of all windows and optionally adds an outline, with
minimal impact on performance.

%prep
%setup -q -n KDE-Rounded-Corners-%{version}

%files
%license LICENSE
%doc README.md
%{_qtdir}/plugins/kwin/effects/configs/kwin_shapecorners_config.so
%{_qtdir}/plugins/kwin/effects/plugins/kwin4_effect_shapecorners.so
%{_datadir}/kwin/shaders/shapecorners.frag
%{_datadir}/kwin/shaders/shapecorners_core.frag
%{_datadir}/locale/*/LC_MESSAGES/kcmcorners.mo*
