title: Your first transaction

This section is a quick start guide for interacting with the Algorand network using Python. This guide will help to install ***sandbox***, which provides a node for testing and development. This guide will also help to install the Python SDK, create an account and submit your first transaction on Algorand. 

# Alternative Guide

If you are a visual learner, try our submitting your first transaction live demo or watch a full video that explains the following steps.  
[`Try Live Demo`](https://replit.com/@Algorand/gettingStartedPython#main.py){target=_blank}   
[`Watch Full Video`](https://www.youtube.com/watch?v=ku2hFalMWmA){target=_blank}  

# Install Sandbox

!!! Prerequisites
    - Docker Compose ([install guide](https://docs.docker.com/compose/install/){target=_blank})
    - Git ([install guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git){target=_blank}) 

Algorand provides a docker instance for setting up a node, which can be used to get started developing quickly. To install and use this instance, follow these instructions.
​
```bash
git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up testnet
```
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=23){target=_blank}    
[`More Information`](https://developer.algorand.org/articles/introducing-sandbox-20/){target=_blank}    

This will install a Sandbox node connected to the Algorand TestNet. To read more about Algorand networks see [Algorand Networks](../../get-details/algorand-networks/index.md){target=_blank}. 
 
!!! Warning
    The sandbox installation may take a few minutes to startup in order to catch up to the current block round. To learn more about fast catchup, see [Sync Node Network using Fast Catchup](../../run-a-node/setup/install.md#sync-node-network-using-fast-catchup){target=_blank}

# Install SDK
Algorand provides an SDK for Python which is available as a pip package. To install the Python SDK, open a terminal and run the following command:
​
``` bash
pip3 install py-algorand-sdk
``` 
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=128){target=_blank}   ​

Alternatively, choose and download a [distribution file](https://pypi.org/project/py-algorand-sdk/#files){target=_blank}, and run

``` bash
pip3 install [file name].
``` 

The [GitHub repository](https://github.com/algorand/py-algorand-sdk){target=_blank} contains additional documentation and examples.

See the Python SDK [reference documentation](https://py-algorand-sdk.readthedocs.io/en/latest/){target=_blank} for more information on methods.  
​
The SDK is installed and can now interact with the Sandbox created earlier.​ 

# Create an Account on Algorand
In order to interact with the Algorand blockchain, you must have a funded account. To quickly create a test account use the following code.
​
```python
from algosdk import account, mnemonic

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
```
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=161){target=_blank}    
[`More Information`](../../get-details/accounts/create.md#standalone){target=_blank}  

!!! Tip
    Make sure to save your account's address and passphrase in a seperate place, as they will be used later on.
​
!!! Warning
    Never share mnemonic and private key. Production environments require stringent private key management. For more information on key management in community Wallets, click [here](https://developer.algorand.org/docs/community/#wallets){target=_blank}. For the [Algorand open source wallet](https://developer.algorand.org/articles/algorand-wallet-now-open-source/){target=_blank}, click [here](https://github.com/algorand/algorand-wallet){target=_blank}.

# Fund the Account
Before sending transactions to the Algorand network, the account must be funded to cover the minimal transaction fees that exist on Algorand. To fund the account use the [Algorand faucet](https://dispenser.testnet.aws.algodev.network/){target=_blank}. 
​
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=257){target=_blank}    
​
!!! Info
    All Algorand accounts require a minimum balance to be registered in the ledger. To read more about Algorand minimum balance, see [Account Overview](../../get-details/accounts/index.md#minimum-balance){target=_blank}.  

# Connect Your Client
Client must be instantiated prior to making calls to the API endpoints. You must provide values for `<algod-address>` and `<algod-token>`. The CLI tools implement the client natively. By default, the `algod_token` for each [sandbox](https://github.com/algorand/sandbox) is set to its `aaa...` value and the `algod_address` corresponds to `http://localhost:4001`.

Code beyond this point will be put into the ***first_transaction_example*** function to create a single script.

```python
from algosdk.v2client import algod

def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)
```
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=322){target=_blank}  

!!! Info
    The example code connects to the sandbox Algod client. If you want to connect to a Purestake client, see Purestake's [code samples](https://developer.purestake.io/code-samples){target=_blank}.

# Check Your Balance
Before moving on to the next step, make sure your account has been funded by the faucet.

```python
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
```
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=381){target=_blank}  

# Build First Transaction
Transactions are used to interact with the Algorand network. To create a payment transaction use the following code.
​
```python
# build transaction
from algosdk import transaction
from algosdk import constants


    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE 
    receiver = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
    note = "Hello World".encode()
	amount = 1000000
    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)
```
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=398){target=_blank}  
​
!!! Info
    Algorand supports many transaction types. To see what types are supported see [Transactions](../../get-details/transactions/index.md#transaction-types){target=_blank}. 

# Sign First Transaction
Before the transaction is considered valid, it must be signed by a private key. Use the following code to sign the transaction.
​
```python
	# sign transaction
    signed_txn = unsigned_txn.sign(private_key)
``` 
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=454){target=_blank}  
​
!!! Info
    Algorand provides many ways to sign transactions. To see other ways see [Authorization](../../get-details/transactions/signatures.md#single-signatures){target=_blank}. 
    
# Submit the Transaction
The signed transaction can now be submitted to the network. `wait_for_confirmation` SDK Method is called after the transaction is submitted to wait until the transaction is broadcast to the Algorand blockchain and is confirmed. 
​
```python
import json
import base64


    #submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation	
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
	print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
	print("Amount transfered: {} microAlgos".format(amount) )    
	print("Fee: {} microAlgos".format(params.fee) ) 


	account_info = algod_client.account_info(my_address)
	print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
    
```

[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=480){target=_blank}  

# Complete Example
The complete example below illustrates how to quickly submit your first transaction.
​
```python
import json
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk import transaction


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

# Write down the address, private key, and the passphrase for later usage
generate_algorand_keypair()

def first_transaction_example(private_key, my_address):
	algod_address = "http://localhost:4001"
	algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	algod_client = algod.AlgodClient(algod_token, algod_address)

	print("My address: {}".format(my_address))
	account_info = algod_client.account_info(my_address)
	print("Account balance: {} microAlgos".format(account_info.get('amount')))

	# build transaction
	params = algod_client.suggested_params()
	# comment out the next two (2) lines to use suggested fees
	params.flat_fee = constants.MIN_TXN_FEE 
	params.fee = 1000
	receiver = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
	amount = 100000
	note = "Hello World".encode()

	unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

	# sign transaction
	signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
	txid = algod_client.send_transaction(signed_txn)
	print("Signed transaction with txID: {}".format(txid))

    # wait for confirmation	
	try:
		confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
	except Exception as err:
		print(err)
		return

	print("Transaction information: {}".format(
		json.dumps(confirmed_txn, indent=4)))
	print("Decoded note: {}".format(base64.b64decode(
		confirmed_txn["txn"]["txn"]["note"]).decode()))
    
	print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
	print("Amount transfered: {} microAlgos".format(amount) )    
	print("Fee: {} microAlgos".format(params.fee) ) 


	account_info = algod_client.account_info(my_address)
	print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")



# replace private_key and my_address with your private key and your address.
first_transaction_example(private_key, my_address)​
```
[`Run Code`](https://replit.com/@Algorand/gettingStartedPython#main.py){target=_blank}    
[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=556){target=_blank}    
[`Go to Github`](https://github.com/algorand/docs/blob/staging/examples/start_building/v2/python/your_first_transaction.py){target=_blank}  
​​
!!! Warning 
    In order for this transaction to be successful, the account must be funded. 

# View the Transaction
To view the transaction, open [AlgoExplorer](https://testnet.algoexplorer.io/){target=_blank} or [Goal Seeker](https://goalseeker.purestake.io/algorand/testnet){target=_blank} and paste the transaction ID into the search bar.  

[`Watch Video`](https://youtu.be/ku2hFalMWmA?t=618){target=_blank}   

# Set Up Your Editor/Framework
The Algorand community provides many editors, frameworks, and plugins that can be used to work with the Algorand Network. Tutorials have been created for configuring each of these for use with Algorand. Select your Editor preference below.  

* [Setting Up VSCode](https://developer.algorand.org/tutorials/vs-code-javascript/){target=_blank}  
* [AlgoDEA IntelliJ Plugin](https://developer.algorand.org/articles/making-development-easier-algodea-intellij-plugin/){target=_blank}  
* [Algorand Builder Framework](https://developer.algorand.org/articles/introducing-algorand-builder/){target=_blank}  
