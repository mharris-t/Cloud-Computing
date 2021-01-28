import requests
import pytest
import json

def test_get_root_check_status_code_equals_200(app, client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_get_root_check_content_type_equals_json(client):
    rv = client.get('/')
    assert rv.content_type == 'application/json'

def test_get_root_check_message_equals_css(client):
    rv = client.get('/')
    assert rv.json == {'message': 'Cloud Software and Systems'}
