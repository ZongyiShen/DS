#ifndef STACK
#define STACK
#include <cmath>
#include <string>
#include <stdio.h>
#include <iostream>
using namespace std;
class stack;
class StackNode{
private:
    int data;
    StackNode *next;
public:
    StackNode():data(0){
        next = 0;
    }
    StackNode(int x):data(x){
        next = 0;
    }
    StackNode(int x, StackNode *nextNode):data(x),next(nextNode){};
    void setdata(int x){
        data = x;
    }
    friend class stack;
};
class stack{
private:
    StackNode *top;     // remember the address of top element 
    int size;           // number of elements in Stack
public:                 
    stack():size(0),top(0){};
    void Push(int x){
        StackNode * a;
        a=new StackNode;
        a->setdata(x);
        a->next=top;
        top=a;
        size+=1;
    }
    void Pop(){
        if(top == NULL){
            cout << "stack is empty" << endl;
        }
        else{
            StackNode *now=top;
            top=now->next;
            delete now;
            now=0;
            size-=1;
        }
    }
    bool IsEmpty(){
        if(top == NULL){
            return true;
        }
        else{
            return false;
        }
    }
    int Top(){
        if(top != NULL)
            return top->data;
        else
        {
            cout << "stack is empty" << endl;
            return -1;
        }
    }
    int getSize(){
        return size;
    }
};

#endif
