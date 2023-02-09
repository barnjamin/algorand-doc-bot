[algosdk](../README.md) / [Exports](../modules.md) / EncodedSignedTransaction

# Interface: EncodedSignedTransaction

A structure for an encoded signed transaction object

## Table of contents

### Properties

- [lsig](EncodedSignedTransaction.md#lsig)
- [msig](EncodedSignedTransaction.md#msig)
- [sgnr](EncodedSignedTransaction.md#sgnr)
- [sig](EncodedSignedTransaction.md#sig)
- [txn](EncodedSignedTransaction.md#txn)

## Properties

### lsig

• `Optional` **lsig**: [`EncodedLogicSig`](EncodedLogicSig.md)

Logic signature

#### Defined in

[types/transactions/encoded.ts:402](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/encoded.ts#L402)

___

### msig

• `Optional` **msig**: [`EncodedMultisig`](EncodedMultisig.md)

Multisig structure

#### Defined in

[types/transactions/encoded.ts:397](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/encoded.ts#L397)

___

### sgnr

• `Optional` **sgnr**: `Buffer`

The signer, if signing with a different key than the Transaction type `from` property indicates

#### Defined in

[types/transactions/encoded.ts:407](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/encoded.ts#L407)

___

### sig

• `Optional` **sig**: `Buffer`

Transaction signature

#### Defined in

[types/transactions/encoded.ts:387](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/encoded.ts#L387)

___

### txn

• **txn**: [`EncodedTransaction`](EncodedTransaction.md)

The transaction that was signed

#### Defined in

[types/transactions/encoded.ts:392](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/encoded.ts#L392)
