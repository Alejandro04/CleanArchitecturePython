def validate_email_format(email):
    if '@' not in email:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    local_part, domain_part = parts

    if not local_part or not domain_part:
        return False

    if '.' not in domain_part:
        return False

    return True