[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / EvalDelta

# Class: EvalDelta

[indexerModels](../modules/indexerModels.md).EvalDelta

Represents a TEAL value delta.

## Hierarchy

- `default`

  ↳ **`EvalDelta`**

## Table of contents

### Constructors

- [constructor](indexerModels.EvalDelta.md#constructor)

### Properties

- [action](indexerModels.EvalDelta.md#action)
- [attribute\_map](indexerModels.EvalDelta.md#attribute_map)
- [bytes](indexerModels.EvalDelta.md#bytes)
- [uint](indexerModels.EvalDelta.md#uint)

### Methods

- [get\_obj\_for\_encoding](indexerModels.EvalDelta.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.EvalDelta.md#from_obj_for_encoding)

## Constructors

### constructor

• **new EvalDelta**(`«destructured»`)

Creates a new `EvalDelta` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `action` | `number` \| `bigint` |
| › `bytes?` | `string` |
| › `uint?` | `number` \| `bigint` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:2874](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2874)

## Properties

### action

• **action**: `number` \| `bigint`

(at) delta action.

#### Defined in

[client/v2/indexer/models/types.ts:2856](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2856)

___

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### bytes

• `Optional` **bytes**: `string`

(bs) bytes value.

#### Defined in

[client/v2/indexer/models/types.ts:2861](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2861)

___

### uint

• `Optional` **uint**: `number` \| `bigint`

(ui) uint value.

#### Defined in

[client/v2/indexer/models/types.ts:2866](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2866)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`EvalDelta`](indexerModels.EvalDelta.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`EvalDelta`](indexerModels.EvalDelta.md)

#### Defined in

[client/v2/indexer/models/types.ts:2896](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2896)
