cmake_minimum_required(VERSION 3.8)
project(Testing)


set(CMAKE_CXX_STANDARD 11)

#add_executable(OutputTesting main.cpp my_first_function.cpp)

if (APPLE)
    add_definitions(-DGTEST_USE_OWN_TR1_TUPLE)
    add_definitions(-D__GLIBCXX__)
endif (APPLE)



find_package(GTest REQUIRED)
find_package(Threads REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

add_executable(
    RunTests
    cmake_test.cpp
    test.cpp
    my_first_function.cpp
    TestWithFixtures.cpp
)

target_link_libraries(RunTests ${GTEST_LIBRARIES} Threads::Threads)

enable_testing()
add_test(Tests RunTests)

