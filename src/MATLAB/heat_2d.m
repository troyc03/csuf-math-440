% 1. Parameters and grid setup
L = 1;              % Domain size (L x L)
T_final = 0.1;      % Final time
alpha = 0.01;       % Thermal diffusivity
Nx = 40;            % Grid points in x
Ny = 40;            % Grid points in y
Nt = 500;           % Number of time steps

dx = L / (Nx - 1);
dy = L / (Ny - 1);
dt = T_final / Nt;

% Courant-Friedrichs-Lewy (CFL) stability parameters
rx = alpha * dt / dx^2;
ry = alpha * dt / dy^2;

% Stability check for 2D explicit FTCS (rx + ry <= 0.5)
if (rx + ry) > 0.5
    error('Stability criterion violated: reduce dt or increase spatial points.');
end

% 2. Coordinate grids
x = linspace(0, L, Nx);
y = linspace(0, L, Ny);
[X, Y] = meshgrid(x, y);

% 3. Initial Condition: 2D Gaussian Distribution
u0 = 1.0;           % Peak temperature
x0 = 0.5; y0 = 0.5; % Center of the Gaussian pulse
sigma = 0.1;        % Width of the pulse
u = u0 * exp(-((X - x0).^2 + (Y - y0).^2) / (2 * sigma^2));
u_new = u;

% 4. Prepare Figure for Animation
figure('Color', 'w');
hSurf = surf(X, Y, u);
colorbar;
colormap('hot');
zlim([0 1]);
xlabel('X coordinate');
ylabel('Y coordinate');
zlabel('Temperature (U)');
view(3); % Enforce 3D view
shading interp; % Smooth surface visualization

% 5. Time-stepping loop (2D Finite Difference)
for n = 1:Nt
    % Vectorized internal node update for efficiency
    u_new(2:Ny-1, 2:Nx-1) = u(2:Ny-1, 2:Nx-1) + ...
        rx * (u(2:Ny-1, 3:Nx) - 2*u(2:Ny-1, 2:Nx-1) + u(2:Ny-1, 1:Nx-2)) + ...
        ry * (u(3:Ny, 2:Nx-1) - 2*u(2:Ny-1, 2:Nx-1) + u(1:Ny-2, 2:Nx-1));
    
    % Dirichlet Boundary Conditions (u = 0 at all edges)
    u_new(1, :) = 0;
    u_new(Ny, :) = 0;
    u_new(:, 1) = 0;
    u_new(:, Nx) = 0;
    
    % Update solution matrix
    u = u_new;
    
    % Real-time rendering update
    if mod(n, 5) == 0
        set(hSurf, 'ZData', u, 'CData', u);
        title(['Time step: ', num2str(n), ' / ', num2str(Nt)]);
        drawnow;
    end
end
