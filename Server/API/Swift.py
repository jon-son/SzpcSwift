import swiftclient.service
import swiftclient
from config import swiftConf



class swiftFunsion(object):
    ### swift
    def connection(self):
        conn = swiftclient.Connection(
            authurl=swiftConf['authurl'],
            user=swiftConf['user'],
            key=swiftConf['key'],
            tenant_name=swiftConf['tenant_name'],
            auth_version=swiftConf['auth_version']
        )
        return conn

    def upload(self,container, up_path, path, filename, content_type):
        conn = self.connection()
        with open(up_path, 'rb') as local:
            conn.put_object(
                container,
                path + filename,
                contents=local.read(),
                content_type=content_type
            )

    # dir:type=1
    # file:type=2
    def object_list(self,container, path,type):
        conn = self.connection()
        name = []
        bytes = []
        last_modified = []
        for data in conn.get_container(container)[1]:
            if type == 1:
                if data['name'][len(data['name']) - 1] == '/':
                    if path == data['name'][0:len(path)] and len(
                            data['name'][len(path):len(data['name'])].split("/")) == 2:
                        name.append(data['name'])
                        bytes.append(data['bytes'])
                        last_modified.append(data['last_modified'])
            if type == 2:
                if data['name'][len(data['name']) - 1] != '/':
                    if path == data['name'][0:len(path)] and len(
                            data['name'][len(path):len(data['name'])].split("/")) == 1:
                        name.append(data['name'])
                        bytes.append(data['bytes'])
                        last_modified.append(data['last_modified'])

        return name, bytes, last_modified

    def download(self,container,path, filename):
        swiftfunsion = swiftFunsion()
        conn = swiftfunsion.connection()
        obj_tuple = conn.get_object(container, path + filename)
        return obj_tuple[1]

    def delete(self,container, path, filename):
        conn = self.connection()
        conn.delete_object(container, path + filename)

    def user_list(self):
        conn = self.connection()
        user = []
        for container in conn.get_account()[1]:
            user.append(container['name'])
        return user

    def add_container(self,container):
        conn = self.connection()
        conn.put_container(container)

    def delete_container(self,container):
        conn = self.connection()
        for data in conn.get_container(container)[1]:
            conn.delete_object(container, data['name'])
        conn.delete_container(container)

