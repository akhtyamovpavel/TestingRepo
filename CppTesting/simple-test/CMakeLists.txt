add_executable(
	RunTests
	main_test.cpp
	my_first_function.cpp
	test.cpp
)

target_link_libraries(RunTests ${GTEST_LIBRARIES} Threads::Threads)
