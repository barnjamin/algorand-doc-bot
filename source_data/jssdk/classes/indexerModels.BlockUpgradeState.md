[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / BlockUpgradeState

# Class: BlockUpgradeState

[indexerModels](../modules/indexerModels.md).BlockUpgradeState

Fields relating to a protocol upgrade.

## Hierarchy

- `default`

  ↳ **`BlockUpgradeState`**

## Table of contents

### Constructors

- [constructor](indexerModels.BlockUpgradeState.md#constructor)

### Properties

- [attribute\_map](indexerModels.BlockUpgradeState.md#attribute_map)
- [currentProtocol](indexerModels.BlockUpgradeState.md#currentprotocol)
- [nextProtocol](indexerModels.BlockUpgradeState.md#nextprotocol)
- [nextProtocolApprovals](indexerModels.BlockUpgradeState.md#nextprotocolapprovals)
- [nextProtocolSwitchOn](indexerModels.BlockUpgradeState.md#nextprotocolswitchon)
- [nextProtocolVoteBefore](indexerModels.BlockUpgradeState.md#nextprotocolvotebefore)

### Methods

- [get\_obj\_for\_encoding](indexerModels.BlockUpgradeState.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.BlockUpgradeState.md#from_obj_for_encoding)

## Constructors

### constructor

• **new BlockUpgradeState**(`«destructured»`)

Creates a new `BlockUpgradeState` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `currentProtocol` | `string` |
| › `nextProtocol?` | `string` |
| › `nextProtocolApprovals?` | `number` \| `bigint` |
| › `nextProtocolSwitchOn?` | `number` \| `bigint` |
| › `nextProtocolVoteBefore?` | `number` \| `bigint` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:2542](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2542)

## Properties

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### currentProtocol

• **currentProtocol**: `string`

(proto) The current protocol version.

#### Defined in

[client/v2/indexer/models/types.ts:2510](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2510)

___

### nextProtocol

• `Optional` **nextProtocol**: `string`

(nextproto) The next proposed protocol version.

#### Defined in

[client/v2/indexer/models/types.ts:2515](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2515)

___

### nextProtocolApprovals

• `Optional` **nextProtocolApprovals**: `number` \| `bigint`

(nextyes) Number of blocks which approved the protocol upgrade.

#### Defined in

[client/v2/indexer/models/types.ts:2520](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2520)

___

### nextProtocolSwitchOn

• `Optional` **nextProtocolSwitchOn**: `number` \| `bigint`

(nextswitch) Round on which the protocol upgrade will take effect.

#### Defined in

[client/v2/indexer/models/types.ts:2525](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2525)

___

### nextProtocolVoteBefore

• `Optional` **nextProtocolVoteBefore**: `number` \| `bigint`

(nextbefore) Deadline round for this protocol upgrade (No votes will be consider
after this round).

#### Defined in

[client/v2/indexer/models/types.ts:2531](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2531)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`BlockUpgradeState`](indexerModels.BlockUpgradeState.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`BlockUpgradeState`](indexerModels.BlockUpgradeState.md)

#### Defined in

[client/v2/indexer/models/types.ts:2572](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2572)
