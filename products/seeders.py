from .models import db, Product, Category


def create_categories_seeder():
    categories = [
        Category(
            name='Laptop'
        ),
        Category(
            name='Phones'
        ),
        Category(
            name='Tablets'
        ),
    ]
    db.session.add_all(categories)
    db.session.commit()
    print('categories seeder successfuly created')


def create_products_seeder():
    products = [
        Product(
            name='Macbook Pro',
            slug='macbook-pro',
            details='15 inch, 1TB SSD, 32GB RAM',
            price=249999,
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has '
                        'been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took '
                        'a galley of type and scrambled it to make a type specimen book. It has survived not only '
                        'five centuries, but also the leap into electronic typesetting, remaining essentially '
                        'unchanged. It was popularised in the 1960s with the release of Letraset sheets containing '
                        'Lorem Ipsum passages, and more recently with desktop publishing software like Aldus '
                        'PageMaker including versions of Lorem Ipsum.',
            category_id=1

        ),
        Product(
            name='Laptop 2',
            slug='laptop-2',
            details='15 inch, 1TB SSD, 16GB RAM',
            price=249999,
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has '
                        'been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took '
                        'a galley of type and scrambled it to make a type specimen book. It has survived not only '
                        'five centuries, but also the leap into electronic typesetting, remaining essentially '
                        'unchanged. It was popularised in the 1960s with the release of Letraset sheets containing '
                        'Lorem Ipsum passages, and more recently with desktop publishing software like Aldus '
                        'PageMaker including versions of Lorem Ipsum.',
            category_id=1

        ),
        Product(
            name='Laptop 3',
            slug='laptop-3',
            details='15 inch, 1TB SSD, 16GB RAM',
            price=149999,
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has '
                        'been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took '
                        'a galley of type and scrambled it to make a type specimen book. It has survived not only '
                        'five centuries, but also the leap into electronic typesetting, remaining essentially '
                        'unchanged. It was popularised in the 1960s with the release of Letraset sheets containing '
                        'Lorem Ipsum passages, and more recently with desktop publishing software like Aldus '
                        'PageMaker including versions of Lorem Ipsum.',
            category_id=1

        ),
        Product(
            name='Laptop 4',
            slug='laptop-4',
            details='15 inch, 1TB SSD, 16GB RAM',
            price=149999,
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has '
                        'been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took '
                        'a galley of type and scrambled it to make a type specimen book. It has survived not only '
                        'five centuries, but also the leap into electronic typesetting, remaining essentially '
                        'unchanged. It was popularised in the 1960s with the release of Letraset sheets containing '
                        'Lorem Ipsum passages, and more recently with desktop publishing software like Aldus '
                        'PageMaker including versions of Lorem Ipsum.',
            category_id=1

        ),
        Product(
            name='Laptop 5',
            slug='laptop-5',
            details='15 inch, 1TB SSD, 16GB RAM',
            price=149999,
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has '
                        'been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took '
                        'a galley of type and scrambled it to make a type specimen book. It has survived not only '
                        'five centuries, but also the leap into electronic typesetting, remaining essentially '
                        'unchanged. It was popularised in the 1960s with the release of Letraset sheets containing '
                        'Lorem Ipsum passages, and more recently with desktop publishing software like Aldus '
                        'PageMaker including versions of Lorem Ipsum.',
            category_id=1

        ),
    ]
    db.session.add_all(products)
    db.session.commit()
    print('products seeder successfully created')
