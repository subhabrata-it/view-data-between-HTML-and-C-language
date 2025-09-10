#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *lenstr;
    long len;
    char postdata[1024];

    printf("Content-Type: text/html\n\n");
    printf("<html><body>");

    lenstr = getenv("CONTENT_LENGTH");
    if (lenstr != NULL) {
        len = strtol(lenstr, NULL, 10);
        fread(postdata, 1, len, stdin);
        postdata[len] = '\0';

        // Show the received data
        printf("<h2>Received Data:</h2>");
        printf("<p>%s</p>", postdata);
    } else {
        printf("<p>No data received</p>");
    }

    printf("</body></html>");
    return 0;
}
