[algosdk](../README.md) / [Exports](../modules.md) / ABIMethod

# Class: ABIMethod

## Table of contents

### Constructors

- [constructor](ABIMethod.md#constructor)

### Properties

- [args](ABIMethod.md#args)
- [description](ABIMethod.md#description)
- [name](ABIMethod.md#name)
- [returns](ABIMethod.md#returns)

### Methods

- [getSelector](ABIMethod.md#getselector)
- [getSignature](ABIMethod.md#getsignature)
- [toJSON](ABIMethod.md#tojson)
- [txnCount](ABIMethod.md#txncount)
- [fromSignature](ABIMethod.md#fromsignature)

## Constructors

### constructor

• **new ABIMethod**(`params`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `params` | [`ABIMethodParams`](../interfaces/ABIMethodParams.md) |

#### Defined in

[abi/method.ts:81](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L81)

## Properties

### args

• `Readonly` **args**: { `description?`: `string` ; `name?`: `string` ; `type`: [`ABIArgumentType`](../modules.md#abiargumenttype)  }[]

#### Defined in

[abi/method.ts:73](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L73)

___

### description

• `Optional` `Readonly` **description**: `string`

#### Defined in

[abi/method.ts:72](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L72)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[abi/method.ts:71](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L71)

___

### returns

• `Readonly` **returns**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `description?` | `string` |
| `type` | [`ABIReturnType`](../modules.md#abireturntype) |

#### Defined in

[abi/method.ts:79](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L79)

## Methods

### getSelector

▸ **getSelector**(): `Uint8Array`

#### Returns

`Uint8Array`

#### Defined in

[abi/method.ts:122](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L122)

___

### getSignature

▸ **getSignature**(): `string`

#### Returns

`string`

#### Defined in

[abi/method.ts:116](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L116)

___

### toJSON

▸ **toJSON**(): [`ABIMethodParams`](../interfaces/ABIMethodParams.md)

#### Returns

[`ABIMethodParams`](../interfaces/ABIMethodParams.md)

#### Defined in

[abi/method.ts:137](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L137)

___

### txnCount

▸ **txnCount**(): `number`

#### Returns

`number`

#### Defined in

[abi/method.ts:127](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L127)

___

### fromSignature

▸ `Static` **fromSignature**(`signature`): [`ABIMethod`](ABIMethod.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `signature` | `string` |

#### Returns

[`ABIMethod`](ABIMethod.md)

#### Defined in

[abi/method.ts:153](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/method.ts#L153)
