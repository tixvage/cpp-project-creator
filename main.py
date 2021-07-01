import os

project = input("pls enter the project name: ")
location = input("pls enter the location of "+ project + ": ")

command = "cd " + location + " && mkdir " + project + " && cp reqs/CMakeLists.txt " + location + "/" + project + "  && cp reqs/run.sh "+ location + "/" + project + " && cd " + location + "/" + project +  " && mkdir build && mkdir src && mkdir include && touch src/main.cpp"

os.system(command)