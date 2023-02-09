[algosdk](../README.md) / [Exports](../modules.md) / SourceMap

# Class: SourceMap

## Table of contents

### Constructors

- [constructor](SourceMap.md#constructor)

### Properties

- [lineToPc](SourceMap.md#linetopc)
- [mappings](SourceMap.md#mappings)
- [names](SourceMap.md#names)
- [pcToLine](SourceMap.md#pctoline)
- [sources](SourceMap.md#sources)
- [version](SourceMap.md#version)

### Methods

- [getLineForPc](SourceMap.md#getlineforpc)
- [getPcsForLine](SourceMap.md#getpcsforline)

## Constructors

### constructor

• **new SourceMap**(`«destructured»`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `«destructured»` | `Object` |
| › `mappings` | `string` |
| › `names` | `string`[] |
| › `sources` | `string`[] |
| › `version` | `number` |

#### Defined in

[logic/sourcemap.ts:12](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L12)

## Properties

### lineToPc

• **lineToPc**: `Object`

#### Index signature

▪ [key: `number`]: `number`[]

#### Defined in

[logic/sourcemap.ts:10](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L10)

___

### mappings

• **mappings**: `string`

#### Defined in

[logic/sourcemap.ts:7](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L7)

___

### names

• **names**: `string`[]

#### Defined in

[logic/sourcemap.ts:6](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L6)

___

### pcToLine

• **pcToLine**: `Object`

#### Index signature

▪ [key: `number`]: `number`

#### Defined in

[logic/sourcemap.ts:9](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L9)

___

### sources

• **sources**: `string`[]

#### Defined in

[logic/sourcemap.ts:5](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L5)

___

### version

• **version**: `number`

#### Defined in

[logic/sourcemap.ts:4](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L4)

## Methods

### getLineForPc

▸ **getLineForPc**(`pc`): `number`

#### Parameters

| Name | Type |
| :------ | :------ |
| `pc` | `number` |

#### Returns

`number`

#### Defined in

[logic/sourcemap.ts:60](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L60)

___

### getPcsForLine

▸ **getPcsForLine**(`line`): `number`[]

#### Parameters

| Name | Type |
| :------ | :------ |
| `line` | `number` |

#### Returns

`number`[]

#### Defined in

[logic/sourcemap.ts:64](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/logic/sourcemap.ts#L64)
