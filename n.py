import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))