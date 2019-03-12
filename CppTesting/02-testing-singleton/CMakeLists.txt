add_executable(02_testing_singleton Singleton.cpp main.cpp)
target_link_libraries(02_testing_singleton Threads::Threads)

add_executable(02_tests Singleton.cpp MockSingleton.cpp run_tests.cpp)
target_link_libraries(02_tests Threads::Threads ${GTEST_LIBRARIES} ${GMOCK_BOTH_LIBRARIES})