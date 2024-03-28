
class UniqueList(list):
    def append(self, item):
        if item in self:
            return
        super().append(item)
i=UniqueList()
i.append(1)
i.append(2)
i.append(4)
i.append(1)
print(i)