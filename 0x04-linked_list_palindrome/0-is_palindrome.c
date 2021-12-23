#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function to check if singly linked list is a palindrome
 * @head: double pointer to begining of the list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *end_node = (*head);
	int idx = 0; /* the count */
	int start = 0;
	int list[4096];

	/* If the list is non existent */
	if (head == NULL)
		return (0);

	/* If the list is empty, but exists */
	if (*head == NULL)
		return (1);

	/* Move end node through the list to the end, to find length */
	while (end_node != NULL)
	{
		list[idx] = end_node->n;
		idx++;
		end_node = end_node->next;
	}

	while (start <= idx - 1) /* idx - 1 is the end of the list */
	{
		if (list[start] == list[idx - 1])
		{
			start++;
			idx--;
		}
		else
		{
			return (0);
		}

	}
	return (1);
}
