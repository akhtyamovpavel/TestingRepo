//
// Created by Pavel Akhtyamov on 05/04/2018.
//

#include "TestWithFixtures.h"

std::vector<int> TestWithFixtures::very_big_array_;

void TestWithFixtures::SetUpTestCase() {
  for (int i = 0; i < 1000000; ++i) {
    very_big_array_.push_back(i);
  }
}


void TestWithFixtures::SetUp() {
  for (int i = 0; i < 10; ++i) {
    very_big_array_[i] += 10;
  }
}


int TestWithFixtures::GetElement(size_t index) {
  return TestWithFixtures::very_big_array_.at(index);
}

void TestWithFixtures::TearDown() {
  for (int i = 0; i < 10; ++i) {
    very_big_array_[i] -= 10;
  }
}

TEST_F(TestWithFixtures, LastElementGot) {
  EXPECT_EQ(TestWithFixtures::GetElement(10000), 10000);
}

TEST_F(TestWithFixtures, FirstElements) {
  EXPECT_EQ(TestWithFixtures::GetElement(0), 10);
}

TEST_F(TestWithFixtures, UpdateElements) {
  EXPECT_EQ(TestWithFixtures::GetElement(0), 10);
}
