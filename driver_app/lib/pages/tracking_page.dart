import 'dart:async';
import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import '../services/api_service.dart';

class TrackingPage extends StatefulWidget {
  final int busId;
  TrackingPage({required this.busId});

  @override
  State<TrackingPage> createState() => _TrackingPageState();
}

class _TrackingPageState extends State<TrackingPage> {
  bool tracking = false;
  Timer? timer;

  startTracking() {
    timer = Timer.periodic(Duration(seconds: 2), (_) async {
      Position pos = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.high,
      );

      await ApiService.sendLocation(
        widget.busId,
        pos.latitude,
        pos.longitude,
        pos.speed * 3.6, // m/s → km/h
      );
    });

    setState(() => tracking = true);
  }

  stopTracking() {
    timer?.cancel();
    setState(() => tracking = false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Live Tracking"),
      ),
      body: Center(
        child: tracking
            ? ElevatedButton(
                onPressed: stopTracking,
                child: Text("Stop Tracking"),
              )
            : ElevatedButton(
                onPressed: startTracking,
                child: Text("Start Tracking"),
              ),
      ),
    );
  }
}
