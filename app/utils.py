import hashlib
from typing import Dict, Any
from datetime import datetime

def mask_ip(ip,method):
    if method == 'sha256':
        return hashlib.sha256(ip.encode("utf-8")).hexdigest()
    elif method == 'md5':
        return hashlib.md5(ip.encode()).hexdigest()

def mask_device_id(device_id,method):
    if method == 'sha256':
        return hashlib.sha256(device_id.encode("utf-8")).hexdigest()
    elif method == 'md5':
        return hashlib.md5(device_id.encode()).hexdigest()



def mask_data(data,method):
    masked_data = {
        "user_id": data["user_id"],
        "app_version": data["app_version"],
        "device_type": data["device_type"],
        "masked_ip": mask_ip(data["ip"],method=method),
        "locale": data["locale"],
        "masked_device_id": mask_device_id(data["device_id"],method=method),
        # Added this line to include the create_date field
        "create_date": datetime.utcnow().date()
    }
    return masked_data

