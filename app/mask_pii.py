import hashlib
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.utils import mask_ip,mask_device_id,mask_data



# Function to create masked data record
def mask_pii_data(data):
    # Extract values from the input data
    user_id = data.get("user_id")
    device_type = data.get("device_type")
    ip = data.get("ip")
    device_id = data.get("device_id", "unknown")
    locale = data.get("locale", "unknown")
    app_version = data.get("app_version")

    print(f"Raw data: {data}")

    # Check for required fields in the input data
    if user_id is None or device_type is None or ip is None or app_version is None:
        print(f"Invalid data: {data}")
        return None

    masked_data = mask_data(data,method='md5')

    return masked_data