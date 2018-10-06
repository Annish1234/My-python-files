#include<stdio.h>
#include<stdlib.h>
void create();
void dispaly():
void insert_begin();
void insert_end();
void insert_pos();
void delete_begin();
void delete_end();
void delete_pos();
struct node 
{
	int data;
	struct node*next;
};
struct node*first=NULL;
int main()
{
	int choice;
	while(1){
		printf("\n***SINGLE LINKED LIST OPERATIONS:***\n");
		printf("\n MENU \n");
		printf("____________________\n");
		printf("\n 1.Create \n");
		printf("\n 2.Display\n");
		printf("\n 3.Insert at the beginning \n");
		printf("\n 4.Insert at the end \n");
		printf("\n 5.Insert at the specified postion \n");
		printf("\n 6.Delete from beginning \n");
		printf("\n 7.Delete from the end \n");
		printf("\n 8.Delete from the specified postion\n");
		printf("\n 9.Exit \n");
		printf("\n______________________\n");
		printf("Enter your choice:\t");
		scanf("%d",&choice);
		switch(choice)
		{
			case1:
	              create();
			      break;


            case2:
                 dispaly();
                 break;

            case3:
                  insert_begin();
                  break;

            case4:
                  insert_end();
                  break;
            case5:
                  insert_pos();
                  break;
            case6:
                  delete_begin();
                  break;
             case7:
                   delete_end();
                   break;
             case8:
                  delete_pos();
                  break;

              default:
                      printf("\n Wrong Choice:\n");
                      break;

		}//end of switch()

	}
	return 0;
}
void create()
{
	struct node *temp,*ptr;
	temp=(struct node *)malloc(size of(struct node));
	if(temp==NULL)
	{
		printf("\nOut of Memory Space:\n");
		exit(0);

	}
		printf("\nEnter the data value for the node:\t");
		scanf("%d",&temp->data);
		temp->next=NULL;
		if(first==NULL)
		{
			first=temp;
		}
		else
		{
			ptr=first:
			while(ptr->next!=NULL)
			{
				ptr=ptr->next;

			}
			ptr->next=temp;
		}

	}
	void dispaly()
	{
		struct node *ptr;
		if(first==NULL)
		{
			printf("\nList is empty:\n");
			return;
		}
		else 
		{
			ptr=first;
			printf("\nThe List elements are:\n");
			while(ptr!=NULL)
			{
				printf("%d\t",ptr->data);
				ptr=ptr->next;
			}
		}
	}
	void insert_begin()
	{
		struct node*temp;
		temp=(struct node*)malloc(sizeof(structnode));
		if(temp==NULL)
		{
			printf("\nOut of Memory Space:\n");
			return;
		}
	printf("\nEnter the data value for the node:\t");
	scanf("%d",&temp->data);
	temp->next=NULL;
	if(first==NULL)
	{
		first=temp;
	}
	else
	{
		temp->next=first;
		first =temp;
	}
}
void insert_end()
{
	struct node*temp,*ptr;
		temp=(struct node*)malloc(sizeof(structnode));
		if(temp==NULL)
		{
			printf("\nOut of Memory Space:\n");
			return;
		}
	printf("\nEnter the data value for the node:\t");
	scanf("%d",&temp->data);
	temp->next=NULL;
	if(first==NULL)
	{
		first=temp;
	}
	else 
	{
		ptr=first;
		while(ptr->next!=NULL)
		{
			ptr=ptr->next;
		}
		ptr->next=temp;
	}
}

void insert_pos()
{
	struct node*ptr,*temp;
	inti,pos;
		temp=(struct node*)malloc(sizeof(structnode));
		if(temp==NULL)
		{
			printf("\nOut of Memory Space:\n");
			return;
		}
		printf("\nEnter the postion for the new node to be inserted:\t");
		scanf("%d",&pos);
		printf("\nEnter the data value of the node:\t");
		scanf("%d",&temp->data);

		temp->next=NULL;
		if(pos==0)
		{
			temp->next=first;
			first=temp;
			
		}
}