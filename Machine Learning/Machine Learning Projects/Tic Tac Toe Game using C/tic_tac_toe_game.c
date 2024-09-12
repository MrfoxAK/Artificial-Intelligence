#include <stdio.h>
#define N 3



int main()
{
     int arr[N][N];
     int row, col;
     int player1, player2;
     for (int i = 0; i < N; i++)
     {
          for (int j = 0; j < N; j++)
          {
               arr[i][j] = 0;
          }
     }
     for (int i = 0; i < N; i++)
     {
          for (int j = 0; j < N; j++)
          {
               printf("%d ",arr[i][j]);
          }
          printf("\n");
     }
     printf("Lets Start the Game:\n");
     while (1)
     {
          printf("Player 1 - ");
          printf("Enter row: ");
          scanf("%d",&row);
          printf("Enter col: ");
          scanf("%d",&col);
          arr[row][col] = 1;
          // If condition should be here
          if( ((arr[row][0] == 1) && (arr[row][1] == 1) && (arr[row][2] == 1)) || ((arr[0][col] == 1) && (arr[1][col] == 1) && (arr[2][col] == 1)) ){
               printf("player 1 Wins");
               break;
          }
          printf("Player 2 - ");
          printf("Enter row: ");
          scanf("%d",&row);
          printf("Enter col: ");
          scanf("%d",&col);
          arr[row][col] = -1;
          if( ((arr[row][0] == -1) && (arr[row][1] == -1) && (arr[row][2] == -1)) || ((arr[0][col] == -1) && (arr[1][col] == -1) && (arr[2][col] == -1))){
               printf("player 2 Wins");
               break;
          }
     }
     // without diagonal position
     return 0;
}