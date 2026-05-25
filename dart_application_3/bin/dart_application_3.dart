import 'dart:io';
import 'dart:math';
import 'package:characters/characters.dart';

enum Mood {
  happy,
  sad,
  excited,
  tired,
  angry,
  relaxed,
  surprised,
  inLove;

  String get emoji {
    switch (this) {
      case Mood.happy:
        return '\u{1F600}'; // 😀
      case Mood.sad:
        return '\u{1F622}'; // 😢
      case Mood.excited:
        return '\u{1F60E}'; // 😎
      case Mood.tired:
        return '\u{1F634}'; // 😴
      case Mood.angry:
        return '\u{1F620}'; // 😠
      case Mood.relaxed:
        return '\u{1F60A}'; // 😊
      case Mood.surprised:
        return '\u{1F632}'; // 😲
      case Mood.inLove:
        return '\u{1F60D}'; // 😍
    }
  }

  String get description {
    switch (this) {
      case Mood.happy:
        return 'счастливый';
      case Mood.sad:
        return 'грустный';
      case Mood.excited:
        return 'взволнованный';
      case Mood.tired:
        return 'уставший';
      case Mood.angry:
        return 'злой';
      case Mood.relaxed:
        return 'расслабленный';
      case Mood.surprised:
        return 'удивленный';
      case Mood.inLove:
        return 'влюбленный';
    }
  }

  int get energy {
    switch (this) {
      case Mood.happy:
        return 8;
      case Mood.sad:
        return 3;
      case Mood.excited:
        return 9;
      case Mood.tired:
        return 2;
      case Mood.angry:
        return 6;
      case Mood.relaxed:
        return 5;
      case Mood.surprised:
        return 7;
      case Mood.inLove:
        return 8;
    }
  }
}

void main() {
  stdout.write('Введите ваше имя: ');
  String name = stdin.readLineSync()!;
  print('');
  print('Генерируем случайное настроение...');
  final random = Random();
  final moods = Mood.values;
  final randomMood = moods[random.nextInt(moods.length)];
  print('Привет, $name! Твое настроение: ${randomMood.emoji} ${randomMood.description} (энергия: ${randomMood.energy}/10)');
  print('');
  final unicodeValue = randomMood.emoji.runes.first.toRadixString(16).toUpperCase().padLeft(6, '0');
  print('Юникод вашего эмодзи: U+$unicodeValue');
  print('');
  stdout.write('Хотите просмотреть сложные эмодзи? (да/нет): ');
  String answer = stdin.readLineSync()!.toLowerCase();
  print('');

  if (answer == 'да') {
    stdout.write('Введите комбинацию эмодзи: ');
    String emojiString = stdin.readLineSync()!;
    print('');
    print('Анализ строки "$emojiString":');
    print('- 16-битных единиц: ${emojiString.length}');
    print('- Кодовых точек: ${emojiString.runes.length}');
    print('- Реальных символов: ${emojiString.characters.length}');
    print('');
    print('Подробный вывод юникода:');
    int charCounter = 1;
    for (var rune in emojiString.runes) {
      String hexValue = rune.toRadixString(16).toUpperCase().padLeft(4, '0');
      if (hexValue.length > 4) {
        hexValue = hexValue.padLeft(6, '0');
      }
      print('Символ $charCounter: ${String.fromCharCode(rune)} → U+$hexValue');
      charCounter++;
    }
    print('');
    
    print('Спасибо, приходите снова!');
  } else {
    print('Спасибо, приходите снова!');
  }
}

//кол-во символов, если строка - lenght. в строке - кол-во клеточек для смайликов
//смайлик семья состоит из дочерних(сурогатных) смайликов
//runes - число, которое представляет кодовую точку под которой содержится в системе.
//кодовая точка - руна, с помощью которой узнается какой конкретный символ хранится в руне
//fromCharCode{число руны} - выводит руну
//codeUnits - список из всех кодовых точек
//runes.first.ToRadixString(16) - преобразование в 16-тиричный формат с целью узнать кодировку Unicode у смайлика
//строка - последовательность символов в Utf-16
//что такое Unicode? отличие строки от руны? что такое characters? что такое перечисление?
//
// 
//
//
//
//