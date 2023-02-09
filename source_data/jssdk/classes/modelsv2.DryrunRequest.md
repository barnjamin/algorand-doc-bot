[algosdk](../README.md) / [Exports](../modules.md) / [modelsv2](../modules/modelsv2.md) / DryrunRequest

# Class: DryrunRequest

[modelsv2](../modules/modelsv2.md).DryrunRequest

Request data type for dryrun endpoint. Given the Transactions and simulated
ledger state upload, run TEAL scripts and return debugging information.

## Hierarchy

- `default`

  ↳ **`DryrunRequest`**

## Table of contents

### Constructors

- [constructor](modelsv2.DryrunRequest.md#constructor)

### Properties

- [accounts](modelsv2.DryrunRequest.md#accounts)
- [apps](modelsv2.DryrunRequest.md#apps)
- [attribute\_map](modelsv2.DryrunRequest.md#attribute_map)
- [latestTimestamp](modelsv2.DryrunRequest.md#latesttimestamp)
- [protocolVersion](modelsv2.DryrunRequest.md#protocolversion)
- [round](modelsv2.DryrunRequest.md#round)
- [sources](modelsv2.DryrunRequest.md#sources)
- [txns](modelsv2.DryrunRequest.md#txns)

### Methods

- [get\_obj\_for\_encoding](modelsv2.DryrunRequest.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](modelsv2.DryrunRequest.md#from_obj_for_encoding)

## Constructors

### constructor

• **new DryrunRequest**(`«destructured»`)

Creates a new `DryrunRequest` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `accounts` | [`Account`](modelsv2.Account.md)[] |
| › `apps` | [`Application`](modelsv2.Application.md)[] |
| › `latestTimestamp` | `number` \| `bigint` |
| › `protocolVersion` | `string` |
| › `round` | `number` \| `bigint` |
| › `sources` | [`DryrunSource`](modelsv2.DryrunSource.md)[] |
| › `txns` | [`EncodedSignedTransaction`](../interfaces/EncodedSignedTransaction.md)[] |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/algod/models/types.ts:1840](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1840)

## Properties

### accounts

• **accounts**: [`Account`](modelsv2.Account.md)[]

#### Defined in

[client/v2/algod/models/types.ts:1801](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1801)

___

### apps

• **apps**: [`Application`](modelsv2.Application.md)[]

#### Defined in

[client/v2/algod/models/types.ts:1803](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1803)

___

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### latestTimestamp

• **latestTimestamp**: `number` \| `bigint`

LatestTimestamp is available to some TEAL scripts. Defaults to the latest
confirmed timestamp this algod is attached to.

#### Defined in

[client/v2/algod/models/types.ts:1809](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1809)

___

### protocolVersion

• **protocolVersion**: `string`

ProtocolVersion specifies a specific version string to operate under, otherwise
whatever the current protocol of the network this algod is running in.

#### Defined in

[client/v2/algod/models/types.ts:1815](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1815)

___

### round

• **round**: `number` \| `bigint`

Round is available to some TEAL scripts. Defaults to the current round on the
network this algod is attached to.

#### Defined in

[client/v2/algod/models/types.ts:1821](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1821)

___

### sources

• **sources**: [`DryrunSource`](modelsv2.DryrunSource.md)[]

#### Defined in

[client/v2/algod/models/types.ts:1823](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1823)

___

### txns

• **txns**: [`EncodedSignedTransaction`](../interfaces/EncodedSignedTransaction.md)[]

#### Defined in

[client/v2/algod/models/types.ts:1825](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1825)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`DryrunRequest`](modelsv2.DryrunRequest.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`DryrunRequest`](modelsv2.DryrunRequest.md)

#### Defined in

[client/v2/algod/models/types.ts:1878](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1878)
