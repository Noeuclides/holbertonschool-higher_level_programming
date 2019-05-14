#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * create_node - create a new node.
 *
 * @new: pointer to a new node created.
 *
 * @num: integer value of the node
 *
 * Return: Address of the new node or NULL if it fails.
 */

listint_t *create_node(listint_t *new, int num)
{
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = num;
	new->next = NULL;
	return (new);
}

/**
 * insert_node - compare values of a linked list with a new node to insert.
 *
 * @number: value of the node to add
 *
 * @head: address of the first node
 *
 * Return: Address of the new node or NULL if it fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *aux, *prev;
	int i;

	new = create_node(new, number);
	if (!new)
		return (NULL);
	if (!*head)
	{
		*head = new;
		return (*head);
	}
	aux = *head;
	if (aux->n >= new->n)
	{
		new->next = aux;
		*head = new;
		return (*head);
	}
	aux = aux->next;
	prev = *head;
	for (i = 0; aux->next != NULL; i++)
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

