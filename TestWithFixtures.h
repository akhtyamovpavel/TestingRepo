//
// Created by Pavel Akhtyamov on 05/04/2018.
//

#pragma once

#include <gtest/gtest.h>

class TestWithFixtures : public ::testing::Test {
 public:
  static void SetUpTestCase();
  void SetUp() override;
  void TearDown() override;
  static int GetElement(size_t index);
 private:
  static std::vector<int> very_big_array_;
};
