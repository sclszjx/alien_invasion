# -*- coding: gbk -*-
class Settings():
    """�洢�����������֡����������õ���"""
    
    def __init__(self):
        """��ʼ����Ϸ������"""
        # ��Ļ����
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # �ɴ���λ��
        self.ship_speed_factor = 1.5

        # �ӵ�����
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
