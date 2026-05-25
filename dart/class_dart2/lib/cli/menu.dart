//в этой же папке будет проверка валидаций, а так папка cli для работы с пользовательскими данными, этот файл для меню
import 'package:class_dart2/data/class_dart2.dart';
import 'package:class_dart2/data/database.dart';
import 'package:class_dart2/data/rep_client.dart';
import 'dart:io';
import 'package:sqlite3/sqlite3.dart';
import 'package:class_dart2/data/class_dart2.dart';


void runMenu(){
  while(true){
    stdout.writeln( // для автоматического пробела
      """Салон красоты Эстель 
      1. список клиентов
      2. добавить клиентов
      3. изменить клиента
      4. удалить клиента
      """
    );
    final choice=stdin.readLineSync()?.trim(); //валидация с трим, убирающая лишние пробелы
    switch(choice){
      case "1":
      
    }
  }
}

void _addClient(SalonRepository salonRep){
  final id=_read('id');
  final name=_read('name');
  final phone=_read('phone');
  salonRep.insertClient(Client(id: id, name: name, phone: phone));
}

void _deleteClient(SalonRepository salonRep){ //УДАЛЕНИЕ ТОЛЬКО ПО АЙДИШНИКУ
  final id=_read('id');
  salonRep.deleteClient(id);
}

//вывод клиента
void _printClient(SalonRepository salonRep){
  final id=_read('id');
  final name=_read('name');
  final phone=_read('phone');
  salonRep.getAllClients(Client(id: id, name: name, phone: phone));
}

String _read(String label){
  stdout.write("$label");
  return stdin.readLineSync()?.trim()??'';
}

// void _printUser(SalonRepository db){
//   final id=;

