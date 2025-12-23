import 'package:flutter/material.dart';
import 'tracking_page.dart';

class DashboardPage extends StatelessWidget {
  final Map user;

  DashboardPage({required this.user});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Driver Dashboard"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("Welcome, ${user['name']}",
                style: TextStyle(fontSize: 20)),
            SizedBox(height: 20),
            Text("Assigned Bus: ${user['bus_number']}"),
            Text("Route: ${user['route_name']}"),
            SizedBox(height: 30),
            ElevatedButton.icon(
              icon: Icon(Icons.gps_fixed),
              label: Text("Start Live Tracking"),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => TrackingPage(busId: user["bus_id"]),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
