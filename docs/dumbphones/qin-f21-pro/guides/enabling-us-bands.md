# Enabling US Bands

{{ mt8766_warning_subdir }}

## Overview

Enable additional US LTE bands on the Qin F21 Pro by transplanting modem configuration from the Qin F30, a US-market variant. This modification adds support for bands 2, 4, 12, 13, 17, 66, and 71—enabling compatibility with major US carriers like T-Mobile and Verizon.

```{admonition} What you'll accomplish
- Enable US LTE bands (2, 4, 12, 13, 17, 66, 71)
- Improve compatibility with US carriers
- Maintain device functionality
```

```{danger}
**Advanced Modification:** This requires an unlocked bootloader and flashing critical system partitions. Errors can result in lost network connectivity or device brick. Windows PC required.
```

This guide uses modem files from the Qin F30, community-extracted scatter files, SP Flash Tool for flashing, and SN Write Tool for identifier restoration.

## Understanding the Modification

### The F30 Connection

The Qin F30 is a US-market variant of the F21 Pro with identical hardware but US-optimized cellular bands. This modification replaces three NV partitions (`nvram`, `nvdata`, `nvcfg`) and the modem image (`md1img_a`) with F30 versions, enabling frequencies already supported in hardware but disabled in software.

### Supported Bands After Modification

- **LTE Band 2** (1900 MHz) - AT&T, T-Mobile, Verizon
- **LTE Band 4** (1700/2100 MHz) - T-Mobile, AT&T
- **LTE Band 12** (700 MHz) - T-Mobile extended range
- **LTE Band 13** (700 MHz) - Verizon primary
- **LTE Band 17** (700 MHz) - AT&T primary
- **LTE Band 66** (AWS) - T-Mobile, AT&T capacity
- **LTE Band 71** (600 MHz) - T-Mobile extended range

### Hardware Limitations

The F21 Pro's antenna design was optimized for Chinese frequencies. Bands 12, 13, 17, and 71 (lower frequencies) often show weaker reception than US-designed phones. Bands 2, 4, and 66 typically perform better. Performance is adequate in strong signal areas but may struggle in fringe coverage.

## Prerequisites

### Software & Tools (Windows Only)

- Windows PC (7 or newer, 64-bit recommended)
- Python (latest version, with "Add to PATH" enabled)
- [MTKClient](https://github.com/bkerler/mtkclient)
- SP Flash Tool
- SN Write Tool
- MediaTek USB VCOM drivers
- F30 US Bands Package (modem files, scatter file, databases)

### Device Requirements

- **Unlocked bootloader** (see [Unlocking the Bootloader](unlocking-bootloader.md))
- Battery charged to 80%+
- Quality USB data cable

## Critical: Record Your Identifiers

```{danger}
**DO NOT SKIP:** Flashing F30 partitions overwrites your unique identifiers with dummy values. You **must** record and restore them.
```

### Record These Values

Navigate to **Settings → About Phone** and record:

- **IMEI** (15 digits, usually starts with 86...)
- **Wi-Fi MAC address** (format: `XX:XX:XX:XX:XX:XX`)
- **Bluetooth address** (format: `XX:XX:XX:XX:XX:XX`)

Save these in a text file named `my-f21-identifiers.txt`. You'll enter them manually into SN Write Tool later.

## Installation Steps

### Step 1: Install Prerequisites

1. **Install Python:**
   ```{prompt} bash
   # Download from python.org
   # Check "Add Python to PATH" during installation
   python --version
   ```

2. **Install MTKClient:**
   ```{prompt} bash
   cd C:\mtkclient
   pip3 install -r requirements.txt
   ```

3. **Install MediaTek USB VCOM drivers**
   - Run installer from extracted package
   - Restart computer after installation

4. **Extract SP Flash Tool** to `C:\SPFlashTool`

5. **Extract SN Write Tool** from F30 package

### Step 2: Back Up NV Partitions

Create recovery backups before modification:

1. **Power off device**

2. **Run backup command:**
   ```{prompt} bash
   cd C:\mtkclient
   python mtk r nvram,nvdata,nvcfg nvram_backup.bin,nvdata_backup.bin,nvcfg_backup.bin
   ```

3. **Enter BROM mode:**
   - Hold **Volume Up + Volume Down**
   - While holding, plug in USB cable
   - Keep holding until MTKClient detects device

4. **Wait for completion** (1-2 minutes)

**Optional full backup:**
```{prompt} bash
python mtk rl --skip userdata f21_full_backup
```

### Step 3: Flash F30 Modem and NV Partitions

1. **Launch SP Flash Tool:**
   - Run `flash_tool.exe` as Administrator
   - Click **Scatter-loading**
   - Select `MT6761_Android_scatter.txt` from F30 package

2. **Configure partitions:**
   - **UNCHECK ALL partitions**
   - Check **ONLY** these four:
     - `nvcfg`
     - `nvdata`
     - `nvram`
     - `md1img_a`

   ```{danger}
   **Critical:** Verify `preloader` is unchecked. Flashing wrong preloader will brick your device.
   ```

3. **Verify file paths:**
   - Click each checked partition
   - Confirm path points to correct `.img` file from F30 package

4. **Flash partitions:**
   - Click **Download** button
   - Power off device
   - Hold **Back button** (top right)
   - While holding, plug in USB cable
   - SP Flash Tool will auto-detect and flash
   - Wait for green "Download OK" checkmark
   - Disconnect USB

### Step 4: Restore Identifiers with SN Write Tool

1. **Launch SN Write Tool:**
   - Run `SN_Writer.exe` as Administrator

2. **Configure settings:**
   - Click **System Config**
   - In **Write Option**, check only:
     - ☑ IMEI
     - ☑ BT Address
     - ☑ Wifi Address
   - Under **IMEI Option**, select **Dual IMEI**

3. **Load database files:**
   - Check "Load AP DB from DUT"
   - Check "Load Modem DB from DUT"
   - Click **MD1_DB** → Select `MDDB_InfoCustomAppSrcP_MT6761...` from `AP DB Base\MT6761`
   - Click **AP_DB** → Select `APDB_MT6761...` from same folder
   - Click **Save**

4. **Write identifiers:**
   - Click **Start**
   - Enter your values from recorded identifiers:
     - **IMEI_1:** Your original IMEI
     - **BT Address:** Your Bluetooth MAC
     - **Wifi Address:** Your Wi-Fi MAC
   - Click **OK**

5. **Flash identifiers:**
   - Power off device
   - Hold **Back button**
   - While holding, plug in USB cable
   - Wait for green **PASS** message
   - Disconnect USB

### Step 5: Verification

1. **Check identifiers:**
   - Power on device
   - Go to **Settings → About Phone**
   - Verify IMEI and MAC addresses match your recorded values

2. **Verify enabled bands:**
   - Dial `*#*#3646633#*#*` to open Engineer Mode
   - Tap **Telephony** → **Band Mode**
   - Confirm LTE bands 2, 4, 12, 13, 17, 66, 71 are enabled

   ```{warning}
   Do not change settings in Engineer Mode unless you know what you're doing.
   ```

3. **Test connectivity:**
   - Insert US carrier SIM
   - Enable mobile data in **Settings → Network & internet**
   - Verify LTE icon appears
   - Make test call and browse web

## Troubleshooting

### No IMEI or Invalid IMEI

**Cause:** Step 4 skipped or SN Write Tool failed.

**Solution:**
- Repeat Step 4, carefully entering YOUR original IMEI
- Check IMEI on device box or under battery (if accessible)

### Signal Shows But No Network Connection

**Cause:** Carrier hasn't activated IMEI, or weak signal area.

**Solution:**
- Contact carrier to refresh IMEI on network
- Reset network settings: **Settings → System → Reset → Reset Wi-Fi, mobile & Bluetooth**

### SP Flash Tool "PMT Changed" Error

**Cause:** Scatter file partition layout mismatch.

**Solution:**
- Verify using scatter file from F30 US Bands Package
- Confirm F21 Pro is 4GB/64GB variant

### SP Flash Tool Doesn't Detect Device

**Cause:** Drivers not installed or incorrect button timing.

**Solution:**
- Verify MediaTek VCOM drivers in Device Manager
- Use USB 2.0 port instead of USB 3.0
- Confirm holding **Back button** (top right) while plugging in
- Try different USB cable

### Weak Signal After Modification

**Cause:** Expected hardware limitation—antenna design not optimized for US frequencies.

**Solution:**
- Normal behavior for bands 12, 13, 17, 71
- Performance better on bands 2, 4, 66
- Consider carrier using bands 2/4 primarily (T-Mobile urban areas)
- No software fix available

## Reverting to Chinese Bands

1. **Restore NV partitions:**
   ```{prompt} bash
   python mtk w nvram,nvdata,nvcfg nvram_backup.bin,nvdata_backup.bin,nvcfg_backup.bin
   ```

2. **Flash stock Chinese modem** with SP Flash Tool

3. **Original identifiers** restore automatically from backup
