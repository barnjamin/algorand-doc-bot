[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / MiniAssetHolding

# Class: MiniAssetHolding

[indexerModels](../modules/indexerModels.md).MiniAssetHolding

A simplified version of AssetHolding

## Hierarchy

- `default`

  ↳ **`MiniAssetHolding`**

## Table of contents

### Constructors

- [constructor](indexerModels.MiniAssetHolding.md#constructor)

### Properties

- [address](indexerModels.MiniAssetHolding.md#address)
- [amount](indexerModels.MiniAssetHolding.md#amount)
- [attribute\_map](indexerModels.MiniAssetHolding.md#attribute_map)
- [deleted](indexerModels.MiniAssetHolding.md#deleted)
- [isFrozen](indexerModels.MiniAssetHolding.md#isfrozen)
- [optedInAtRound](indexerModels.MiniAssetHolding.md#optedinatround)
- [optedOutAtRound](indexerModels.MiniAssetHolding.md#optedoutatround)

### Methods

- [get\_obj\_for\_encoding](indexerModels.MiniAssetHolding.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.MiniAssetHolding.md#from_obj_for_encoding)

## Constructors

### constructor

• **new MiniAssetHolding**(`«destructured»`)

Creates a new `MiniAssetHolding` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `address` | `string` |
| › `amount` | `number` \| `bigint` |
| › `deleted?` | `boolean` |
| › `isFrozen` | `boolean` |
| › `optedInAtRound?` | `number` \| `bigint` |
| › `optedOutAtRound?` | `number` \| `bigint` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:3252](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3252)

## Properties

### address

• **address**: `string`

#### Defined in

[client/v2/indexer/models/types.ts:3222](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3222)

___

### amount

• **amount**: `number` \| `bigint`

#### Defined in

[client/v2/indexer/models/types.ts:3224](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3224)

___

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### deleted

• `Optional` **deleted**: `boolean`

Whether or not this asset holding is currently deleted from its account.

#### Defined in

[client/v2/indexer/models/types.ts:3231](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3231)

___

### isFrozen

• **isFrozen**: `boolean`

#### Defined in

[client/v2/indexer/models/types.ts:3226](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3226)

___

### optedInAtRound

• `Optional` **optedInAtRound**: `number` \| `bigint`

Round during which the account opted into the asset.

#### Defined in

[client/v2/indexer/models/types.ts:3236](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3236)

___

### optedOutAtRound

• `Optional` **optedOutAtRound**: `number` \| `bigint`

Round during which the account opted out of the asset.

#### Defined in

[client/v2/indexer/models/types.ts:3241](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3241)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`MiniAssetHolding`](indexerModels.MiniAssetHolding.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`MiniAssetHolding`](indexerModels.MiniAssetHolding.md)

#### Defined in

[client/v2/indexer/models/types.ts:3286](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3286)
