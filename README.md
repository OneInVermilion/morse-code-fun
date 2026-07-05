# morse-code-fun

A flexible Morse code encoder and decoder that supports multiple input and output formats, customizable signal representations, and the extended Morse alphabet.

## Features

* **Translate between multiple formats**

  * Plain text ↔ Morse code symbols (`.` and `-`)
  * Morse code symbols ↔ Morse code signals

* **Customizable representations**

  * Configure the characters used for:
    * Dots
    * Dashes
    * Signal (`1`)
    * Silence (`0`)

Makes it easy to adapt the script for custom protocols or alternative Morse representations.

* **Extended Morse alphabet**

  * Supports letters, numbers, punctuation, and other symbols included in the extended International Morse code standard.

## Morse Signal Encoding

The signal representation follows the standard Morse timing rules:

| Element                                    | Representation |
| ------------------------------------------ | -------------- |
| Dot                                        | `1`            |
| Dash                                       | `111`          |
| Gap between dots/dashes within a character | `0`            |
| Gap between letters                        | `000`          |
| Gap between words                          | `0000000`      |

## Customization

The script allows customization of the representations used during encoding and decoding. For example, you can define your own symbols for:

* Dot
* Dash
* Signal (logical `1`)
* Silence (logical `0`)
