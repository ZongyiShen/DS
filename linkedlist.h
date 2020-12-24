#ifndef LINKEDLIST
#define LINKEDLIST
#include <cmath>
#include <string>
#include <stdio.h>
#include <iostream>
using namespace std;
class linkedlist;
class node{
    private:
        int data;
        node *next;
        node *prev;
    public:
        node():data(0),next(0),prev(0){}; //default constructor
        node(int a):data(a),next(0),prev(0){}; //constructor
        int getdata() const{
            return data;
        }
        void setdata(int a){
            data=a;
        }
        node * getnext() const{
            return next;
        }
        node * getprev() const{
            return prev;
        }
        friend class linkedlist;
};
class linkedlist{
    private:
        int size;
        node *head;
    public:
    linkedlist():size(0),head(0){};
    void PrintList(){
        node *now =head;
        while(now != NULL){
            cout << now->data << endl;
            now=now->next;
        }
    }// 印出list的所有資料
    void Push_front(int x){
        node *n;
        n=new node;
        n->setdata(x);
        n->next=head;
        head=n;
        size+=1;
    }// 在list的開頭新增node
    void Push_back(int x){
        node *n;
        n=new node;
        n->setdata(x);
        if(head == NULL){
            Push_front(x);
        }
        else{
            node *now=head;
            while(now->next != NULL){
                now=now->next;
            }
            now->next=n;
            n->prev=now;
        }
        size+=1;
    }
    void insert(node *n,int x){
        node *now=head;
        if(n == head){
            Push_front(x);
        }
        while(now != NULL){
            if(now == n){
                node *x1;
                x1=new node;
                x1->setdata(x);
                now->prev->next=x1;
                x1->next=now;
            }
            now=now->next;
        }
        size+=1;
    }//把data為x的node插入到node n的位置
    void insertat(int locate,int x){
        node *now=head;
        for(int i=0;i<locate;i++){
            now=now->next;
        }
        insert(now,x);
    }//把data為x的node插入到index為locate的位置
    void Delete(int x){
        node *now=head;
        if(head == NULL){
            cout <<"empty list!" << endl;
        }
        else if(now->data == x){
            head=now->next;
            delete now;
            size-=1;
        }
        else{
            while(now->next != NULL){
                if(now->data == x){
                    now->prev->next=now->next;
                    now->next->prev=now->prev;
                    delete now;
                    size-=1;
                }
                else{
                    now=now->next;
                }
            }
            if(now->next == NULL && now->data == x){
                now->prev->next=NULL;
                delete now;
                size-=1;
            }
        }
    }//刪除第一個data為x的node
    node * at(int x){
        node *now=head;
        for(int i=0;i<x;i++){
            now=now->next;
        }
        return now;
    }//回傳index為x的node
    void Clear(){
        while(head != NULL){
            node *now=head;
            head=head->next;
            delete now;
            now=0;
        }
    }// 把整串list刪除
    void arraytolinkedlist(int a[],int len){
        node *now=head;
        Push_front(a[0]);
        for(int i=1;i<len;i++){
            Push_back(a[i]);
        }
        size=len;
    }//把array轉成linkedlist
    void Reverse(){
        node *previous=NULL;
        node *current=head;
        node *preceding=head->next;
        while(preceding != NULL){
            current->next=previous;
            previous=current;
            current=preceding;
            preceding=preceding->next;
        }
        current->next=previous;
        head=current;
    }// 將list反轉: 7->3->14 => 14->3->7
    node * gethead() const{
        return head;
    }
    int getsize() const{
        return size;
    }
};
#endif