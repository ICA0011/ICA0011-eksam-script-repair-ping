import ping.py;

def test_ping():
    assert ping.check_server_status("http://itcollege.ee") == True
