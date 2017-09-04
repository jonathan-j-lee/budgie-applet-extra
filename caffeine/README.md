# Caffeine

A Budgie applet to toggle screen dimming temporarily.

## Rationale

It is typically good security practice to have strict lock settings to reduce the risk of an intruder physically gaining access to a system while the user is away.
However, when the user present but does not need to interact with his or her current session, there should be a mechanism to toggle between guarded and unguarded states easily.
This application fulfills that role.

## Details

Caffeine takes the form of a toggle button that is initially deactivated. It controls four settings:

1. `idle-dim`, which controls whether the screen dims when idle,
2. `sleep-inactive-ac-type`, which controls the sleep behavior during inactivity while on AC power,
3. `sleep-inactive-battery-type`, which is the counterpart for `sleep-inactive-ac-type` on battery power, and
4. `idle-delay`, which controls when to issue a blank screen.

Then,

1. When the button is activated, the applet saves the current values of the above four settings, then overwrites them with:
    1. `idle-dim` to `false`,
    2. `sleep-inactive-ac-type` to `"nothing"`,
    3. `sleep-inactive-battery-type` to `"nothing"`, and
    4. `idle-delay` to `0`, which indicates the screen should never blank.
2. When the button is then deactivated, the applet restores the settings saved on activation.

## Screenshots

![Deactivated button](deactivated.png)

![Activated button](activated.png)
