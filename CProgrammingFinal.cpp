/*
C Programming Final
Name: Elias Perez
Date: August 30th, 2018
*/

#include <Windows.h>
#include <stdio.h>
#include "TestCode.h"
#include <string.h>

/////////////////////////////////////////////////////////////
// Test 1: For this task, you will receive two pointers to NULL terminated strings: 
//		   a 'sentence', and a 'word'. The objective will be to delete (in place) the first 
//		   occurrence of 'word' in the sentence. 
//
// Expected Return Values:
//		- the task is successful: should return ERROR_SUCCESS (0).
//		- provided parameters are bad: should return ERROR_INVALID_PARAMETER (87)
//		- the provided 'word' is not part of 'sentence': should return ERROR_NOT_FOUND (1168)
/////////////////////////////////////////////////////////////

//c-programmed substring function
int search(char[], char[]);
//removes the substring from the sentence
int delete_word(char[], char[], int);

//delete word function complete, moving on to test 3
int deleteWord(char* sentence, char* word)
{
	char temp[sizeof(word)] = { 0 }; //we create a temporary buffer, to hold the substrings passed
	int status = ERROR_SUCCESS;
	int count = 0;
	//alright, so we get a word and a sentence. what we need to do is pull the word out of the sentence. since we arent using c#, i cant use .contains(), 
	//so ill have to try and use a substring function, or something similar
	if (sentence == NULL)
	{
		status = ERROR_INVALID_PARAMETER;
	}
	else if (word == NULL)
	{
		status = ERROR_INVALID_PARAMETER;
	}
	else if ((sentence != NULL) && (word != NULL))
	{
		int index;

		index = search(sentence, word);
		if (index != -1)
		{
			delete_word(sentence, word, index);
		}
		else if (index == -1)
		{
			return ERROR_NOT_FOUND;
		}
	}
	//return the proper error dependent upon value
	return status;
}  

//here we find the substring inside the string, and return a value indicating we then delete the word
int search(char str[], char word[])
{
	int l, i, j;

	/* finding length of word */
	for (l = 0; word[l] != '\0'; l++);

	for (i = 0, j = 0; str[i] != '\0' && word[j] != '\0'; i++)
	{
		if (str[i] == word[j])
		{
			j++;
		}
		else
		{
			j = 0;
		}
	}

	if (j == l)
	{
		/* substring found */
		return (i - j);
	}
	else
	{
		return  -1;
	}
}

//deletes the word from our sentence
int delete_word(char str[], char word[], int index)
{
	int i, length;

	/* finding length of word */
	for (length = 0; word[length] != '\0'; length++);
	length--; //pull one of the length to include the space

	for (i = index; str[i] != '\0'; i++)
	{
		if (str[i] == " ")
		{
			//do nothing for spaces. keep them
		}
		else 
		{
			//iterate and DESTROY THA WORD
			str[i] = str[i + length + 1];
		}
	}
}

/////////////////////////////////////////////////////////////
// Test 3 (part one): This task will involve allocating a buffer
//				of (sizeOfData) bytes, and reading up to that amount
//				into it from the file specified in 'filename'. Additionally,
//				the data in the file has been pseudo-encryped (poorly) with a single-
//				byte XOR, which you will be required to undo (the byte that the buffer
//				was XOR'd against will be provided in 'key'). Finally, assuming the task
//				was successful, (and all pointers are valid) the pointer to the resulting 
//				buffer should be stored in the area referenced by buffPtr.
//
// Expected Return Values:
//			- task was completed successfully: ERROR_SUCCESS (0)
//			- bad input was provided: ERROR_INVALID_PARAMETER (87)
//			- you were unable to allocate enough memory: ERROR_OUTOFMEMORY (14)
//			- you were unable to open the file: ERROR_OPEN_FAILED (110)
/////////////////////////////////////////////////////////////
int decodeFromFile(char* filename, unsigned int sizeOfData, unsigned char key, void** buffPtr)
{
	int status = ERROR_SUCCESS;
	//alright first allocate the buffer of (sizeOfData)
	char *inputString = "";

	//lets pull some null checks for bad input
	if (filename == NULL)
	{
		status = ERROR_INVALID_PARAMETER;
	}
	else if (sizeOfData == NULL)
	{
		status = ERROR_INVALID_PARAMETER;
	}
	else if (key == NULL)
	{
		status = ERROR_INVALID_PARAMETER;
	}
	else if (buffPtr == NULL)
	{
		status = ERROR_INVALID_PARAMETER;
	}
	else
	{
		//build a counter variable for the buffer we will be using
			*buffPtr = inputString;
			int count = 0;
			FILE * file_ptr = fopen(filename, "r");//opens a read-only file
			char read_from_file = 0; //just need it to exist here for a sec so i can properly follow the example ya'll gave us
			if (file_ptr != NULL)
			{	
				inputString = malloc(sizeOfData);
				if (inputString != NULL)
				{
					while ((read_from_file != sizeOfData) && (read_from_file != EOF) && (inputString != NULL)) //since we only want to read a certain portion of the file
					{
						//double check for null pointers
						read_from_file = getc(file_ptr);
						inputString[count] = read_from_file ^ key; //read it into the buffer, but decoded
						count++;
					}
					fclose(file_ptr); //Fclose(). yknow. friggin close the file

					//the resulting pointer needs to be referenced to the area in buffPtr.... whatever that means. 
					//it might just be the wording, but that dont make jack for sense to me
				}
				else 
				{
					fclose(file_ptr); //Fclose(). yknow. friggin close the file
					return ERROR_OUTOFMEMORY;
					
				}
			}
			else
			{
				status = ERROR_OPEN_FAILED; //oops! didnt open
			}
	}
	*buffPtr = inputString;
	return status;
}

/////////////////////////////////////////////////////////////
// Test 3 (part two): The second part of the task; this simply requires you
//				  to appropriately free the buffer allocated in the last task
//				  (if possible).
//
// Expected Return Values:
//			- the task completed successfully: TRUE
//			- the task failed/bad input: FALSE
/////////////////////////////////////////////////////////////
BOOL freeDecodedBuffer(void* buffer)
{
	BOOL out = FALSE;

	free(buffer);

	return out;
}