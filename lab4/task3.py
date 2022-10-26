def delete(list_, index=None):
    if index is None:
        return list_[:-1]
        # del list_[-1]
    else:
        return list_[:index]+list_[index+1:]
        # del list_[index]

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
