#include <stdlib.h>
#include <stdio.h>

typedef struct Node {

	struct Node *next;
	char letter;

}Node;

int displayall(struct Node **stack) {

	int countelements = 0;
	Node *letter;
	if ( !(letter = *stack) ) {
		printf("\n The stack is empty \n");
		return -1;
	}
	if (!(letter->letter)) { 
		printf("\n The stack is empty \n");
		return -1;
	}
	while(letter->next != NULL) {

		printf("%c\n", letter->letter);
		letter = letter->next;
	}

	printf("%c\n", letter->letter);
	return 0;
}

int pop(struct Node **stack) {

	Node *letter;
	if ( !(letter = *stack) ) {
		printf("\n The stack is empty \n");
		return -1;
	}
	if (letter->letter) { 
		*stack = letter->next;
		free(letter);
		return 0;
	}
	else {
		printf("\n The stack is empty \n");
		return -1;
	}
	

}

int push (struct Node **stack, char letter) {

	struct Node *newletter = malloc(sizeof(struct Node));
	if ( !newletter ) {
		return -1;
	}
	newletter->letter = letter;
	newletter->next = *stack;
	*stack = newletter;
	return 0;

}

void parser(char *input, struct Node **stackA, struct Node **stackB, struct Node **stackC) {

	int counter = 0;
	while(*input) {
		if (*input >= 'A' && *input <= 'Z') {

			if (counter == 0) {
				push(stackA, *input);
			}
			else if (counter == 1) {
				push(stackB, *input);
			}
			else if (counter == 2) {
				push(stackC, *input);
			}
		

		}
		if(*input == ';') {

			counter++;
		}
		input++;
	}
}

int main() {
	
	int maxheight;
	int stacksheight[3] = {0,0,0,};
	char *input = malloc(sizeof(char) * 20);
	struct Node *stackA = malloc(sizeof(struct Node));
	struct Node *stackB = malloc(sizeof(struct Node));
	struct Node *stackC = malloc(sizeof(struct Node));
	printf("\n Give the max height number \n");
	
	//scanf("%i%*c", &maxheight);

	printf("\n Give the actual state of the stacks \n");

	scanf("%[^\n]s", input);
	parser(input, &stackA, &stackB, &stackC);
	printf("First stack\n");
	displayall(&stackA);
		printf("Second stack\n");

	displayall(&stackB);
		printf("Third stack\n");

	displayall(&stackC);
	printf("\n Give the result \n");

	return 0;
}