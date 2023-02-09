[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / Box

# Class: Box

[indexerModels](../modules/indexerModels.md).Box

Box name and its content.

## Hierarchy

- `default`

  ↳ **`Box`**

## Table of contents

### Constructors

- [constructor](indexerModels.Box.md#constructor)

### Properties

- [attribute\_map](indexerModels.Box.md#attribute_map)
- [name](indexerModels.Box.md#name)
- [value](indexerModels.Box.md#value)

### Methods

- [get\_obj\_for\_encoding](indexerModels.Box.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.Box.md#from_obj_for_encoding)

## Constructors

### constructor

• **new Box**(`«destructured»`)

Creates a new `Box` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `name` | `string` \| `Uint8Array` |
| › `value` | `string` \| `Uint8Array` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:2666](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2666)

## Properties

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### name

• **name**: `Uint8Array`

(name) box name, base64 encoded

#### Defined in

[client/v2/indexer/models/types.ts:2654](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2654)

___

### value

• **value**: `Uint8Array`

(value) box value, base64 encoded.

#### Defined in

[client/v2/indexer/models/types.ts:2659](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2659)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`Box`](indexerModels.Box.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`Box`](indexerModels.Box.md)

#### Defined in

[client/v2/indexer/models/types.ts:2690](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L2690)
