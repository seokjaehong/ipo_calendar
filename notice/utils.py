from account.models import User
from stocks.models import IPO


def get_ipo_list():
    result =[]
    # for user in User.objects.all():
    #     p_ipo_list = IPO.objects.filter(is_finished=False, stock_brokers__in=user.accounts.all()).distinct()
    #     result.append(
    #         {'user':user , 'p_ipo_list':p_ipo_list}
    #     )
    user = User.objects.filter(id=2).first()
    p_ipo_list = IPO.objects.filter(is_finished=False, stock_brokers__in=user.accounts.all()).distinct()
    print(p_ipo_list)
    return result

if __name__ == '__main__':
    aa=get_ipo_list()
    print(len(aa))
    for a in aa:
        print(a)