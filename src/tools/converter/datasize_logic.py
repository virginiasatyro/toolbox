from typing import NamedTuple


BYTE_TO_KB = 1024
KB_TO_MB = 1024
MB_TO_GB = 1024
GB_TO_TB = 1024


class DataSizeConversion(NamedTuple):
    bytes_val: float
    kb: float
    mb: float
    gb: float
    tb: float


def convert_data_size(value: float, from_unit: str) -> DataSizeConversion:
    """Convert data size between Byte, KB, MB, GB, TB.
    
    Args:
        value: Size value
        from_unit: "B", "KB", "MB", "GB", or "TB"
    
    Returns:
        DataSizeConversion with all units
    """
    from_unit = from_unit.strip().upper()
    
    if from_unit == "B":
        bytes_val = value
    elif from_unit == "KB":
        bytes_val = value * BYTE_TO_KB
    elif from_unit == "MB":
        bytes_val = value * BYTE_TO_KB * KB_TO_MB
    elif from_unit == "GB":
        bytes_val = value * BYTE_TO_KB * KB_TO_MB * MB_TO_GB
    elif from_unit == "TB":
        bytes_val = value * BYTE_TO_KB * KB_TO_MB * MB_TO_GB * GB_TO_TB
    else:
        raise ValueError("from_unit must be 'B', 'KB', 'MB', 'GB', or 'TB'")
    
    return DataSizeConversion(
        bytes_val=round(bytes_val, 2),
        kb=round(bytes_val / BYTE_TO_KB, 2),
        mb=round(bytes_val / (BYTE_TO_KB * KB_TO_MB), 2),
        gb=round(bytes_val / (BYTE_TO_KB * KB_TO_MB * MB_TO_GB), 2),
        tb=round(bytes_val / (BYTE_TO_KB * KB_TO_MB * MB_TO_GB * GB_TO_TB), 2),
    )
