%global _enable_debug_package 0
%global debug_package %{nil}

%global commit f35e1b38665fa236ed21731d9de208ee55e82c2c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20240731T035249Z
%global tag 3.14.26

Name: wallpaper-engine-kde-plugin

Version:        %{tag}^%{git_date}.g%{shortcommit}
Release:        %autorelease
Summary:        KDE wallpaper plugin integrating wallpaper engine

License: GPLv2
URL: https://github.com/catsout/wallpaper-engine-kde-plugin

BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(plasma-workspace)
BuildRequires: pkgconfig(KF6Plasma)

BuildRequires: gstreamer1-plugin-libav
BuildRequires: lz4-devel
BuildRequires: mpv-libs-devel
BuildRequires: python3-websockets

BuildRequires: pkgconfig(Qt6Gui-private)
BuildRequires: pkgconfig(Qt6X11Extras)
BuildRequires: pkgconfig(Qt6WebChannel)
BuildRequires: pkgconfig(Qt6WebSockets)

BuildRequires: git
BuildRequires: cmake

BuildRequires: kf6-rpm-macros

%description
%{name} is a wallpaper plugin integrating wallpaper engine into the KDE wallpaper settings.

%package libs
Summary:	libs for %{name}
%description libs
%summary

%prep
git clone --single-branch --branch main https://github.com/catsout/wallpaper-engine-kde-plugin %{_builddir}/%{name}-%{version}

cd %{_builddir}/%{name}-%{version}
git checkout %{commit}
git submodule update --init --recursive

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6 -DBUILD_QML=ON -DUSE_PLASMAPKG=OFF
%cmake_build

%install
%cmake_install

%files

%changelog 
%autochangelog
