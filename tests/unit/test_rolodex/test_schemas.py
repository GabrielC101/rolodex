from rolodex.schemas import SchemaOne, SchemaTwo, SchemaThree  # isort:skip


def test_schema_one():
    assert SchemaOne.fields
    assert SchemaOne.descriptions
    assert SchemaOne.validators

    schema = SchemaOne()
    assert schema.is_valid(['Green', 'Harry', '3338675309', 'green', '90210'])
    assert not schema.is_valid(['Green', 'Harry', 'green', '3338675309', '90210'])

    assert schema.length == 5
    assert schema.expected_location('zipcode') == 4
    assert schema.descriptions == ['lastname', 'firstname', 'phonenumber', 'color', 'zipcode']
    assert len(schema.validators) == 5


def test_schema_two():
    assert SchemaTwo.fields
    assert SchemaTwo.descriptions
    assert SchemaTwo.validators

    schema = SchemaTwo()
    assert schema.is_valid(['Harry', 'Green', 'green', '90210', '3338675309'])
    assert not schema.is_valid(['Green', 'Harry', 'green', '3338675309', '90210'])

    assert schema.length == 5
    assert schema.expected_location('phonenumber') == 4
    assert schema.descriptions == ['firstname', 'lastname', 'color', 'zipcode', 'phonenumber']
    assert len(schema.validators) == 5


def test_schema_three():
    assert SchemaThree.fields
    assert SchemaThree.descriptions
    assert SchemaThree.validators

    schema = SchemaThree()
    assert schema.is_valid(['Harry', 'Green', '90210', '3338675309', 'green'])
    assert not schema.is_valid(['Green', 'Harry', 'green', '3338675309', '90210'])

    assert schema.length == 5
    assert schema.expected_location('color') == 4
    assert schema.descriptions == ['firstname', 'lastname', 'zipcode', 'phonenumber', 'color']
    assert len(schema.validators) == 5
