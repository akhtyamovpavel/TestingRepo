//
// Created by akhtyamovpavel on 3/25/21.
//

#include "MockDumper.h"

using ::testing::Return;
using ::testing::_;


TEST(DumperTest, TestDumpWorker) {
  testing::NiceMock<MockDumper> dumper;
  ON_CALL(
      dumper,
      GetCheckpointsFolder()
  ).WillByDefault(Return("test_dumps"));


  dumper.TrainModel();

  std::filesystem::path path = "test_dumps";

  ASSERT_TRUE(std::filesystem::exists(path / std::to_string(0)));
  std::filesystem::remove_all(path);
}

TEST(DumperTest, TestDumpNumCalls) {
  MockDumperChecksDumper dumper;
  ON_CALL(
      dumper,
      GetCheckpointsFolder()
  ).WillByDefault(Return("test_dumps"));

  EXPECT_CALL(dumper, Dump(_)).Times(3);

  dumper.TrainModel();
}