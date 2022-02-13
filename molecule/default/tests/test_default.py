import pytest


@pytest.fixture
def role_vars(host):
    """Loading standard role variables."""
    defaults_files = "file=./defaults/main.yml name=role_defaults"
    vars_files = "file=./vars/main.yml name=role_vars"

    ansible_vars = host.ansible("include_vars", defaults_files)["ansible_facts"]["role_defaults"]
    ansible_vars.update(
        host.ansible("include_vars", vars_files)["ansible_facts"]["role_vars"]
    )
    return ansible_vars


def test_hostname(host):
    """Check the hostname."""
    expected_hostname = host.ansible.get_variables().get("inventory_hostname")
    fact_hostname = host.run("hostname").stdout
    assert fact_hostname == expected_hostname, "The host name is incorrect"


def test_base_packages(host, role_vars):
    """Check that all standard packages are installed."""
    packages = role_vars.get("bootstrap_apt_packages")
    for package in packages:
        pkg = host.package(package)
        assert pkg.is_installed, f"{package} is not installed"


def test_ntp_package(host):
    """Checking the installation and operation of the NTP service."""
    ntp = host.package("ntp")
    ntp_service = host.service("ntp")
    assert ntp.is_installed, "NTP is not installed"
    assert ntp_service.is_running, "NTP service is not running"
    assert ntp_service.is_enabled, "NTP service is not enabled"


def test_timezone(host, role_vars):
    """Check the set time zone in the system."""
    expected_timezone = role_vars.get("bootstrap_timezone")
    fact_timezone = host.run("timedatectl show | grep 'Timezone' | awk -F '=' '{ print $2 }'").stdout
    assert expected_timezone == fact_timezone, "Invalid time zone"
