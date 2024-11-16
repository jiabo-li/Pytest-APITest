class g_context(object):
    _dic = {}

    def set_dict(self,key,value):
        self._dic[key] = value

    def get_dict_by_key(self,key):
        if key in self._dic.keys():
            return self._dic[key]
        else:
            return None

    def get_dict(self):
        return self._dic

    def show_dict(self):
        print(self._dic)