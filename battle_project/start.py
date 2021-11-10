# 飞机大战游戏
import sys  # 增加系统模块
import pygame  # 加入 py-game 模块
import pygame.locals  # 加入本地策略
import random  # 加入随机数



NAME = "Plane Battle v.1.0 姜维洋出品"  # 游戏标题名
ICO_IMAGE = "res/app.ico"   # 游戏图标
a = random.randint(1,5)
BACKGROUND_IMAGE = "res/img_bg_level_%d.jpg" % a   # 游戏背景图片
BACKGROUND_SPEED = 0.8  # 游戏背景移动速度

# ENERMY_IMAGE = "res/img-plane_%d.png" % enemyPlane.b # 敌机图片
Number_enemy = 2  # 敌机数量
Speed_enemy = 0.5  # 敌机速度
PLAY_PLANE = "res/hero.png"  # 添加玩家飞机图片的路径
IMG_BULLET = "res/bullet_10.png"  # 设置子弹图片
IMG_BOMB = "res/image 4.png"


class Model:
    window = None  # 定义主窗体对象， 用于模型访问使用
    def __init__(self, img_path, x, y):  # 定义背景图片的状态
        self.img = pygame.image.load(img_path)  # 调用背景图片的路径
        self.x = x  # 背景图片的x轴
        self.y = y  # 背景图片的y轴

    def display(self):  # 做出了对象抽取，可以适用于其他类
        Model.window.blit(self.img, (self.x, self.y))  # 将调用过的图片导入窗口里面


# TODO 1.背景类
class Background(Model):
    def move(self):  # 加入背景移动的判定
        if self.y <= Game.WINDOW_HEIGHT:
            self.y += BACKGROUND_SPEED  # 游戏背景移动
        else:  # 游戏背景回到0
            self.y = 0

    def display(self):  # 覆盖之前父类的操作
        Model.window.blit(self.img, (self.x, self.y))  # 将调用过的图片导入窗口里面
        Model.window.blit(self.img, (self.x, self.y-768))  # 将调用过的图片导入窗口里面


# TODO 2.玩家类
class PlayerPlane(Model):
    def __init__(self, img_path, x, y):  # 覆盖了玩家飞机的路径
        super().__init__(img_path, x, y)  # 调用父类的玩家飞机
        self.bullets = []  # 定义了子弹列表，默认没有子弹

    def display(self, enemys):  # 重写玩家飞机display的方法
        super().display()  # 调用父类中对于飞机加入窗体的操作
        remove_bullets = []  # 建立一个空集合用于存储超出界面的子弹
        for bullet in self.bullets:  # 循环飞机中的子弹列表
            bullet.move()  # 调用子弹的移动
            bullet.display()  # 调用子弹加入窗体中
            if bullet.y < -29:  # 如果子弹超出页面
                remove_bullets.append(bullet)  # 将超出界面的子弹存储在空列表中
            else:
                bullet_rect = pygame.locals.Rect(bullet.x, bullet.y, 20, 29)  # TODO 碰撞检测 导入子弹的矩形范围
                for enemy in enemys:
                    enemy_rect = pygame.locals.Rect(enemy.x, enemy.y, 100, 68)  # 导入敌机的矩形范围
                    if pygame.Rect.colliderect(bullet_rect,enemy_rect):  # 如果两个范围相交
                        

                        bomb = Bomb(IMG_BOMB, enemy.x, enemy.y)
                        bomb.display()

                        enemy_plane = EnemyPlane()
                        enemy.img = pygame.image.load(enemy_plane.ENERMY_IMAGE)  # 敌机恢复初始位置
                        enemy.x = random.randint(0, Game.WINDOW_WIDTH - 100)   # 敌机恢复初始位置
                        enemy.y = random.randint(-Game.WINDOW_WIDTH, 0)  # 敌机恢复初始位置

                        remove_bullets.append(bullet)  # 将子弹加入到碰撞列表里面
                        break  # 不在进行碰撞检测

        for bullet in remove_bullets:  # 对于在删除列表中的子弹
            self.bullets.remove(bullet)  # TODO 进行删除命令，会减少内存占用 这个地方要用初始列表，因为那个东西之前在初始列表里才要被删除的


# TODO 3.敌机类
class EnemyPlane(Model):
    def __init__(self):  # 定义敌机
        b = random.randint(1, 7)
        self.ENERMY_IMAGE = "res/img-plane_%d.png" % b  # 敌机图片
        self.img = pygame.image.load(self.ENERMY_IMAGE)  # 定义敌机的图片位置
        self.x = random.randint(0, Game.WINDOW_WIDTH -100)  # 定义敌机的随机x轴位置
        self.y = random.randint(-Game.WINDOW_WIDTH, 0)  # 定义敌机的随机y轴位置

    def move(self):  # 输入敌机移动命令
        if self.y > Game.WINDOW_HEIGHT:  # 输入敌机超出屏幕后，返回的命令
            self.x = random.randint(0, Game.WINDOW_WIDTH -100)  # 定义敌机移动的随机值，让它每一次移动都不确定
            self.y = random.randint(-Game.WINDOW_WIDTH, 0)
        else:
            self.y += Speed_enemy  # 定义敌机的移动速度

# 爆炸类
class Bomb(Model):
    pass


# TODO 4.子弹类
class Bullet(Model):
    def move(self):
        self.y -= 4



# TODO 5.游戏类
class Game:
    # TODO 6.主程序，运行游戏入口
    WINDOW_WIDTH = 512  # 窗口宽度值
    WINDOW_HEIGHT = 768     # 窗口高度值
    def run(self):
        self.frame_init()  # TODO 执行窗体初始化
        self.model_init()

        while True:
            pygame.display.update()  # TODO 刷新页面
            self.background.move()  # 反复移动背景图片
            self.background.display()  # 反复将背景导入游戏中
            for enemy in self.enemys:  # 让敌机依次运动起来
                enemy.move()  # 反复移动敌机
                enemy.display()  # 反复导入敌机
            self.player.display(self.enemys)  # 将玩家飞机导入游戏中
            self.event_init()  # 反复监控事件
            player_plane = pygame.locals.Rect(self.player.x, self.player.y, 100, 68)
            for enemy in self.enemys:
                enemy_rect = pygame.locals.Rect(enemy.x, enemy.y, 100, 68)
                if pygame.Rect.colliderect(player_plane,enemy_rect):
                    sys.exit()


    # TODO 初始化窗体
    def frame_init(self):  # 用来设置窗口界面
        self.window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
        Model.window = self.window  # 将主窗体进行赋值
        # 窗口宽度值 窗口高度值
        # TODO 游戏窗口设置(长度，高度)
        img = pygame.image.load(ICO_IMAGE)  # 导入ico图标图片，但不能放到窗口里
        pygame.display.set_icon(img)  # 把图标导入窗口里面
        pygame.display.set_caption(NAME)  # 设置标题文字


    def event_init(self):  # 监控事件
        for event in pygame.event.get():  # 反复访问监控 py-game 里面的事件
            if event.type == pygame.locals.QUIT:  # 如果事件里面我访问到了退出按钮
                sys.exit()  # 那么程序终止，窗口关闭
            if event.type == pygame.locals.MOUSEMOTION: # 获取鼠标的所有事件
                pos = pygame.mouse.get_pos()  # 将鼠标移动事件定义为坐标
                self.player.x = pos[0] - 100/2  # 设置玩家飞机x轴的移动为鼠标移动
                self.player.y = pos[1] - 78/2 + 6  # 设置玩家飞机y轴的移动为鼠标移动
            mouse_state = pygame.mouse.get_pressed()  # 获取鼠标按压状态
            if mouse_state[0] == 1:  # 如果鼠标按压状态为左键
                pos = pygame.mouse.get_pos()  # 那么获取鼠标位置
                self.player.bullets.append(Bullet(IMG_BULLET, pos[0] - 20/2, pos[1] - 29 - 50))  # 定义和调用子弹的路径和坐标



    def model_init(self):  # 用来给游戏添加对象
        self.background = Background(BACKGROUND_IMAGE, 0, 0)  # 调用 Background 的函数
        # 删除创建一个敌机的命令
        """self.EnemyPlane = EnemyPlane(ENERMY_IMAGE, 200, 200)
        """
        # 创建一个空集用于存放飞机
        self.enemys = []
        for _ in range(Number_enemy):  # 创建敌机飞机 利用随机数来让飞机乱飞
             self.enemys.append(EnemyPlane())

        self.player = PlayerPlane(PLAY_PLANE, 200, 500)  # 将游戏飞机提取出来。定义路径

        """ 这一步没有意义了，因为上面有反复添加的操作了
        self.background.display()  # 导入图片进入游戏窗口
        """



# TODO 设置测试类入口操作
if __name__ == "__main__":
    """这个是指当前py文件调用方式的方法。如果他等于__main__就表示直接执行，
    如果不是，则用来被别的文件调用，这个时候if就为FALSE，
    那么它就不会执行最外层的代码了
    这样的话就是只有我在这个文件里面执行，底下的代码才会运行
    如果我调用这个文件的话，底下的代码就不会运行（测试程序）
    """
    Game().run()

