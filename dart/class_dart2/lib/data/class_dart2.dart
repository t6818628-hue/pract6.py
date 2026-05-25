import 'package:sqlite3/sqlite3.dart'; // импорт пакета SQLLITE3, после / то что подключаем и с каким расширением. 
// dart pub get - если не работает импорт пакета, после нажать CTRL+S, закрыть все файлы и вернуться обратно. не забыть точку с запятой после испорта пакета
import 'package:path/path.dart' as p; //импорт пакта для того, чтобы создать псевдоним дял проекта (псевдоним "p")

abstract class Id{ //класс, чтобы каждая модель понимала, что у нёё есть ID
  String get id;
}

class Client implements Id { // класс на основе Id, обязанность переопределить метод но со своей реализацией
  @override
  final id;
  final name; //final чтобы просто создать таблицу, но не заполнять значения сразу
  final phone; //запись осуществляется по номеру телефона

  Client({required this.id, required this.name, required this.phone}); //конструктор с именованными параметрами

  Map<String,dynamic> toMap()=>{ 
  "id":id,
  "name":name,
  "phone":phone
  };//динамик - потому что поле может быть в любом типе, чтобы преобразовать его в дальнейшем. toMap - чтобы сохранить эти данные в файл

  factory Client.fromMap(Map<String,dynamic> map){   //возвращает уже известный результат
    return Client( //возвращаем результат
      id: map["id"] as String,
      name: map["name"] as String,
      phone: map["phone"] as String // перезапись значений
    );
  }
}

class Service implements Id { // класс на основе Id, обязанность переопределить метод но со своей реализацией
  @override
  final id;
  final title; //final чтобы просто создать таблицу, но не заполнять значения сразу
  final description; //запись осуществляется по номеру телефона
  final int durationMinutes;
  final double price;

  Service({required this.id, required this.title, required this.description, required this.durationMinutes, required this.price}); //конструктор с именованными параметрами

  Map<String,dynamic> toMap()=>{ 
  "id":id,
  "title":title,
  "desription":description,
  "durationMinutes":durationMinutes,
  "price":price
  };//динамик - потому что поле может быть в любом типе, чтобы преобразовать его в дальнейшем. toMap - чтобы сохранить эти данные в файл

  factory Service.fromMap(Map<String,dynamic> map){   //возвращает уже известный результат
    return Service( //возвращаем результат
      id: map["id"] as String,
      title: map["title"] as String,
      description: map["description"] as String // перезапись значений
      durationMinutes: _isInt(map["durationMinutes"]), //в момент сериализации проверяем в каком типе.
      price: _isDouble(map["price"])
      );
    }

  static int _isInt(Object? v){
    if (v is int) return v.toInt();
    if (v is double) return v.toDouble();
    throw FormatException("Ожидали число", v);
  }
  static int _isDouble(Object? b){
    if (b is double) return b.toDouble();
    if (b is int) return b.toInt();
    throw FormatException("Ожидали число", b);
  }
}

class Appoinments implements Id { // класс на основе Id, обязанность переопределить метод но со своей реализацией
  @override
  final String id;
  final DateTime time; //final чтобы просто создать таблицу, но не заполнять значения сразу
  final String clientId; //запись осуществляется по номеру телефона
  final String serviceId;

  Appoinments({required this.id, required this.time, required this.clientId, required this.serviceId}); //конструктор с именованными параметрами

  Map<String,dynamic> toMap()=>{ 
  "id":id,
  "time":time.toIso8601String(), //стандарт для времени и даты
  "clientId":clientId,
  "serviceId":serviceId
  };//динамик - потому что поле может быть в любом типе, чтобы преобразовать его в дальнейшем. toMap - чтобы сохранить эти данные в файл

  factory Appoinments.fromMap(Map<String,dynamic> map){   //возвращает уже известный результат
    return Appoinments( //возвращаем результат
      id: map["id"] as String,
      time: DateTime.parse(map["time"] as String,
      clientId: map["clientId"] as String, // перезапись значений
      sericeId: map["serviceId"]) //в момент сериализации проверяем в каком типе.
      );
    }
//должны серилиазовать эти объекты в качестве строк. десериализация - строка в объект. 