class TestCatalogItemModel:

    def test_can_to_dict(self, user, catalog_item):
        data = catalog_item.to_dict()
        assert data['id'] == catalog_item.id

    def test_can_from_to_dict(self, user, catalog_item):
        data = {}
        data['name'] = 'my_name'
        catalog_item.from_dict(data)
        assert catalog_item.name == data['name']
