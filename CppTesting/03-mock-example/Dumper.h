//
// Created by akhtyamovpavel on 3/25/21.
//


#pragma once

#include <filesystem>

class Dumper {
 public:
  void TrainModel();
  virtual void Dump(int iteration);
 private:
  virtual std::filesystem::path GetCheckpointsFolder();
};


