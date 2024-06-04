#!/usr/bin/env python3
""" auth file
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ authentication required"""
        if path is None:
            return True
        if len(excluded_paths) == 0 or excluded_paths is None:
            return True
        normalized_path = path.rstrip('/')
        normalized_excluded_paths = [excluded_path.rstrip('/')
                                     for excluded_path in excluded_paths]
        if normalized_path in normalized_excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method"""
        return None
