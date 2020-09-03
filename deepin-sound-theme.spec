Name:           deepin-sound-theme
Version:        15.10.3
Release:        1
Summary:        Deepin sound theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        https://mirror.deepines.com/deepin/pool/main/d/deepin-sound-theme/%{name}_%{version}.orig.tar.xz	
BuildArch:      noarch

%description
Sound files for the Deeping Desktop Environment.

%prep
%setup -q

%build

%install
%make_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/index.theme
%{_datadir}/sounds/deepin/stereo/*.wav

%changelog
* Thu Sep 3 2020 weidong <weidong@uniontech.com> - 15.10.3-1
- Initial release for OpenEuler
