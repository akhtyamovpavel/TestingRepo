//
// Created by Pavel Akhtyamov on 2019-03-12.
//

#include "MockSingleton.h"


using ::testing::AtLeast;
using ::testing::Return;
using ::testing::ElementsAre;


TEST(SingletonTest, CheckReadFile) {
  MockSingleton singleton;
  EXPECT_CALL(singleton, GetFile())
  .Times(AtLeast(1))
  .WillOnce(Return("mock.txt"));

  auto result = singleton.ReadFile();
  ASSERT_THAT(result, ElementsAre("Hello", "World"));
}