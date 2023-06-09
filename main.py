import hashlib as hasher
import datetime as date
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import uuid
import sqlite3


def central_Database(In_BlockChain, ID_of_patient):
    name_of_database = str(uuid.uuid4())
    con = sqlite3.connect("DataCenter.db")
    cursor = con.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS NamesOfDatabases (id INTEGER PRIMARY KEY AUTOINCREMENT, 'Identifier' TEXT,"
        "'uuid' TEXT)")
    cursor.execute("SELECT EXISTS(SELECT * FROM NamesOfDatabases  WHERE 'Identifier' = ?)", (ID_of_patient,))
    result = cursor.fetchone()
    if result[0] == 0:
        cursor.execute("INSERT INTO NamesOfDatabases('Identifier','uuid') VALUES (?,?)",
                       (ID_of_patient, name_of_database))
        con.commit()
        con.close()
        SaveToSQL(In_BlockChain, name_of_database)
    else:
        con.close()


def SaveToSQL(In_BlockChain, database_name):
    con = sqlite3.connect(database_name + ".db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS block"
                   "('index' INTEGER,timestamp TEXT,data BLOB,iv BLOB ,previous_hash BLOB , hash BLOB)")
    for in_block in In_BlockChain:
        cursor.execute("INSERT INTO block('index',timestamp,data,iv,previous_hash,hash) VALUES (?,?,?,?,?,?)",
                       (in_block.index, in_block.timestamp, in_block.data, in_block.iv, in_block.previous_hash,
                        in_block.hash,))
    con.commit()
    con.close()


def retrieve_data(patient_ID):
    con = sqlite3.connect("DataCenter.db")
    cursor = con.cursor()
    cursor.execute("SELECT EXISTS(SELECT uuid FROM NamesOfDatabases where Identifier = '" + patient_ID + "')")
    if cursor.fetchone()[0]:
        cursor.execute("SELECT uuid FROM NamesOfDatabases where Identifier = '" + patient_ID + "'")
        patient_uuid = cursor.fetchone()[0] + ".db"
        con = sqlite3.connect(patient_uuid)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM block ")
        rows = cursor.fetchall()
        con.close()
        return rows
    else:
        con.close()
        return 'Nothing found!'


class Block:
    def __init__(self, index, timestamp, data, iv, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.iv = iv
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __repr__(self):
        return "%04d: %s, %s : %s :%s" % (
            self.index, self.timestamp, str(self.data), str(self.previous_hash), str(self.iv))

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(repr(self).encode('UTF-8'))
        print("SHA256 HASH(", self.index, "):", sha.hexdigest())
        return sha.hexdigest()


class Information:
    def __init__(self, ID, age, address, phone_number, insurance, medical_history):
        self.ID = str(ID)
        self.age = str(age)
        self.address = str(address)
        self.phone_number = str(phone_number)
        self.insurance = str(insurance)
        self.medical_history = str(medical_history)
        self.finaldata = FinalData(self)


def FinalData(obj):
    rawdata = ' |  ' + obj.ID + ' |  ' + obj.age + ' |  ' + obj.address + ' |  ' + obj.phone_number + ' |  ' \
              + obj.insurance + ' |  ' + obj.medical_history
    rawdataBlocks = Blocks_With_Data(rawdata)
    return rawdataBlocks


def Blocks_With_Data(rawdata):
    BlockSize = 20
    Length_Of_Data = len(rawdata)
    while True:
        if Length_Of_Data % BlockSize == 0:
            SizeInBlock = int(Length_Of_Data / BlockSize)
            BlockWithData = []
            splits = [rawdata[j:j + SizeInBlock] for j in range(0, Length_Of_Data, SizeInBlock)]
            for part in splits:
                BlockWithData.append(part)
            return BlockWithData
        BlockSize += 1


def create_genesis_block():
    genesis_block = Block(0, date.datetime.now(), 'genesis block', bytes(0), "0")
    genesis_block.data, genesis_block.iv = EncryptBlock(genesis_block.data, genesis_block.hash_block())
    genesis_block.hash = genesis_block.hash_block()
    return genesis_block


def next_block(last_block, info):
    new_index = last_block.index + 1
    new_timestamp = date.datetime.now()
    new_data, new_iv = EncryptBlock(info, last_block.hash)
    previous_hash = last_block.hash
    print(new_data)
    return Block(new_index, new_timestamp, new_data, new_iv, previous_hash)


def validate_blockchain(in_blockchain):
    invalid_block = 0

    for current_position in range(1, len(in_blockchain)):
        previous_position = current_position - 1
        if in_blockchain[previous_position].hash_block() != in_blockchain[current_position].previous_hash:
            invalid_block += 1

    if invalid_block != 0:
        return False
    else:
        return True


def read_blockchain_data(in_blockchain):
    validation = validate_blockchain(in_blockchain)

    if validation:
        data_in_block = ''
        for i in range(1, len(in_blockchain)):
            decryptedData = DecryptBlock(in_blockchain[i].data, in_blockchain[i].previous_hash, in_blockchain[i].iv)
            data_in_block += decryptedData[2:len(decryptedData) - 1]

        split_data = data_in_block.split(' | ')
        data_after_reconstruct = data_reconstruct(split_data)
        return data_after_reconstruct
    else:
        print('Data Is Not Valid..')


def data_reconstruct(rawdata):
    return dict(ID=rawdata[1], age=rawdata[2], address=rawdata[3], phone_number=rawdata[4],
                insurance=rawdata[5], medical_history=rawdata[6])


def EncryptBlock(plain_block, secret_key):
    hex_string = '0x' + secret_key
    num_bytes = bytes.fromhex(hex_string[2:])
    key = num_bytes
    plaintext_bytes = plain_block.encode()
    padded_plaintext = pad(bytes(plaintext_bytes), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(padded_plaintext)
    iv = cipher.iv
    return cipher_text, iv


def DecryptBlock(CipherBlock, secret_key, iv):
    hex_string = '0x' + secret_key
    num_bytes = bytes.fromhex(hex_string[2:])
    key = num_bytes
    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = decrypt_cipher.decrypt(CipherBlock)
    un_padded_plaintext = str(unpad(plain_text, AES.block_size))
    return un_padded_plaintext


def EnterInfo(pid, age, address, phone, insurance, medical):
    MainBlockChain = [create_genesis_block()]
    previous_block = MainBlockChain[0]
    IDOfpatient = str(pid)
    AgeOfpatient = str(age)
    AddressOfpatient = str(address)
    PhoneOfpatient = str(phone)
    insuranceOfpatient = str(insurance)
    medicalHistoryOfpatient = str(medical)

    information_patient = Information(IDOfpatient, AgeOfpatient, AddressOfpatient, PhoneOfpatient,
                                      insuranceOfpatient,
                                      medicalHistoryOfpatient)

    for block in information_patient.finaldata:
        new_block = next_block(previous_block, block)
        MainBlockChain.append(new_block)
        previous_block = new_block

    central_Database(MainBlockChain, IDOfpatient)
    return 'Information Added successfully'


def SearchInfo(search_ID):
    rows = retrieve_data(search_ID)

    if rows != 'Nothing found!':
        NewBlockChain = []
        for row in rows:
            newblock = Block(row[0], row[1], row[2], row[3], row[4])
            newblock.hash = row[5]
            NewBlockChain.append(newblock)
        var = read_blockchain_data(NewBlockChain)
        return var

    else:
        return rows
