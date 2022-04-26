#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - adds a new node with a number into a sorted singly linked list
 * @head: pointer to the head of the list.
 * @number: data to insert in the node.
 * Return: address of the new element, or NULL if it failed
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev_node = *head;
	unsigned int count;

	count = 0;

	if (*head != NULL || head != NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
		{
			return (NULL);
		}
		if (prev_node->n > number)
		{
			new_node->n = number;
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
		while (prev_node != NULL && prev_node->next != NULL)
		{
			if (prev_node->next->n > number)
			{
				new_node->n = number;
				new_node->next = prev_node->next;
				prev_node->next = new_node;
				return (new_node);
			}
			prev_node = prev_node->next;
			count++;
		}
	}
	new_node->n = number;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
