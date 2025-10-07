# Boot Modes Reference Guide

The Qin F21 Pro supports several special boot modes for system maintenance, firmware flashing, and device recovery. This guide provides the button combinations needed to access each mode.

**Critical:** Device must be completely powered off before entering any boot mode. Hold power button for 10+ seconds if needed to force shutdown.

## Button Reference

- **Power Button** - Right side of device
- **Owl/Heart Button** - Heart-shaped button, left side below screen
- **Star (*)** - Keypad, lower left
- **Back Button** - Top right of device (alternatively, keys 4+7 pressed simultaneously produce the same keycode)
- **Joystick Up** - Center navigation pad, press upward

## Recovery Mode

**Used for:** Factory resets, accessing TWRP, entering fastboot/fastbootd modes

### Button Combination Method
1. Power off device
2. Hold: **Star (*)** + **Owl/Heart** + **Power**
3. When Duoqin logo appears, **release Power only**
4. Continue holding Star + Owl/Heart until "No command" screen appears
5. Press: **Joystick Up** + **Power** (may require multiple attempts)

### ADB Method (requires USB debugging enabled)
```{prompt} bash $
adb reboot recovery
```
Then press **Joystick Up** + **Power** when "No command" appears.

**Navigation:** Joystick to move, Power to select

## Fastboot Mode

**Used for:** Bootloader unlocking, flashing boot/recovery images

### Through Recovery (Recommended)
1. Enter Recovery Mode
2. Select "Reboot to bootloader"

### ADB Method
```{prompt} bash $
adb reboot bootloader
```

**Display:** Black screen showing "=> FASTBOOT mode"

**Exit:** Hold Power for 10 seconds or use:
```{prompt} bash $
fastboot reboot
```

## Fastbootd Mode

**Used for:** Flashing super partition, dynamic partition operations, GSI ROMs

### Through Recovery
1. Enter Recovery Mode
2. Select "Enter fastboot"

### From Fastboot
```{prompt} bash $
fastboot reboot fastboot
```

### ADB Method
```{prompt} bash $
adb reboot fastboot
```

**Display:** Menu with reboot options

## Preloader Mode

**Used for:** MTKClient/SP Flash Tool operations, complete ROM backups

### Connection Method
1. Power off device completely
2. Start MTKClient or SP Flash Tool on computer
3. **Connect USB cable without pressing any buttons**
4. Tool will detect "Preloader" with MT6761 chipset info

**Display:** None (screen remains off; detected by computer only)

**Troubleshooting:**
- Ensure device is fully powered off
- Try different USB cable/port
- Verify tool is running before connecting

## BROM Mode

**Used for:** Emergency recovery, hardware-level access when preloader fails

### Button Combination Method
1. Power off device
2. Start MTKClient or SP Flash Tool
3. Hold: **Owl/Heart** + **Back**
4. While holding, **connect USB cable**
5. Hold until tool detects "BROM mode"

**Display:** None (screen remains off; detected by computer only)

## Quick Reference

| Mode | Access Method | Display |
|------|--------------|---------|
| Recovery | * + Owl/Heart + Power → (release Power at logo) → Up + Power | Android robot + menu |
| Fastboot | Recovery menu: "Reboot to bootloader" | "=> FASTBOOT mode" |
| Fastbootd | Recovery menu: "Enter fastboot" | Menu with options |
| Preloader | Connect USB without buttons (device off) | None (computer detection) |
| BROM | Owl/Heart + Back + connect USB | None (computer detection) |

## Troubleshooting

**Device won't enter mode:**
- Verify device is completely powered off
- For recovery: Try Up + Power combination multiple times
- For preloader/BROM: Ensure tool is running before connecting USB

**Computer won't detect:**
- Install MediaTek USB drivers (preloader/BROM)
- Try different USB cable and port (USB 2.0 preferred)
- Verify detection (fastboot mode):
  ```{prompt} bash $
  fastboot devices
  ```

**Stuck in boot mode:**
- Hold Power button 10+ seconds to force restart
- From fastboot:
  ```{prompt} bash $
  fastboot reboot
  ```
- Last resort: Drain battery, recharge, restart
