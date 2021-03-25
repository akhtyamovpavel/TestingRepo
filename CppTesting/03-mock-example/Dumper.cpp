//
// Created by akhtyamovpavel on 3/25/21.
//

#include "Dumper.h"

#include <filesystem>
#include <string>

void Dumper::TrainModel() {
  for (int i = 0; i < 3; ++i) {
    Dump(i);
  }
}

void Dumper::Dump(int iteration) {
  std::filesystem::create_directories(GetCheckpointsFolder() / std::to_string(iteration));
}

std::filesystem::path Dumper::GetCheckpointsFolder() {
  return "dumps";
}
