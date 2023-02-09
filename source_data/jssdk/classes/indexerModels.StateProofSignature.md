[algosdk](../README.md) / [Exports](../modules.md) / [indexerModels](../modules/indexerModels.md) / StateProofSignature

# Class: StateProofSignature

[indexerModels](../modules/indexerModels.md).StateProofSignature

## Hierarchy

- `default`

  ↳ **`StateProofSignature`**

## Table of contents

### Constructors

- [constructor](indexerModels.StateProofSignature.md#constructor)

### Properties

- [attribute\_map](indexerModels.StateProofSignature.md#attribute_map)
- [falconSignature](indexerModels.StateProofSignature.md#falconsignature)
- [merkleArrayIndex](indexerModels.StateProofSignature.md#merklearrayindex)
- [proof](indexerModels.StateProofSignature.md#proof)
- [verifyingKey](indexerModels.StateProofSignature.md#verifyingkey)

### Methods

- [get\_obj\_for\_encoding](indexerModels.StateProofSignature.md#get_obj_for_encoding)
- [from\_obj\_for\_encoding](indexerModels.StateProofSignature.md#from_obj_for_encoding)

## Constructors

### constructor

• **new StateProofSignature**(`«destructured»`)

Creates a new `StateProofSignature` object.

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `falconSignature?` | `string` \| `Uint8Array` |
| › `merkleArrayIndex?` | `number` \| `bigint` |
| › `proof?` | [`MerkleArrayProof`](indexerModels.MerkleArrayProof.md) |
| › `verifyingKey?` | `string` \| `Uint8Array` |

#### Overrides

BaseModel.constructor

#### Defined in

[client/v2/indexer/models/types.ts:3641](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3641)

## Properties

### attribute\_map

• **attribute\_map**: `Record`<`string`, `string`\>

#### Inherited from

BaseModel.attribute\_map

#### Defined in

[client/v2/basemodel.ts:56](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/basemodel.ts#L56)

___

### falconSignature

• `Optional` **falconSignature**: `Uint8Array`

#### Defined in

[client/v2/indexer/models/types.ts:3623](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3623)

___

### merkleArrayIndex

• `Optional` **merkleArrayIndex**: `number` \| `bigint`

#### Defined in

[client/v2/indexer/models/types.ts:3625](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3625)

___

### proof

• `Optional` **proof**: [`MerkleArrayProof`](indexerModels.MerkleArrayProof.md)

#### Defined in

[client/v2/indexer/models/types.ts:3627](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3627)

___

### verifyingKey

• `Optional` **verifyingKey**: `Uint8Array`

(vkey)

#### Defined in

[client/v2/indexer/models/types.ts:3632](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3632)

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

▸ `Static` **from_obj_for_encoding**(`data`): [`StateProofSignature`](indexerModels.StateProofSignature.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Record`<`string`, `any`\> |

#### Returns

[`StateProofSignature`](indexerModels.StateProofSignature.md)

#### Defined in

[client/v2/indexer/models/types.ts:3673](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/indexer/models/types.ts#L3673)
