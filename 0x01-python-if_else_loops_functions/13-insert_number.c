#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
listint_t *create_node(listint_t *new, int num)
{
	new = malloc(sizeof(listint_t));
        if (!new)
	{
		return (NULL);
	}
	new->n = num;
	new->next = NULL;
	return (NULL);
}

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *aux, *prev;
        int i;

	new = create_node(new, number);
	if (!new)
		return (NULL);
	aux = *head;
	if (aux->n >= new->n)
	{
		new->next = aux;
		*head = new;
		return (*head);
	}
	aux = aux->next;
	prev = *head;
	for (i = 0; aux->next == NULL; i++)
	{
		if (aux->n >= new->n)
		{
			prev->next = new;
			new->next = aux;
			return (new);
		}
		aux = aux->next;
		prev = prev->next;
	}
	aux->next = new;
	return (new);

}

