#include "lists.h"

/**
 * check_cycle - is a function that checks if a singly linked list
 *		has a cycle in it.
 *
 * @list: head of linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list, *last = list;

	if (!list)
		return (0);

	while (1)
	{
		if (first->next != NULL && first->next->next != NULL)
		{
			first = first->next->next;
			last = last->next;

			if (first == last)
				return (1);
		}
		else
			return (0);
	}

}
