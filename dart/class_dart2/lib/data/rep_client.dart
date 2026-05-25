//здесь все круды, только для каждой таблицы нужно создавать отдельные файлы дял крудов
import 'dart:ffi';
import 'package:sqlite3/sqlite3.dart';
import 'package:class_dart2/data/class_dart2.dart'; //все модели сейчас в одном файле, но их надо разделить на три пакета

class SalonRepository{
  final Database _sqlite;
  SalonRepository(this._sqlite);

  void insertClient(Client client){ //название объекта метод для добалвения
    _sqlite.execute('INSERT INTO clients(id,name,phone) VALUES(?,?,?)',
    [client.id,
    client.name,
    client.phone]); //заполняем все значения которые опрелеляются с помощью ?, в массиве определяем все значения 
  }

  void insertService(Service service){
    _sqlite.execute('INSERT OR REPLACE services(id,title,desc,durationMinutes,price) VALUES(?,?,?,?,?)',
    [service.id,
    service.title,
    service.description,
    service.durationMinutes,
    service.price]);
  }

  void insertApp(Appoinments app){
    _sqlite.execute('INSERT OR REPLACE appoinments(id,clientId,serviceId,time) VALUES(?,?,?,?)',
    [app.id,
    app.clientId,
    app.serviceId,
    app.time.toIso8601String()]
    ); //стандарт преобразования даты
  }

  List<Client> getAllClients(Client client){
    final rows=_sqlite.select('SELECT * FROM clients');
    return rows.map((row)=>Client.fromMap(row)).toList();
  }

  List<Service> getAllService(Client client){
    final rows=_sqlite.select('SELECT * FROM services');
    return rows.map((row)=>Service.fromMap(row)).toList();
  }

  List<Appoinments> getAllAppoinments(Client client){
    final rows=_sqlite.select('SELECT * FROM appoinments');
    return rows.map((row)=>Appoinments.fromMap(row)).toList();
  }

  Client? getClientById(String id){
    final rows=_sqlite.select('SELECT * FROM clients where id=?',[id]);
    return rows.isNotEmpty ? Client.fromMap(rows.first) : null;
  }

  Service? getServiceById(String id){
    final rows=_sqlite.select('SELECT * FROM services where id=?',[id]);
    return rows.isNotEmpty ? Service.fromMap(rows.first) : null;
  }

  Appoinments? getAppById(String id){
    final rows=_sqlite.select('SELECT * FROM appoinments where id=?',[id]);
    return rows.isNotEmpty ? Appoinments.fromMap(rows.first) : null;
  }

  void updateClient(String id){
    _sqlite.execute('UPDATE clients SET name=?, phone=? WHERE id=?',[id]);
  }

  void deleteClient(String id){
    _sqlite.execute('DELETE FROM clients WHERE id=?', [id]);
  }
}