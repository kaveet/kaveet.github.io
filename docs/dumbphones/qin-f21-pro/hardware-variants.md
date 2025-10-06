# Hardware Variants

{{ mt8766_warning }}

The Qin F21 Pro comes in a handful of configurations that differ in memory/storage capacity, color options, and keyboard layouts.

## Base Specifications

All Qin F21 Pro variants share these core specs:

| Component | Specification |
|-----------|--------------|
| **Display** | 2.8-inch IPS capacitive touchscreen, 480x640 pixels (portrait) |
| **Processor** | MediaTek Helio A22 (MT6761), quad-core up to 2.0 GHz* |
| **GPU** | PowerVR Rogue GE8300 |
| **Rear Camera** | 5MP with autofocus and LED flash |
| **Battery** | 2,120mAh with 7.5W fast charging (USB Type-C) |
| **Dimensions** | 132×53×9.5mm |
| **Weight** | 102g |
| **Connectivity** | Wi-Fi, Bluetooth 5.0, GPS, hotspot, infrared remote control |
| **Audio** | Dual microphones (main + noise reduction) |

*\*Note: Some later F21 Pro units were manufactured with the MT8766 processor instead of the MT6761. This guide covers MT6761 devices only.*

## What's NOT Included

Before purchasing, it's important to understand what the F21 Pro lacks compared to modern smartphones:

| Missing Feature | Notes |
|-----------------|--------|
| **No microSD card slot** | Storage cannot be expanded beyond the built-in 32GB or 64GB |
| **No 3.5mm headphone jack** | USB-C to 3.5mm adapters CAN be used |
| **No NFC** | Cannot use for contactless payments (Google Pay, etc.) or NFC tags |
| **No fingerprint sensor** | Security relies on PIN/pattern/password only |
| **No wireless charging** | Charging only via USB Type-C cable |
| **No stereo speakers** | Single mono speaker only |
| **No water/dust resistance rating** | Not officially rated for IP certification |
| **No 5G support** | Maximum network speed is 4G LTE |
| **No notification LED** | No LED indicator for missed notifications |

## Memory and Storage Variants

The F21 Pro is available in two primary hardware configurations. **This is the most important distinction** when purchasing, as it affects both performance and price:

| RAM | Storage | Notes |
|-----|---------|-------|
| 3GB | 32GB | Lower-cost option, suitable for basic use |
| 4GB | 64GB | Better multitasking performance, recommended for most users |

The community reports that the 4GB variant runs noticeably smoother, particularly when using multiple apps or Google Play services. Both variants use LPDDR3 memory. **Neither model supports microSD card expansion**, so choose your storage capacity carefully.

## Color Options

The F21 Pro is officially available in two colors:

- **Porcelain White** (also called simply "White")
- **Iron Grey** (also called "Black")

Both colors feature the same matte finish and are identical in every aspect except appearance. The outer screen covering and the colored face plate are a single part.

## Keyboard Layouts

The physical keyboard layout varies. The most common layouts are:

- English/Latin
- Russian
- Hebrew

## Regional Models

While not officially designated as different models, F21 Pro units sold in different regions may vary in the following ways.

### Default Language Support

- **Chinese models**: Chinese, with possible bloatware and Chinese-specific apps
- **Global/International models**: Multi-language support, typically including English, with varying degrees of translation completeness

### Pre-installed Software

The phone comes in different software configurations that you'll want to pay close attention to. See the [Software Variants](software-variants) section for more.

## Cellular Band Support

This is a critical consideration for users, particularly those in the United States. The F21 Pro's advertised band support differs from what can be unlocked through modification.

### Advertised (Out-of-Box) Bands

| Network Type | Supported Bands |
|--------------|-----------------|
| **2G GSM** | 850 / 900 / 1800 / 1900 |
| **3G WCDMA/UMTS** | 850 / 900 / 2100 |
| **4G LTE – FDD** | B1 / B3 / B5 / B7 / B8 |
| **4G LTE – TDD** | B38 / B40 / B41 |

### Important US Band Limitations

Out of the box, the F21 Pro has limited functionality in the United States. While it includes some compatible bands (notably B2 and B4), it lacks crucial US carrier bands including **B12, B13, B66, and B71**. This results in:

- **Partial T-Mobile compatibility** - Works in some areas but with coverage gaps
- **Limited AT&T compatibility** - Service is generally unreliable
- **Poor Verizon compatibility** - Even when functional, service is inconsistent (requires CDMA-less mode activation)

### US Band Unlocking (Post-Modification)

The F21 Pro can be modified to support additional US bands by flashing modem files from the Qin F30 (the US-market variant). After this modification, the phone can support:

**LTE Bands**: B2, B4, B12, B13, B17, B66, B71

This modification process is detailed in the [Enabling US Bands](guides/enabling-us-bands) guide. **However, there's an important caveat from the community**: Some users report that while the phone will display these bands as available in engineering mode after modification, the actual hardware may not fully utilize all bands as effectively as a native F30 device. The modification enables the software to recognize and attempt to use these bands, but real-world signal performance may vary by location and carrier.

For the best US compatibility, consider:

- **T-Mobile and T-Mobile MVNOs** (Mint Mobile, US Mobile): Generally work best after modification
- **AT&T**: Not recommended even after modification
- **Verizon**: Possible but requires special account configuration (CDMA-less mode) and only works reliably with postpaid plans

## Xiaomi vs. Duoqin: Manufacturing Relationship

There's often confusion about who actually manufactures the F21 Pro. Here's the clarification:

The **Qin F21 Pro is manufactured by Shenzhen Duoqin Technology Co., Ltd.**, not directly by Xiaomi. Duoqin is part of the Xiaomi ecosystem (similar to how companies like Amazfit or Roborock operate within the Xiaomi chain), which is why the phone is sometimes marketed as "Xiaomi Qin F21 Pro" or simply "Duoqin F21 Pro."

In practical terms, when searching for ROMs, guides, or specifications, you may find the device listed under either "Xiaomi Qin F21 Pro" or "Duoqin F21 Pro"--these refer to the same device.

