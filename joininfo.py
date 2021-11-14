from join import Join


class Infoall:
    def __init__(self):
        self.info_list = []

    def add_info(self):
        # 회원가입
        info_id = input('>> ID : ')
        # id 중복확인
        for info in self.info_list:
            if info_id == info.id:
                print('존재 하는 ID 입니다.')
                return

        new_info = Join(info_id)
        new_info.set_joininfo()

        self.info_list.append(new_info)

    def search_info(self):
        # 정보확인(본인인지 확인 절차)
        info_id = input('>> ID : ')
        searched_info = []

        for info in self.info_list:
            if info_id in info.id:
                print(info)
                searched_info.append(info)

        if len(searched_info) == 0:
            choice = input('입력하신 ID의 정보가 없습니다. ')
            return choice
