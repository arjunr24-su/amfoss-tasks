document.addEventListener('DOMContentLoaded', () => {
    const productCatalog = document.getElementById('product-catalog');
    const terminalOutput = document.querySelector('.terminal-output');
    const terminalInput = document.querySelector('.terminal-input input');
    let products = [];
    let cart = [];

    // Fetch products from the Fake Store API
    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(data => {
            products = data;
            displayProducts(products);
        })
        .catch(error => console.error('Error fetching products:', error));

    function displayProducts(products) {
        productCatalog.innerHTML = '';
        products.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';

            const productImage = document.createElement('img');
            productImage.src = product.image;
            productImage.alt = product.title;

            const productTitle = document.createElement('h2');
            productTitle.textContent = product.title;

            const productPrice = document.createElement('p');
            productPrice.textContent = `$${product.price}`;

            productCard.appendChild(productImage);
            productCard.appendChild(productTitle);
            productCard.appendChild(productPrice);

            productCatalog.appendChild(productCard);
        });
    }

    function executeCommand(command) {
        const [cmd, ...args] = command.split(' ');
        switch (cmd) {
            case 'list':
                listProducts();
                break;
            case 'details':
                viewDetails(args[0]);
                break;
            case 'add':
                addToCart(args[0]);
                break;
            case 'remove':
                removeFromCart(args[0]);
                break;
            case 'cart':
                viewCart();
                break;
            case 'buy':
                buyItems();
                break;
            case 'clear':
                clearTerminal();
                break;
            case 'search':
                searchProducts(args.join(' '));
                break;
            case 'sort':
                sortProducts(args[0]);
                break;
            default:
                printToTerminal(`Unknown command: ${cmd}`);
        }
    }

    function listProducts() {
        printToTerminal('Available products:');
        products.forEach(product => {
            printToTerminal(`${product.id}: ${product.title} - $${product.price}`);
        });
    }

    function viewDetails(productId) {
        const product = products.find(p => p.id == productId);
        if (product) {
            printToTerminal(`Details of ${product.title}:`);
            printToTerminal(`Price: $${product.price}`);
            printToTerminal(`Description: ${product.description}`);
        } else {
            printToTerminal(`Product with ID ${productId} not found.`);
        }
    }

    function addToCart(productId) {
        const product = products.find(p => p.id == productId);
        if (product) {
            cart.push(product);
            printToTerminal(`${product.title} added to cart.`);
        } else {
            printToTerminal(`Product with ID ${productId} not found.`);
        }
    }

    function removeFromCart(productId) {
        const index = cart.findIndex(p => p.id == productId);
        if (index !== -1) {
            const removedProduct = cart.splice(index, 1)[0];
            printToTerminal(`${removedProduct.title} removed from cart.`);
        } else {
            printToTerminal(`Product with ID ${productId} not found in cart.`);
        }
    }

    function viewCart() {
        if (cart.length === 0) {
            printToTerminal('Your cart is empty.');
        } else {
            printToTerminal('Items in your cart:');
            cart.forEach(product => {
                printToTerminal(`${product.id}: ${product.title} - $${product.price}`);
            });
        }
    }

    function buyItems() {
        if (cart.length === 0) {
            printToTerminal('Your cart is empty.');
        } else {
            let total = 0;
            cart.forEach(product => {
                total += product.price;
            });
            printToTerminal(`Total price: $${total.toFixed(2)}`);
            printToTerminal('Proceeding to purchase...');
            // Redirect to a new page or handle purchase logic here
        }
    }

    function clearTerminal() {
        terminalOutput.innerHTML = '';
    }

    function searchProducts(query) {
        const results = products.filter(product => product.title.toLowerCase().includes(query.toLowerCase()));
        if (results.length > 0) {
            printToTerminal('Search results:');
            results.forEach(product => {
                printToTerminal(`${product.id}: ${product.title} - $${product.price}`);
            });
        } else {
            printToTerminal(`No products found for query: ${query}`);
        }
    }

    function sortProducts(criteria) {
        if (criteria === 'price') {
            products.sort((a, b) => a.price - b.price);
        } else if (criteria === 'name') {
            products.sort((a, b) => a.title.localeCompare(b.title));
        } else {
            printToTerminal(`Unknown sort criteria: ${criteria}`);
            return;
        }
        displayProducts(products);
        printToTerminal(`Products sorted by ${criteria}.`);
    }

    function printToTerminal(message) {
        const messageElement = document.createElement('div');
        messageElement.textContent = message;
        terminalOutput.appendChild(messageElement);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }

    terminalInput.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            const command = terminalInput.value.trim();
            terminalInput.value = '';
            printToTerminal(`$ ${command}`);
            executeCommand(command);
        }
    });
});
