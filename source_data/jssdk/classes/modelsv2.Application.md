[algosdk](../README.md) / [Exports](../modules.md) / [modelsv2](../modules/modelsv2.md) / Application

# Class: Application

[modelsv2](../modules/modelsv2.md).Application

Application index and its parameters

## Hierarchy

- `default`

  ↳ **`Application`**

## Table of contents

### Constructors

- [constructor](modelsv2.Application.md#constructor)

### Properties

- [attribute\_map](modelsv2.Application.md#attribute_map)
- [id](modelsv2.Application.md#id)
- [params](modelsv2.Application.md#params)

### Methods

- [get\_obj\_for\_encoding](modelsv2.Application.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](modelsv2.Application.md#from_obj_for_encoding)

## Constructors

### constructor

• **new Application**(`«destructured»`)

Creates a new `Application` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `id` | `number` \| `bigint` |
| › `params` | [`ApplicationParams`](modelsv2.ApplicationParams.md) |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/algod/models/types.ts:755](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L755)

## Properties

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### id

• **id**: `number` \| `bigint`

(appidx) application index.

#### Defined in

[client/v2/algod/models/types.ts:743](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L743)

___

### params

• **params**: [`ApplicationParams`](modelsv2.ApplicationParams.md)

(appparams) application parameters.

#### Defined in

[client/v2/algod/models/types.ts:748](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L748)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`Application`](modelsv2.Application.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`Application`](modelsv2.Application.md)

#### Defined in

[client/v2/algod/models/types.ts:773](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/models/types.ts#L773)
