#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - function that checks if a list is palindrome.
*
*@head: linked list.
*
*Return: 1 if is palindrome, -1 if not
*/
int is_palindrome(listint_t **head)
{
	int array[1000];
	int i, j, n, l;
	listint_t *aux;

	aux = *head;
	for (i = 0; aux != NULL; i++)
	{
		array[i] = aux->n;
		aux = aux->next;
	}
	if (i % 2 == 0)
		n = i - 1;
	else
		n = i;
	for (j = n, l = 0; j > (n / 2) && l < (n / 2); j--, l++)
	{
		if (array[j] != array[l])
			return (-1);
	}
	return (1);
}

