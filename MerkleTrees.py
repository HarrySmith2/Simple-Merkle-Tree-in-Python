# 0. Import the needed library
import hashlib,json
from collections import OrderedDict

# 1. Declare the class trees
class MerkelTree:

    # 2. Initiate the class object
    def __init__(self,listOfTransaction=None):
        self.listOfTransaction = listOfTransaction
        self.pastTransaction = OrderedDict()

    # 3. Create the Merkle Tree  
    def createTree(self):

        # 3.0 Continue on the declaration
        listOfTransaction = self.listOfTransaction
        pastTransaction = self.pastTransaction
        tempTransaction = []

        # 3.1 For each transaction in list of Transactions
        for index in range(0,len(listOfTransaction),2):


            # 3.2 Get the left most (last) element of transaction list
            current = listOfTransaction[index]
            print ("-"*10)
            print ("Current Value = "+current)
            

            # 3.3 If there is still an index left, get the right of the left most element
            if index+1 != len(listOfTransaction):
                currentRight = listOfTransaction[index+1]
                

            # 3.4 If we reached the limit of the list then make a empty string
            else:
                currentRight = ''
            print("current Right Value = " + currentRight)
            

            # 3.5 Apply sha256 Hash function to the current values
            currentHash = hashlib.sha256((current).encode())
            

            # 3.6 If the current right hash is not a '' <- empty string
            # 3.6.1 sha256 Hash the currentRight string.
            if currentRight != '':
                currentRightHash = hashlib.sha256((currentRight).encode())

            # 3.7 Add the Transaction to the dictionary 
            pastTransaction[listOfTransaction[index]] = currentHash.hexdigest()
            print ("Current hash = "+ pastTransaction[listOfTransaction[index]])

            # 3.8 If the next right is not empty
            if currentRight != '':
                pastTransaction[listOfTransaction[index+1]] = currentRightHash.hexdigest()
                print("Current Right Hash = "+ pastTransaction[listOfTransaction[index+1]])

            # 3.9 Create the new list of transaction
            if currentRight != '':
                tempTransaction.append(currentHash.hexdigest() + currentRightHash.hexdigest())

            # 3.01 If the left most is an empty string then only add the current value
            else:
                tempTransaction.append(currentHash.hexdigest())

        # 3.02 Update the variables and rerun the function again 
        if len(listOfTransaction) != 1:

            self.listOfTransaction = tempTransaction
            self.pastTransaction = pastTransaction

            # 3.03 Call the function repeatly again and again until we get the root 
            self.createTree()

    # 4. Return the past Transaction 
    def getPastTransaction(self):
        return self.pastTransaction

    # 5. Get the root of the transaction
    def getRootLeaf(self):
        lastKey = list(self.pastTransaction.keys())[-1]
        return self.pastTransaction[lastKey]

# Declare the main part of the function to run
if __name__ == "__main__":

    # a) Create the new class of Jae_MerkTree
    TxTree = MerkelTree()

    # b) Give list of transaction
    transaction = ['tx1','tx2','tx3','tx4']

    # c) pass on the transaction list 
    TxTree.listOfTransaction = transaction

    # d) Create the Merkle Tree transaction
    TxTree.createTree()

    # e) Retrieve the transaction 
    pastTransaction = TxTree.getPastTransaction()

    # f) Get the last transaction and print all 
    print ("\n---- Proof Merkel Tree implementation is correct ----\n")
    print ('Root(top) of the tree : ',TxTree.getRootLeaf())

    # -- Proof Merkel Tree implementation is correct --
    
    # g) Print hash value of tx1+tx2
    print ("Hash of tx1 and tx2:")
    print (pastTransaction[pastTransaction['tx1']+pastTransaction['tx2']])
        # h) Print hash value of tx3+tx3
    print ("Hash of tx3 and tx4:")
    print (pastTransaction[pastTransaction['tx3']+pastTransaction['tx4']])
    # j) Prints hash of tx1+tx2 and tx3+tx4
    print ("Hash of root:")
    rootValue = pastTransaction[pastTransaction[pastTransaction['tx1']+pastTransaction['tx2']]+pastTransaction[pastTransaction['tx3']+pastTransaction['tx4']]]


    #print(json.dumps(pastTransaction, indent=4))
    print ("Comparing root of tree hash to hash of (tx1+tx2) + (tx3+tx4)...")
    if rootValue == TxTree.getRootLeaf():
            print (True)
    print ("-" * 50) 
