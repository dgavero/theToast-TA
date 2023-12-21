import pytest


@pytest.mark.usefixtures("log_on_failure", "web_driver")
class base_tests:
    pass
