import pygame
import sys
import time
import win32gui
import win32con
import win32api

# 初始化pygame
pygame.init()

# 获取屏幕尺寸
screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# 定义函数，实现打字效果的动画
def type_out_text(screen, text, font, color, shadow_color, time_per_character, final_pause_s):
    # 在文本显示前暂停一段时间
    time.sleep(final_pause_s)

    # 文本的总字符数
    characters = len(text)
    # 当前显示的文本
    displayed_text = ""
    # 获取初始时间
    start_ticks = pygame.time.get_ticks()
    accumulated_time = 0

    while len(displayed_text) < characters:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        # 计算经过的时间
        now_ticks = pygame.time.get_ticks()
        accumulated_time += now_ticks - start_ticks
        start_ticks = now_ticks

        # 如果累计时间超过了单个字符显示的时间，则显示下一个字符
        if accumulated_time > time_per_character:
            accumulated_time -= time_per_character
            displayed_text += text[len(displayed_text)]

        # 渲染文本
        text_surface = font.render(displayed_text + "_", True, color)
        text_rect = text_surface.get_rect(center=(screen_width//2, screen_height//2))

        shadow_surface = font.render(displayed_text + "_", True, shadow_color)
        shadow_rect = text_surface.get_rect(center=(screen_width // 2 + 2, screen_height // 2 + 2))

        screen.fill((0, 0, 0))  # 清屏，填充为黑色
        screen.blit(shadow_surface, shadow_rect)
        screen.blit(text_surface, text_rect)
        # 更新屏幕显示
        pygame.display.flip()

        # 控制帧率
        pygame.time.Clock().tick(60)

    # 在文本显示完毕后暂停一段时间
    time.sleep(final_pause_s)

# 主程序
def main():
    # 设置屏幕大小
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption('Type Out Text Animation');

    # 设置字体和颜色
    font = pygame.font.SysFont("Aqum", 256)  # 增大字体大小
    color = "#0078B9"  # 蓝色
    shadow_color = "#000000"
    # 调用函数，开始动画
    type_out_text(screen, "Hello, World!", font, color, shadow_color, 256, 2)  # 100毫秒每个字符，结束后暂停2秒

    # 退出pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
