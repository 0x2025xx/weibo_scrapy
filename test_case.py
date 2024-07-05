# coding:utf-8


def get_douban_info():
    #
    import requests

    url = 'https://movie.douban.com/top250?start='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    # return

    def fetch(session, page):
        with (session.get(f'{url}{page * 25}', headers=headers) as r,
              open(f'./douban_movie_html/top250-{page}.html', 'w') as f):
            f.write(r.text)

    def run_task():
        with requests.Session() as session:
            for p in range(25):
                fetch(session, p)
        return

    def run_task2():
        from multiprocessing import Pool

        with requests.Session() as session:
            data = ([(session, p) for p in range(25)])
            print(data)

        def fetch_proj(session, page):
            with (session.get(f'{url}{page * 25}', headers=headers) as r,
                  open(f'./douban_movie_html/top250-{page}.html', 'w') as f):
                f.write(r.text)

        with (Pool() as pool, requests.Session() as session):
            pool.starmap(fetch_proj, data)

        return

    # run_task()
    # run_task2()


if __name__ == '__main__':
    get_douban_info()

    print('=end=')
