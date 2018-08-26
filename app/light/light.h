#ifndef _LIGHT_H_
#define _LIGHT_H_

/* 共12个LED,分2组,每组6个 */

/* 东-西P1.0 - P1.2*/
#define WE_R P10
#define WE_Y P11
#define WE_G P12
/* 南-北P1.3 - P1.5 */
#define NS_R P13
#define NS_Y P14
#define NS_G P15

#define ON 0
#define OFF 1

extern void TrafficLight();

#endif
