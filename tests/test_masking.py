import pytest
from app.utils import mask_ip
from app.utils import mask_data

def test_mask_pii_sha256():
    input_data = "241.6.88.151"
    expected_output = "7b03f7d723535706b4777384fc906d18a4376bb84cebb50dc22c6eb9bddf00cb"

    # Test if the mask_pii function returns the correct SHA-256 hash for the given input
    assert mask_ip(input_data,'sha256') == expected_output

def test_mask_pii_md5():
    input_data = "241.6.88.151"
    expected_output = "177bc093bf2ec84c9c4132428c362658"

    # Test if the mask_pii function returns the correct SHA-256 hash for the given input
    assert mask_ip(input_data,'md5') == expected_output

# def test_mask_pii_invalid_method():
#     data = {"user_id": "60b9441c-e39d-406f-bba0-c7ff0e0ee07f", "app_version": "0.4.6", "device_type": "android", "ip": "223.31.97.46", "locale": "FR", "device_id": "149-99-5185"}
#     with pytest.raises(ValueError):
#         # Test if the mask_pii function raises a ValueError when an invalid method is provided
#         mask_data(data, method="unsupported_method")
