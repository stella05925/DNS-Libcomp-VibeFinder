def UIRN_RUN(s, count):
    return (UIRN_RUN(s, count - 1) ^ ord(s[count - 1])) * 16777619 if count else 2166136261

def GENHASH(X):
    return UIRN_RUN(X, len(X))
