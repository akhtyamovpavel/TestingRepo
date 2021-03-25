//
// Created by Pavel Akhtyamov on 2019-03-11.
//

#pragma once

#include <vector>
#include <string>

class MockSingleton;

class Singleton {
 public:
  static Singleton* GetInstance();
  std::vector<std::string> ReadFile() const;
 private:
  Singleton();
  static Singleton* instance;
  static bool initialized;
  virtual std::string GetFile() const;
  friend class MockSingleton;
};



