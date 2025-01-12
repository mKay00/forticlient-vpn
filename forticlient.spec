Name:           forticlient
Version:        7.4.0.1636
Release:        1%{?dist}
Summary:        The VPN-only version of FortiClient offers SSL VPN and IPSecVPN
Group:          Misc

License:        https://www.fortinet.com/content/dam/fortinet/assets/legal/EULA.pdf
URL:            https://www.fortinet.com/support/product-downloads#vpn
Source0:        https://links.fortinet.com/%{name}/rhel/vpnagent

%description
The FortiClient VPN-only version provides secure remote access through
SSL VPN and IPSecVPN protocols, allowing users to connect to corporate
networks securely from various locations.

%prep
rpm2cpio %{_sourcedir}/vpnagent | cpio -idmv

%install
QA_RPATHS=0x0002
cp -r etc lib opt usr %{buildroot}

%files
/*

%changelog
* Sun Jan 12 13:14:31 CET 2025 Mario Kneidinger
- Created package
