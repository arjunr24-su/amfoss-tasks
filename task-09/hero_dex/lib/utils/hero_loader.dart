// lib/utils/hero_loader.dart
import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;
import 'package:hero_dex/models/hero.dart';

Future<List<Hero>> loadHeroesFromJson() async {
  final String response =
      await rootBundle.loadString('assets/superheroes.json');
  final List<dynamic> data = json.decode(response);
  return data.map((json) => Hero.fromJson(json)).toList();
}
