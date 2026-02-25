/*
 * 机器人面部舵机控制Demo（C语言）
 * 适配STM32单片机，模拟控制面部舵机实现基础表情（眨眼/微笑）
 */
#include <stdio.h>
#include <unistd.h>  // 用于延时函数（Windows系统可替换为windows.h）

// 舵机角度控制函数（模拟）
void set_servo_angle(int servo_id, int angle) {
    // 模拟向舵机发送角度指令
    printf("舵机%d：设置角度为%d度\n", servo_id, angle);
}

// 基础表情：眨眼（控制眼部舵机）
void blink_eye() {
    printf("\n=== 执行眨眼动作 ===\n");
    set_servo_angle(1, 90);  // 左眼舵机：闭眼（90度）
    set_servo_angle(2, 90);  // 右眼舵机：闭眼（90度）
    sleep(1);                // 保持闭眼1秒（Windows用Sleep(1000)）
    set_servo_angle(1, 0);   // 左眼舵机：睁眼（0度）
    set_servo_angle(2, 0);   // 右眼舵机：睁眼（0度）
    sleep(1);                // 保持睁眼1秒
}

// 基础表情：微笑（控制嘴部舵机）
void smile() {
    printf("\n=== 执行微笑动作 ===\n");
    set_servo_angle(3, 45);  // 嘴部舵机：微笑角度（45度）
    sleep(2);                // 保持微笑2秒
    set_servo_angle(3, 0);   // 嘴部舵机：恢复原位（0度）
}

int main() {
    printf("=== 机器人面部表情控制系统 ===\n");
    printf("支持动作：1-眨眼  2-微笑  0-退出\n");
    
    int choice;
    while (1) {
        printf("\n请选择要执行的动作：");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1:
                blink_eye();
                break;
            case 2:
                smile();
                break;
            case 0:
                printf("系统退出\n");
                return 0;
            default:
                printf("无效选择，请重新输入！\n");
        }
    }
    return 0;
}