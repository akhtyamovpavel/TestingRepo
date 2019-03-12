//
// Created by Pavel Akhtyamov on 2019-03-11.
//

#include <string>
#include <fstream>
#include "Singleton.h"

bool Singleton::initialized = false;
Singleton* Singleton::instance = nullptr;


Singleton* Singleton::GetInstance() {
  if (!initialized) {
    instance = new Singleton;
    initialized = true;
    return instance;
  }
  return instance;
}



Singleton::Singleton() = default;

std::string Singleton::GetFile() const {
  return "time.txt";
}

std::vector<std::string> Singleton::ReadFile() const {
  std::ifstream file(GetFile());
  std::vector<std::string> result;
  std::string line;
  while (std::getline(file, line)) {
    result.push_back(line);
  }
  file.close();
  return result;
}
