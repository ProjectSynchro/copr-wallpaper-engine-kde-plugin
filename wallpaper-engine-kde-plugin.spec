%global _enable_debug_package 0
%global debug_package %{nil}

%global commit 9e55b26ec8121f0f2558060eb58f0ccb1a64c635
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20240908T180101Z
%global tag v0.5.4

Name:           wallpaper-engine-kde-plugin

Version:        %{tag}^%{git_date}.g%{shortcommit}
Release:        %autorelease
Summary:        KDE wallpaper plugin integrating wallpaper engine

License: GPLv2
URL: https://github.com/catsout/wallpaper-engine-kde-plugin

BuildRequires: pkgconfig(vulkan)

BuildRequires: plasma-workspace-devel
BuildRequires: gstreamer1-plugin-libav
BuildRequires: lz4-devel
BuildRequires: mpv-libs-devel
BuildRequires: python3-websockets

BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtwebsockets-devel
BuildRequires: qt6-qtwebchannel-devel

BuildRequires: git
BuildRequires: cmake
BuildRequires: extra-cmake-modules

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
cd %{_builddir}/%{name}-%{version}
%cmake_kf6 -DQT_MAJOR_VERSION=6 -DBUILD_QML=ON -DUSE_PLASMAPKG=OFF
%cmake_build

%install
%cmake_install

%files

%changelog 
%autochangelog
