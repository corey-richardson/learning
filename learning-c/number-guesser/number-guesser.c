#include <stdio.h>
#include <stdlib.h>  
#include <time.h>

int main(){
    int number_to_guess = 0;
    int guess_counter = 1;
    int guessed = 0; // 0 false, 1 true
    int user_guess;

    srand(time(NULL)); // Initialization, should only be called once.
    number_to_guess = rand() % 100 + 1; // generates a number less than 100
    number_to_guess = (int)number_to_guess; // casts to an int
    // printf("%i\n", number_to_guess); // used to test

    while (guessed == 0){ // while the number has not been guessed:
        printf("Enter your guess: ");
        scanf("%i", &user_guess); // user input, takes an int and saves to the memory address of "user_guess"
        if (user_guess == number_to_guess){ // if the guess is correct
            printf("\nCorrect! You guessed the number %i in %d attempts!\n",number_to_guess, guess_counter);
            guessed = 1; // when guessed, set guessed to 1 to break the while loop
        } 
        else {
            guess_counter++; // increment
            if (number_to_guess < user_guess){
                printf("Too high!\n");
            } 
            else if (number_to_guess > user_guess){
                printf("Too low!\n");
            } 
            else {
                printf("you shouldnt see this lol\n"); // brokey
            }    
        }
    }
}