#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <conio.h>
#include <math.h>

struct node{
	int data;
	struct node *next;
	struct node *prev;
	struct node *child;
	struct node *parent;
	int degree;
	int mark;
};

struct node *start = NULL;
struct node *st1 = NULL;
struct node *st2 = NULL;

int num_trees=0;
struct node *display(struct node *star){
	struct node *ptr=star;
	if(start == NULL){
		printf("List is empty");
	}
	else{
		if(ptr!=NULL){
			do{
				printf("%d",ptr->data);
				display(ptr->child);
				ptr=ptr->next;
			}while(ptr!=star);
		}
	}
}

struct node *join_list(struct node *f1,struct node *f2){
	if(f1==NULL&&f2==NULL){
		return f1;
	}
	else if(f1==NULL&&f2!=NULL){
		return f2;	
	}
	else if(f1!=NULL&&f2==NULL){
		return f1;
	}
	else{
		struct node *t1, *t2;
		t1 = f1->prev;
		t2 = f2->prev;
		t1->next=f2;
		f2->prev=t1;
		f1->prev=t2;
		t2->next=f1;
		return f1;		
	}
}

struct node *merge(struct node *f1,struct node *f2){
	if(f1==NULL&&f2==NULL){
		return f1;
	}
	else if(f1==NULL&&f2!=NULL){
		return f2;	
	}
	else if(f1!=NULL&&f2==NULL){
		return f1;
	}
	else{
		struct node *t1, *t2;
		t1 = f1->prev;
		t2 = f2->prev;
		t1->next=f2;
		f2->prev=t1;
		f1->prev=t2;
		t2->next=f1;
		if(f1->data<f2->data){
			return f1;
		}
		else{
			return f2;
		}		
	}
}

struct node *fib_heap_link(struct node *temp, struct node *temp1){
	struct node *ptr=temp;
	ptr->prev->next=temp1;
	temp1->prev=ptr->prev;
	temp->mark=0;
	ptr->next=ptr;
	ptr->prev=ptr;
	struct node *ptr1;
	ptr1=temp1->child;
	ptr1=join_list(ptr1,ptr);
	temp1->child=ptr1;
	temp1->degree+=1;
	return temp1;	
}

struct node *consolidate(struct node *star, int num_nodes){
	struct node *ptr=star;
	struct node *temp;
	int n,reduced_trees=0;
	if(ptr!=NULL){
		double b = (double)num_nodes;
	    n=floor((log(b)/log(2)));
	    int a[n+1];
	    int i;
	    for(i=0;i<=n;i++){
	    	a[i]=-1;
		}
		int d,trees_count=0;
		struct node *temp_ad,*c;
		do{
			temp=ptr;
			if(star->data>temp->data){
				star=temp;
			}
			d=temp->degree;
			while(a[d]!=-1){
				temp_ad=a[d];
				reduced_trees+=1;
				if((temp->data)>(temp_ad->data)){
					ptr=fib_heap_link(temp,temp_ad);
				}
				else{
					ptr=fib_heap_link(temp_ad,temp);
				}
				a[d]=-1;
				d+=1;
			}
		a[d]=temp;
		ptr=ptr->next;
		trees_count+=1;
		}while (trees_count<num_trees);
	}
	num_trees-=reduced_trees;
	return star;
}

struct node *extract_min(struct node *star, int num_nodes){
	struct node *ptr=star;
	if(ptr==NULL){
		printf("Nothing can be deleted");
	}
	else{
		struct node *temp,*temp1;
		temp1=ptr->child;
		num_trees+=ptr->degree;
		num_trees-=1;
		if(ptr==ptr->next){
			free(star);
			star=NULL;
		}
		else{
			while(ptr->next!=star){
				ptr=ptr->next;
			}
			ptr->next=star->next;
			temp=star;
			star=star->next;
			star->prev=ptr;
			free(temp);	
		}
		star = join_list(star,temp1);
		star = consolidate(star,num_nodes);		
	}
	return star;
}

struct node *find_key(struct node *star, int num, int *flag){
	struct node *ptr=star;
	if(start == NULL){
		printf("Heap is empty");
	}
	else{
		if(ptr!=NULL){
			do{
				if(ptr->data==num){
					*flag=1;
					break;
				}
				else if(ptr->data<num){
					ptr=find_key(ptr->child,num,&flag);
				}
				if(*flag==0){
					ptr=ptr->next;
				}				
			}while(ptr!=star&&*flag!=1);
		}
	}
	printf("%d",ptr->data);
	return ptr;
}

struct node *insert(struct node *star, int num){
	struct node *new_node,*ptr;
	ptr=star;
	new_node = (struct node *)malloc(sizeof(struct node));
	if(ptr==NULL){
		new_node->data=num;
		new_node->next=new_node;
		new_node->prev=new_node;
		new_node->parent=NULL;
		new_node->child=NULL;
		new_node->degree=0;
		new_node->mark=0;
		ptr=new_node;
	}
	else{
		new_node->data=num;
		struct node *temp1,*temp2;
		temp1=ptr->next;
		temp2=ptr->prev;
		new_node->next=temp1;
		new_node->prev=ptr;
		new_node->parent=NULL;
		new_node->child=NULL;
		new_node->degree=0;
		new_node->mark=0;
		ptr->next=new_node;
		if(ptr->next==start){
			ptr->prev=new_node;
		}
		int s1,s2;
		s1=star->data;
		s2=star->next->data;
		if(s2<s1){
			ptr=star->next;
		}
	}
	num_trees+=1;
	return ptr;
}

int main(){
	int choice;
	int num_nodes=0;
	do{
	printf("1. Insert a node : \n");
	printf("2. Extract Min : \n");
	printf("3. Merge two Fibonocci Heaps : \n");
	printf("4. Decrease Key : \n");
	printf("5. Delete : \n");
	printf("6. Print Heap in Inorder Traversal : \n");
	printf("7. Exit : \n");
	printf("Enter your choice : ");
	scanf("%d",&choice);
	switch(choice){
		case 1:{
		int num;
	    printf("Enter the number : ");
	    scanf("%d",&num);
	    num_nodes+=1;
		start = insert(start, num );
		break;
		}
		case 2:{
		num_nodes-=1;
		start=extract_min(start,num_nodes);
		break;
		}
		case 3:{
			st1=merge(start,start->child);
			printf("After merging start and its child : \n");
		    display(st1);
			break;
		}
		case 4:{
			int num,new_num;
			printf("Enter the number whose key you want to change : ");
			scanf("%d",&num);
			printf("Enter the new key : ");
			scanf("%d",&new_num);
			int flag=0;
			struct node *ptr;
			ptr=find_key(start,num,&flag);
			printf("%d",flag);
			if(flag==1){
				//printf("%d",ptr->data);
			}
			break;
		}
		case 5:{
			break;
		}
		case 6:{
			printf("Displaying Linked List : \n");
			display(start);
			printf("\n");
			break;
		}
		
	}
	printf("\n");
	}while(choice!=7);
}
