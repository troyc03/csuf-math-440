#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>

using namespace std;

int main() {
    double x0, y0, R, x, y, vx, vy, ax, ay, t, t0, tf, dt;
    double theta, omega;

    cout << "Enter omega: ";
    cin >> omega;
    cout << "Enter center of circle (x0, y0) and radius R: ";
    cin >> x0 >> y0 >> R;
    cout << "Enter t0, tf, dt: ";
    cin >> t0 >> tf >> dt;

    ofstream outFile("trajectory.dat");
    if (!outFile) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    // Header maps out 7 distinct data columns
    outFile << "# " << setw(8) << "Time" 
            << setw(12) << "X" << setw(12) << "Y" 
            << setw(12) << "Vx" << setw(12) << "Vy"
            << setw(12) << "Ax" << setw(12) << "Ay" << "\n";

    outFile << fixed << setprecision(4);

    for (t = t0; t <= tf; t += dt) {
        theta = omega * t;
        x = x0 + R * cos(theta);
        y = y0 + R * sin(theta);
        
        vx = -R * omega * sin(theta); 
        vy = R * omega * cos(theta);

        // Centripetal Acceleration Math
        ax = -R * omega * omega * cos(theta);
        ay = -R * omega * omega * sin(theta);

        outFile << setw(10) << t 
                << setw(12) << x << setw(12) << y 
                << setw(12) << vx << setw(12) << vy
                << setw(12) << ax << setw(12) << ay << "\n";
    }

    outFile.close();
    cout << "\nData exported with acceleration columns!" << endl;
    return 0;
}
