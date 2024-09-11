// lib/widgets/hero_item.dart
import 'package:flutter/material.dart';
import 'package:hero_dex/models/hero.dart' as customHero;

class HeroItem extends StatelessWidget {
  final customHero.Hero hero;

  const HeroItem({super.key, required this.hero});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(hero.name),
      subtitle: Text('Power: ${hero.powerstats['power']}'),
      leading: Image.network(hero.images['sm'] ?? ''),
      onTap: () {
        // Navigate to hero detail screen
      },
    );
  }
}
