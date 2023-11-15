 //6

const html = `
    <html>
        <body>
            <img src="Image1.jpg" alt="Image 1">
            <img src="Image2.jpg" alt="Image 2">
        </body>
    </html>
`;

const imgRegex = /<img[^>]+src\s*=\s*['"]([^'"]+)['"][^>]*>/g;
const matches = html.matchAll(imgRegex);

for (const match of matches) {
    console.log("Image URL: " + match[1]);
}
