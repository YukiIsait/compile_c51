#ifndef _TIMER_H_
#define _TIMER_H_

#define T0RH 0xB0  //50ms
#define T0RL 0x3C

void InterruptTimer0() __interrupt 1;//申请使用定时器

extern unsigned char TmrCount;
extern void Timer0Init();
extern void ResetTmr();

#endif
