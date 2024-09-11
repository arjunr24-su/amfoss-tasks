document.addEventListener('DOMContentLoaded', () => {
    const productCatalog = document.getElementById('product-catalog');

    // Fetch products from the Fake Store API
    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(products => {
            products.forEach(product => {
                // Create product card
                const productCard = document.createElement('div');
                productCard.className = 'product-card';

                // Product image
                const productImage = document.createElement('img');
                productImage.src = product.image;
                productImage.alt = product.title;

                // Product title
                const productTitle = document.createElement('h2');
                productTitle.textContent = product.title;

                // Product price
                const productPrice = document.createElement('p');
                productPrice.textContent = `$${product.price}`;

                // Append elements to product card
                productCard.appendChild(productImage);
                productCard.appendChild(productTitle);
                productCard.appendChild(productPrice);

                // Append product card to catalog
                productCatalog.appendChild(productCard);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
});
