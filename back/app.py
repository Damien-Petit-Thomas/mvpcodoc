from flask import Flask, jsonify, request
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

secret_code = "Unguessable"
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)
public_key = key.publickey().export_key()
private_key = key.export_key(passphrase=secret_code)

app = Flask(__name__)

# Endpoint pour la vérification de la santé
@app.route('/health', methods=['GET'])
def health_check():
    return '', 200  # Réponse vide avec un statut 200


# Générer une paire de clés RSA
# (public_key, private_key) = rsa.newkeys(512)

# Endpoint pour récupérer la clé publique RSA
@app.route('/key', methods=['GET'])
def get_public_key():
    # Convertir la clé publique en format PEM pour l'envoyer
    public_key_pem =  public_key.decode('utf-8')
    private_key_pem = private_key.decode('utf-8')
    return jsonify({'public_key': public_key_pem, 'private_key': private_key_pem})

# Endpoint pour décoder un message avec la clé publique RSA
@app.route('/decode', methods=['GET'])
def decode_message():
    private_key_obj = RSA.import_key(private_key, passphrase=secret_code)  # Importer la clé privée
    cipher = PKCS1_OAEP.new(private_key_obj, hashAlgo=SHA256)  # Initialiser le chiffreur PKCS1_OAEP
    # Récupérer le message encodé depuis le paramètre de requête 'msg'
    encoded_message = request.args.get('msg')
    if encoded_message is None:
        return 'Missing message parameter', 400

    try:
        # Convertir la chaîne hexadécimale en objets bytes
        encoded_bytes = bytes.fromhex(encoded_message)
        # Décoder le message
        decoded_message = cipher.decrypt(encoded_bytes)
        # Convertir le message décodé en chaîne de caractères
        return jsonify({'decoded_message': decoded_message.decode('utf-8')})
    except ValueError as e:
        # Gérer les erreurs de décodage ici
        return 'Error decoding message: {}'.format(str(e)), 400




if __name__ == '__main__':
    app.run()
