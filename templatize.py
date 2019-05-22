
# Author: Pierce Brooks

import os
import sys
import shutil
import inspect
import subprocess
import xml.etree.ElementTree as xml_tree

class Node(object):
	def __init__(self, tree, tag, index):
		self.tree = tree
		self.tag = tag
		self.index = index
		self.children = []
		
	def getTree(self):
		return self.tree
		
	def getTag(self):
		return self.tag
		
	def getIndex(self):
		return self.index
		
	def getChildren(self):
		return self.children
		
	def addChild(self, child):
		if not (child in self.children):
			self.children.append(child)
		
class Tree(object):
	def __init__(self):
		self.root = None
		self.nodes = []
		self.tags = []
		
	def getRoot(self):
		return self.root
		
	def getNodes(self):
		return self.nodes
		
	def getTags(self):
		return self.tags
		
	def getTagIndex(self, tag):
		index = 0
		for i in range(len(self.tags)):
			if (self.tags[i] == tag):
				index = i+1
		return index
		
	def getPopulation(self):
		return len(self.nodes)
		
	def addNode(self, node, parent):
		if (parent == None):
			self.root = node
		else:
			parent.addChild(node)
		if not (node in self.nodes):
			self.nodes.append(node)
			self.addTag(node.getTag())
		
	def addTag(self, tag):
		if not (tag in self.tags):
			self.tags.append(tag)

def parse(tree, root, parent):
	node = Node(tree, root.tag, tree.getPopulation())
	tree.addNode(node, parent)
	for child in root:
		node.addChild(parse(tree, child, node))
	return node
	
def cwd():
	filename = inspect.getframeinfo(inspect.currentframe()).filename
	path = os.path.dirname(os.path.abspath(filename))
	return path
	
def write(handle, line):
	handle.write(line+"\n")
	
def output(handle, node):
	name = "Node_"+str(node.getIndex()+1)
	tag = "Tag_"+str(node.getTree().getTagIndex(node.getTag()))
	children = []
	for child in node.getChildren():
		children.append(output(handle, child))
	templates = ""
	for i in range(len(children)):
		templates += children[i]
		if not (i == len(children)-1):
			templates += ", "
	if not (len(templates) == 0):
		tag += ", "
	write(handle, "struct "+name+" : public Node<"+tag+templates+"> {};")
	return name
	
def make(path, name):
	if not (os.path.isdir(path)):
		os.makedirs(path)
	handle = open(os.path.join(path, name), "w")
	return handle
	
def execute(command, base):
	executable = ""
	for i in range(len(command)):
		executable += "\""+command[i]+"\""
		if not (i == len(command)-1):
			executable += " "
	print(executable)
	handle = make(base, "command.txt")
	write(handle, "")
	write(handle, executable)
	write(handle, "")
	handle.close()
	process = subprocess.Popen(command, cwd=base, shell=False)
	(output, error) = process.communicate()
	status = process.wait()
	print(output)
		
def run(target, generator):
	src = "src"
	main = "main.cpp"
	name = "TemplatizeXML"
	project = "templatizeXML"
	cpp = "14"
	tree = Tree()
	xml = xml_tree.parse(target)
	root = xml.getroot()
	node = parse(tree, root, None)
	base = cwd()
	build = os.path.join(base, "build")
	base = os.path.join(base, "xml")
	print(build)
	print(base)
	if (os.path.isdir(build)):
		shutil.rmtree(build)
	if (os.path.isdir(base)):
		shutil.rmtree(base)
		
	handle = make(base, "CMakeLists.txt")
	write(handle, "cmake_minimum_required(VERSION 3.4.1)")
	write(handle, "set(CMAKE_CXX_FLAGS \"${CMAKE_CXX_FLAGS} -std=c++"+cpp+"\")")
	write(handle, "set(CMAKE_EXE_LINKER_FLAGS \"${CMAKE_EXE_LINKER_FLAGS} -std=c++"+cpp+"\")")
	write(handle, "set(CMAKE_SHARED_LINKER_FLAGS \"${CMAKE_SHARED_LINKER_FLAGS} -std=c++"+cpp+"\")")
	write(handle, "project("+project+")")
	write(handle, "add_subdirectory("+src+")")
	write(handle, "")
	handle.close()
	
	base = os.path.join(base, src)
	handle = make(base, "CMakeLists.txt")
	write(handle, "set(SOURCES )")
	write(handle, "set(DEFINES )")
	write(handle, "list(APPEND SOURCES ${CMAKE_CURRENT_LIST_DIR}/"+main+")")
	write(handle, "add_executable("+name+" ${SOURCES})")
	write(handle, "target_compile_definitions("+name+" PRIVATE ${DEFINES})")
	write(handle, "set_property(TARGET "+name+" PROPERTY CXX_STANDARD "+cpp+")")
	write(handle, "set_property(TARGET "+name+" PROPERTY CXX_STANDARD_REQUIRED ON)")
	write(handle, "")
	handle.close()
	
	handle = make(base, main)
	tags = tree.getTags()
	nodes = tree.getNodes()
	templates = []
	template = ""
	write(handle, "#include <string>")
	write(handle, "#include <iostream>")
	write(handle, "#include <utility>")
	write(handle, "#define TAB \"  \"")
	
	write(handle, "template <typename T, typename... U>")
	write(handle, "struct Node;")
	write(handle, "template <typename T>")
	write(handle, "struct Tag;")
	
	write(handle, "template <typename T>")
	write(handle, "const std::string& getTag() {")
	write(handle, "return T::getInstance().getTag(); }")
	
	write(handle, "template <typename T, typename... U>")
	write(handle, "struct Node : public T {")
	write(handle, "public: void output(int level) {}")
	write(handle, "void doOutput(int level) {")
	write(handle, "for (int i = 0; i != level; ++i) {")
	write(handle, "std::cout << TAB; }")
	write(handle, "std::cout << getTag<T>() << std::endl;")
	write(handle, "output(level, U()...); }")
	write(handle, "void output() {")
	write(handle, "doOutput(0); }")
	write(handle, "template <typename V>")
	write(handle, "void output(int level, V node) {")
	write(handle, "node.doOutput(level+1); }")
	write(handle, "template <typename V, typename... W>")
	write(handle, "void output(int level, V node, W... nodes) {")
	write(handle, "output(level, node);")
	write(handle, "output(level, std::forward<W>(nodes)...); } };")
	write(handle, "template <typename T>")
	write(handle, "struct Tag {")
	write(handle, "public: virtual const std::string& getTag() const = 0;")
	write(handle, "static const T& getInstance();")
	write(handle, "static const T* instance; };")
	write(handle, "template <typename T>")
	write(handle, "const T& Tag<T>::getInstance() {")
	write(handle, "return *instance; }")
	write(handle, "")
	
	for i in range(len(nodes)):
		write(handle, "struct Node_"+str(i+1)+";")
		templates.append("Node_"+str(i+1))
	write(handle, "")
	for i in range(len(tags)):
		write(handle, "struct Tag_"+str(i+1)+";")
		templates.append("Tag_"+str(i+1))
	write(handle, "")
	for i in range(len(templates)):
		template += templates[i]
		if not (i == len(templates)-1):
			template += ", "
	write(handle, "template <typename... T>")
	write(handle, "struct Tree {};")
	write(handle, "typedef Tree<"+template+"> XML;")
	write(handle, "typedef Node_"+str(tree.getRoot().getIndex()+1)+" Root;")
	write(handle, "")
	
	for i in range(len(tags)):
		write(handle, "struct Tag_"+str(i+1)+" : public Tag<Tag_"+str(i+1)+"> {")
		write(handle, "public: static const std::string tag;")
		write(handle, "const std::string& getTag() const override; };")
		write(handle, "const std::string Tag_"+str(i+1)+"::tag = \""+tags[i]+"\";")
		write(handle, "const std::string& Tag_"+str(i+1)+"::getTag() const { return tag; }")
		write(handle, "template <>")
		write(handle, "const Tag_"+str(i+1)+"* Tag<Tag_"+str(i+1)+">::instance = new Tag_"+str(i+1)+"();")
	write(handle, "")
	output(handle, node)
	write(handle, "")
	
	write(handle, "int main(int argc, char ** argv) {")
	write(handle, "Root().output();");
	write(handle, "return 0; }")
	write(handle, "")
	handle.close()
	
	cmake = ["cmake", "-G", generator, base]
	execute(cmake, build)
	cmake = ["cmake", "--build", "."]
	execute(cmake, build)
	return True

if (__name__ == "__main__"):
	arguments = sys.argv
	if (len(arguments) > 2):
		print(run(arguments[1], arguments[2]))
