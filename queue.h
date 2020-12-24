#ifndef QUEUE
#define QUEUE
#include <cmath>
#include <string>
#include <stdio.h>
#include <iostream>
using namespace std;
class queue;
class QueueNode{
    private:
        int data;
        QueueNode *next;
    public:
        QueueNode():data(0),next(0){};
        QueueNode(int x):data(x),next(0){};
        void setdata(int x){
            data=x;
        }
        friend queue;
};

class queue{
private:
    QueueNode *front;
    QueueNode *back;
    int size;
public:
    queue():front(0),back(0),size(0){};
    void Push(int x){
        QueueNode * a;
        a = new QueueNode;
        a->setdata(x);
        if(front == NULL){
            front=a;
            back=a;
        }
        else if(front == back){
            back=a;
            front->next=back;
        }
        else{
            back->next=a;
            back=a;
        }
        size +=1;
    }
    void Pop(){
        if(front == NULL){
            cout << "queue is empty" << endl;
        }
        else{
            QueueNode *now=front;
            front=now->next;
            delete now;
            now = 0;
            size-=1;
        }
    }
    bool IsEmpty(){
        if(front == NULL){
            return true;
        }
        else{
            return false;
        }
    }
    int getFront(){
        if(front == NULL){
            cout << "queue is empty" << endl;
            return -1;
        }
        else{
            return front->data;
        }
    }
    int getBack(){
        if(front == NULL){
            cout << "queue is empty" << endl;
            return -1;
        }
        else{
            return back->data;
        }
    }
    int getSize(){
        return size;
    }
};
#endif