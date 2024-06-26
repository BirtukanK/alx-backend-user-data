#!/usr/bin/env python3
""" Basic authentication"""


from api.v1.auth.auth import Auth
import binascii
import base64


class BasicAuth(Auth):
    """ Basic authentcation class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ header extraction"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[-1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decodes header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            res = base64.b64decode(base64_authorization_header,
                                   validate=True,
                                   )
            return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None
