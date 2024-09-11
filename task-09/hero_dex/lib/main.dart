import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:hero_dex/providers/hero_provider.dart';
import 'package:hero_dex/screens/home_screen.dart';

void main() {
  runApp(HeroDexApp());
}

class HeroDexApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => HeroProvider()),
      ],
      child: MaterialApp(
        title: 'Hero Dex',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: HomeScreen(),
      ),
    );
  }
}
