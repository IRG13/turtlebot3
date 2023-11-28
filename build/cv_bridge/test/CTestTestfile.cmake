# CMake generated Testfile for 
# Source directory: /home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test
# Build directory: /home/maddy/turtlebot3_ws/build/cv_bridge/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(cv_bridge-utest "/usr/bin/python3.10" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/cv_bridge-utest.gtest.xml" "--package-name" "cv_bridge" "--output-file" "/home/maddy/turtlebot3_ws/build/cv_bridge/ament_cmake_gtest/cv_bridge-utest.txt" "--append-env" "LD_LIBRARY_PATH=/home/maddy/turtlebot3_ws/build/cv_bridge/src" "--command" "/home/maddy/turtlebot3_ws/build/cv_bridge/test/cv_bridge-utest" "--gtest_output=xml:/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/cv_bridge-utest.gtest.xml")
set_tests_properties(cv_bridge-utest PROPERTIES  LABELS "gtest" REQUIRED_FILES "/home/maddy/turtlebot3_ws/build/cv_bridge/test/cv_bridge-utest" TIMEOUT "60" WORKING_DIRECTORY "/home/maddy/turtlebot3_ws/build/cv_bridge/test" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_gtest/cmake/ament_add_gtest_test.cmake;86;ament_add_test;/opt/ros/humble/share/ament_cmake_gtest/cmake/ament_add_gtest.cmake;93;ament_add_gtest_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;16;ament_add_gtest;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;0;")
add_test(enumerants.py "/usr/bin/python3.10" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/enumerants.py.xunit.xml" "--package-name" "cv_bridge" "--output-file" "/home/maddy/turtlebot3_ws/build/cv_bridge/ament_cmake_pytest/enumerants.py.txt" "--command" "/usr/bin/python3.10" "-u" "-m" "pytest" "/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/enumerants.py" "-o" "cache_dir=/home/maddy/turtlebot3_ws/build/cv_bridge/test/ament_cmake_pytest/enumerants.py/.cache" "--junit-xml=/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/enumerants.py.xunit.xml" "--junit-prefix=cv_bridge")
set_tests_properties(enumerants.py PROPERTIES  LABELS "pytest" TIMEOUT "60" WORKING_DIRECTORY "/home/maddy/turtlebot3_ws/build/cv_bridge/test" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;32;ament_add_pytest_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;0;")
add_test(conversions.py "/usr/bin/python3.10" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/conversions.py.xunit.xml" "--package-name" "cv_bridge" "--output-file" "/home/maddy/turtlebot3_ws/build/cv_bridge/ament_cmake_pytest/conversions.py.txt" "--command" "/usr/bin/python3.10" "-u" "-m" "pytest" "/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/conversions.py" "-o" "cache_dir=/home/maddy/turtlebot3_ws/build/cv_bridge/test/ament_cmake_pytest/conversions.py/.cache" "--junit-xml=/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/conversions.py.xunit.xml" "--junit-prefix=cv_bridge")
set_tests_properties(conversions.py PROPERTIES  LABELS "pytest" TIMEOUT "600" WORKING_DIRECTORY "/home/maddy/turtlebot3_ws/build/cv_bridge/test" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;33;ament_add_pytest_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;0;")
add_test(python_bindings.py "/usr/bin/python3.10" "-u" "/opt/ros/humble/share/ament_cmake_test/cmake/run_test.py" "/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/python_bindings.py.xunit.xml" "--package-name" "cv_bridge" "--output-file" "/home/maddy/turtlebot3_ws/build/cv_bridge/ament_cmake_pytest/python_bindings.py.txt" "--command" "/usr/bin/python3.10" "-u" "-m" "pytest" "/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/python_bindings.py" "-o" "cache_dir=/home/maddy/turtlebot3_ws/build/cv_bridge/test/ament_cmake_pytest/python_bindings.py/.cache" "--junit-xml=/home/maddy/turtlebot3_ws/build/cv_bridge/test_results/cv_bridge/python_bindings.py.xunit.xml" "--junit-prefix=cv_bridge")
set_tests_properties(python_bindings.py PROPERTIES  LABELS "pytest" TIMEOUT "60" WORKING_DIRECTORY "/home/maddy/turtlebot3_ws/build/cv_bridge/test" _BACKTRACE_TRIPLES "/opt/ros/humble/share/ament_cmake_test/cmake/ament_add_test.cmake;125;add_test;/opt/ros/humble/share/ament_cmake_pytest/cmake/ament_add_pytest_test.cmake;169;ament_add_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;34;ament_add_pytest_test;/home/maddy/turtlebot3_ws/src/vision_opencv/cv_bridge/test/CMakeLists.txt;0;")
subdirs("../gtest")
