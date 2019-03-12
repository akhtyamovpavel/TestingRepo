//
// Created by Pavel Akhtyamov on 2019-03-11.
//


#include <iostream>

#include "Singleton.h"
int main() {
  Singleton* instance = Singleton::GetInstance();
  for (const std::string& line : instance->ReadFile()) {
    std::cout << line << std::endl;
  }
}

