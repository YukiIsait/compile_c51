#include "../include/include.h"

void Init()
{
	EA = 1;//开启总中断
	Timer0Init();//开启T0定时器
}

int main()
{
	Init();
	while(1){
		TrafficLight();//交通灯显示函数
	}
}
