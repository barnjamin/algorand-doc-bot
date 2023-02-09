[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / AssetResponse

# Class: AssetResponse

[indexerModels](../modules/indexerModels.md).AssetResponse

## Hierarchy

- `default`

  ↳ **`AssetResponse`**

## Table of contents

### Constructors

- [constructor](indexerModels.AssetResponse.md#constructor)

### Properties

- [asset](indexerModels.AssetResponse.md#asset)
- [attribute\_map](indexerModels.AssetResponse.md#attribute_map)
- [currentRound](indexerModels.AssetResponse.md#currentround)

### Methods

- [get\_obj\_for\_encoding](indexerModels.AssetResponse.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.AssetResponse.md#from_obj_for_encoding)

## Constructors

### constructor

• **new AssetResponse**(`«destructured»`)

Creates a new `AssetResponse` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `asset` | [`Asset`](indexerModels.Asset.md) |
| › `currentRound` | `number` \| `bigint` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:2000](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2000)

## Properties

### asset

• **asset**: [`Asset`](indexerModels.Asset.md)

Specifies both the unique identifier and the parameters for an asset

#### Defined in

[client/v2/indexer/models/types.ts:1988](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L1988)

___

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### currentRound

• **currentRound**: `number` \| `bigint`

Round at which the results were computed.

#### Defined in

[client/v2/indexer/models/types.ts:1993](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L1993)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`AssetResponse`](indexerModels.AssetResponse.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`AssetResponse`](indexerModels.AssetResponse.md)

#### Defined in

[client/v2/indexer/models/types.ts:2018](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2018)
