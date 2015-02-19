# Aviation Weather Summarizer (avwxsummarizer)

[![Build Status](https://travis-ci.org/NicholasMerrill/avwxsummarizer.svg?branch=master)](https://travis-ci.org/NicholasMerrill/avwxsummarizer)

The Summarizer gives you a quick picture of the important weather components
for your flight today, checking the current METARs for basic warning
indicators.

**This library uses highly arbitrary thresholds and should not be relied
upon as a primary aviation resource. It also relies on
[avwx](https://github.com/NicholasMerrill/avwx), a library that is under
development and potentially unstable.**

## Installation

1. `pip install avwxsummarizer`

## Examples

### As a script

Go ahead and use it right from the shell if you're feeling lazy.

![Shell usage example](http://i.imgur.com/YzBaP2m.png)

## Coming Soon

The Summarizer will soon take into account the following:

* TAFs
* Winds aloft
* SIGMETs
* AIRMETs
* PIREPs

It will also allow specification of wheels-up time to allow looking ahead
to tomorrow's weather instead of the default (current weather).

