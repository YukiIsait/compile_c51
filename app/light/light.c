#include "../include/include.h"
#include "light.h"

/* 共12个LED,分2组,每组6个 */
/* 共用6个IO,东-西P1.0 - P1.2,南-北P1.3 - P1.5 */

/* 交通灯显示函数 */
void TrafficLight()
{
	switch(TmrCount){
		case 0:
			NS_R = ON;
			NS_Y = OFF;
			NS_G = OFF;
			WE_R = OFF;
			WE_Y = OFF;
			WE_G = ON;
		break;//南北红,东西绿
		case 30:
			WE_Y = ON;
			NS_Y = ON;
			WE_G = OFF;
		break;//过渡
		case 33:
			NS_R = OFF;
			NS_Y = OFF;
			NS_G = ON;
			WE_R = ON;
			WE_Y = OFF;
			WE_G = OFF;
		break;//南北绿,东西红
		case 63:
			WE_Y = ON;
			NS_Y = ON;
			NS_G = OFF;
		break;//过渡
		case 66:
			ResetTmr();
			TmrCount = 0;
		break;//恢复初始状态
	}
}
