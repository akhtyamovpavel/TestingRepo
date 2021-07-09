//
// Created by Pavel Akhtyamov on 02/04/2018.
//


#include <cmath>
#include "my_first_function.h"


float square(float x) {
  return x * x;
}

float my_sqrt(float x) {
  if (x > 10) {
	return x;
  }
  return static_cast<float>(sqrt(x));
}
