def unify(x, y, subst):
    """
    Unifies two terms x and y, returning a substitution.

    Args:
        x: The first term.
        y: The second term.
        subst: The current substitution.

    Returns:
        A substitution that unifies x and y, or None if unification fails.
    """

    if isinstance(x, str) and x.islower():
        # x is a variable
        if (x, y) not in subst:
            subst[(x, y)] = True
            return subst
        elif subst[(x, y)]:
            return subst
        else:
            return None

    elif isinstance(y, str) and y.islower():
        # y is a variable
        if (y, x) not in subst:
            subst[(y, x)] = True
            return subst
        elif subst[(y, x)]:
            return subst
        else:
            return None

    elif x == y:
        # x and y are identical
        return subst

    elif isinstance(x, list) and isinstance(y, list):
        # x and y are lists
        if len(x) != len(y):
            return None
        else:
            for i in range(len(x)):
                s = unify(x[i], y[i], subst.copy())
                if s is None:
                    return None
                subst.update(s)
            return subst

    else:
        return None


# Example usage
subst = {}
x = ['P', 'x', 'y']
y = ['P', 'a', 'f(x)']

result = unify(x, y, subst)
if result:
    print("Unification successful!")
    print("Substitution:", subst)
else:
    print("Unification failed.")