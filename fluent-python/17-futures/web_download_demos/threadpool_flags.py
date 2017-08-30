# -*- coding: utf-8 -*-


from concurrent import futures

from flags import save_flag, get_flag, show, main


MAX_WORKERS = 20


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


# Inspect `futures` object
def download_many_ac(cc_list):
    """Using `futures.as_completed`
    The higher level `executor.map` call is replaced by two for loops:
    one to create and schedule the futures,
    the other to retrieve their results.
    """
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many)
    # main(download_many_ac)
