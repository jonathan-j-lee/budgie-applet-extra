# budgie-applet-extra

Extra Budgie applets.

| Name                 | Description                       |
| -------------------- | --------------------------------- |
| [Caffeine](caffeine) | Toggle screen dimming temporarily |

## Installation Example

To install the `caffeine` applet, for instance:

```shell
$ git clone https://github.com/jonathan-j-lee/budgie-applet-extra.git
$ cd budgie-applet-extra/
$ applet_dir=/usr/lib/budgie-desktop/plugins/org.budgie-applet-extra.applet.caffeine
$ mkdir $applet_dir
$ cp caffeine/Caffeine.plugin $applet_dir
$ cp caffeine/caffeine.py $applet_dir
$ chmod +x $applet_dir/caffeine.py
```

This may require `sudo`.

Then, simply reboot or run `budgie-panel --replace`, and add Caffeine to the panel from Raven. The installation process for the other applets is similar.

## Acknowledgements

Many thanks to the creators of [these applet examples](https://github.com/budgie-desktop/budgie-desktop-examples) for guidance.
