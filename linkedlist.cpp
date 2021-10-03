#include "iostream"

using namespace std;

struct node{
    int data;
    struct node* link;
};

void add_node(struct node* HEAD,int data){
    
    struct node* current_node;

    if(HEAD -> data == NULL){
        HEAD -> data = data;
        cout << "[+]Data is added too the head\n";
    }
    else{
        current_node = HEAD;
       
        while(current_node -> link != NULL){
            current_node = current_node -> link;
        }

        struct node* new_node = (struct node*)malloc(sizeof(struct node));
        new_node -> data = data;
        new_node -> link = NULL;
        current_node -> link = new_node;

        cout <<"[+]Data has been added after: " << current_node -> data <<"\n";
    }
}

void add_after(struct node* HEAD, int after_this, int new_data)
{
    int node_count = 0;
    struct node* current_node = HEAD;

    while(current_node -> link != NULL){
        if(current_node -> data == after_this){
            struct node* new_node = (struct node*)malloc(sizeof(struct node));
            new_node -> data = new_data;
            new_node -> link = current_node -> link;
            current_node -> link = new_node;
            cout << "[+]Data had been added after: " << current_node -> data << " and before: "<< new_node -> link -> data <<"\n";
            return;
        }
        else
            current_node = current_node -> link;
    }

    if(current_node -> data == after_this)
    {
        struct node* new_node = (struct node*)malloc(sizeof(struct node));
        new_node -> data = new_data;
        new_node -> link = NULL;
        current_node -> link = new_node;
        cout <<"[+]Data has been added after: "<< current_node -> data <<" and new node is the tail node\n";
    }
    else
        cout <<"[-]Operation failed -- "<< after_this<<" does not exist in the linked list.\n"; 

}

void add_at_position(struct node* HEAD, int position, int new_data){
    
    if(position == 0)
    {
        struct node* new_node = (struct node*)malloc(sizeof(struct node));
        new_node -> data = HEAD -> data;
        new_node -> link = HEAD -> link;
        HEAD -> data = new_data;
        HEAD -> link = new_node;
        cout << "[+]New node has been added at 0 and assigned head.";
        return; 
    }

    struct node* current_node = HEAD;
    struct node* prev_node;
    int i = 0;
    cout<<"Entered here\n";

    while(i<position){
        cout << i <<"\n";
        prev_node = current_node;
        cout << "Prev node done\n";
        current_node = current_node -> link;
        cout<<"This done\n";
        i++;

        if(current_node == NULL and i != position){
            cout<<"[-]Operation failed: Given index is out of range \n";
            return;
        }
    }

    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    new_node -> data = new_data;
    new_node -> link = current_node;
    prev_node -> link = new_node;
    cout<< "[+]Data has been added after: "<< prev_node -> data<<" and before : "<< current_node -> data <<"\n";
}

void print_linked_list(struct node* HEAD)
{
    struct node* current_node = HEAD;

    cout << "# Beginning of the linkedlist\n";
    while(current_node -> link != NULL)
    {
        cout << current_node -> data <<"\n";
        current_node = current_node -> link;
    }
    cout << current_node -> data <<"\n";
    cout << "# End of the linkedlist\n";
}

int main(){
    struct node* HEAD = NULL;
    HEAD =(struct node*)malloc(sizeof(struct node));
    HEAD -> data = NULL;
    HEAD -> link = NULL;
    
    char nothing;
    int choice;
    int new_data;
    int after_this;
    int position;
    while(true)
    {
        cout<<"\n---------- MAKE YOUR CHOICE ----------\n";
        cout<<"1. Add a new node\n";
        cout<<"2. Add a new node after a value\n";
        cout<<"3. Add a new node at a position (0 indexed)\n";
        cout<<"4. Print the linked list\n";
        cout<<"Enter your choicee: ";
        cin >> choice;
        cout << "\n";

        switch(choice)
        {
            case 1: cout<< "Please enter the value to insert: ";
                    cin>> new_data;
                    add_node(HEAD,new_data);
                    break;
            case 2: cout<< "Please enter the value after which new value has to be inserted: ";
                    cin >> after_this;
                    cout<< "Please enter the value to insert: ";
                    cin>> new_data;
                    add_after(HEAD,after_this,new_data);
                    break;
            case 3: cout<<"Enter the position: ";
                    cin >> position;
                    cout<< "Please enter the value to insert: ";
                    cin>> new_data;
                    add_at_position(HEAD,position,new_data);
                    break;
            case 4: print_linked_list(HEAD);
                    break;
            default:cout << "Please enter a valid input !!\n";
                    break;
        }
    }
return 0;
}
