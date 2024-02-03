def _parse_d(s: dict) -> dict:
    result = {}
    
    for k, v in s.items():
        if isinstance(v, str):
            result[k] = v
            continue
        
        parsed_value = _parse_l(v) if isinstance(v, list) else _parse_d(v)
        for pk, pv in parsed_value.items():
            result[f"{k}_{pk}"] = pv
    
    return result
    

def _parse_l(s: list) -> dict[str, str]:
    result = {}
    
    for idx, v in enumerate(s):
        if isinstance(v, str):
            result[str(idx)] = v
            continue
        
        parsed_value = _parse_l(v) if isinstance(v, list) else _parse_d(v)
        for pk, pv in parsed_value.items():
            result[f"{idx}_{pk}"] = pv
        
    return result

def parse(s: list) -> dict[str, str]:
    if isinstance(s, list):
        return _parse_l(s)
    elif isinstance(s, dict):
        return _parse_d(s)
    else:
        raise TypeError("Unexpected input type")
    