//
// Created by Pavel Akhtyamov on 2019-03-12.
//

#pragma once

#include "Singleton.h"
#include <gmock/gmock.h>

class MockSingleton: public Singleton {
 public:
  MOCK_METHOD(std::string, GetFile, (), (const, override));
};



