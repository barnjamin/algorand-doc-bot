title: 3. Your First Transaction

After you successfully connect to **algod** using your preferred SDK, explore the methods available to read from and write to the blockchain. Remember that writing to the Algorand blockchain is simply sending a transaction to the network that is later confirmed within a block. 

Follow the guide below to send your first transaction on Algorand and familiarize yourself with some of the core functions of the SDKs. Examples of `goal` commands and REST API calls are included when they are the same or similar, allowing you to cross-verify and gain fluency across all available tools and platforms. 

Code snippets are abbreviated for conciseness and clarity. See the full code example for each SDK at the bottom of this guide.

!!! info 
    Full running code examples for each SDK and both API versions are available within the GitHub repo at [/examples/start_building](https://github.com/algorand/docs/tree/master/examples/start_building) and for [download](https://github.com/algorand/docs/blob/master/examples/start_building/start_building.zip?raw=true) (.zip).

# Create an account
In order to send a transaction, you first need an [account](../../../get-details/accounts#accounts) on Algorand. Create an account by generating an Algorand public/private key pair and then funding the public address with Algos on your chosen network. 

!!! info
	The terms **account**, **public key**, and **address** are used interchangeably in certain contexts, but they have slightly different meanings. Read more about these differences in the [Accounts Overview](../../../get-details/accounts).


## Generate a public/private key pair

=== "JavaScript"
    ```javascript 
    const algosdk = require('algosdk');

    var account = algosdk.generateAccount();
    var passphrase = algosdk.secretKeyToMnemonic(account.sk);
    console.log( "My address: " + account.addr );
    console.log( "My passphrase: " + passphrase );
    ```
=== "Python"
    ```python 
    from algosdk import account, mnemonic

    def generate_algorand_keypair():
        private_key, address = account.generate_account()
        print("My address: {}".format(address))
        print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    ```
=== "Java"
    ```java 
    import com.algorand.algosdk.account.Account;	

    Account myAccount = new Account();
    System.out.println("My Address: " + myAccount.getAddress());
    System.out.println("My Passphrase: " + myAccount.toMnemonic());
    ```
=== "Go"
    ```go
    import (
        "fmt"

        "github.com/algorand/go-algorand-sdk/crypto"
        "github.com/algorand/go-algorand-sdk/mnemonic"
    )

    func main() {
        account := crypto.GenerateAccount()
        passphrase, err := mnemonic.FromPrivateKey(account.PrivateKey)

        if err != nil {
            fmt.Printf("Error creating transaction: %s\n", err)
        } else {
            fmt.Printf("My address: %s\n", account.Address)
            fmt.Printf("My passphrase: %s\n", passphrase)
        }
    }
    ```
=== "goal"
    ```bash 
    $ goal account new
    Created new account with address [ADDRESS]

    $ goal account export -a <address>
    Exported key for account [ADDRESS]: [PASSPHRASE]
    ```

=== "algokey"
    ```bash 
    $ algokey generate
    Private key mnemonic: [PASSPHRASE]
    Public key: [ADDRESS]
    ```

_Learn more about [Creating Accounts on Algorand](../../../get-details/accounts/create)._

## Add funds
For [TestNet](../../reference/algorand-networks/testnet/#faucet) and [BetaNet](../../reference/algorand-networks/betanet/#faucet), copy and paste the public portion of your key pair in the corresponding faucet prompt and click "Submit". A `200` response means the transaction went through and your balance increased by 100,000,000 microAlgos (i.e. 100 Algos).

!!! info
	Amounts are returned in microAlgos - the base unit for Algos. Micro denotes a unit x 10^-6. Therefore, 1 Algo equals 1,000,000 microAlgos.

## Connect your client

Each SDK provides a client which must instantiate prior to making calls to the API endpoints. You must provide values for `<algod-address>`, `<port>` and `<algod-token>`. The CLI tools implement the client natively. 

_Learn more about [Connecting to a Node](connect)._

=== "JavaScript"
    ```js
    const algodToken = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    const algodServer = "http://localhost";
    const algodPort = 4001;

    let algodClient = new algosdk.Algodv2(algodToken, algodServer, algodPort);
    ```

=== "Python"
```py
from algosdk.v2client import algod

algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)
```

=== "Java"
    ```java 
    import com.algorand.algosdk.v2.client.common.AlgodClient;
    import com.algorand.algosdk.v2.client.common.Client;

    final String ALGOD_API_ADDR = "localhost";
    final Integer ALGOD_PORT = 4001;
    final String ALGOD_API_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";

    AlgodClient client = new AlgodClient(ALGOD_API_ADDR, ALGOD_PORT, ALGOD_API_TOKEN);
    ```

=== "Go"
    ```Go 
    package main

    import (
        "github.com/algorand/go-algorand-sdk/client/v2/algod" 
    )

    const algodAddress = "http://localhost:4001"
    const algodToken = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    func main() {
        algodClient, err := algod.MakeClient(algodAddress, algodToken)
        if err != nil {
            fmt.Printf("Issue with creating algod client: %s\n", err)
            return
        }
    }
    ```

## Check your balance

Check your balance to confirm the added funds.

=== "JavaScript"
```js

	const passphrase = "Your 25-word mnemonic generated and displayed above";

	let myAccount = algosdk.mnemonicToSecretKey(passphrase)
	console.log("My address: %s", myAccount.addr)

    let accountInfo = await algodClient.accountInformation(myAccount.addr).do();
    console.log("Account balance: %d microAlgos", accountInfo.amount);
```

=== "Python"
    ```python 
    passphrase = "Your 25-word mnemonic generated and displayed above"

    private_key = mnemonic.to_private_key(passphrase)
    my_address = mnemonic.to_public_key(passphrase)
    print("My address: {}".format(my_address))

    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))
    ```

=== "Java"
    ```java 
    final String PASSPHRASE = "Your 25-word mnemonic generated and displayed above";
    com.algorand.algosdk.account.Account myAccount = new Account(PASSPHRASE);
    System.out.println("My Address: " + myAccount.getAddress());
    String myAddress = myAccount.getAddress().toString();
    Response <com.algorand.algosdk.v2.client.model.Account> respAcct = client.AccountInformation(myAccount.getAddress()).execute();
    if (!respAcct.isSuccessful()) {
        throw new Exception(respAcct.message());
    }
    com.algorand.algosdk.v2.client.model.Account accountInfo = respAcct.body();
    System.out.println(String.format("Account Balance: %d microAlgos", accountInfo.amount));

    ```

=== "Go"
    ```go 
    passphrase := "Your 25-word mnemonic generated and displayed above"
    privateKey, err := mnemonic.ToPrivateKey(passphrase)
    if err != nil {
        fmt.Printf("Issue with mnemonic conversion: %s\n", err)
        return
    }

    var myAddress types.Address
    publicKey := privateKey.Public()
    cpk := publicKey.(ed25519.PublicKey)
    copy(myAddress[:], cpk[:])
    fmt.Printf("My address: %s\n", myAddress.String())

    accountInfo, err := algodClient.AccountInformation(myAddress.String()).Do(context.Background())
    if err != nil {
        fmt.Printf("Error getting account info: %s\n", err)
        return
    }
    fmt.Printf("Account balance: %d microAlgos\n", accountInfo.Amount)
    ```

=== "cURL"
    ```bash 
    curl -i -X GET \
       -H "X-Algo-API-Token:<algod-token>" \
     'http://<algod-address>:<algod-port>/v2/account/<address>'
    ```

=== "goal"
    ```bash 
    $ goal account balance -a <my-address>
    [AMOUNT] microAlgos
    ```

# Construct the transaction

Create a transaction to send 1 Algo from your account to the TestNet faucet address (`GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A`) with the note "Hello World".

Transactions require a certain minimum set of parameters to be valid. Mandatory fields include the **round validity range**, the **fee**, and the **genesis hash** for the network the transaction is valid for. Read all about Transaction types, fields, and configurations in the [Transactions Feature Guide](../../../get-details/transactions). For now, construct a payment transaction as follows. Use the _suggested parameters_ methods to initialize network-related 
fields. 

=== "JavaScript"

    ```javascript
    let params = await algodClient.getTransactionParams().do();
    // comment out the next two lines to use suggested fee
    params.fee = 1000;
    params.flatFee = true;
    const receiver = "GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A";
    const enc = new TextEncoder();
    let note = enc.encode("Hello World");
    let txn = algosdk.makePaymentTxnWithSuggestedParams(myAccount.addr, receiver, 1000000, undefined, note, params);        
    ```

=== "Python"

    ```python 
    from algosdk.transaction import PaymentTxn

    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = 1000
    receiver = "GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A"
    note = "Hello World".encode()

    unsigned_txn = PaymentTxn(my_address, params, receiver, 1000000, None, note)
    ```

=== "Java"

    ```java 
    // Construct the transaction
    final String RECEIVER = "L5EUPCF4ROKNZMAE37R5FY2T5DF2M3NVYLPKSGWTUKVJRUGIW4RKVPNPD4";
    String note = "Hello World";
    Response < TransactionParametersResponse > resp = client.TransactionParams().execute();
    if (!resp.isSuccessful()) {
        throw new Exception(resp.message());
    }
    TransactionParametersResponse params = resp.body();
    if (params == null) {
        throw new Exception("Params retrieval error");
    }
    Transaction txn = Transaction.PaymentTransactionBuilder()
        .sender(myAddress)
        .note(note.getBytes())
        .amount(100000)
        .receiver(new Address(RECEIVER))
        .suggestedParams(params)
        .build();
    ```

=== "Go"
    ```go 
    txParams, err := algodClient.SuggestedParams().Do(context.Background())
    if err != nil {
        fmt.Printf("Error getting suggested tx params: %s\n", err)
        return
    }
    // comment out the next two (2) lines to use suggested fees
    txParams.FlatFee = true
    txParams.Fee = 1000

    fromAddr := myAddress.String()
    toAddr := "GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A"
    var amount uint64 = 1000000
    var minFee uint64 = 1000
    note := []byte("Hello World")
    genID := txParams.GenesisID
    genHash := txParams.GenesisHash
    firstValidRound := uint64(txParams.FirstRoundValid)
    lastValidRound := uint64(txParams.LastRoundValid)

    txn, err := transaction.MakePaymentTxnWithFlatFee(fromAddr, toAddr, minFee, amount, firstValidRound, lastValidRound, note, "", genID, genHash)
    if err != nil {
        fmt.Printf("Error creating transaction: %s\n", err)
        return
    }
    ```
=== "goal"

    ```bash 
    $ goal clerk send --from=<my-account> --to=GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A --fee=1000 --amount=1000000 --note="Hello World" --out="hello-world.txn"
    ```

!!! info
    Some of the SDKs provide wrapper functions for creating certain types of transactions, like `makePaymentTxn` in Go. 

_Learn more about the [Structure of Transactions on Algorand](../../../get-details/transactions)._

# Sign the transaction
Sign the transaction with your private key. This creates a new signed transaction object in the SDKs. Retrieve the transaction ID of the signed transaction.
=== "JavaScript"
    ```javascript
    let signedTxn = txn.signTxn(myAccount.sk);
    let txId = txn.txID().toString();
    console.log("Signed transaction with txID: %s", txId);
    ```
=== "Python"
    ```python 
    signed_txn = unsigned_txn.sign(mnemonic.to_private_key(passphrase))
    ```

=== "Java"
    ```java 
    SignedTransaction signedTxn = myAccount.signTransaction(txn);
    System.out.println("Signed transaction with txid: " + signedTxn.transactionID);
    ```

=== "Go"
    ```go 
    txID, signedTxn, err := crypto.SignTransaction(privateKey, txn)
    if err != nil {
        fmt.Printf("Failed to sign transaction: %s\n", err)
        return
    }
    fmt.Printf("Signed txid: %s\n", txID)
    ```
=== "goal"
    ```bash 
    $ goal clerk sign --infile="hello-world.txn" --outfile="hello-world.stxn"
    ```


_Learn more about [Authorizing Transactions on Algorand](../../../get-details/transactions/signatures)._

# Submit the transaction
Send the signed transaction to the network with your algod client. 

=== "JavaScript"
    ```javascript 
    await algodClient.sendRawTransaction(signedTxn).do();
    ```

=== "Python"
    ```python 
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))
    ```

=== "Java"
    ```java 
    // Submit the transaction to the network
    byte[] encodedTxBytes = Encoder.encodeToMsgPack(signedTxn);
    Response < PostTransactionsResponse > rawtxresponse = client.RawTransaction().rawtxn(encodedTxBytes).execute();
    if (!rawtxresponse.isSuccessful()) {
        throw new Exception(rawtxresponse.message());
    }
    String id = rawtxresponse.body().txId;
    System.out.println("Successfully sent tx with ID: " + id);
    ```
=== "Go"
    ```go 
    sendResponse, err := algodClient.SendRawTransaction(signedTxn).Do(context.Background())
    if err != nil {
        fmt.Printf("failed to send transaction: %s\n", err)
        return
    }
    fmt.Printf("Submitted transaction %s\n", sendResponse)
    ```

=== "cURL"
    ```bash 
    curl -i -X POST \
       -H "X-Algo-API-Token:<algod-token>" \
       -H "Content-Type:application/x-binary" \
       -T "hello-world.stxn" \
     'http://<algod-address>:<algod-port>/v2/transactions'
    ```
=== "goal"
    ```bash 
    $ goal clerk rawsend --filename="hello-world.stxn"
    Sent 1000000 MicroAlgos from account [ADDRESS] to address GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A, transaction ID: [TXID]. Fee set to 1000
    Transaction [TXID] still pending as of round [LAST_ROUND]
    Transaction [TXID] committed in round [COMMITTED_ROUND]

    # Or construct, sign, and submit in one line
    $ goal clerk send --from=<my-account> --to=GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A --fee=1000 --amount=1000000 --note="Hello World"
    Sent 1000000 MicroAlgos from account [ADDRESS] to address GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A, transaction ID: [TXID]. Fee set to 1000
    Transaction [TXID] still pending as of round [LAST_ROUND]
    Transaction [TXID] committed in round [COMMITTED_ROUND]
    ```


# Wait for confirmation

Successfully submitting your transaction to the network does not necessarily mean the network confirmed it. Always check that the network confirmed your transaction within a block before proceeding. 

!!! info
    On Algorand, transactions are final as soon as they are incorporated into a block and blocks are produced, on average, every 5 seconds. This means that transactions are confirmed, on average, in **5 seconds**! Read more about the [Algorand's Consensus Protocol](../../../get-details/algorand_consensus) and how it achieves such high confirmation speeds and immediate transaction finality.

=== "JavaScript"
    ```javascript 
    /**
     * Wait until the transaction is confirmed or rejected, or until 'timeout'
     * number of rounds have passed.
     * @param {algosdk.Algodv2} algodClient the Algod V2 client
     * @param {string} txId the transaction ID to wait for
     * @param {number} timeout maximum number of rounds to wait
     * @return {Promise<*>} pending transaction information
     * @throws Throws an error if the transaction is not confirmed or rejected in the next timeout rounds
     */
    const waitForConfirmation = async function (algodClient, txId, timeout) {
        if (algodClient == null || txId == null || timeout < 0) {
            throw new Error("Bad arguments");
        }

        const status = (await algodClient.status().do());
        if (status === undefined) {
            throw new Error("Unable to get node status");
        }

        const startround = status["last-round"] + 1;
        let currentround = startround;

        while (currentround < (startround + timeout)) {
            const pendingInfo = await algodClient.pendingTransactionInformation(txId).do();
            if (pendingInfo !== undefined) {
                if (pendingInfo["confirmed-round"] !== null && pendingInfo["confirmed-round"] > 0) {
                    //Got the completed Transaction
                    return pendingInfo;
                } else {
                    if (pendingInfo["pool-error"] != null && pendingInfo["pool-error"].length > 0) {
                        // If there was a pool error, then the transaction has been rejected!
                        throw new Error("Transaction " + txId + " rejected - pool error: " + pendingInfo["pool-error"]);
                    }
                }
            }
            await algodClient.statusAfterBlock(currentround).do();
            currentround++;
        }

        throw new Error("Transaction " + txId + " not confirmed after " + timeout + " rounds!");
    };

    private String printBalance(com.algorand.algosdk.account.Account myAccount) throws Exception {
        String myAddress = myAccount.getAddress().toString();
        Response < com.algorand.algosdk.v2.client.model.Account > respAcct = client.AccountInformation(myAccount.getAddress()).execute();
        if (!respAcct.isSuccessful()) {
            throw new Exception(respAcct.message());
        }
        com.algorand.algosdk.v2.client.model.Account accountInfo = respAcct.body();
        System.out.println(String.format("Account Balance: %d microAlgos", accountInfo.amount));
        return myAddress;
    }
    ```

=== "Python"
    ```python 
    # utility for waiting on a transaction confirmation
    def wait_for_confirmation(client, transaction_id, timeout):
        """
        Wait until the transaction is confirmed or rejected, or until 'timeout'
        number of rounds have passed.
        Args:
            transaction_id (str): the transaction to wait for
            timeout (int): maximum number of rounds to wait    
        Returns:
            dict: pending transaction information, or throws an error if the transaction
                is not confirmed or rejected in the next timeout rounds
        """
        start_round = client.status()["last-round"] + 1;
        current_round = start_round

        while current_round < start_round + timeout:
            try:
                pending_txn = client.pending_transaction_info(transaction_id)
            except Exception:
                return 
            if pending_txn.get("confirmed-round", 0) > 0:
                return pending_txn
            elif pending_txn["pool-error"]:  
                raise Exception(
                    'pool error: {}'.format(pending_txn["pool-error"]))
            client.status_after_block(current_round)                   
            current_round += 1
        raise Exception(
            'pending tx not found in timeout rounds, timeout value = : {}'.format(timeout))

    ```

=== "Java"
    ```java 
    /**
     * utility function to wait on a transaction to be confirmed
     * the timeout parameter indicates how many rounds do you wish to check pending transactions for
     */
    public PendingTransactionResponse waitForConfirmation(AlgodClient myclient, String txID, Integer timeout)
    throws Exception {
        if (myclient == null || txID == null || timeout < 0) {
            throw new IllegalArgumentException("Bad arguments for waitForConfirmation.");
        }
        Response < NodeStatusResponse > resp = myclient.GetStatus().execute();
        if (!resp.isSuccessful()) {
            throw new Exception(resp.message());
        }
        NodeStatusResponse nodeStatusResponse = resp.body();
        Long startRound = nodeStatusResponse.lastRound + 1;
        Long currentRound = startRound;
        while (currentRound < (startRound + timeout)) {
            // Check the pending transactions                 
            Response < PendingTransactionResponse > resp2 = myclient.PendingTransactionInformation(txID).execute();
            if (resp2.isSuccessful()) {
                PendingTransactionResponse pendingInfo = resp2.body();
                if (pendingInfo != null) {
                    if (pendingInfo.confirmedRound != null && pendingInfo.confirmedRound > 0) {
                        // Got the completed Transaction
                        return pendingInfo;
                    }
                    if (pendingInfo.poolError != null && pendingInfo.poolError.length() > 0) {
                        // If there was a pool error, then the transaction has been rejected!
                        throw new Exception("The transaction has been rejected with a pool error: " + pendingInfo.poolError);
                    }
                }
            }
            resp = myclient.WaitForBlock(currentRound).execute();
            if (!resp.isSuccessful()) {
                throw new Exception(resp.message());
            }
            currentRound++;
        }
        throw new Exception("Transaction not confirmed after " + timeout + " rounds!");
    }
    ```

=== "Go"
    ```go 
    // Function that waits for a given txId to be confirmed by the network
    func waitForConfirmation(txID string, client *algod.Client, timeout uint64) (models.PendingTransactionInfoResponse, error) {
        pt := new(models.PendingTransactionInfoResponse)
        if client == nil || txID == "" || timeout < 0 {
            fmt.Printf("Bad arguments for waitForConfirmation")
            var msg = errors.New("Bad arguments for waitForConfirmation")
            return *pt, msg

        }

        status, err := client.Status().Do(context.Background())
        if err != nil {
            fmt.Printf("error getting algod status: %s\n", err)
            var msg = errors.New(strings.Join([]string{"error getting algod status: "}, err.Error()))
            return *pt, msg
        }
        startRound := status.LastRound + 1
        currentRound := startRound

        for currentRound < (startRound + timeout) {

            *pt, _, err = client.PendingTransactionInformation(txID).Do(context.Background())
            if err != nil {
                fmt.Printf("error getting pending transaction: %s\n", err)
                var msg = errors.New(strings.Join([]string{"error getting pending transaction: "}, err.Error()))
                return *pt, msg
            }
            if pt.ConfirmedRound > 0 {
                fmt.Printf("Transaction "+txID+" confirmed in round %d\n", pt.ConfirmedRound)
                return *pt, nil
            }
            if pt.PoolError != "" {
                fmt.Printf("There was a pool error, then the transaction has been rejected!")
                var msg = errors.New("There was a pool error, then the transaction has been rejected")
                return *pt, msg
            }
            fmt.Printf("waiting for confirmation\n")
            status, err = client.StatusAfterBlock(currentRound).Do(context.Background())
            currentRound++
        }
        msg := errors.New("Tx not found in round range")
        return *pt, msg
    }
    ```

=== "cURL"
    ```bash 
    curl -i -X GET \
       -H "X-Algo-API-Token:<algod-token>" \
     'http://<algod-address>:<algod-port>/v2/transactions/pending/<txid>'
    ```

=== "goal"
    ```bash 
    $ goal clerk rawsend --filename="hello-world.stxn"
    Sent 1000000 MicroAlgos from account [ADDRESS] to address GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A, transaction ID: [TXID]. Fee set to 1000
    Transaction [TXID] still pending as of round [LAST_ROUND]
    Transaction [TXID] committed in round [COMMITTED_ROUND]

    # Or construct, sign, and submit in one line
    $ goal clerk send --from=<my-account> --to=GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A --fee=1000 --amount=1000000 --note="Hello World"
    Sent 1000000 MicroAlgos from account [ADDRESS] to address GD64YIY3TWGDMCNPP553DZPPR6LDUSFQOIJVFDPPXWEG3FVOJCCDBBHU5A, transaction ID: [TXID]. Fee set to 1000
    Transaction [TXID] still pending as of round [LAST_ROUND]
    Transaction [TXID] committed in round [COMMITTED_ROUND]
    ```

# Read the transaction from the blockchain

Read your transaction back from the blockchain. 

!!! info
    Although you can read any transaction on the blockchain, only archival nodes store the whole history. By default, most nodes store only the last 1000 rounds and the APIs return errors when calling for information from earlier rounds. If you need to access data further back, make sure your algod client is connected to an archival, indexer node. Read more about node configurations in the Network Participation Guide or reach out to your service provider to understand how their node is configured. 

=== "JavaScript"
    ```js 
        // Wait for confirmation
        let confirmedTxn = await waitForConfirmation(algodClient, txId, 4);
        //Get the completed Transaction
        console.log("Transaction " + txId + " confirmed in round " + confirmedTxn["confirmed-round"]);
        let mytxinfo = JSON.stringify(confirmedTxn.txn.txn, undefined, 2);
        console.log("Transaction information: %o", mytxinfo);
        var string = new TextDecoder().decode(confirmedTxn.txn.txn.note);
        console.log("Note field: ", string);
    ```

=== "Python"
    ```python 
        import base64

        # wait for confirmation	
        try:
            confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
        except Exception as err:
            print(err)
            return

        print("Transaction information: {}".format(
            json.dumps(confirmed_txn, indent=4)))
        print("Decoded note: {}".format(base64.b64decode(
            confirmed_txn["txn"]["txn"]["note"]).decode()))
    ```

=== "Java"
    ```java 
        // Wait for transaction confirmation
        PendingTransactionResponse pTrx = waitForConfirmation(client, id, 4);

        System.out.println("Transaction " + id + " confirmed in round " + pTrx.confirmedRound);
        // Read the transaction
        JSONObject jsonObj = new JSONObject(pTrx.toString());
        System.out.println("Transaction information (with notes): " + jsonObj.toString(2));
        System.out.println("Decoded note: " + new String(pTrx.txn.tx.note));
        printBalance(myAccount);
    ```

=== "Go"
    ```go 
        // Wait for confirmation
        confirmedTxn, err := waitForConfirmation(txID, algodClient, 4)
        if err != nil {
            fmt.Printf("Error waiting for confirmation on txID: %s\n", txID)
            return
        }
        txnJSON, err := json.MarshalIndent(confirmedTxn.Transaction.Txn, "", "\t")
        if err != nil {
            fmt.Printf("Can not marshall txn data: %s\n", err)
        }
        fmt.Printf("Transaction information: %s\n", txnJSON)

        fmt.Printf("Decoded note: %s\n", string(confirmedTxn.Transaction.Txn.Note))
    ```

=== "cURL"
    ```bash 
    curl -i -X GET \
       -H "X-Algo-API-Token:<algod-token>" \
     'http://<algod-address>:<port>/v2/account/<my-address>/transaction/<txid>'
    ```

Notice above the pattern of constructing a transaction, authorizing it, submitting it to the network, and confirming its inclusion in a block. This is a framework to familiarize yourself with as it appears often in blockchain-related development.

!!! info
    Example code snippets were provided throughout this page. Full running code examples for each SDK are available within the GitHub repo at [/examples/start_building](https://github.com/algorand/docs/tree/master/examples/start_building) and for [download](https://github.com/algorand/docs/blob/master/examples/start_building/start_building.zip?raw=true) (.zip).

