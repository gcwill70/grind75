# solution 1:
# hash map with emails as primary key. ignore duplicates.
# sort map by values
# merge entries that have the same value (name)
# swap keys with values

# solution 2:
# sort the list by name - O(N*logN)
# collect entries with the same key (name) and merge email lists and sort - O(N*MlogM)

# solution 3:
# merged = [accounts[0]]
# for each


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # sort list by name
        accounts.sort(key=lambda account: account[0])
        merged = [accounts[0]]
        i = 1
        while i < len(accounts):  # iterate through accounts
            j = i
            # find all duplicates
            while j < len(accounts) and accounts[j][0] == accounts[i][0]:
                j += 1
            # create sorted list of all emails
            emails = []
            for k in range(i, j):
                for email in accounts[k][1:]:
                    if email not in emails:
                        emails.append(email)
            # add sorted list to merged
            merged.append([accounts[i][0]] + emails)
            # move to next non-duplicate
            i = j
        return merged
