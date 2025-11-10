//
// Created by Pavel Akhtyamov on 2019-03-05.
//

#include "TestAdd.h"
#include <exception>

TEST_F(TestAdd, TwoPlusTwo) {
  ASSERT_EQ(4, 2 + 2);
}

TEST_F(TestAdd, NegativeNumbers) {
  ASSERT_EQ(-4, -2 - 2);
}


TEST(IncludeTest, IncludeTest) {
  EXPECT_THROW({
    int x = 0; throw std::runtime_error("division by zero");
  }, std::runtime_error);
}