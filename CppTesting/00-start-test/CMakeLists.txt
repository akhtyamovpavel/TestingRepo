cmake_minimum_required(VERSION 3.5)

project(00-start-test)

find_package(GTest REQUIRED)
find_package(Threads REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

add_executable(00_start_test run_tests.cpp TestAdd.cpp TestAdd.h)
target_link_libraries(00_start_test ${GTEST_LIBRARIES} Threads::Threads)


