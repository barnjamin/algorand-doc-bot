[algosdk](../README.md) / [Exports](../modules.md) / IntDecoding

# Enumeration: IntDecoding

Configure how integers in JSON response will be decoded.

## Table of contents

### Enumeration Members

- [BIGINT](IntDecoding.md#bigint)
- [DEFAULT](IntDecoding.md#default)
- [MIXED](IntDecoding.md#mixed)
- [SAFE](IntDecoding.md#safe)

## Enumeration Members

### BIGINT

• **BIGINT** = ``"bigint"``

All integers will be decoded as BigInts.

#### Defined in

[types/intDecoding.ts:26](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/intDecoding.ts#L26)

___

### DEFAULT

• **DEFAULT** = ``"default"``

All integers will be decoded as Numbers, meaning any values greater than
Number.MAX_SAFE_INTEGER will lose precision.

#### Defined in

[types/intDecoding.ts:9](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/intDecoding.ts#L9)

___

### MIXED

• **MIXED** = ``"mixed"``

Integers will be decoded as Numbers if they are less than or equal to
Number.MAX_SAFE_INTEGER, otherwise they will be decoded as BigInts.

#### Defined in

[types/intDecoding.ts:21](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/intDecoding.ts#L21)

___

### SAFE

• **SAFE** = ``"safe"``

All integers will be decoded as Numbers, but if any values are greater than
Number.MAX_SAFE_INTEGER an error will be thrown.

#### Defined in

[types/intDecoding.ts:15](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/intDecoding.ts#L15)
