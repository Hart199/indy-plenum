import pytest


@pytest.mark.skipif(True, "Test incomplete")
def test_send_new_steward_txn(cli):
    assert cli.lastCmdOutput == "Genesis transaction added"
