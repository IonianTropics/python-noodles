
class CookieClicker:

    def __init__(self, cps):
        self.cps = cps
        return

    def set_cps(self, cps):
        self.cps = cps
        return True

    def min_cookies(self):
        return self.cps*55944000

