[algosdk](../README.md) / [Exports](../modules.md) / SignedTransaction

# Interface: SignedTransaction

Object representing a transaction with a signature

## Table of contents

### Properties

- [lsig](SignedTransaction.md#lsig)
- [msig](SignedTransaction.md#msig)
- [sgnr](SignedTransaction.md#sgnr)
- [sig](SignedTransaction.md#sig)
- [txn](SignedTransaction.md#txn)

## Properties

### lsig

• `Optional` **lsig**: [`EncodedLogicSig`](EncodedLogicSig.md)

Logic signature

#### Defined in

[transaction.ts:1326](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/transaction.ts#L1326)

___

### msig

• `Optional` **msig**: [`EncodedMultisig`](EncodedMultisig.md)

Multisig structure

#### Defined in

[transaction.ts:1321](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/transaction.ts#L1321)

___

### sgnr

• `Optional` **sgnr**: `Buffer`

The signer, if signing with a different key than the Transaction type `from` property indicates

#### Defined in

[transaction.ts:1331](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/transaction.ts#L1331)

___

### sig

• `Optional` **sig**: `Buffer`

Transaction signature

#### Defined in

[transaction.ts:1311](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/transaction.ts#L1311)

___

### txn

• **txn**: [`Transaction`](../classes/Transaction.md)

The transaction that was signed

#### Defined in

[transaction.ts:1316](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/transaction.ts#L1316)
