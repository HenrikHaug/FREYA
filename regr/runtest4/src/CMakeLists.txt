#----------------------------------------------------------------------------
# 
# Jerome Verbeke
#
# Created 12/11/2018
#

# Setup the project
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

project(testEngConsAllActinides C)

file(GLOB sources ${PROJECT_SOURCE_DIR}/*.c)

# override built-in version of llnl fission library with new version (libFission.*)
# location of the LLNL Fission Library
set(LLNLFISSLIBDIR "$ENV{FREYADATAPATH}/../lib")
find_library(LFISSION Fission
             PATHS ${LLNLFISSLIBDIR}
             DOC "fission library"
             NO_DEFAULT_PATH
            )
if(NOT LFISSION)
  message(FATAL_ERROR "fission library not found")
endif()

message(STATUS "Overriding built-in fission library with ${LLNLFISSLIBDIR}/libFission.*")
include_directories(${LLNLFISSLIBDIR}/../include)

# build executable
add_executable(${PROJECT_NAME} ${sources})
target_link_libraries(${PROJECT_NAME} ${LFISSION} m) # for some reason we are missing -lm
add_definitions(-DFREYA)

