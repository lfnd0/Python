#! python

class Animal:
    @property
    def capabilities(self):
        return('sleep', 'eat', 'drink')


class Man(Animal):
    @property
    def capabilities(self):
        return super().capabilities + ('love', 'talk', 'study')


class Spider(Animal):
    @property
    def capabilities(self):
        return super().capabilities + ('make web', 'walk the walls')


class SpiderMan(Spider, Man):
    @property
    def capabilities(self):
        return super().capabilities + ('beat bandits', 'throw webs between walls')


if __name__ == "__main__":
    logan = Man()
    print(f'Logan: {logan.capabilities}')

    spider = Spider()
    print(f'Spider: {spider.capabilities}')

    peter_parker = SpiderMan()
    print(f'Peter Parker: {peter_parker.capabilities}')
