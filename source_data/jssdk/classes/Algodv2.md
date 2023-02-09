[algosdk](../README.md) / [Exports](../modules.md) / Algodv2

# Class: Algodv2

Algod client connects an application to the Algorand blockchain. The algod client requires a valid algod REST endpoint IP address and algod token from an Algorand node that is connected to the network you plan to interact with.

Algod is the main Algorand process for handling the blockchain. Messages between nodes are processed, the protocol steps are executed, and the blocks are written to disk. The algod process also exposes a REST API server that developers can use to communicate with the node and the network. Algod uses the data directory for storage and configuration information.

#### Relevant Information
[How do I obtain an algod address and token?](https://developer.algorand.org/docs/archive/build-apps/setup/?from_query=algod#how-do-i-obtain-an-algod-address-and-token)

[Run Algod in Postman OAS3](https://developer.algorand.org/docs/rest-apis/restendpoints/?from_query=algod#algod-indexer-and-kmd-rest-endpoints)

## Hierarchy

- `default`

  ↳ **`Algodv2`**

## Table of contents

### Constructors

- [constructor](Algodv2.md#constructor)

### GET Methods

- [accountApplicationInformation](Algodv2.md#accountapplicationinformation)
- [accountAssetInformation](Algodv2.md#accountassetinformation)
- [accountInformation](Algodv2.md#accountinformation)
- [block](Algodv2.md#block)
- [genesis](Algodv2.md#genesis)
- [getApplicationBoxByName](Algodv2.md#getapplicationboxbyname)
- [getApplicationBoxes](Algodv2.md#getapplicationboxes)
- [getApplicationByID](Algodv2.md#getapplicationbyid)
- [getAssetByID](Algodv2.md#getassetbyid)
- [getBlockHash](Algodv2.md#getblockhash)
- [getTransactionParams](Algodv2.md#gettransactionparams)
- [getTransactionProof](Algodv2.md#gettransactionproof)
- [healthCheck](Algodv2.md#healthcheck)
- [pendingTransactionByAddress](Algodv2.md#pendingtransactionbyaddress)
- [pendingTransactionInformation](Algodv2.md#pendingtransactioninformation)
- [pendingTransactionsInformation](Algodv2.md#pendingtransactionsinformation)
- [status](Algodv2.md#status)
- [statusAfterBlock](Algodv2.md#statusafterblock)
- [supply](Algodv2.md#supply)
- [versionsCheck](Algodv2.md#versionscheck)

### Other Methods

- [disassemble](Algodv2.md#disassemble)
- [getIntEncoding](Algodv2.md#getintencoding)
- [getLightBlockHeaderProof](Algodv2.md#getlightblockheaderproof)
- [getStateProof](Algodv2.md#getstateproof)
- [setIntEncoding](Algodv2.md#setintencoding)

### POST Methods

- [compile](Algodv2.md#compile)
- [dryrun](Algodv2.md#dryrun)
- [sendRawTransaction](Algodv2.md#sendrawtransaction)

## Constructors

### constructor

• **new Algodv2**(`tokenOrBaseClient`, `baseServer`, `port?`, `headers?`)

Create an AlgodClient from
* either a token, baseServer, port, and optional headers
* or a base client server for interoperability with external dApp wallets

#### Example
```typescript
const token  = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
const server = "http://localhost";
const port   = 4001;
const algodClient = new algosdk.Algodv2(token, server, port);
```

**`Remarks`**

The above configuration is for a sandbox private network.
For applications on production, you are encouraged to run your own node, or use an Algorand REST API provider with a dedicated API key.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `tokenOrBaseClient` | `string` \| [`BaseHTTPClient`](../interfaces/BaseHTTPClient.md) \| `AlgodTokenHeader` \| `CustomTokenHeader` | The algod token from the Algorand node you are interacting with |
| `baseServer` | `string` | REST endpoint |
| `port?` | `string` \| `number` | Port number if specifically configured by the server |
| `headers` | `Record`<`string`, `string`\> | Optional headers |

#### Overrides

ServiceClient.constructor

#### Defined in

[client/v2/algod/algod.ts:67](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L67)

## GET Methods

### accountApplicationInformation

▸ **accountApplicationInformation**(`account`, `index`): `default`

Returns the given account's application information for a specific application.

#### Example
```typescript
const address = "XBYLS2E6YI6XXL5BWCAMOA4GTWHXWENZMX5UHXMRNWWUQ7BXCY5WC5TEPA";
const index = 60553466;
const accountInfo = await algodClient.accountApplicationInformation(address, index).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2accountsaddress)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `account` | `string` | The address of the account to look up. |
| `index` | `number` | The application ID to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:186](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L186)

___

### accountAssetInformation

▸ **accountAssetInformation**(`account`, `index`): `default`

Returns the given account's asset information for a specific asset.

#### Example
```typescript
const address = "XBYLS2E6YI6XXL5BWCAMOA4GTWHXWENZMX5UHXMRNWWUQ7BXCY5WC5TEPA";
const index = 60553466;
const accountAssetInfo = await algodClient.accountAssetInformation(address, index).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2accountsaddress)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `account` | `string` | The address of the account to look up. |
| `index` | `number` | The asset ID to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:162](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L162)

___

### accountInformation

▸ **accountInformation**(`account`): `default`

Returns the given account's status, balance and spendable amounts.

#### Example
```typescript
const address = "XBYLS2E6YI6XXL5BWCAMOA4GTWHXWENZMX5UHXMRNWWUQ7BXCY5WC5TEPA";
const accountInfo = await algodClient.accountInformation(address).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2accountsaddress)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `account` | `string` | The address of the account to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:143](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L143)

___

### block

▸ **block**(`roundNumber`): `default`

Gets the block info for the given round.

#### Example
```typescript
const roundNumber = 18038133;
const block = await algodClient.block(roundNumber).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2blocksround)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `roundNumber` | `number` | The round number of the block to get. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:208](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L208)

___

### genesis

▸ **genesis**(): `default`

Returns the entire genesis file.

#### Example
```typescript
const genesis = await algodClient.genesis().do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-genesis)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:524](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L524)

___

### getApplicationBoxByName

▸ **getApplicationBoxByName**(`index`, `boxName`): `default`

Given an application ID and the box name (key), return the value stored in the box.

#### Example
```typescript
const index = 60553466;
const boxName = Buffer.from("foo");
const boxResponse = await algodClient.getApplicationBoxByName(index, boxName).do();
const boxValue = boxResponse.value;
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2applicationsapplication-idbox)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `index` | `number` | The application ID to look up. |
| `boxName` | `Uint8Array` | - |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:486](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L486)

___

### getApplicationBoxes

▸ **getApplicationBoxes**(`index`): `default`

Given an application ID, return all the box names associated with the app.

#### Example
```typescript
const index = 60553466;
const boxesResponse = await algodClient.getApplicationBoxes(index).max(3).do();
const boxNames = boxesResponse.boxes.map(box => box.name);
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2applicationsapplication-idboxes)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `index` | `number` | The application ID to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:509](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L509)

___

### getApplicationByID

▸ **getApplicationByID**(`index`): `default`

Given an application ID, return the application information including creator, approval
and clear programs, global and local schemas, and global state.

#### Example
```typescript
const index = 60553466;
const app = await algodClient.getApplicationByID(index).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2applicationsapplication-id)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `index` | `number` | The application ID to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:467](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L467)

___

### getAssetByID

▸ **getAssetByID**(`index`): `default`

Given an asset ID, return asset information including creator, name, total supply and
special addresses.

#### Example
```typescript
const asset_id = 163650;
const asset = await algodClient.getAssetByID(asset_id).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2assetsasset-id)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `index` | `number` | The asset ID to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:449](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L449)

___

### getBlockHash

▸ **getBlockHash**(`roundNumber`): `default`

Get the block hash for the block on the given round.

#### Example
```typescript
const roundNumber = 18038133;
const block = await algodClient.getBlockHash(roundNumber).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2blocksroundhash)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `roundNumber` | `number` | The round number of the block to get. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:225](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L225)

___

### getTransactionParams

▸ **getTransactionParams**(): `default`

Returns the common needed parameters for a new transaction.

#### Example
```typescript
const suggestedParams = await algodClient.getTransactionParams().do();
const amountInMicroAlgos = algosdk.algosToMicroalgos(2); // 2 Algos
const unsignedTxn = algosdk.makePaymentTxnWithSuggestedParamsFromObject({
  from: senderAddress,
  to: receiverAddress,
  amount: amountInMicroAlgos,
  suggestedParams: suggestedParams,
});
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2transactionsparams)

**`Remarks`**

Often used with
[`makePaymentTxnWithSuggestedParamsFromObject`](../modules.md#makepaymenttxnwithsuggestedparamsfromobject), [`algosToMicroalgos`](../modules.md#algostomicroalgos)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:363](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L363)

___

### getTransactionProof

▸ **getTransactionProof**(`round`, `txID`): `default`

Returns a Merkle proof for a given transaction in a block.

#### Example
```typescript
const round = 18038133;
const txId = "MEUOC4RQJB23CQZRFRKYEI6WBO73VTTPST5A7B3S5OKBUY6LFUDA";
const proof = await algodClient.getTransactionProof(round, txId).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2blocksroundtransactionstxidproof)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `round` | `number` | The round in which the transaction appears. |
| `txID` | `string` | The transaction ID for which to generate a proof. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:543](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L543)

___

### healthCheck

▸ **healthCheck**(): `default`

Returns OK if healthy.

#### Example
```typescript
const health = await algodClient.healthCheck().do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-health)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:91](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L91)

___

### pendingTransactionByAddress

▸ **pendingTransactionByAddress**(`address`): `default`

Returns the list of pending transactions sent by the address, sorted by priority, in decreasing order, truncated at the end at MAX.
If MAX = 0, returns all pending transactions.

#### Example 1
```typescript
const address = "XBYLS2E6YI6XXL5BWCAMOA4GTWHXWENZMX5UHXMRNWWUQ7BXCY5WC5TEPA";
const pendingTxnsByAddr = await algodClient.pendingTransactionByAddress(address).do();
```

#### Example 2
```typescript
const maxTxns = 5;
const address = "XBYLS2E6YI6XXL5BWCAMOA4GTWHXWENZMX5UHXMRNWWUQ7BXCY5WC5TEPA";
const pendingTxns = await algodClient
    .pendingTransactionByAddress(address)
    .max(maxTxns)
    .do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2accountsaddresstransactionspending)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `address` | `string` | The address of the sender. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:305](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L305)

___

### pendingTransactionInformation

▸ **pendingTransactionInformation**(`txid`): `default`

Returns the transaction information for a specific pending transaction.

#### Example
```typescript
const txId = "DRJS6R745A7GFVMXEXWP4TGVDGKW7VILFTA7HC2BR2GRLHNY5CTA";
const pending = await algodClient.pendingTransactionInformation(txId).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2transactionspendingtxid)

**`Remarks`**

<br><br>
There are several cases when this might succeed:
- transaction committed (committed round > 0)
- transaction still in the pool (committed round = 0, pool error = "")
- transaction removed from pool due to error (committed round = 0, pool error != "")

Or the transaction may have happened sufficiently long ago that the node no longer remembers it, and this will return an error.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `txid` | `string` | The TxID string of the pending transaction to look up. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:252](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L252)

___

### pendingTransactionsInformation

▸ **pendingTransactionsInformation**(): `default`

Returns the list of pending transactions in the pool, sorted by priority, in decreasing order, truncated at the end at MAX.
If MAX = 0, returns all pending transactions.

#### Example 1
```typescript
const pendingTxns = await algodClient.pendingTransactionsInformation().do();
```

#### Example 2
```typescript
const maxTxns = 5;
const pendingTxns = await algodClient
    .pendingTransactionsInformation()
    .max(maxTxns)
    .do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2transactionspending)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:277](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L277)

___

### status

▸ **status**(): `default`

Retrieves the StatusResponse from the running node.

#### Example
```typescript
const status = await algodClient.status().do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2status)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:320](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L320)

___

### statusAfterBlock

▸ **statusAfterBlock**(`round`): `default`

Waits for a specific round to occur then returns the `StatusResponse` for that round.

#### Example
```typescript
const round = 18038133;
const statusAfterBlock = await algodClient.statusAfterBlock(round).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2statuswait-for-block-afterround)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `round` | `number` | The number of the round to wait for. |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:337](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L337)

___

### supply

▸ **supply**(): `default`

Returns the supply details for the specified node's ledger.

#### Example
```typescript
const supplyDetails = await algodClient.supply().do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-v2ledgersupply)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:378](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L378)

___

### versionsCheck

▸ **versionsCheck**(): `default`

Retrieves the supported API versions, binary build versions, and genesis information.

#### Example
```typescript
const versionsDetails = await algodClient.versionsCheck().do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#get-versions)

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:106](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L106)

___

## Other Methods

### disassemble

▸ **disassemble**(`source`): `default`

Given the program bytes, return the TEAL source code in plain text.

#### Example
```typescript
const bytecode = "TEAL bytecode";
const disassembledSource = await algodClient.disassemble(bytecode).do();
```

**`Remarks`**

This endpoint is only enabled when a node's configuration file sets EnableDeveloperAPI to true.

#### Parameters

| Name | Type |
| :------ | :------ |
| `source` | `string` \| `Uint8Array` |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:413](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L413)

___

### getIntEncoding

▸ **getIntEncoding**(): [`IntDecoding`](../enums/IntDecoding.md)

Get the default int decoding method for all JSON requests this client creates.

#### Returns

[`IntDecoding`](../enums/IntDecoding.md)

#### Inherited from

ServiceClient.getIntEncoding

#### Defined in

[client/v2/serviceClient.ts:83](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/serviceClient.ts#L83)

___

### getLightBlockHeaderProof

▸ **getLightBlockHeaderProof**(`round`): `default`

Gets a proof for a given light block header inside a state proof commitment.

#### Example
```typescript
const round = 11111111;
const lightBlockHeaderProof = await algodClient.getLightBlockHeaderProof(round).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2#get-v2blocksroundlightheaderproof)

#### Parameters

| Name | Type |
| :------ | :------ |
| `round` | `number` |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:559](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L559)

___

### getStateProof

▸ **getStateProof**(`round`): `default`

Gets a state proof that covers a given round.

#### Example
```typescript
const round = 11111111;
const stateProof = await algodClient.getStateProof(round).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2#get-v2stateproofsround)

#### Parameters

| Name | Type |
| :------ | :------ |
| `round` | `number` |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:575](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L575)

___

### setIntEncoding

▸ **setIntEncoding**(`method`): `void`

Set the default int decoding method for all JSON requests this client creates.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `method` | [`IntDecoding`](../enums/IntDecoding.md) | {"default" \| "safe" \| "mixed" \| "bigint"} method The method to use when parsing the response for request. Must be one of "default", "safe", "mixed", or "bigint". See JSONRequest.setIntDecoding for more details about what each method does. |

#### Returns

`void`

#### Inherited from

ServiceClient.setIntEncoding

#### Defined in

[client/v2/serviceClient.ts:76](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/serviceClient.ts#L76)

___

## POST Methods

### compile

▸ **compile**(`source`): `default`

Compiles TEAL source code to binary, returns base64 encoded program bytes and base32 SHA512_256 hash of program bytes (Address style).

#### Example
```typescript
const source = "TEAL SOURCE CODE";
const compiledSmartContract = await algodClient.compile(source).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#post-v2tealcompile)

**`Remarks`**

This endpoint is only enabled when a node's configuration file sets `EnableDeveloperAPI` to true.

#### Parameters

| Name | Type |
| :------ | :------ |
| `source` | `string` \| `Uint8Array` |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:397](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L397)

___

### dryrun

▸ **dryrun**(`dr`): `default`

Provides debugging information for a transaction (or group).

Executes TEAL program(s) in context and returns debugging information about the execution. This endpoint is only enabled when a node's configureation file sets `EnableDeveloperAPI` to true.

#### Example
```typescript
const dryRunResult = await algodClient.dryrun(dr).do();
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#post-v2tealdryrun)

#### Parameters

| Name | Type |
| :------ | :------ |
| `dr` | [`DryrunRequest`](modelsv2.DryrunRequest.md) |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:431](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L431)

___

### sendRawTransaction

▸ **sendRawTransaction**(`stxOrStxs`): `default`

Broadcasts a raw transaction to the network.

#### Example
```typescript
const { txId } = await algodClient.sendRawTransaction(signedTxns).do();
const result = await waitForConfirmation(algodClient, txid, 3);
```

[Response data schema details](https://developer.algorand.org/docs/rest-apis/algod/v2/#post-v2transactions)

**`Remarks`**

Often used with [`waitForConfirmation`](../modules.md#waitforconfirmation)

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `stxOrStxs` | `Uint8Array` \| `Uint8Array`[] | Signed transactions |

#### Returns

`default`

#### Defined in

[client/v2/algod/algod.ts:126](https://github.com/algorand/js-algorand-sdk/blob/13a5d73/src/client/v2/algod/algod.ts#L126)
