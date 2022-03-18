from flask import abort, request
import jwt


class JWTDecorator:

    def validacion_jwt(func):
        def wrapper(*args):

            headers = dict(request.headers)
            if "Token" not in headers or headers["Token"] == "":
                abort(400,"El header token es incorrecto")
            
            try:
                token = headers['Token']
                pubkey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyGpkUJ6m2WLm4WMHtpszcd3TxjLOJJDRVnv4GA7lROcz3xCe94IjCEzofVkafgqMYwCKKtjFHJZzGvV6Pe39jacBp4a5YZRv5/3ZgqnEo5sllNTbOblLCnSiiXzYx+slKYgcPr4zGFSROQekSdEjDCRmfiuyKKroutsJCNYXJiT8RrWl/jmyyT4Fn6kSnT6QP4fvQ7jhI55T+B/c5hTeYphpwe5dX1mYJr2swjy0bSZYQwSGXUk/W7jsTpFQjM8eT7W+hQJHZKVOFTntnEC7UdRUNxGN6Q2kre7I7lOVREXj9/bH+sboJk26Vu7G1pv3QHL7C/p9/SBjO8uWX+TbjQIDAQAB"
                # token = "eyJraWQiOiJvcHRpb25hbC11bmlxdWUtaWRlbnRpZmllci1mb3ItcHJpdmF0ZWtleS1oZXJlIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJkRU5laVwvSmU4TlJOVmJPN09PVUIrelZiZXMrUEI0UkFsK21mMW0yc083c3NPbjVQaDZpVW5GU0ZyZzF2elNxRGFqa3Y1XC8ybjAyUnRHUmlXWDdDRXRuc3RCMkI0S1kwMGFIdW5tVWV6Y3NjTjJvbXFLXC9jb0FTbmhOWkdEMkI3V2c5OUxLTlwvSm13dXF6WjlLQzc2QWprV29UeWl4VkNXVCt2WStjWXFsV013NXFGbGpyZnFBa3pFRjh0cytpU3UranhBV0F3bUYrZjA1U2tUSjI0dVpmR3Z3TlE5Y3hBOCtWS3VyT3Qra3B5NlpMMnVoTE9PNDByTVdIV0RROFBhRDk3cnlPM2RVT1RJMzVhT0JiMDloU0hhRGo0N0pVeUg5MzhsUVNrMUoxbkpUZUhNQUpmNDhOK0k0YnFFVk9rOGRwNGRlRFFxUHI0NGhuRlJSVTNzU3BRPT0iLCJleHAiOjE2NDIwOTk5MTMsImlhdCI6MTY0MTkyNzExMywianRpIjoiY2FjOWI0YzItODY3Zi00OWRhLTkyM2UtYjBiODNjNzdmZGEzIn0.MaYcZLoozcUxXdMkr8mL7Aor8TqfEjIPAl2q9oS9OO3toZHIhpCFPCL88RyiHGnNgUVyWlrJCPzron5fu07kUJDTWy723OWaG3ysSdrc-vfn9yAgWZ15rMUeLXSyANQFxMtdam8DEtQruZzSpsU3f_s1fa0gz4QDm621EoCPYpDg6OCR4KBGtqDTttZfzrPmUjQGHNENPwYdfhbYTqLAdGf5prz_XVBBovv48_OVPuujooJ9rPjUHTg3QjpSP0h5q9GzeEpo9t53CuxNjXvNiNJXb0ZHKAc_cs9SWuEPc8L4mNa2CegokZaKrbqsD_LaYekI6mM3kbNcMGbFMwANNg"
                token = token.encode()
                publicKey = "-----BEGIN PUBLIC KEY-----\n" + pubkey + "\n-----END PUBLIC KEY-----"
                result = jwt.decode(jwt=token, key=publicKey,
                                    algorithms=['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512', 'ES256',
                                                'ES384',
                                                'ES512', 'PS256', 'PS384', 'PS512'])
                if 'sub' in result:
                    response = func(*args)
                else:
                    abort(400, "Token inválido")
            except jwt.ExpiredSignatureError:
                abort(400, "Token inválido")
            except jwt.DecodeError:
                abort(400, "Token inválido")
            except jwt.InvalidTokenError:
                abort(400, "Token inválido")

            return response

        return wrapper