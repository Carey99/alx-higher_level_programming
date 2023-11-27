#include "lists.h"
/**
 * check_cycle - Checking for cycle
 * @list: Head pointer
 * Return: 0 if cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t **head = malloc(sizeof(listint_t));

	if (list == NULL)
	{
	return (0);
	}
	if (*head == NULL)
	{
	return (-1);
	}
	while (*head != NULL && (*head)->next != NULL)
	{
	*head = (*head)->next;
	*head = (*head)->next->next;

	if (*head == list)
	{
	return (1);
	}
	}
	return (0);
}
