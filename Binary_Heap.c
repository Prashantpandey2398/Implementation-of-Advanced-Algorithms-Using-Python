#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <conio.h>
#include <math.h>

struct node{
	int data;
	struct node *left;
	struct node *right;
};

struct node *root = NULL;

struct node *display(struct node *ptr){
	if(ptr == NULL){
		if(root==NULL){
		printf("Heap is empty\n");	
		}
		return;
	}
	display(ptr->left);
	printf("%d ",ptr->data);
	display(ptr->right);
}

struct node *heapify(struct node *ptr){
	int ro,le,ri,temp;
	if(!(ptr->left==NULL)){
		if(!(ptr->right==NULL)){
			ro=ptr->data;
			le=ptr->left->data;
			ri=ptr->right->data;
			if(le<ri){
				if(le<ro){
					temp=ptr->left->data;
					ptr->left->data=ptr->data;
					ptr->data=temp;
					heapify(ptr->left);
				}
			}
			else{
				if(ri<ro){
					temp=ptr->right->data;
					ptr->right->data=ptr->data;
					ptr->data=temp;
					heapify(ptr->right);
				}
			}
		}
		else{
			ro=ptr->data;
			le=ptr->left->data;
			if(le<ro){
				temp=ptr->left->data;
				ptr->left->data=ptr->data;
				ptr->data=temp;
				heapify(ptr->left);
			}
		}
	}  	
}

int extract_min(struct node *lt_root,int a[], int n, int index){
	int flag=1;
	if(root==NULL){
		printf("Unable to delete as heap is empty");
		flag=0;  
	}
	else{
		if(n==1){
			root=NULL;
		}
		else{
		struct node *ptr;
		ptr=lt_root;
		int temp;
		if(index==(n-2)){
			if(a[index+1]==0){
			temp=ptr->left->data;	
			ptr->left=NULL;
			root->data=temp;				
			}
			else{
			temp=ptr->right->data;	
			ptr->right=NULL;
			root->data=temp;
			}
			heapify(root);				
		}
		else{
			if(a[index+1]==0){
			ptr=ptr->left;				
			}
			else{
			ptr=ptr->right;					
			}
			index+=1;
			extract_min(ptr, a, n, index);
		}	
		}
	}
	return flag;
}
struct node *insert(struct node *lt_root, int num, int a[], int n, int index){
	struct node *new_node;
	new_node = (struct node *)malloc(sizeof(struct node));
	if(root==NULL){
		new_node->data=num;
		new_node->left=NULL;
		new_node->right=NULL;
		root=new_node;
	}
	else{
		struct node *ptr;
		ptr=lt_root;
		if(index==(n-2)){
			if(a[index+1]==0){
			new_node->data=num;
		    new_node->left=NULL;
		    new_node->right=NULL;
			ptr->left=new_node;				
			}
			else{
			new_node->data=num;
		    new_node->left=NULL;
		    new_node->right=NULL;
			ptr->right=new_node;					
			}
		}
		else{
			if(a[index+1]==0){
			ptr=ptr->left;				
			}
			else{
			ptr=ptr->right;					
			}
			index+=1;
			insert(ptr, num, a, n, index);
		}
		int ro,le,ri,temp;
		if(!(lt_root->left==NULL)){
			if(!(lt_root->right==NULL)){
				ro=lt_root->data;
				le=lt_root->left->data;
				ri=lt_root->right->data;
				if(le<ri){
					if(le<ro){
						temp=lt_root->left->data;
						lt_root->left->data=lt_root->data;
						lt_root->data=temp;
					}
				}
				else{
					if(ri<ro){
						temp=lt_root->right->data;
						lt_root->right->data=lt_root->data;
						lt_root->data=temp;
					}
				}
			}
			else{
				ro=lt_root->data;
				le=lt_root->left->data;
				if(le<ro){
					temp=lt_root->left->data;
					lt_root->left->data=lt_root->data;
					lt_root->data=temp;
				}
			}
		}  		
	}
}

int isempty(struct node *root){
	int flag=1;
	if(root== NULL){
		flag=0;
	}
	return flag;
}

int main(){
	int flag;
	int choice;
	int num_nodes=0;
	do{
	printf("1. Insert a node : \n");
	printf("2. Extract Min : \n");
	printf("3. Is Empty : \n");
	printf("4. Print Heap in Inorder Traversal : \n");
	printf("5. Exit : \n");
	printf("Enter your choice : ");
	scanf("%d",&choice);
	switch(choice){
		case 1:{
		num_nodes+=1;
		int n;
		double b = num_nodes;
	    n=ceil((log(b+1)/log(2)));
	    int a[n];
	    int num;
	    printf("Enter the number : ");
	    scanf("%d",&num);
	    int i=0,rem;
	    int div=num_nodes;
	    while(div!=0){
	    	rem=div%2;
	    	a[n-i-1]=rem;
	    	i+=1;
	    	div/=2;
		}
		insert(root, num , a , n, 0);
		break;
		}
		case 2:{
		int n;
		double b = num_nodes;
	    n=ceil((log(b+1)/log(2)));
	    int a[n];
		int i=0,rem;
	    int div=num_nodes;
	    while(div!=0){
	    	rem=div%2;
	    	a[n-i-1]=rem;
	    	i+=1;
	    	div/=2;
		}
		int flag = extract_min(root, a , n, 0);
		if(flag!=0){
		num_nodes-=1;
		printf("Root is deleted\n");	
	}
		break;
		}
		case 3:{
			flag = isempty(root);
		              if(!flag){
		       	printf("Heap is empty\n");
			}
			else{
			printf("Heap is not empty\n");
			}
		               break;
		}
		case 4:{
			printf("Displaying Min-Heap in Inorder Traversal : \n");
			display(root);
			printf("\n");
			break;
		}
	}
	printf("\n");
	}while(choice!=5);
	return 0;
}
