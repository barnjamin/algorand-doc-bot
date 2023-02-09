[algosdk](../README.md) / [Exports](../modules.md) / TransactionWithSigner

# Interface: TransactionWithSigner

Represents an unsigned transactions and a signer that can authorize that transaction.

## Table of contents

### Properties

- [signer](TransactionWithSigner.md#signer)
- [txn](TransactionWithSigner.md#txn)

## Properties

### signer

• **signer**: [`TransactionSigner`](../modules.md#transactionsigner)

A transaction signer that can authorize txn

#### Defined in

[signer.ts:88](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/signer.ts#L88)

___

### txn

• **txn**: [`Transaction`](../classes/Transaction.md)

An unsigned transaction

#### Defined in

[signer.ts:86](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/signer.ts#L86)
