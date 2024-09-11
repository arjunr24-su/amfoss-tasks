// lib/widgets/hero_list.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:hero_dex/providers/hero_provider.dart';
import 'package:hero_dex/widgets/hero_item.dart';

class HeroList extends StatelessWidget {
  const HeroList({super.key});

  @override
  Widget build(BuildContext context) {
    return Consumer<HeroProvider>(
      builder: (context, heroProvider, child) {
        if (heroProvider.isLoading) {
          return const Center(child: CircularProgressIndicator());
        } else if (heroProvider.heroes.isEmpty) {
          return const Center(child: Text('No heroes found'));
        } else {
          return ListView.builder(
            itemCount: heroProvider.heroes.length,
            itemBuilder: (context, index) {
              return HeroItem(hero: heroProvider.heroes[index]);
            },
          );
        }
      },
    );
  }
}
