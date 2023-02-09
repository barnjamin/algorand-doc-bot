[algosdk](../README.md) / [Exports](../modules.md) / [modelsv2](../modules/modelsv2.md) / ApplicationStateSchema

# Class: ApplicationStateSchema

[modelsv2](../modules/modelsv2.md).ApplicationStateSchema

Specifies maximums on the number of each type that may be stored.

## Hierarchy

- `default`

  ↳ **`ApplicationStateSchema`**

## Table of contents

### Constructors

- [constructor](modelsv2.ApplicationStateSchema.md#constructor)

### Properties

- [attribute\_map](modelsv2.ApplicationStateSchema.md#attribute_map)
- [numByteSlice](modelsv2.ApplicationStateSchema.md#numbyteslice)
- [numUint](modelsv2.ApplicationStateSchema.md#numuint)

### Methods

- [get\_obj\_for\_encoding](modelsv2.ApplicationStateSchema.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](modelsv2.ApplicationStateSchema.md#from_obj_for_encoding)

## Constructors

### constructor

• **new ApplicationStateSchema**(`«destructured»`)

Creates a new `ApplicationStateSchema` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `numByteSlice` | `number` \| `bigint` |
| › `numUint` | `number` \| `bigint` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/algod/models/types.ts:1006](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1006)

## Properties

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### numByteSlice

• **numByteSlice**: `number` \| `bigint`

(nbs) num of byte slices.

#### Defined in

[client/v2/algod/models/types.ts:999](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L999)

___

### numUint

• **numUint**: `number` \| `bigint`

(nui) num of uints.

#### Defined in

[client/v2/algod/models/types.ts:994](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L994)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`ApplicationStateSchema`](modelsv2.ApplicationStateSchema.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`ApplicationStateSchema`](modelsv2.ApplicationStateSchema.md)

#### Defined in

[client/v2/algod/models/types.ts:1024](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L1024)
