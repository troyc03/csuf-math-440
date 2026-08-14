#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    double x0, y0, R, x, y, vx, vy, t, t0, tf, dt;
    double theta, omega;

    cout << "Enter omega:";
    cin >> omega;
    cout << "Enter center of circle (x0, y0) and radius R: ";
    cin >> x0 >> y0 >> R;
    cout << "Enter t0, tf, dt: ";
    cin >> t0 >> tf >> dt;

    cout << fixed << setprecision(4);
    cout << "Omega: " << omega << endl;
    cout << "Initial position (x): " << x0 << "\n";
    cout << "Initial position (y): " << y0 << "\n";
    cout << "Radius (R): " << R << "\n";
    cout << "Initial time (t0): " << t0 << "\n";
    cout << "Final time (tf): " << tf << "\n";
    cout << "Time step (dt): " << dt << "\n";
    cout << "----------------------------------------\n";
    cout << setw(10) << "Time" << setw(12) << "X" << setw(12) << "Y" 
         << setw(12) << "Vx" << setw(12) << "Vy" << endl;

    for (t = t0; t <= tf; t += dt) {
        theta = omega * t;
        x = x0 + R * cos(theta);
        y = y0 + R * sin(theta);
        vx = -R * omega * sin(theta);
        vy = R * omega * cos(theta);

        cout << setw(10) << t << setw(12) << x << setw(12) << y 
             << setw(12) << vx << setw(12) << vy << endl;
    }

    return 0;
}
