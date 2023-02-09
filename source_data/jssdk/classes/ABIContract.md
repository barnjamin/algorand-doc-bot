[algosdk](../README.md) / [Exports](../modules.md) / ABIContract

# Class: ABIContract

## Table of contents

### Constructors

- [constructor](ABIContract.md#constructor)

### Properties

- [description](ABIContract.md#description)
- [methods](ABIContract.md#methods)
- [name](ABIContract.md#name)
- [networks](ABIContract.md#networks)

### Methods

- [getMethodByName](ABIContract.md#getmethodbyname)
- [toJSON](ABIContract.md#tojson)

## Constructors

### constructor

• **new ABIContract**(`params`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `params` | [`ABIContractParams`](../interfaces/ABIContractParams.md) |

#### Defined in

[abi/contract.ts:24](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L24)

## Properties

### description

• `Optional` `Readonly` **description**: `string`

#### Defined in

[abi/contract.ts:20](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L20)

___

### methods

• `Readonly` **methods**: [`ABIMethod`](ABIMethod.md)[]

#### Defined in

[abi/contract.ts:22](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L22)

___

### name

• `Readonly` **name**: `string`

#### Defined in

[abi/contract.ts:19](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L19)

___

### networks

• `Readonly` **networks**: [`ABIContractNetworks`](../interfaces/ABIContractNetworks.md)

#### Defined in

[abi/contract.ts:21](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L21)

## Methods

### getMethodByName

▸ **getMethodByName**(`name`): [`ABIMethod`](ABIMethod.md)

#### Parameters

| Name | Type |
| :------ | :------ |
| `name` | `string` |

#### Returns

[`ABIMethod`](ABIMethod.md)

#### Defined in

[abi/contract.ts:48](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L48)

___

### toJSON

▸ **toJSON**(): [`ABIContractParams`](../interfaces/ABIContractParams.md)

#### Returns

[`ABIContractParams`](../interfaces/ABIContractParams.md)

#### Defined in

[abi/contract.ts:39](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/abi/contract.ts#L39)
