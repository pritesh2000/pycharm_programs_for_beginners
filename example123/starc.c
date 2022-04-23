int n;
char ch;
printf("\nEnter the number of rows");
scanf("%d", &n);
fflush(stdin);
printf("\nEnter the character");
scanf("%c", &ch);
for(t=1;t<=3;t++){
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            printf("%c", ch);
        }
        printf("\n");
    }
}

for(i=n;i>=1;i--){
    for(j=1;j<=i;j++){
        printf("%c",ch);
    }
    printf("\n");
}
