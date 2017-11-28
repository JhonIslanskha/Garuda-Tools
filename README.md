What is GarudaTools v1.10?
========================

GarudaTools adalah kerangka sederhana yang telah dibuat untuk alat uji penetrasi. Kerangka GarudaTools menawarkan struktur sederhana, CLI dasar, dan fitur yang berguna untuk alat uji penetrasi yang berkembang. GarudaTools pada tahap awal dan mungkin tidak stabil,  GarudaTools berada di bawah lisensi Master Linux Indonesia, dengan kata lain Anda dapat melakukan apa yang Anda inginkan dengan kode sumbernya.

Apa yang harus saya jalankan? GarudaTools?
========================================

GarudaTools ditulis dalam python 3, dan dikembangkan terutama di Arch Linux. Jadi Anda harus mendapatkan kerangka kerja GarudaTools yang berjalan dengan sistem operasi berbasis Linux, python 3.5, dan dependensi.

OS support
==========

Linux       supported, and developed on/for linux
OS X        support not planned
Windows     support not planned

Fitur dasar
==============

GarudaTools fitur dasar CLI untuk memuat dan menjalankan alat pengujian penetrasi, antarmuka scripting sederhana, dan python api.

Jumlah Total Modules: 25
=======================
* apache_users
* arp_dos
* arp_monitor
* arp_spoof
* bluetooth_pod
* cloudflare_resolver
* dhcp_dos
* dir_scanner
* dns_spoof
* email_bomber
* hostname_resolver
* mac_spoof
* mitm
* network_kill
* pma_scanner
* port_scanner
* proxy_scout
* whois
* web_killer
* web_scout
* wifi_jammer
* zip_cracker
* rar_cracker
* wordlist_gen
* hijacking_king

Ketergantungan
==============

GarudaTools sendiri tidak membutuhkan apa-apa selain python 3.5, tapi pemindai jaringan itu membutuhkan tcpdump. GarudaTools mencakup semua dependensi python sehingga Anda tidak perlu menginstalnya. Semua dependensi modul tercantum di bawah ini. ettool, aircrack-ng, ettercap-text-only, dsniff, xterm, driftnet, tcpdump, libnetfilter-queue-dev, python3.5-dev, hcitool, sslstrip, l2ping

Web pages
=========

* Official website: http://Jalansawa.bloggspot.co.id
* Github: https://github.com/JhonIslanskha/GarudaTools

GarudaTools berada di bawah lisensi Jh0n 1sl4nskh4_404