// lib/providers/hero_provider.dart
import 'package:flutter/material.dart';
import 'package:hero_dex/models/hero.dart';
import 'package:hero_dex/utils/hero_loader.dart';

class HeroProvider with ChangeNotifier {
  List<Hero> _heroes = [];
  bool _isLoading = false;

  List<Hero> get heroes => _heroes;
  bool get isLoading => _isLoading;

  Future<void> loadHeroes() async {
    _isLoading = true;
    notifyListeners();

    try {
      _heroes = await loadHeroesFromJson();
    } catch (error) {
      // Handle error if needed
      print('Error loading heroes: $error');
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
