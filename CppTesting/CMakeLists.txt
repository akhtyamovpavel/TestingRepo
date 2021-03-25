cmake_minimum_required(VERSION 3.8)
project(Testing)

set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH}" ${CMAKE_SOURCE_DIR}/cmake)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${Testing_SOURCE_DIR}/bin)


find_package(GTest REQUIRED)
find_package(GMock REQUIRED)
find_package(Threads REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})
include_directories(${GMOCK_INCLUDE_DIRS})

add_subdirectory(simple-test)
add_subdirectory(00-start-test)
add_subdirectory(01-set-up-tear-down)
add_subdirectory(02-testing-singleton)
add_subdirectory(03-mock-example)

#target_link_libraries(RunTests ${GTEST_LIBRARIES} Threads::Threads)

enable_testing()

add_test(Test00 ${Testing_SOURCE_DIR}/bin/00_start_test)
add_test(Test01 ${Testing_SOURCE_DIR}/bin/01_setup_teardown)
add_test(Test02 ${Testing_SOURCE_DIR}/bin/02_testing_singleton)


