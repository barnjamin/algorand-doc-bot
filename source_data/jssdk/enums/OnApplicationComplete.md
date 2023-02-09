[algosdk](../README.md) / [Exports](../modules.md) / OnApplicationComplete

# Enumeration: OnApplicationComplete

Enums for application transactions on-transaction-complete behavior

## Table of contents

### Enumeration Members

- [ClearStateOC](OnApplicationComplete.md#clearstateoc)
- [CloseOutOC](OnApplicationComplete.md#closeoutoc)
- [DeleteApplicationOC](OnApplicationComplete.md#deleteapplicationoc)
- [NoOpOC](OnApplicationComplete.md#noopoc)
- [OptInOC](OnApplicationComplete.md#optinoc)
- [UpdateApplicationOC](OnApplicationComplete.md#updateapplicationoc)

## Enumeration Members

### ClearStateOC

• **ClearStateOC** = ``3``

ClearStateOC is similar to CloseOutOC, but may never fail. This
allows users to reclaim their minimum balance from an application
they no longer wish to opt in to.

#### Defined in

[types/transactions/base.ts:81](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/base.ts#L81)

___

### CloseOutOC

• **CloseOutOC** = ``2``

CloseOutOC indicates that an application transaction will deallocate
some LocalState for the application from the user's account

#### Defined in

[types/transactions/base.ts:74](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/base.ts#L74)

___

### DeleteApplicationOC

• **DeleteApplicationOC** = ``5``

DeleteApplicationOC indicates that an application transaction will
delete the AppParams for the application from the creator's balance
record

#### Defined in

[types/transactions/base.ts:94](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/base.ts#L94)

___

### NoOpOC

• **NoOpOC** = ``0``

NoOpOC indicates that an application transaction will simply call its
ApprovalProgram

#### Defined in

[types/transactions/base.ts:62](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/base.ts#L62)

___

### OptInOC

• **OptInOC** = ``1``

OptInOC indicates that an application transaction will allocate some
LocalState for the application in the sender's account

#### Defined in

[types/transactions/base.ts:68](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/base.ts#L68)

___

### UpdateApplicationOC

• **UpdateApplicationOC** = ``4``

UpdateApplicationOC indicates that an application transaction will
update the ApprovalProgram and ClearStateProgram for the application

#### Defined in

[types/transactions/base.ts:87](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/types/transactions/base.ts#L87)
