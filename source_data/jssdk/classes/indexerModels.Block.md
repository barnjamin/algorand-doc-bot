[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / Block

# Class: Block

[indexerModels](../modules/indexerModels.md).Block

Block information.
Definition:
data/bookkeeping/block.go : Block

## Hierarchy

- `default`

  ↳ **`Block`**

## Table of contents

### Constructors

- [constructor](indexerModels.Block.md#constructor)

### Properties

- [attribute\_map](indexerModels.Block.md#attribute_map)
- [genesisHash](indexerModels.Block.md#genesishash)
- [genesisId](indexerModels.Block.md#genesisid)
- [participationUpdates](indexerModels.Block.md#participationupdates)
- [previousBlockHash](indexerModels.Block.md#previousblockhash)
- [rewards](indexerModels.Block.md#rewards)
- [round](indexerModels.Block.md#round)
- [seed](indexerModels.Block.md#seed)
- [stateProofTracking](indexerModels.Block.md#stateprooftracking)
- [timestamp](indexerModels.Block.md#timestamp)
- [transactions](indexerModels.Block.md#transactions)
- [transactionsRoot](indexerModels.Block.md#transactionsroot)
- [transactionsRootSha256](indexerModels.Block.md#transactionsrootsha256)
- [txnCounter](indexerModels.Block.md#txncounter)
- [upgradeState](indexerModels.Block.md#upgradestate)
- [upgradeVote](indexerModels.Block.md#upgradevote)

### Methods

- [get\_obj\_for\_encoding](indexerModels.Block.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.Block.md#from_obj_for_encoding)

## Constructors

### constructor

• **new Block**(`«destructured»`)

Creates a new `Block` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `genesisHash` | `string` \| `Uint8Array` |
| › `genesisId` | `string` |
| › `participationUpdates?` | [`ParticipationUpdates`](indexerModels.ParticipationUpdates.md) |
| › `previousBlockHash` | `string` \| `Uint8Array` |
| › `rewards?` | [`BlockRewards`](indexerModels.BlockRewards.md) |
| › `round` | `number` \| `bigint` |
| › `seed` | `string` \| `Uint8Array` |
| › `stateProofTracking?` | [`StateProofTracking`](indexerModels.StateProofTracking.md)[] |
| › `timestamp` | `number` \| `bigint` |
| › `transactions?` | [`Transaction`](indexerModels.Transaction.md)[] |
| › `transactionsRoot` | `string` \| `Uint8Array` |
| › `transactionsRootSha256` | `string` \| `Uint8Array` |
| › `txnCounter?` | `number` \| `bigint` |
| › `upgradeState?` | [`BlockUpgradeState`](indexerModels.BlockUpgradeState.md) |
| › `upgradeVote?` | [`BlockUpgradeVote`](indexerModels.BlockUpgradeVote.md) |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:2222](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2222)

## Properties

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### genesisHash

• **genesisHash**: `Uint8Array`

(gh) hash to which this block belongs.

#### Defined in

[client/v2/indexer/models/types.ts:2108](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2108)

___

### genesisId

• **genesisId**: `string`

(gen) ID to which this block belongs.

#### Defined in

[client/v2/indexer/models/types.ts:2113](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2113)

___

### participationUpdates

• `Optional` **participationUpdates**: [`ParticipationUpdates`](indexerModels.ParticipationUpdates.md)

Participation account data that needs to be checked/acted on by the network.

#### Defined in

[client/v2/indexer/models/types.ts:2156](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2156)

___

### previousBlockHash

• **previousBlockHash**: `Uint8Array`

(prev) Previous block hash.

#### Defined in

[client/v2/indexer/models/types.ts:2118](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2118)

___

### rewards

• `Optional` **rewards**: [`BlockRewards`](indexerModels.BlockRewards.md)

Fields relating to rewards,

#### Defined in

[client/v2/indexer/models/types.ts:2161](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2161)

___

### round

• **round**: `number` \| `bigint`

(rnd) Current round on which this block was appended to the chain.

#### Defined in

[client/v2/indexer/models/types.ts:2123](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2123)

___

### seed

• **seed**: `Uint8Array`

(seed) Sortition seed.

#### Defined in

[client/v2/indexer/models/types.ts:2128](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2128)

___

### stateProofTracking

• `Optional` **stateProofTracking**: [`StateProofTracking`](indexerModels.StateProofTracking.md)[]

Tracks the status of state proofs.

#### Defined in

[client/v2/indexer/models/types.ts:2166](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2166)

___

### timestamp

• **timestamp**: `number` \| `bigint`

(ts) Block creation timestamp in seconds since eposh

#### Defined in

[client/v2/indexer/models/types.ts:2133](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2133)

___

### transactions

• `Optional` **transactions**: [`Transaction`](indexerModels.Transaction.md)[]

(txns) list of transactions corresponding to a given round.

#### Defined in

[client/v2/indexer/models/types.ts:2171](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2171)

___

### transactionsRoot

• **transactionsRoot**: `Uint8Array`

(txn) TransactionsRoot authenticates the set of transactions appearing in the
block. More specifically, it's the root of a merkle tree whose leaves are the
block's Txids, in lexicographic order. For the empty block, it's 0. Note that
the TxnRoot does not authenticate the signatures on the transactions, only the
transactions themselves. Two blocks with the same transactions but in a
different order and with different signatures will have the same TxnRoot.

#### Defined in

[client/v2/indexer/models/types.ts:2143](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2143)

___

### transactionsRootSha256

• **transactionsRootSha256**: `Uint8Array`

(txn256) TransactionsRootSHA256 is an auxiliary TransactionRoot, built using a
vector commitment instead of a merkle tree, and SHA256 hash function instead of
the default SHA512_256. This commitment can be used on environments where only
the SHA256 function exists.

#### Defined in

[client/v2/indexer/models/types.ts:2151](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2151)

___

### txnCounter

• `Optional` **txnCounter**: `number` \| `bigint`

(tc) TxnCounter counts the number of transactions committed in the ledger, from
the time at which support for this feature was introduced.
Specifically, TxnCounter is the number of the next transaction that will be
committed after this block. It is 0 when no transactions have ever been
committed (since TxnCounter started being supported).

#### Defined in

[client/v2/indexer/models/types.ts:2180](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2180)

___

### upgradeState

• `Optional` **upgradeState**: [`BlockUpgradeState`](indexerModels.BlockUpgradeState.md)

Fields relating to a protocol upgrade.

#### Defined in

[client/v2/indexer/models/types.ts:2185](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2185)

___

### upgradeVote

• `Optional` **upgradeVote**: [`BlockUpgradeVote`](indexerModels.BlockUpgradeVote.md)

Fields relating to voting for a protocol upgrade.

#### Defined in

[client/v2/indexer/models/types.ts:2190](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2190)

## Methods

### get\_obj\_for\_encoding

▸ **get_obj_for_encoding**(`binary?`): `Record`<`string`, `any`\>

Get an object ready for encoding to either JSON or msgpack.

#### Parameters

| Name | Type | Default value | Description |
| :------ | :------ | :------ | :------ |
| `binary` | `boolean` | `false` | Use true to indicate that the encoding can handle raw binary objects (Uint8Arrays). Use false to indicate that raw binary objects should be converted to base64 strings. True should be used for objects that will be encoded with msgpack, and false should be used for objects that will be encoded with JSON. |

#### Returns

`Record`<`string`, `any`\>

#### Inherited from

BaseModel.get\_obj\_for\_encoding

#### Defined in

[client/v2/basemodel.ts:65](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L65)

___

### from\_obj\_for\_encoding

▸ `Static` **from_obj_for_encoding**(`data`): [`Block`](indexerModels.Block.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`Block`](indexerModels.Block.md)

#### Defined in

[client/v2/indexer/models/types.ts:2307](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2307)
