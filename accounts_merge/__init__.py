# solution 1:
# hash map with emails as primary key. ignore duplicates.
# sort map by values
# merge entries that have the same value (name)
# swap keys with values

# solution 2:
# sort the list by name - O(N*logN)
# collect entries with the same key (name) and merge email lists and sort - O(N*MlogM)

# solution 3:
# create hash table of names and emails {'name': set('email1', 'email2', ...)}
# for each account, if name and email is shared, merged lists - O(M)
# at the end, sort email lists


class Solution:
    def __merge(self, db, name: str, items: set[str]):
        if name not in db:
            db[name] = [items]
            return
        # get indeces of colliding entries
        indeces = []
        for i in range(0, len(db[name])):
            if db[name][i] & items:
                indeces.append(i)
        # merge colliding entries
        eset = items
        val = []
        for i in range(0, len(db[name])):
            if i in indeces:
                eset |= db[name][i]
            else:
                val.append(db[name][i])
        db[name] = val + [eset]

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # create initial database
        db: dict[str, list[set[str]]] = {accounts[0][0]: [set(accounts[0][1:])]}
        # add accounts to db
        for i in range(1, len(accounts)):
            name = accounts[i][0]
            emails = set(accounts[i][1:])
            self.__merge(db, name, emails)
        # convert map to list format
        ret = []
        for name, sets in db.items():
            for eset in sets:
                eset = list(eset)
                eset.sort(key=lambda x: x)
                ret.append([name] + eset)
        return ret
