#include<iostream>
#include<windows.h>
using namespace std;

int mian(){
	
	int h,m,s;
	cout<<"---Set Current Time-----"<<endl;
	
	do{
		cout<<"Enter Hpurs:";
		cin>>h;
		
		
	}
	while(!(h<24));
	do{
		cout<<"Enter Minutes:";
		cin>>m;
		
	}	
	while(!(m<60));
	do{
		cout<<"Enter Seconds: ";
		cin>>s;
	}	
	while(!(s<60));
	system("cls");
	
	while(true){
		system("cls");
		cout<<"\n   ---------------";
		cout<<"\n   |  "<<h<<":"<<m<<":"<<s<<"    |";
		cout<<"\n   ----------------";
		
		Sleep(1000);
		s++;
		if(s>59){
			s=0;
			m++;
		}
		if(m>59){
			m=0;
			h++;
		}
		if(h>24){
			h=0;
		}
	}
	

	return 0;
}

