import streamlit as st
import time
from mcq_parser import parse_questions
from game_state import GameState

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = GameState()
if 'game_active' not in st.session_state:
    st.session_state.game_active = False
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'questions' not in st.session_state:
    st.session_state.questions = []

def load_questions():
    # Your MCQ text content - you can also load this from a file
    mcq_text = """What is a blockchain?
a) A centralized database
b) A continuously growing list of records called blocks
c) A type of cryptocurrency
d) A network of computers
Answer: b) A continuously growing list of records called blocks


What is the primary purpose of a blockchain?
a) To create digital currencies
b) To store data in a centralized manner
c) To provide a secure and immutable ledger of transactions
d) To eliminate the need for encryption
Answer: c) To provide a secure and immutable ledger of transactions


Which of the following is a characteristic of public blockchains?
a) They are owned by a single organization
b) They require permission to access
c) They are open and accessible to anyone
d) They are not decentralized
Answer: c) They are open and accessible to anyone


What is the role of miners in a blockchain network?
a) To store data
b) To validate transactions and create new blocks
c) To manage user accounts
d) To control the network
Answer: b) To validate transactions and create new blocks


What is a smart contract?
a) A traditional legal contract
b) A self-executing contract with terms written in code
c) A type of cryptocurrency
d) A method for securing data
Answer: b) A self-executing contract with terms written in code


What is the main advantage of using a decentralized network?
a) Increased control by a single entity
b) Reduced risk of single points of failure
c) Higher transaction costs
d) Slower transaction speeds
Answer: b) Reduced risk of single points of failure


Which consensus mechanism is commonly used in Bitcoin?
a) Proof of Stake
b) Proof of Work
c) Delegated Proof of Stake
d) Byzantine Fault Tolerance
Answer: b) Proof of Work


What is the purpose of a hash function in blockchain?
a) To encrypt data
b) To create a unique identifier for data
c) To store data
d) To manage user permissions
Answer: b) To create a unique identifier for data


What is the first block in a blockchain called?
a) Parent Block
b) Child Block
c) Genesis Block
d) Root Block
Answer: c) Genesis Block


What is the significance of the target hash in mining?
a) It indicates the transaction fee
b) It determines the difficulty of mining a new block
c) It is used to identify users
d) It stores transaction data
Answer: b) It determines the difficulty of mining a new block


What is a Merkle Tree used for in blockchain?
a) To store user data
b) To verify the integrity of transactions
c) To manage network security
d) To create new blocks
Answer: b) To verify the integrity of transactions


Which of the following is a disadvantage of public blockchains?
a) Lack of transparency
b) High transaction speed
c) Vulnerability to attacks
d) Centralized control
Answer: c) Vulnerability to attacks


What is the main challenge of maintaining a blockchain?
a) High transaction costs
b) Balancing security, scalability, and decentralization
c) Lack of user adoption
d) Centralized control
Answer: b) Balancing security, scalability, and decentralization


What is the role of a lightweight node?
a) To store a complete copy of the blockchain
b) To validate transactions
c) To connect to the network without storing the entire blockchain
d) To increase transaction fees
Answer: c) To connect to the network without storing the entire blockchain


What is the primary function of the Ethereum Virtual Machine (EVM)?
a) To store transaction data
b) To execute smart contracts
c) To validate transactions
d) To increase transaction costs
Answer: b) To execute smart contracts


What is the main benefit of using a hybrid blockchain?
a) Centralized control
b) Increased transaction costs
c) Combining the advantages of both public and private blockchains
d) Slower transaction speeds
Answer: c) Combining the advantages of both public and private blockchains


What is the significance of the longest chain rule in blockchain?
a) It determines the transaction fees
b) It ensures all participants agree on the same chain of blocks
c) It connects blocks together
d) It stores transaction data
Answer: b) It ensures all participants agree on the same chain of blocks


What is a disadvantage of using Proof of Work?
a) Vulnerability to 51% attacks
b) High transaction speed
c) Low energy consumption
d) Centralized control
Answer: a) Vulnerability to 51% attacks


Which of the following is a type of Proof of Stake?
a) Regular Proof of Stake
b) Proof of Work
c) Delegated Proof of Work
d) Byzantine Fault Tolerance
Answer: a) Regular Proof of Stake


What is the primary purpose of cryptographic protocols in blockchain?
a) To secure transactions and data integrity
b) To manage user accounts
c) To increase transaction fees
d) To eliminate the need for contracts
Answer: a) To secure transactions and data integrity

What is a block in a blockchain?
a) A single transaction
b) A collection of transactions
c) A type of cryptocurrency
d) A central database
Answer: b) A collection of transactions


What is the main purpose of a consensus algorithm?
a) To increase transaction fees
b) To ensure agreement among nodes on the state of the blockchain
c) To store user data
d) To manage network security
Answer: b) To ensure agreement among nodes on the state of the blockchain


What is the primary function of mining in blockchain?
a) To create new cryptocurrencies
b) To validate transactions and add them to the blockchain
c) To manage user accounts
d) To increase transaction costs
Answer: b) To validate transactions and add them to the blockchain


What is the main challenge of Proof of Work?
a) High transaction speed
b) High energy consumption
c) Centralized control
d) Lack of transparency
Answer: b) High energy consumption


What does the term "block propagation" refer to?
a) The process of creating new blocks
b) The distribution of blocks across the network
c) The validation of transactions
d) The storage of user data
Answer: b) The distribution of blocks across the network


What is the purpose of a mining pool?
a) To centralize mining operations
b) To combine resources for more efficient mining
c) To eliminate transaction fees
d) To manage user accounts
Answer: b) To combine resources for more efficient mining


What is the main advantage of using a GPU for mining?
a) Lower energy consumption
b) Higher processing power for complex calculations
c) Easier to set up than a CPU
d) Lower cost
Answer: b) Higher processing power for complex calculations


What is the significance of the block size in a blockchain?
a) It determines the transaction fees
b) It affects the speed of transaction processing
c) It controls the number of miners
d) It stores user data
Answer: b) It affects the speed of transaction processing


What is the primary function of a transaction in a blockchain?
a) To create new blocks
b) To store user data
c) To transfer value between parties
d) To manage network security
Answer: c) To transfer value between parties


What is the role of a full node in a blockchain network?
a) To store a complete copy of the blockchain
b) To validate transactions
c) To manage user accounts
d) To increase transaction fees
Answer: a) To store a complete copy of the blockchain



What is a disadvantage of using a private blockchain?
a) Lack of transparency
b) High transaction speed
c) c) Increased security
d) Lower transaction costs
Answer: a) Lack of transparency



What is the main purpose of a Merkle Tree in blockchain?
a) To store user data
b) To verify the integrity of transactions
c) To increase transaction fees
d) To manage network security
Answer: b) To verify the integrity of transactions


What is the significance of the Genesis Block in a blockchain?
a) It is the last block in the chain
b) It is the first block in the blockchain
c) It contains the highest transaction fees
d) It is the most secure block
Answer: b) It is the first block in the blockchain


What does the term "block relay" refer to in blockchain networks?
a) The process of creating new blocks
b) The distribution of transaction information between nodes
c) The validation of transactions
d) The storage of user data
Answer: b) The distribution of transaction information between nodes


What is the primary benefit of using blockchain technology in trade finance?
a) Increased paperwork
b) Slower transaction speeds
c) Streamlined processes and reduced documentation
d) Centralized control
Answer: c) Streamlined processes and reduced documentation


How does blockchain technology help in combating money laundering?
a) By increasing transaction fees
b) By providing a transparent record of transactions
c) By eliminating the need for audits
d) By centralizing financial records
Answer: b) By providing a transparent record of transactions


What is the role of a digital signature in blockchain transactions?
a) To increase transaction fees
b) To verify the authenticity of the transaction
c) To store user data
d) To manage network security
Answer: b) To verify the authenticity of the transaction


What is a key characteristic of public blockchains?
a) They are controlled by a single entity
b) They are accessible to anyone
c) They have high transaction fees
d) They are not transparent
Answer: b) They are accessible to anyone


What is the main advantage of using a decentralized network in blockchain?
a) Increased control by a central authority
b) Reduced transaction speeds
c) Enhanced security and trust
d) Higher transaction costs
Answer: c) Enhanced security and trust


What is the purpose of using encryption in blockchain technology?
a) To increase transaction fees
b) To secure data and ensure privacy
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To secure data and ensure privacy

What is a hash function used for in blockchain?
a) To create new cryptocurrencies
b) To verify the integrity of data
c) To manage user accounts
d) To increase transaction fees
Answer: b) To verify the integrity of data


What is the main advantage of using digital signatures in blockchain?
a) They increase transaction costs
b) They provide proof of ownership and authenticity
c) They eliminate the need for contracts
d) They centralize control
Answer: b) They provide proof of ownership and authenticity


What does the term "51% attack" refer to in blockchain?
a) A method to increase transaction fees
b) A situation where a single entity controls the majority of the network's computational power
c) A type of digital signature
d) A method to validate transactions
Answer: b) A situation where a single entity controls the majority of the network's computational power


What is the purpose of key management in blockchain security?
a) To increase transaction fees
b) To manage user accounts
c) To secure cryptographic keys used for transactions
d) To eliminate the need for contracts
Answer: c) To secure cryptographic keys used for transactions


What is the primary function of a public key in blockchain?
a) To encrypt data
b) To verify digital signatures
c) To create new blocks
d) To manage user accounts
Answer: b) To verify digital signatures


What is the significance of the Nash Equilibrium in blockchain?
a) It determines transaction fees
b) It ensures that miners act in a way that is beneficial to the network
c) It manages user accounts
d) It increases transaction speeds
Answer: b) It ensures that miners act in a way that is beneficial to the network


What is the role of game theory in blockchain?
a) To increase transaction fees
b) To manage user accounts
c) To ensure that participants act in a way that maintains the integrity of the network
d) To eliminate the need for contracts
Answer: c) To ensure that participants act in a way that maintains the integrity of the network


What is the primary benefit of using blockchain technology for data storage?
a) Increased transaction fees
b) Enhanced security and immutability
c) Slower transaction speeds
d) Centralized control
Answer: b) Enhanced security and immutability


What is the main challenge associated with blockchain scalability?
a) High transaction speeds
b) Increased transaction costs
c) Maintaining security while increasing throughput
d) Centralized control
Answer: c) Maintaining security while increasing throughput


What is the purpose of redundancy in blockchain networks?
a) To increase transaction fees
b) To ensure data integrity and availability
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To ensure data integrity and availability



What is the purpose of a Merkle Tree in blockchain?
a) To increase transaction fees
b) To efficiently verify large sets of data
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To efficiently verify large sets of data


What is the primary function of a digital signature in blockchain transactions?
a) To encrypt data
b) To provide proof of authenticity and integrity
c) To create new blocks
d) To manage user accounts
Answer: b) To provide proof of authenticity and integrity


What does the term "immutability" refer to in the context of blockchain?
a) The ability to change data easily
b) The inability to alter data once it has been recorded
c) The speed of transaction processing
d) The centralization of control
Answer: b) The inability to alter data once it has been recorded


What is the role of consensus algorithms in blockchain?
a) To increase transaction fees
b) To ensure agreement among nodes on the validity of transactions
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To ensure agreement among nodes on the validity of transactions


What is the main advantage of using public key cryptography in blockchain?
a) It increases transaction fees
b) It allows for secure communication without sharing private keys
c) It eliminates the need for contracts
d) It centralizes control
Answer: b) It allows for secure communication without sharing private keys


What is the significance of the hash value in a blockchain?
a) It determines transaction fees
b) It connects blocks and ensures data integrity
c) It manages user accounts
d) It eliminates the need for contracts
Answer: b) It connects blocks and ensures data integrity


What is a potential weakness of blockchain technology?
a) High transaction speeds
b) Vulnerability to 51% attacks
c) Centralized control
d) Increased transaction costs
Answer: b) Vulnerability to 51% attacks


What is the purpose of transaction endorsement in blockchain?
a) To increase transaction fees
b) To ensure that transactions are validated by multiple parties
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To ensure that transactions are validated by multiple parties


How does blockchain technology enhance data privacy?
a) By centralizing data storage
b) By using cryptographic techniques to secure data
c) By increasing transaction fees
d) By eliminating the need for contracts
Answer: b) By using cryptographic techniques to secure data


What is the main benefit of using a decentralized network in blockchain?
a) Increased control by a central authority
b) Reduced transaction speeds
c) Enhanced security and trust
d) Higher transaction costs
Answer: c) Enhanced security and trust


What is the primary purpose of mining in blockchain?
a) To create new cryptocurrencies
b) To validate transactions and add them to the blockchain
c) To increase transaction fees
d) To manage user accounts
Answer: b) To validate transactions and add them to the blockchain


What is the "Proof-of-Work" consensus mechanism?
a) A method to increase transaction fees
b) A process that requires miners to solve complex mathematical problems
c) A way to manage user accounts
d) A method to eliminate the need for contracts
Answer: b) A process that requires miners to solve complex mathematical problems


What is a mining pool?
a) A group of miners who combine their resources to increase their chances of finding a block
b) A centralized authority that manages mining operations
c) A method to increase transaction fees
d) A way to eliminate the need for contracts
Answer: a) A group of miners who combine their resources to increase their chances of finding a block


What is the impact of CPU and GPU on mining?
a) They increase transaction fees
b) They determine the processing power available for mining
c) They manage user accounts
d) They eliminate the need for contracts
Answer: b) They determine the processing power available for mining


What is the main challenge of individual mining?
a) High transaction speeds
b) Low chances of successfully finding a block
c) Centralized control
d) Increased transaction costs
Answer: b) Low chances of successfully finding a block


What happens when a miner successfully finds a block?
a) They lose their investment
b) They receive a reward in the form of cryptocurrency
c) They must pay transaction fees
d) They are banned from the network
Answer: b) They receive a reward in the form of cryptocurrency


What is block propagation in the context of blockchain?
a) The process of increasing transaction fees
b) The distribution of new blocks to all nodes in the network
c) The management of user accounts
d) The elimination of the need for contracts
Answer: b) The distribution of new blocks to all nodes in the network


What is the role of transaction verification in the Bitcoin network?
a) To increase transaction fees
b) To ensure that inputs are valid and authorized
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To ensure that inputs are valid and authorized


What is the significance of the block relay in blockchain?
a) It increases transaction fees
b) It facilitates the communication of new blocks between nodes
c) It manages user accounts
d) It eliminates the need for contracts
Answer: b) It facilitates the communication of new blocks between nodes


What is the primary benefit of using mining pools?
a) Increased autonomy for individual miners
b) Higher chances of profitability through combined resources
c) Reduced transaction fees
d) Centralized control
Answer: b) Higher chances of profitability through combined resources



What is the main purpose of blockchain mining?
a) To increase transaction fees
b) To validate transactions and add them to the blockchain
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To validate transactions and add them to the blockchain


What is a mining pool?
a) A group of miners who combine their resources to increase the chances of finding a block
b) A centralized authority that manages mining activities
c) A type of cryptocurrency
d) A software used for mining
Answer: a) A group of miners who combine their resources to increase the chances of finding a block


What is the impact of CPU and GPU on mining?
a) They determine the processing power available for mining
b) They increase transaction fees
c) They manage user accounts
d) They eliminate the need for contracts
Answer: a) They determine the processing power available for mining


What is the significance of block propagation in blockchain?
a) It increases transaction fees
b) It facilitates the distribution of new blocks to all nodes in the network
c) It manages user accounts
d) It eliminates the need for contracts
Answer: b) It facilitates the distribution of new blocks to all nodes in the network


What is the role of transaction verification in the Bitcoin network?
a) To increase transaction fees
b) To ensure that inputs are valid and authorized
c) To manage user accounts
d) To eliminate the need for contracts
Answer: b) To ensure that inputs are valid and authorized


What happens when a miner successfully finds a block?
a) They lose their investment
b) They receive a reward in the form of cryptocurrency
c) They must pay transaction fees
d) They are banned from the network
Answer: b) They receive a reward in the form of cryptocurrency


What is the primary benefit of using mining pools?
a) Increased autonomy for individual miners
b) Higher chances of profitability through combined resources
c) Reduced transaction fees
d) Centralized control
Answer: b) Higher chances of profitability through combined resources


What is the main challenge of individual mining?
a) High transaction speeds
b) Low chances of successfully finding a block
c) Centralized control
d) Increased transaction costs
Answer: b) Low chances of successfully finding a block


What is the significance of the block relay in blockchain?
a) It increases transaction fees
b) It facilitates the communication of new blocks between nodes
c) It manages user accounts
d) It eliminates the need for contracts
Answer: b) It facilitates the communication of new blocks between nodes


How can blockchain technology improve transaction verification?
a) By increasing transaction fees
b) By ensuring that all transactions are recorded and validated by the network
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By ensuring that all transactions are recorded and validated by the network


What is one of the primary applications of blockchain in the automotive industry?
a) Increasing transaction fees
b) Enhancing supply chain traceability
c) Centralizing data storage
d) Eliminating the need for contracts
Answer: b) Enhancing supply chain traceability


How can blockchain technology improve international payments?
a) By increasing transaction fees
b) By providing a tamper-proof log of transactions
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By providing a tamper-proof log of transactions


What is a significant benefit of using blockchain in supply chain management?
a) Increased transaction speeds
b) Enhanced transparency and trust
c) Centralized control
d) Higher transaction costs
Answer: b) Enhanced transparency and trust


How can blockchain technology assist in healthcare?
a) By increasing transaction fees
b) By securely storing and sharing patient data
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By securely storing and sharing patient data


What is one of the advantages of using blockchain in voting systems?
a) Increased transaction fees
b) Enhanced security and accessibility
c) Centralized control
d) Higher transaction costs
Answer: b) Enhanced security and accessibility


How can blockchain technology help in tax payments?
a) By increasing transaction fees
b) By automating and streamlining the filing process
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By automating and streamlining the filing process


What is a potential application of blockchain in the energy sector?
a) Increasing transaction fees
b) Executing energy supply transactions and managing certificates
c) Centralizing data storage
d) Eliminating the need for contracts
Answer: b) Executing energy supply transactions and managing certificates


How can blockchain technology enhance cybersecurity?
a) By centralizing data storage
b) By removing the risk of a single point of failure
c) By increasing transaction fees
d) By eliminating the need for contracts
Answer: b) By removing the risk of a single point of failure



What is one of the primary applications of blockchain in the automotive industry?
a) Increasing transaction fees
b) Enhancing supply chain traceability
c) Centralizing data storage
d) Eliminating the need for contracts
Answer: b) Enhancing supply chain traceability


How can blockchain technology improve international payments?
a) By increasing transaction fees
b) By providing a tamper-proof log of transactions
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By providing a tamper-proof log of transactions


What is a significant benefit of using blockchain in supply chain management?
a) Increased transaction speeds
b) Enhanced transparency and trust
c) Centralized control
d) Higher transaction costs
Answer: b) Enhanced transparency and trust


How can blockchain technology assist in healthcare?
a) By increasing transaction fees
b) By securely storing and sharing patient data
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By securely storing and sharing patient data


What is one of the main benefits of using blockchain in voting systems?
a) Increased transaction fees
b) Enhanced security and accessibility
c) Centralized control
d) Higher transaction costs
Answer: b) Enhanced security and accessibility


How can blockchain technology help in tax payments?
a) By increasing transaction fees
b) By automating and streamlining the filing process
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By automating and streamlining the filing process


What is a potential application of blockchain in the energy sector?
a) Increasing transaction fees
b) Executing energy supply transactions and managing certificates
c) Centralizing data storage
d) Eliminating the need for contracts
Answer: b) Executing energy supply transactions and managing certificates


How can blockchain technology enhance cybersecurity?
a) By centralizing data storage
b) By removing the risk of a single point of failure
c) By increasing transaction fees
d) By eliminating the need for contracts
Answer: b) By removing the risk of a single point of failure


What is one of the main benefits of using blockchain in big data management?
a) Increased transaction fees
b) Enhanced data integrity and security
c) Centralized control
d) Higher transaction costs
Answer: b) Enhanced data integrity and security


How can blockchain technology improve peer-to-peer transactions?
a) By increasing transaction fees
b) By providing a secure and decentralized method for transactions
c) By managing user accounts
d) By eliminating the need for contracts
Answer: b) By providing a secure and decentralized method for transactions


Certainly! Here are 50 multiple-choice questions based on the provided blockchain content.

---

What is blockchain often referred to as?  
a) Decentralized System  
b) Distributed Ledger Technology  
c) Encrypted Currency  
d) Centralized Ledger  
Answer: b) Distributed Ledger Technology  

What is the main purpose of a Merkle Tree in blockchain?  
a) Storing transaction fees  
b) Efficient and secure data encoding  
c) Verifying digital signatures  
d) Increasing transaction speed  
Answer: b) Efficient and secure data encoding  

In a blockchain, what is the function of a "hash"?  
a) Identifying a unique block  
b) Storing transaction amounts  
c) Transferring data  
d) Determining block size  
Answer: a) Identifying a unique block  

Which is the first block in a blockchain called?  
a) Initial Block  
b) Genesis Block  
c) Root Block  
d) Ledger Block  
Answer: b) Genesis Block  

What mechanism in blockchain prevents tampering by requiring significant computing power?  
a) Proof of Identity  
b) Consensus Mechanism  
c) Proof of Work  
d) Hashing  
Answer: c) Proof of Work  

What role does a "nonce" play in Bitcoin mining?  
a) It initiates the mining process  
b) It stores transaction data  
c) It is used to meet difficulty requirements  
d) It increases transaction fees  
Answer: c) It is used to meet difficulty requirements  

Which of the following is a benefit of a public blockchain?  
a) High transaction speed  
b) Centralized control  
c) Full transparency and open participation  
d) Minimal energy usage  
Answer: c) Full transparency and open participation  

What distinguishes a private blockchain from a public blockchain?  
a) Only selected nodes can participate  
b) Higher transaction fees  
c) Faster transaction speeds  
d) Only limited data is stored  
Answer: a) Only selected nodes can participate  

Which type of blockchain combines elements of both public and private blockchains?  
a) Federated Blockchain  
b) Hybrid Blockchain  
c) Permissioned Blockchain  
d) Decentralized Blockchain  
Answer: b) Hybrid Blockchain  


What is the consensus mechanism used by Cardano?  
a) Proof of Identity  
b) Proof of Stake  
c) Proof of Work  
d) Delegated Proof of Stake  
Answer: b) Proof of Stake  


How does blockchain ensure data immutability?  
a) Using centralized control  
b) Through encryption alone  
c) By linking blocks with previous hashes  
d) By allowing only one block to be added per day  
Answer: c) By linking blocks with previous hashes  


What does a node receive for successfully mining a block in Bitcoin?  
a) Mining Tax  
b) Transaction Fee  
c) Block Reward  
d) Gas Fee  
Answer: c) Block Reward  


What is the purpose of the timestamp in a blockchain block?  
a) To control access  
b) To identify the creator  
c) To track block creation time  
d) To increase security  
Answer: c) To track block creation time  


In which type of blockchain is there no need for central authority?  
a) Private Blockchain  
b) Public Blockchain  
c) Semi-private Blockchain  
d) Sidechain  
Answer: b) Public Blockchain  


Which blockchain is best suited for high privacy and security within an organization?  
a) Private Blockchain  
b) Public Blockchain  
c) Hybrid Blockchain  
d) Consortium Blockchain  
Answer: a) Private Blockchain  


What is Ethereum mainly known for?  
a) Peer-to-peer lending  
b) Running decentralized applications  
c) Storing medical data  
d) Hosting private servers  
Answer: b) Running decentralized applications  


Which type of blockchain allows multiple organizations to participate and verify transactions?  
a) Hybrid Blockchain  
b) Private Blockchain  
c) Consortium Blockchain  
d) Semi-private Blockchain  
Answer: c) Consortium Blockchain  


What is a smart contract?  
a) A digital payment gateway  
b) A self-executing contract with specific rules  
c) A blockchain-based ID system  
d) A data compression tool  
Answer: b) A self-executing contract with specific rules  


What technology powers cryptocurrency transactions?  
a) VPN  
b) Blockchain  
c) Cloud Computing  
d) Big Data Analytics  
Answer: b) Blockchain  


Who is the creator of Bitcoin?  
a) Steve Jobs  
b) Vitalik Buterin  
c) Charles Hoskinson  
d) Satoshi Nakamoto  
Answer: d) Satoshi Nakamoto  


What is a sidechain?  
a) A backup for the main blockchain  
b) An independent blockchain connected to the main network  
c) A part of the public blockchain  
d) A tool for securing nodes  
Answer: b) An independent blockchain connected to the main network  


Which of the following is an example of a proof-of-stake blockchain?  
a) Bitcoin  
b) Ethereum Classic  
c) Cardano  
d) Litecoin  
Answer: c) Cardano  


What is the purpose of "mining pools" in blockchain?  
a) To distribute blockchain access  
b) To enhance transaction speed  
c) To increase miners' chances of validating a block  
d) To reduce energy consumption  
Answer: c) To increase miners' chances of validating a block  


Which part of a block verifies the integrity of all transactions in it?  
a) Timestamp  
b) Nonce  
c) Merkle Root  
d) Genesis Block  
Answer: c) Merkle Root  


Which of the following blockchains is fully decentralized?  
a) Hyperledger  
b) Ripple  
c) Bitcoin  
d) Corda  
Answer: c) Bitcoin  


What does DLT stand for in blockchain?  
a) Digital Ledger Technology  
b) Distributed Ledger Technology  
c) Direct Ledger Technology  
d) Decentralized Ledger Technology  
Answer: b) Distributed Ledger Technology  


What does "P2P" mean in blockchain?  
a) Password to Password  
b) Peer to Peer  
c) Public to Private  
d) Private to Private  
Answer: b) Peer to Peer  


In proof-of-work, what determines the difficulty of mining a block?  
a) Transaction volume  
b) Number of nodes  
c) Hash value complexity  
d) Network capacity  
Answer: c) Hash value complexity  


What type of blockchain is Ethereum?  
a) Private  
b) Permissioned  
c) Public  
d) Consortium  
Answer: c) Public  


What is the main disadvantage of Proof of Work (PoW)?  
a) Requires little energy  
b) High energy consumption  
c) Lack of security  
d) Centralization risk  
Answer: b) High energy consumption  


Which component of a block contains the hash of the previous block?  
a) Block Header  
b) Nonce  
c) Merkle Root  
d) Genesis Block  
Answer: a) Block Header  


Which blockchain consensus mechanism is more energy-efficient?  
a) Proof of Stake  
b) Proof of Identity  
c) Proof of Work  
d) Proof of Authority  
Answer: a) Proof of Stake  


What is a major advantage of using smart contracts?  
a) They eliminate all costs  
b) They are immune to bugs  
c) They automatically execute terms  
d) They can be altered at will  
Answer: c) They automatically execute terms  


Which of these blockchain types is most suitable for a healthcare system with patient data privacy needs?  
a) Public Blockchain  
b) Hybrid Blockchain  
c) Sidechain  
d) Private Blockchain  
Answer: d) Private Blockchain  


What is "Proof of Authority" primarily used for?  
a) Public blockchains  
b) Energy-efficient blockchains  
c) Private or permissioned blockchains  
d) Cryptocurrency wallets  
Answer: c) Private or permissioned blockchains  


What does a node do in a blockchain network?  
a) Stores part of the ledger  
b) Controls transaction fees  
c) Initiates smart contracts  
d) Transfers cryptocurrencies only  
Answer: a) Stores part of the ledger  


Which type of blockchain is best suited for use cases requiring both privacy and public access?  
a) Public Blockchain  
b) Private Blockchain  
c) Hybrid Blockchain  
d) Sidechain  
Answer: c) Hybrid Blockchain  


What is Bitcoin often referred to as?  
a) Digital Cash  
b) Centralized Cryptocurrency  
c) Open Ledger  
d) Block Header  
Answer: a) Digital Cash  


What is a primary feature of permissionless blockchains?  
a) High energy efficiency  
b) Complete central authority  
c) Open participation for everyone  
d) Limited transaction scope  
Answer: c) Open participation for everyone  


Which of the following is NOT a type of blockchain?  
a) Consortium Blockchain  
b) Private Blockchain  
c) Permissioned Blockchain  
d) Data Blockchain  
Answer: d) Data Blockchain  


What does the term "immutable" mean in blockchain?  
a) Tamper-resistant  
b) Easily editable  
c) Interchangeable  
d) Encrypted  
Answer: a) Tamper-resistant  


Which cryptocurrency is known for using a proof-of-work mechanism?  
a) Cardano  
b) Ethereum 2.0  
c) Bitcoin  
d) Ripple  
Answer: c) Bitcoin  


Which of these is a disadvantage of private blockchains?  
a) Slower transaction times  
b) Higher privacy concerns  
c) Risk of centralization  
d) Low transparency  
Answer: c) Risk of centralization
"""  # Add your full question set here
    
    return parse_questions(mcq_text)

def start_new_game():
    st.session_state.game_state.prepare_questions(st.session_state.questions)
    st.session_state.game_active = True
    st.session_state.show_result = False

def main():
    st.set_page_config(
        page_title="Blockchain MCQ Game",
        page_icon="🎮",
        layout="centered"
    )
    
    st.title("🎮 Blockchain MCQ Game")
    
    # Load questions if not already loaded
    if not st.session_state.questions:
        st.session_state.questions = load_questions()
    
    if not st.session_state.game_active:
        st.write("Welcome to the Blockchain MCQ Game!")
        st.write("Test your knowledge of blockchain technology with our interactive quiz.")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Start New Game", key="start"):
                start_new_game()
        with col2:
            if st.button("View Statistics", key="stats"):
                st.session_state.show_result = True
    
    if st.session_state.show_result:
        st.subheader("📊 Game Statistics")
        st.write(f"Total Games Played: {st.session_state.game_state.games_played}")
        if st.session_state.game_state.games_played > 0:
            avg_score = (st.session_state.game_state.total_score / st.session_state.game_state.games_played) * 100
            st.write(f"Average Score: {avg_score:.1f}%")
        
        if st.button("Back to Menu"):
            st.session_state.show_result = False
    
    elif st.session_state.game_active:
        current_question = st.session_state.game_state.get_current_question()
        
        if current_question:
            st.subheader(f"Question {st.session_state.game_state.current_question_index + 1}/{st.session_state.game_state.total_questions}")
            st.write(current_question['question'])
            
            # Create radio buttons for options
            user_answer = st.radio(
                "Select your answer:",
                ['a', 'b', 'c', 'd'],
                format_func=lambda x: f"{x}) {current_question['options'][ord(x) - ord('a')]}"
            )
            
            if st.button("Submit Answer"):
                is_correct = st.session_state.game_state.check_answer(user_answer)
                
                if is_correct:
                    st.success("✅ Correct!")
                else:
                    correct_option = current_question['options'][ord(current_question['answer']) - ord('a')]
                    st.error(f"❌ Wrong! The correct answer was {current_question['answer']}) {correct_option}")
                
                time.sleep(1)
                st.session_state.game_state.next_question()
                st.experimental_rerun()
        
        if st.session_state.game_state.is_game_over():
            st.session_state.game_state.finish_game()
            score_percentage = (st.session_state.game_state.current_score / st.session_state.game_state.total_questions) * 100
            
            st.subheader("🎯 Round Complete!")
            st.write(f"Your score: {st.session_state.game_state.current_score}/{st.session_state.game_state.total_questions}")
            st.write(f"Percentage: {score_percentage:.1f}%")
            
            if score_percentage >= 90:
                st.write("Outstanding performance! 🏆")
            elif score_percentage >= 70:
                st.write("Good job! 👍")
            elif score_percentage >= 50:
                st.write("Not bad! Keep practicing! 📚")
            else:
                st.write("You might want to review the material again! 📖")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Play Again"):
                    start_new_game()
            with col2:
                if st.button("Back to Menu"):
                    st.session_state.game_active = False
                    st.experimental_rerun()

if __name__ == "__main__":
    main()