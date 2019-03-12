include_directories(${GTEST_INCLUDE_DIRS})

add_executable(01_setup_teardown cmake_test.cpp TestWithFixtures.cpp TestWithFixtures.h)
target_link_libraries(01_setup_teardown ${GTEST_LIBRARIES} Threads::Threads)