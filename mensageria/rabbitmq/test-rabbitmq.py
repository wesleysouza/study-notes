from multiprocessing import connection
import pika

class TestRabbitMQ:

    def __init__(self, host, port, virtualhost, username, password):
        self.host = host
        self.port = int(port)
        self.virtualhost = virtualhost
        self.username = username
        self.password = password

    def connection(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, 
        self.port, self.virtualhost, credentials))
        return connection

    def create_queue(self, queue_name):
        channel = self.connection().channel()
        channel.queue_declare(queue=queue_name)

    def sending_simple_mensage(self, mensage, queue_name):
        connection = self.connection()
        channel = connection.channel()
        channel.basic_publish(exchange='', routing_key=queue_name, body=mensage)
        print(" [x] Sent 'Hello World!'")
        connection.close()

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)

    def consuming(self, queue_name):
        connection = self.connection()
        channel = connection.channel()
        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()

    
def menu():
    testRabbitMQ = TestRabbitMQ('localhost', 5672, '/', 'user', 'senha')
    testRabbitMQ.connection

    while True:
        print("TEST RABBITMQ\n\n")
        print("Digite uma das opções abaixo\n")
        print("1 - Criar Fila\n")
        print("2 - Enviar Menagem de Teste\n")
        print("3 - Consumir todas as mensagens\n")
        print("4 - Sair\n")
    
        op = int(input())
        if op == 1:
            print("Criando fila\n")
            print("Digite o nome da fila\n")
            queue_name = input()
            testRabbitMQ.create_queue(queue_name)
        elif op == 2:
            print("Enviando uma mensagem\n")
            print("Digite o nome da fila\n")
            queue_name = input()
            testRabbitMQ.sending_simple_mensage('essa fila funciona?', 'test')
            print("Mensagem enviada\n")
        elif op == 3:
            print("Consumindo dados de toda uma fila\n")
            print("Digite o nome da fila\n")
            queue_name = input()
            testRabbitMQ.consuming(queue_name)
            print("Dados consumidos com sucesso!\n")
        elif op == 4:
            print("Encerando o programa!\n")
            break
        else:
            print("ERRO: Opcao invalida!")


menu()

#testRabbitMQ = TestRabbitMQ('localhost', 5672, '/', 'user', 'senha')
#testRabbitMQ.connection
#testRabbitMQ.create_queue('test')
#testRabbitMQ.sending_simple_mensage('essa fila funciona?', 'test')
#testRabbitMQ.consuming()
    