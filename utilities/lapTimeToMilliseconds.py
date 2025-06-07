import pandas as pd
def lap_time_to_milliseconds(lap_time):
    """
    Converts a lap time in the format 'MM:SS.sss' to milliseconds.
    
    Parameters:
    lap_time (str): The lap time as a string in the format 'MM:SS.sss'.
    
    Returns:
    int: The lap time in milliseconds, or None if the input is invalid.
    """
    if pd.isnull(lap_time) or lap_time in ['\\N', '', None]:
        return None
    try:
        mins, secs_milisecs = lap_time.split(':')
        secs, secs_milisecs = secs_milisecs.split('.')
        return int(mins) * 60 * 1000 + int(secs) * 1000 + int(secs_milisecs)
    except Exception:
        return None