#include <string>
#include <iostream>
#include <utility>
#define TAB "  "
template <typename T, typename... U>
struct Node;
template <typename T>
struct Tag;
template <typename T>
const std::string& getTag() {
return T::getInstance().getTag(); }
template <typename T, typename... U>
struct Node : public T {
public: void output(int level) {}
void doOutput(int level) {
for (int i = 0; i != level; ++i) {
std::cout << TAB; }
std::cout << getTag<T>() << std::endl;
output(level, U()...); }
void output() {
doOutput(0); }
template <typename V>
void output(int level, V node) {
node.doOutput(level+1); }
template <typename V, typename... W>
void output(int level, V node, W... nodes) {
output(level, node);
output(level, std::forward<W>(nodes)...); } };
template <typename T>
struct Tag {
public: virtual const std::string& getTag() const = 0;
static const T& getInstance();
static const T* instance; };
template <typename T>
const T& Tag<T>::getInstance() {
return *instance; }

struct Node_1;
struct Node_2;
struct Node_3;
struct Node_4;
struct Node_5;
struct Node_6;
struct Node_7;
struct Node_8;
struct Node_9;
struct Node_10;
struct Node_11;
struct Node_12;
struct Node_13;
struct Node_14;
struct Node_15;
struct Node_16;
struct Node_17;
struct Node_18;
struct Node_19;
struct Node_20;
struct Node_21;
struct Node_22;
struct Node_23;
struct Node_24;
struct Node_25;
struct Node_26;
struct Node_27;
struct Node_28;
struct Node_29;
struct Node_30;
struct Node_31;
struct Node_32;
struct Node_33;
struct Node_34;
struct Node_35;
struct Node_36;
struct Node_37;
struct Node_38;
struct Node_39;
struct Node_40;
struct Node_41;
struct Node_42;
struct Node_43;
struct Node_44;
struct Node_45;
struct Node_46;
struct Node_47;
struct Node_48;
struct Node_49;
struct Node_50;
struct Node_51;
struct Node_52;
struct Node_53;
struct Node_54;
struct Node_55;
struct Node_56;
struct Node_57;
struct Node_58;

struct Tag_1;
struct Tag_2;

template <typename... T>
struct Tree {};
typedef Tree<Node_1, Node_2, Node_3, Node_4, Node_5, Node_6, Node_7, Node_8, Node_9, Node_10, Node_11, Node_12, Node_13, Node_14, Node_15, Node_16, Node_17, Node_18, Node_19, Node_20, Node_21, Node_22, Node_23, Node_24, Node_25, Node_26, Node_27, Node_28, Node_29, Node_30, Node_31, Node_32, Node_33, Node_34, Node_35, Node_36, Node_37, Node_38, Node_39, Node_40, Node_41, Node_42, Node_43, Node_44, Node_45, Node_46, Node_47, Node_48, Node_49, Node_50, Node_51, Node_52, Node_53, Node_54, Node_55, Node_56, Node_57, Node_58, Tag_1, Tag_2> XML;
typedef Node_1 Root;

struct Tag_1 : public Tag<Tag_1> {
public: static const std::string tag;
const std::string& getTag() const override; };
const std::string Tag_1::tag = "bookmarks";
const std::string& Tag_1::getTag() const { return tag; }
template <>
const Tag_1* Tag<Tag_1>::instance = new Tag_1();
struct Tag_2 : public Tag<Tag_2> {
public: static const std::string tag;
const std::string& getTag() const override; };
const std::string Tag_2::tag = "bookmark";
const std::string& Tag_2::getTag() const { return tag; }
template <>
const Tag_2* Tag<Tag_2>::instance = new Tag_2();

struct Node_5 : public Node<Tag_2> {};
struct Node_6 : public Node<Tag_2> {};
struct Node_7 : public Node<Tag_2> {};
struct Node_8 : public Node<Tag_2> {};
struct Node_4 : public Node<Tag_2, Node_5, Node_6, Node_7, Node_8> {};
struct Node_3 : public Node<Tag_2, Node_4> {};
struct Node_13 : public Node<Tag_2> {};
struct Node_14 : public Node<Tag_2> {};
struct Node_15 : public Node<Tag_2> {};
struct Node_16 : public Node<Tag_2> {};
struct Node_12 : public Node<Tag_2, Node_13, Node_14, Node_15, Node_16> {};
struct Node_18 : public Node<Tag_2> {};
struct Node_19 : public Node<Tag_2> {};
struct Node_20 : public Node<Tag_2> {};
struct Node_21 : public Node<Tag_2> {};
struct Node_22 : public Node<Tag_2> {};
struct Node_23 : public Node<Tag_2> {};
struct Node_24 : public Node<Tag_2> {};
struct Node_25 : public Node<Tag_2> {};
struct Node_17 : public Node<Tag_2, Node_18, Node_19, Node_20, Node_21, Node_22, Node_23, Node_24, Node_25> {};
struct Node_27 : public Node<Tag_2> {};
struct Node_28 : public Node<Tag_2> {};
struct Node_29 : public Node<Tag_2> {};
struct Node_26 : public Node<Tag_2, Node_27, Node_28, Node_29> {};
struct Node_31 : public Node<Tag_2> {};
struct Node_32 : public Node<Tag_2> {};
struct Node_33 : public Node<Tag_2> {};
struct Node_34 : public Node<Tag_2> {};
struct Node_35 : public Node<Tag_2> {};
struct Node_36 : public Node<Tag_2> {};
struct Node_30 : public Node<Tag_2, Node_31, Node_32, Node_33, Node_34, Node_35, Node_36> {};
struct Node_38 : public Node<Tag_2> {};
struct Node_39 : public Node<Tag_2> {};
struct Node_40 : public Node<Tag_2> {};
struct Node_41 : public Node<Tag_2> {};
struct Node_42 : public Node<Tag_2> {};
struct Node_43 : public Node<Tag_2> {};
struct Node_44 : public Node<Tag_2> {};
struct Node_45 : public Node<Tag_2> {};
struct Node_46 : public Node<Tag_2> {};
struct Node_47 : public Node<Tag_2> {};
struct Node_48 : public Node<Tag_2> {};
struct Node_37 : public Node<Tag_2, Node_38, Node_39, Node_40, Node_41, Node_42, Node_43, Node_44, Node_45, Node_46, Node_47, Node_48> {};
struct Node_50 : public Node<Tag_2> {};
struct Node_51 : public Node<Tag_2> {};
struct Node_52 : public Node<Tag_2> {};
struct Node_53 : public Node<Tag_2> {};
struct Node_54 : public Node<Tag_2> {};
struct Node_55 : public Node<Tag_2> {};
struct Node_49 : public Node<Tag_2, Node_50, Node_51, Node_52, Node_53, Node_54, Node_55> {};
struct Node_11 : public Node<Tag_2, Node_12, Node_17, Node_26, Node_30, Node_37, Node_49> {};
struct Node_10 : public Node<Tag_2, Node_11> {};
struct Node_56 : public Node<Tag_2> {};
struct Node_9 : public Node<Tag_2, Node_10, Node_56> {};
struct Node_57 : public Node<Tag_2> {};
struct Node_58 : public Node<Tag_2> {};
struct Node_2 : public Node<Tag_2, Node_3, Node_9, Node_57, Node_58> {};
struct Node_1 : public Node<Tag_1, Node_2> {};

int main(int argc, char ** argv) {
Root().output();
return 0; }

