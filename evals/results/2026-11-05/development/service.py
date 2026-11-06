def rename_order(orders, authenticated_user, order_id, new_name):
    """Return (status, payload). authenticated_user is supplied by trusted auth middleware."""
    # An identity of 0 can be valid; do not use a general truthiness check.
    if authenticated_user is None or authenticated_user == "":
        return 401, {"error": "unauthenticated"}

    order = orders.get(order_id)
    if order is None or order["owner"] != authenticated_user:
        return 404, {"error": "not_found"}

    if not isinstance(new_name, str):
        return 400, {"error": "invalid_name"}
    name = new_name.strip()
    if not 1 <= len(name) <= 80:
        return 400, {"error": "invalid_name"}

    # Mutate only after all authorization and validation checks have passed.
    order["name"] = name
    return 200, {"id": order_id, "name": name}
