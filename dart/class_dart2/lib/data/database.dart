//здесь будут подключения к бд вроде
import 'dart:io';

import 'package:class_dart2/data/class_dart2.dart';
import 'package:sqlite3/sqlite3.dart';
import 'package:path/path.dart' as p1; //создание псевдонима, и обращаться к нему с помощью псевдонима 

class SalonDatabase{
  final Database _sqllite; //переменная типа Database из пакета, приватная переменная

  SalonDatabase(String filepath):_sqllite = sqlite3.open(filepath){
    _createTables();
  }
  factory SalonDatabase.inApp(){
    final filepath=p1.join(Directory.current.path,'p1.db'); //переменная которая хранит в себе создание директории, p1.db - название базы данных
    return SalonDatabase(filepath);
  }

  void _createTables(){
    _sqllite.execute("""
    CREATE TABLE IF NOT EXITS clients( //создаём атрибуты в точно таком же типе данных как и в модели
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
    );
    """); //метод для create,insert,delete,update. для селекта отдельный метод. сейчас создайт таблицу clients //не создавать сразу же одним exceute все таблицы разом, по одной таблицы

    _sqllite.execute("""
    CREATE TABLE IF NOT EXITS services(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    desc TEXT NOT NULL,
    durationMinutes INT NOT NULL,
    price REAL NOT NULL
    );
    """);

    _sqllite.execute("""
    CREATE TABLE IF NOT EXITS apointments(
    id TEXT PRIMARY KEY,
    clientId TEXT NOT NULL,
    serviceId TEXT NOT NULL,
    time DATETIME NOT NULL,
    FOREIGN KEY (clientId) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (serviceId) REFERENCES services(id) ON DELETE CASCADE
    );
    """);
  
    
  }
  Database get sqllite=>_sqllite; //геттер

  //метод, закрывающий соединение на подключение к бд
  void close(){
    _sqllite.dispose();
  }
}