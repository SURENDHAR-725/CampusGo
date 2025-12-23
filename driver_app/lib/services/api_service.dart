import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static String baseUrl = "http://YOUR-SERVER-IP:5000";

  static Future loginDriver(email, password) async {
    final res = await http.post(
      Uri.parse("$baseUrl/driver/login"),
      body: {"email": email, "password": password},
    );

    return jsonDecode(res.body);
  }

  static Future sendLocation(busId, lat, lng, speed) async {
    await http.post(
      Uri.parse("$baseUrl/api/update-location"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "bus_id": busId,
        "lat": lat,
        "lng": lng,
        "speed": speed
      }),
    );
  }
}
