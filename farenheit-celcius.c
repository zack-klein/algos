#include <stdio.h>
 /* print Fahrenheit-Celsius table
    for fahr = 0, 20, ..., 300 */
#define LOWER 0
#define UPPER 300
#define STEP 20


main()
{
  float fahr, celsius;
  fahr = LOWER;
  printf("Fahrenheit -> Celsius!\n");
  printf("----------------------\n");
  while (fahr <= UPPER) {
    celsius = (5.0/9.0) * (fahr-32.0);
    printf("%3.0f\t%6.1f\n", fahr, celsius);
    fahr = fahr + STEP;
  }

  printf("\n\n");

  celsius = LOWER;
  printf("Celsius -> Fahrenheit!\n");
  printf("----------------------\n");
  while (celsius <= UPPER) {
    fahr = celsius * (9.0/5.0) + 32;
    printf("%3.0f\t%6.1f\n", celsius, fahr);
    celsius = celsius + STEP;
  }


}
