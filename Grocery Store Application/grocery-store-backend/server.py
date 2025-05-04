from flask import Flask, jsonify, request
from flask_cors import CORS
from marshmallow import Schema, fields, validate, ValidationError
import logging

from sql_connection import managed_connection
import products_dao
import orders_dao
import uom_dao

# Setup
app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

# ======================
# Schemas for Validation
# ======================

class ProductSchema(Schema):
    name = fields.Str(required=True)
    uom_id = fields.Int(required=True)
    price_per_unit = fields.Float(required=True, validate=validate.Range(min=0))

class OrderSchema(Schema):
    customer_name = fields.Str(required=True)
    total = fields.Float(required=True, validate=validate.Range(min=0))
    datetime = fields.Str(required=True)

class UOMSchema(Schema):
    uom_name = fields.Str(required=True)

# ===================
# Helper Functions
# ===================

VALID_PRODUCT_SORT_FIELDS = ['name', 'price_per_unit', 'uom_name']
VALID_ORDER_SORT_FIELDS = ['datetime', 'total', 'customer_name']
VALID_SORT_ORDERS = ['ASC', 'DESC']

def create_response(status, message=None, data=None):
    return jsonify({
        'status': status,
        'message': message or '',
        'data': data or {}
    })

def validate_sort_params(sort_by, sort_order, valid_fields):
    if sort_by not in valid_fields:
        raise ValueError(f"Invalid sort field '{sort_by}'. Valid options: {valid_fields}")
    if sort_order not in VALID_SORT_ORDERS:
        raise ValueError(f"Invalid sort order '{sort_order}'. Use 'ASC' or 'DESC'.")

# ============
# Product APIs
# ============

@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))
        sort_by = request.args.get('sort_by', 'name')
        sort_order = request.args.get('sort_order', 'ASC')
        validate_sort_params(sort_by, sort_order, VALID_PRODUCT_SORT_FIELDS)

        filters = {}
        for key in ['name', 'uom_id']:
            if key in request.args:
                filters[key] = request.args[key]

        products = products_dao.get_all_products(limit, offset, sort_by, sort_order, filters)
        return create_response('success', data=products)
    except Exception as e:
        logging.error(f"[getProducts] {str(e)}")
        return create_response('error', message=str(e)), 400

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        data = ProductSchema().load(request.get_json())
        product_id = products_dao.insert_new_product(data)
        return create_response('success', data={'product_id': product_id})
    except ValidationError as err:
        return create_response('error', message=err.messages), 400
    except Exception as e:
        logging.error(f"[insertProduct] {str(e)}")
        return create_response('error', message=str(e)), 500

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        product_id = request.get_json().get('product_id')
        if not product_id:
            return create_response('error', message="Missing product_id"), 400
        deleted_id = products_dao.delete_product(product_id)
        return create_response('success', data={'product_id': deleted_id})
    except Exception as e:
        logging.error(f"[deleteProduct] {str(e)}")
        return create_response('error', message=str(e)), 500

# ============
# Order APIs
# ============

@app.route('/getOrders', methods=['GET'])
def get_orders():
    try:
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))
        sort_by = request.args.get('sort_by', 'datetime')
        sort_order = request.args.get('sort_order', 'ASC')
        validate_sort_params(sort_by, sort_order, VALID_ORDER_SORT_FIELDS)

        filters = {}
        for key in ['customer_name']:
            if key in request.args:
                filters[key] = request.args[key]

        orders = orders_dao.get_all_orders(limit, offset, sort_by, sort_order, filters)
        return create_response('success', data=orders)
    except Exception as e:
        logging.error(f"[getOrders] {str(e)}")
        return create_response('error', message=str(e)), 400

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:
        data = OrderSchema().load(request.get_json())
        order_id = orders_dao.insert_new_order(data)
        return create_response('success', data={'order_id': order_id})
    except ValidationError as err:
        return create_response('error', message=err.messages), 400
    except Exception as e:
        logging.error(f"[insertOrder] {str(e)}")
        return create_response('error', message=str(e)), 500

@app.route('/deleteOrder', methods=['POST'])
def delete_order():
    try:
        order_id = request.get_json().get('order_id')
        if not order_id:
            return create_response('error', message="Missing order_id"), 400
        deleted_id = orders_dao.delete_order(order_id)
        return create_response('success', data={'order_id': deleted_id})
    except Exception as e:
        logging.error(f"[deleteOrder] {str(e)}")
        return create_response('error', message=str(e)), 500

# ===========
# UOM APIs
# ===========

@app.route('/getUOMs', methods=['GET'])
def get_uoms():
    try:
        uoms = uom_dao.get_all_uoms()
        return create_response('success', data=uoms)
    except Exception as e:
        logging.error(f"[getUOMs] {str(e)}")
        return create_response('error', message=str(e)), 500

@app.route('/insertUOM', methods=['POST'])
def insert_uom():
    try:
        data = UOMSchema().load(request.get_json())
        uom_id = uom_dao.insert_uom(data)
        return create_response('success', data={'uom_id': uom_id})
    except ValidationError as err:
        return create_response('error', message=err.messages), 400
    except Exception as e:
        logging.error(f"[insertUOM] {str(e)}")
        return create_response('error', message=str(e)), 500

@app.route('/deleteUOM', methods=['POST'])
def delete_uom():
    try:
        uom_id = request.get_json().get('uom_id')
        if not uom_id:
            return create_response('error', message="Missing uom_id"), 400
        deleted_id = uom_dao.delete_uom(uom_id)
        return create_response('success', data={'uom_id': deleted_id})
    except Exception as e:
        logging.error(f"[deleteUOM] {str(e)}")
        return create_response('error', message=str(e)), 500

# ==========
# Run Server
# ==========

if __name__ == '__main__':
    app.run(debug=True)
