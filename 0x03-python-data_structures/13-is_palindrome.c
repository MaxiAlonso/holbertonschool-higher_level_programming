#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head node of the list
 * Return: 1 if list is palindrome 0 if it not
 **/

int is_palindrome(listint_t **head)
{
	int len = 0, middle = 0, i = 0, end = 0, r = 0;
	listint_t *left_node = *head, *right_node = *head, *len_node = *head;

	if (head != NULL)
	{
		while (len_node != NULL)
		{
			len_node = len_node->next;
			len++;
		}
		if (len % 2 == 0)
			middle = len / 2;
		else
			middle = (len + 1) / 2;
		end = len;
		while (i < middle)
		{
			r = 0;
			right_node = *head;
			while (r != end - 1)
			{
				right_node = right_node->next;
				r++;
			}
			if (left_node->n != right_node->n)
			{
				return (0);
			}
			left_node = left_node->next;
			end--;
			i++;
		}
	}
	return (1);
}
