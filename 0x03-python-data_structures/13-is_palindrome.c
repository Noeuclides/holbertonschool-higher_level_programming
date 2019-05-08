#include "lists.h"

/**
* is_palindrome - function that checks if a list is palindrome.
*
*@head: linked list.
*
*Return: 1 if is palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	int array[1000000];
	int i, j, n, l;
	listint_t *aux;

	if (head == NULL || *head == NULL)
		return(1);
	aux = *head;
	for (i = 0; aux != NULL; i++)
	{
		array[i] = aux->n;
		aux = aux->next;
	}
	n = i - 1;
	for (j = n, l = 0; j > (n / 2); j--, l++)
	{
		if (array[j] != array[l])
			return (0);
	}
	return (1);
}

