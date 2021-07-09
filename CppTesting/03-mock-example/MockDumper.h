//
// Created by akhtyamovpavel on 3/25/21.
//


#pragma once

#include "Dumper.h"
#include <gmock/gmock.h>

class MockDumper : public Dumper {
 public:
  MOCK_METHOD(std::filesystem::path, GetCheckpointsFolder, (), (override));

};

class MockDumperChecksDumper: public Dumper {
 public:
  MOCK_METHOD(void, Dump, (int) , (override));
  MOCK_METHOD(std::filesystem::path, GetCheckpointsFolder, (), (override));
};

