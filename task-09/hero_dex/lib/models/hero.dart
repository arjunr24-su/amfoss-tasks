// lib/models/hero.dart
class Hero {
  final int id;
  final String name;
  final String slug;
  final Map<String, int> powerstats;
  final Map<String, dynamic> appearance;
  final Map<String, dynamic> biography;
  final Map<String, dynamic> work;
  final Map<String, dynamic> connections;
  final Map<String, String> images;

  Hero({
    required this.id,
    required this.name,
    required this.slug,
    required this.powerstats,
    required this.appearance,
    required this.biography,
    required this.work,
    required this.connections,
    required this.images,
  });

  factory Hero.fromJson(Map<String, dynamic> json) {
    return Hero(
      id: json['id'],
      name: json['name'],
      slug: json['slug'],
      powerstats: Map<String, int>.from(json['powerstats']),
      appearance: Map<String, dynamic>.from(json['appearance']),
      biography: Map<String, dynamic>.from(json['biography']),
      work: Map<String, dynamic>.from(json['work']),
      connections: Map<String, dynamic>.from(json['connections']),
      images: Map<String, String>.from(json['images']),
    );
  }
}
