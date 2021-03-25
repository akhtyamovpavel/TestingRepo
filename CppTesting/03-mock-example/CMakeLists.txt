add_executable(03-mock-example Dumper.cpp main.cpp)
target_link_libraries(03-mock-example Threads::Threads)

add_executable(03-mock-example-tests Dumper.cpp MockDumper.cpp)
target_link_libraries(03-mock-example-tests Threads::Threads ${GTEST_LIBRARIES} ${GMOCK_BOTH_LIBRARIES})