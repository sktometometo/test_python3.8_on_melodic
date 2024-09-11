cmake_minimum_required(VERSION 3.0.2)
project(test_python38_on_melodic)

find_package(catkin REQUIRED COMPONENTS catkin_virtualenv)

catkin_generate_virtualenv(
    PYTHON_INTERPRETER python3.8
    CHECK_VENV FALSE
    USE_SYSTEM_PACKAGES TRUE
)

catkin_package()

catkin_install_python(
    PROGRAMS scripts/hoge.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
