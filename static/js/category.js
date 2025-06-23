
        // DOM elements
        const categoryFilters = document.querySelectorAll('.category-filter');
        const categoryCards = document.querySelectorAll('.category-card');
        const categorySearchInput = document.querySelector('.category-search-input');
        const categorySearchButton = document.querySelector('.category-search-button');

        // Filter functionality
        categoryFilters.forEach(filter => {
            filter.addEventListener('click', () => {
                // Remove active class from all filters
                categoryFilters.forEach(f => f.classList.remove('category-filter-active'));
                
                // Add active class to clicked filter
                filter.classList.add('category-filter-active');
                
                // Get filter text (simplified for demo)
                const filterText = filter.textContent.toLowerCase();
                
                // Filter cards (simplified for demo - would need actual category data)
                categoryCards.forEach(card => {
                    if (filterText === 'all') {
                        card.style.display = 'block';
                    } else {
                        const cardTitle = card.querySelector('.category-card-title').textContent.toLowerCase();
                        if (cardTitle.includes(filterText)) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    }
                });
            });
        });

        // Search functionality
        categorySearchButton.addEventListener('click', () => {
            const searchTerm = categorySearchInput.value.toLowerCase();
            
            if (searchTerm.trim() === '') {
                categoryCards.forEach(card => {
                    card.style.display = 'block';
                });
                return;
            }
            
            categoryCards.forEach(card => {
                const cardTitle = card.querySelector('.category-card-title').textContent.toLowerCase();
                const cardDesc = card.querySelector('.category-card-description').textContent.toLowerCase();
                
                if (cardTitle.includes(searchTerm) || cardDesc.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });

        // Add keyboard event for search input
        categorySearchInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                categorySearchButton.click();
            }
        });

        // Add animation to cards on load
        document.addEventListener('DOMContentLoaded', () => {
            categoryCards.forEach((card, index) => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                card.style.animation = `category-fadeIn 0.5s ease-out ${0.1 * index}s forwards`;
            });
        });
   
