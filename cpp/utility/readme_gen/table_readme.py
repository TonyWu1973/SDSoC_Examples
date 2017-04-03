#!/usr/bin/env python
from sys import argv
import json
import os
import subprocess

def header(target,data):

    target.write(data["level"])
    target.write("\n")
    target.write("======================\n\n")
    target.write("This is a main repository which contains variety of SDSoC coding guidelines related examples which are intended to help users to get exposed to various important features of SDSoC. Xilinx SDx 2017.1 tool is used to develop these examples.\n\n")
    return


# Get the argument form the description
script, desc_file = argv

# load the description file
print "SDAccel README File Genarator"
print "Opening the description file '%s'" % desc_file
desc = open(desc_file,'r')

# load the json data from the file
print "Parsing the description file"
data = json.load(desc)
desc.close()

print "Generating the README for %s" % data["level"]
target = open("README.md","w")
header(target,data)

target.write("## SDSoC Examples\n")
target.write("\n")
target.write("Table below presents overall summary of each example in a precise manner. These examples are categorized to help users to cover various areas that needs to be focused while using SDSoC for their application optimization\n")
target.write("\n")
target.write("Sl.No | Title | Description | Category\n")
target.write("------|-------|-------------|----------\n")
target.write("1")
target.write("|")
target.write("Array Partition")
target.write("|")
target.write("This example shows how to use array partitioning to improve performance of a kernel")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("2")
target.write("|")
target.write("Burst Read/Write")
target.write("|")
target.write("This is simple example of using AXI4-master interface for burst read and write")
target.write("|")
target.write("Memory Transfer (DDR to PL)")
target.write("|")
target.write("\n")
target.write("3")
target.write("|")
target.write("Custom Data Type")
target.write("|")
target.write("This is a simple example of RGB to HSV conversion to demonstrate Custom DATA Type usage in hardware accelerator. Xilinx HLS compiler supports custom data type to operate within the kernel and also it acts as a memory interface between PL to DDR")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("4")
target.write("|")
target.write("Loop Iteration Dependency")
target.write("|")
target.write("This is a simple example to demonstrate inter dependence attribute. Using inter dependence attribute user can provide additional dependency details to compiler which allow compiler to perform unrolling/pipelining to get better performance")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("5")
target.write("|")
target.write("Full 2D Array Read/Write")
target.write("|")
target.write("This is a simple example of accessing full data from 2d array")
target.write("|")
target.write("Memory Transfer (DDR to PL)")
target.write("|")
target.write("\n")
target.write("6")
target.write("|")
target.write("Two Parallel Read/Write on Local Memory")
target.write("|")
target.write("This is a simple example of vector addition to demonstrate how to utilize both ports of Local Memory")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("7")
target.write("|")
target.write("Loop Fusion")
target.write("|")
target.write("This example will demonstrate how to fuse two loops into one to improve the performance of a C/C++ accelerator.")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("8")
target.write("|")
target.write("Loop Perfect")
target.write("|")
target.write("This nearest neighbor example is to demonstrate how to achieve better performance using perfect loop.")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("9")
target.write("|")
target.write("Loop Pipelining")
target.write("|")
target.write("This example demonstrates how loop pipelining can be used to improve the performance of a kernel")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("10")
target.write("|")
target.write("Loop Reorder for Better Performance")
target.write("|")
target.write("This is a simple example of matrix multiplication (Row x Col) to demonstrate how to achieve better pipeline II factor by loop reordering")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("11")
target.write("|")
target.write("Read/Write Row of 2D Array")
target.write("|")
target.write("This is a simple example of accessing each row of data from 2d array")
target.write("|")
target.write("Memory Transfer (DDR to PL)")
target.write("|")
target.write("\n")
target.write("12")
target.write("|")
target.write("Shift Register")
target.write("|")
target.write("This example demonstrates how to shift values in each clock cycle")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("13")
target.write("|")
target.write("Systolic Array Implementation")
target.write("|")
target.write("This is a simple example of matrix multiplication (Row x Col) to help developers learn systolic array based algorithm design. Note : Systolic array based algorithm design is well suited for FPGA.")
target.write("|")
target.write("Optimization")
target.write("|")
target.write("\n")
target.write("14")
target.write("|")
target.write("Wide Memory Read/Write")
target.write("|")
target.write("This is a simple example of vector addition to demonstrate Wide Memory Access using ap_uint<512> data type. Based on input argument type, sds++ compiler will figure out the memory bandwidth between global memory and kernel. For this example, ap_uint<512> datatype is used, so memory datawidth will be 16 x (integer bit size) = 16 x 32 = 512bit")
target.write("|")
target.write("Memory Transfer (DDR to PL)")
target.write("|")
target.write("\n")
target.write("15")
target.write("|")
target.write("Read/Write Window of 2D Array")
target.write("|")
target.write("This is a simple example of accessing each row of data from 2d array")
target.write("|")
target.write("Memory Transfer (DDR to PL)")
target.write("|")
target.write("\n")
target.write("\n\n")
