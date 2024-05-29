def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 50
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        # Length of the filled part of the bar
        f_l = int(bar_length * progress)
        bar = '|' + '=' * f_l + '>' + ' ' * (bar_length - f_l - 1) + '|'
        perc = '{:.0%}'.format(progress)
        print('\r' + perc + '|' + bar + '| ' + str(i + 1) +
              '/' + str(total), end='', flush=True)
        yield item
    print('\n', end='')
