from northpole import CartesianPoint


def test___eq__() -> None:
    p1: CartesianPoint = CartesianPoint(1, 2)
    p2: CartesianPoint = CartesianPoint(1, 2)

    assert p1 == p2


def test___hash__() -> None:
    data: list[CartesianPoint] = [
        CartesianPoint(1, 2),
        CartesianPoint(4, 6),
        CartesianPoint(1, 2),
    ]

    assert len(set(data)) == 2


def test_down() -> None:
    point: CartesianPoint = CartesianPoint(8, 3)
    expected: CartesianPoint = CartesianPoint(8, 2)

    assert point.down() == expected


def test_left() -> None:
    point: CartesianPoint = CartesianPoint(7, 1)
    expected: CartesianPoint = CartesianPoint(6, 1)

    assert point.left() == expected


def test_right() -> None:
    point: CartesianPoint = CartesianPoint(6, 7)
    expected: CartesianPoint = CartesianPoint(7, 7)

    assert point.right() == expected


def test_up() -> None:
    point: CartesianPoint = CartesianPoint(1, 6)
    expected: CartesianPoint = CartesianPoint(1, 7)

    assert point.up() == expected
