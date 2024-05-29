def ft_filter(function, i):
    if function is None:
        return (item for item in i if item)
    else:
        return (item for item in i if function(item))
