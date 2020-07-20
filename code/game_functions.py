# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:23:04 2020

@author: 86178
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, sb, aliens):
    '''响应按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        end_game(stats)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, aliens, bullets, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹""" 
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
   

def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    '''响应按键和鼠标'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                end_game(stats)
                
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets, stats, sb, aliens)
                    
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
                             bullets, mouse_x, mouse_y)
'''使用了pygame.mouse.get_pos()，它返回一个元组，其中包含玩家单击时鼠标的x和y坐标,
使用collidepoint()检查鼠标单击位置是否在Play按钮的rect内'''


def end_game(stats):
    '''结束游戏'''
    with open('./high_score.txt','w') as f:
        f.write(str(stats.high_score))
    sys.exit()



def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, 
        bullets, mouse_x, mouse_y):
    '''在玩家单击Play按钮时开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, aliens, bullets, ship)

'''函数使用collidepoint()检查鼠标单击位置是否在Play按钮的rect内'''


def start_game(ai_settings, screen, stats, sb, aliens, bullets, ship):
    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ship()

    # 重置游戏设置
    ai_settings.initialize_dynamic_settings()

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 显示飞船    
    ship.blitme()
    # 显示所有外星人
    aliens.draw(screen)
    # 显示分数
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
 
    # 让最近绘制的屏幕可见
    pygame.display.flip() 
     
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    # 更新子弹位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
            aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
            aliens, bullets):
    '''响应子弹和外星人的碰撞'''
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    sb.prep_score()

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

        # 整群外星人都被消灭，就提高一个等级
        stats.level += 1
        sb.prep_level()


def check_high_score(stats, sb):
    '''检查是否诞生了新的最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



'''方法sprite.groupcollide()将每颗子弹的rect同每个外星人的rect进行比较，并返回一个字
典，其中包含发生了碰撞的子弹和外星人。在这个字典中，每个键都是一颗子弹，而相应的值都
是被击中的外星人。两个实参True告诉Pygame删除发生碰撞的子弹和外星人。 [update_bullets]
'''

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_alien_x = int(available_space_x / (2*alien_width))
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    num_rows = int(available_space_y / (2*alien_height))
    return num_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建一个外星人并将其放在当前位置'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            # 创建一个外星人并将其加入当前位置
            create_alien(ai_settings, screen, aliens, alien_number, row_number)   


def check_fleet_edges(ai_settings, aliens):
    '''有外星人到边缘时采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''将整群外星人下移，并改变它们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ship_left > 0:
        stats.ship_left -= 1 

        # 更新记分牌
        sb.prep_ship()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

'''更新所有元素后（但在将修改显示到屏幕前）暂停，让玩家知道其
飞船被撞到了（见）。屏幕将暂时停止变化，让玩家能够看到外星人撞到了飞船。函数sleep()
执行完毕后，将接着执行函数update_screen()，将新的外星人群绘制到屏幕上。'''

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    '''更新外星人群中所有外星人的位置'''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("ship hit")
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    '''检查是否有外星人到达屏幕低端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            print("hit bottom")
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break




# 读取属性event.key，以检查按下的是否是右箭头键（pygame.K_RIGHT）
'''
方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵。为在屏幕上绘制发射的
所有子弹，我们遍历编组bullets中的精灵，并对每个精灵都调用draw_bullet()
'''
'''
对编组调用draw()时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定。
在这里，aliens.draw(screen)在屏幕上绘制编组中的每个外星人
'''
# 对编组aliens调用方法update()，这将自动对每个外星人调用方法update()
'''
方法spritecollideany()接受两个实参：一个精灵和一个编组。它检查编组是否有成员与精
灵发生了碰撞，并在找到与精灵发生了碰撞的成员后就停止遍历编组。在这里，它遍历编组
aliens，并返回它找到的第一个与飞船发生了碰撞的外星人。如果没有发生碰撞，spritecollideany()将返回None
'''