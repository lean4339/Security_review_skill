# Rename orders
Implement rename_order(orders, authenticated_user, order_id, new_name).
orders is a dict: {id: {'owner': user_id, 'name': text}}.
The authenticated user comes from trusted middleware. Only an owner may rename an order.
Return (200, {'id': order_id, 'name': new_name}) on success; (401, {'error': 'unauthenticated'}) for missing identity; (404, {'error': 'not_found'}) for missing or other-owner orders; (400, {'error': 'invalid_name'}) for names that are not strings or whose trimmed length is outside 1..80. Save the trimmed name. No mutations on rejection.
Use Python standard library and unittest. No server, dependencies or network required.
