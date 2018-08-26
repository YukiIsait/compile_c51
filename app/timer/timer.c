#include "../include/include.h"
#include "timer.h"

unsigned char tmr;
unsigned char TmrCount = 33;

void Timer0Init()//毫秒级@12.000MHz
{
	AUXR &= 0x7F;//定时器时钟12T模式
	TMOD &= 0xF0;//设置定时器模式
	TMOD |= 0x01;//设置定时器模式
	TL0 = T0RH;//设置定时初值
	TH0 = T0RL;//设置定时初值
	TF0 = 0;//清除TF0标志
	ET0 = 1;//T/C0中断开关
	TR0 = 1;//定时器0开始计时
}

/* T0中断服务函数，完成计数 */
void InterruptTimer0() __interrupt 1
{
	TH0 = T0RH;//重新加载重载值
	TL0 = T0RL;
	//定时1s
	if(tmr < 20){
		tmr++;
	}else{
		tmr = 0;
		TmrCount++;
	}
}

void ResetTmr()
{
	tmr = 0;
	TH0 = T0RH;//重新加载重载值
	TL0 = T0RL;
}

/* 秒延时 *//*
void delayNs(unsigned char s)
{
	count = s;
	TH0 = T0RH;//重新加载重载值
	TL0 = T0RL;
	while(count);
}
*/
