
LOGIN_MAX_LENTH = 30
LOGIN_MIN_LENTH = 4

PASSWORD_MAX_LENTH = 30
PASSWORD_MIN_LENTH = 4

EMAIL_MAX_LENTH = 40
EMAIL_MIN_LENTH = 10

EMAIL_ERRORS = {
    "min": "Minimum email length " + str(EMAIL_MIN_LENTH) + " characters!",
    "max": "Maximum email length " + str(EMAIL_MAX_LENTH) + " characters!",
    "registered": "Current email is already registered!",
}

LOGIN_ERRORS = {
    "min": "Minimum login length " + str(LOGIN_MIN_LENTH) + " characters!",
    "max": "Maximum login length " + str(LOGIN_MAX_LENTH) + " characters!",
    "registered": "Current login is already registered!",
}

PASSWORD_ERRORS = {
    "min": "Minimum password length " + str(PASSWORD_MIN_LENTH) + " characters!",
    "max": "Maximum password length " + str(PASSWORD_MAX_LENTH) + " characters!",
    "equal": "Passwords do not match!",
    }