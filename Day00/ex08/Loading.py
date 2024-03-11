def ft_tqdm(lst: range) -> None:  # type: ignore
    """
    The yield statement suspends a function s execution \
        and sends a value back to the caller, but retains enough \
            state to enable the function to resume where it left off. \
                When the function resumes, it continues execution immediately\
                    after the last yield run. This allows its code to \
                        produce a series of values over time, rather than \
                            computing them at once and sending them back \
                                like a list.
    """
    for i in lst:
        yield i
        percent = int(((i+1)/len(lst)) * 100)
        print(f'{percent}%|{(percent) * '='}>{(100 - percent) * ' '}| \
{i+1}/{len(lst)}', end='\r')
