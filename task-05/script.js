const terminalOutput = document.querySelector('.terminal-output');
const terminalInput = document.querySelector('input[type="text"]');

terminalInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        const command = terminalInput.value.trim();
        handleInput(command);
    }
});

function handleInput(command) {
    const parts = command.split(' ');
    const action = parts[0];
    const params = parts.slice(1);

    if (action === 'help') {
        viewCommand();
    } else if (action === 'list') {
        listProducts();
    } else if (action === 'details') {
        viewDetails(params[0]);
    } else if (action === 'add') {
        addToCart(params[0]);
    } else if (action === 'remove') {
        removeFromCart(params[0]);
    } else if (action === 'cart') {
        viewCart();
    } else if (action === 'buy') {
        proceedToBuy();
    } else if (action === 'clear') {
        clearTerminal();
    } else if (action === 'search') {
        searchProduct(params.join(' '));
    } else if (action === 'sort') {
        sortProducts(params[0]);
    } else {
        terminalOutput.textContent += `Invalid command: ${command}\n`;
    }

    terminalInput.value = '';
}

function viewCommand() {
    terminalOutput.innerHTML += "Available Commands:\n";
    terminalOutput.innerHTML += "list, details 'product_id', add 'product_id', remove 'product_id', cart, buy, clear, search 'product_name', sort 'price/name'\n";
}

function listProducts() {
    // Fetch and display products from the API
}

function viewDetails(productId) {
    // Fetch and display product details from the API
}

function addToCart(productId) {
    // Add product to the cart
}

function removeFromCart(productId) {
    // Remove product from the cart
}

function viewCart() {
    // Display current items in the cart
}

function proceedToBuy() {
    // Proceed to the checkout page
}

function clearTerminal() {
    terminalOutput.innerHTML = '';
}

function searchProduct(productName) {
    // Search for a product by name
}

function sortProducts(criteria) {
    // Sort products by price or name
}
