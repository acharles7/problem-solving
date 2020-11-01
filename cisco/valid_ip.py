def validIPAddress(IP: str) -> str:

    if '.' in IP:
        ip = IP.split('.')

        if len(ip) != 4: return "Neither"

        for num in ip:
            if not num: return "Neither"
            if not num.isnumeric(): return "Neither"
            elif not 0 <= int(num) <= 255: return "Neither"
            elif len(num) > 1 and num.startswith('0'): return "Neither"    
        return "IPv4"

    else:
        ip = IP.split(':')

        if len(ip) != 8: return "Neither"
        for num in ip:
            if not num: return "Neither"
            if len(num) > 4: return "Neither" 

            for char in num:
                if not char in "0123456789abcdefABCDEF":
                    return "Neither"        
        return "IPv6"

    return "Neither"

