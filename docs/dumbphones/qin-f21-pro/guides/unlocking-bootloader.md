# Unlocking the Bootloader

{{ mt8766_warning }}

## Overview

Unlocking the bootloader enables advanced modifications including custom recovery, custom ROMs, and root access. The bootloader is a security checkpoint that verifies device software—unlocking it removes these restrictions.

```{admonition} What you'll accomplish
- Unlock your device's bootloader for advanced modifications
- Preserve device data during unlock (backup still recommended)
- Prepare for rooting, custom ROMs, and other modifications
```


This guide uses [MTKClient](https://github.com/bkerler/mtkclient), an open-source tool for MediaTek-based devices. It unlocks the bootloader without erasing user data.

## Prerequisites

- [MTKClient](https://github.com/bkerler/mtkclient) installed and working
- Python 3.9 or newer
- USB drivers for MediaTek devices
- Quality USB data cable
- Developer Options enabled with OEM unlocking

### Enable Developer Options

1. Navigate to **Settings → About Phone**
2. Tap **Build Number** seven times
3. Go to **System → Developer Options**
4. Enable **OEM unlocking**
5. Enable **USB debugging**

## Unlock Using MTKClient

### Command Line Method

1. **Power off device completely**

2. **Run unlock command** in MTKClient directory:
   ```
   python mtk da seccfg unlock
   ```

3. **Enter BROM mode:**
   - Hold **Owl/Heart button** (top left) + **Back button**
   - While holding, plug in USB cable
   - Keep holding until device detected

4. **Wait for completion** (10-30 seconds)

   ```{note}
   Some users need to reconnect USB multiple times. If stuck, disconnect and re-enter BROM mode.
   ```

5. **Reboot device:**
   ```
   python mtk reset
   ```

### GUI Method

1. **Launch GUI:**
   ```
   python mtk_gui
   ```

2. **Power off device**

3. **Navigate to "Flashing" tab → Click "Unlock Bootloader"**

4. **Enter BROM mode** (hold Owl/Heart + Back, plug USB)

5. **Wait for completion, then reset device**

## Verification

After unlocking, you'll see an **Orange State** warning on boot:

```
Orange State
Your device has been unlocked and can't be trusted
Your device will boot in 5 seconds
```

This is completely normal and confirms successful unlock. Some Google Play pre-installed devices may not show this message.

## Post-Unlock: Create Backup

Create a complete backup before making modifications:

1. Power off device
2. Launch GUI: `python mtk_gui`
3. Enter BROM mode (hold Owl/Heart + Back, plug USB)
4. Go to **"Read partition(s)"** tab
5. Click **"Select all partitions"**
6. Optionally uncheck **userdata** (encrypted personal data)
7. Enable **"Dump GPT"**
8. Click **"Read Partition(s)"** and choose save location
9. Back up preloader from **"Flash Tools"** tab

```{warning}
**Critical Partition Warnings:**
- **Never** copy `seccfg` between devices—each has unique security config
- Flashing another device's `seccfg` will brick your phone

When restoring, erase these partitions first: `python mtk e seccfg,cache,metadata,userdata,md_udc`
```

## Troubleshooting

### Device Not Detected

If [MTKClient](https://github.com/bkerler/mtkclient) shows "Waiting for PreLoader VCOM" indefinitely:

- Ensure MediaTek USB drivers installed properly
- Use quality **data** cable (not charging-only)
- Try different USB ports (USB 3.0/3.1 often work better)
- Verify button combination: Owl/Heart (top left) + Back
- Confirm device fully powered off
- Windows: Check Device Manager for MediaTek device
- Try Preloader mode: plug USB without holding buttons

### Process Freezes

- Unplug USB, wait 5 seconds, reconnect in BROM mode
- Multiple reconnection attempts may be needed
- Don't touch cable/device during process
- Try USB 2.0 port instead of 3.0

## Relocking the Bootloader

```{danger}
**Only relock with completely stock, unmodified system partitions.**
Relocking with modifications will brick your device.
```

1. Restore to stock firmware
2. Verify all partitions unmodified
3. Power off device
4. Run: `python mtk da seccfg lock`
5. Enter BROM mode when prompted
6. Wait for completion and reboot
