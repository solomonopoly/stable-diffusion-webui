# represent a user
# each user has a standalone work dir

class User:
    def __init__(self, uid, gid, tier):
        self._uid = uid
        self._gid = gid
        self._tier = tier

    @property
    def uid(self):
        return self._uid

    @property
    def tier(self):
        return self._tier

    @classmethod
    def current_user(cls, request):
        uid = ''
        tier = ''
        if request:
            headers = request.headers
            if 'user-id' in headers:
                uid = headers['user-id']
            elif 'User-Id' in headers:
                uid = headers['User-Id']
            if 'User-Tier' in headers:
                tier = headers['User-Tier']
            elif 'user-tier' in headers:
                tier = headers['user-tier']
        if not uid:
            # consider user as anonymous if User-Id is not present in request headers
            uid = 'anonymous'
        return User(uid, '', tier)
