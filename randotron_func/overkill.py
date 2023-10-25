def uniform_dis(n, b0, b1, seed=420):
    alpha = 12512312123
    const = 12314124124
    m = 2 << 31
    state = seed
    samples = []
    for _ in range(n):
        state = (alpha * state + const) % m
        sample = b0 + (b1 - b0) * (state / m)
        samples.append(sample)
    return samples


def random_merge_sort(l):
    if len(l) <= 1:
        return l
    n = len(l) // 2
    left = random_merge_sort(l[:n])
    right = random_merge_sort(l[n:])

    return random_merge(left, right)


def random_merge(left, right):
    combined = []
    while left and right:
        chosen_list = left if r_l[len(combined)] == 'l' else right
        if chosen_list == left and left:
            combined.append(left.pop(0))
        elif chosen_list == right and right:
            combined.append(right.pop(0))
    combined.extend(left if left else right)
    return combined


people = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7']
ud = uniform_dis(len(people) + 1, 0, 3)
r_l = ['l' if i < 1.5 else 'r' for i in ud]
order = random_merge_sort(people)
print(order)
