// ==UserScript==
// @name         Script cifrado
// @namespace    http://tampermonkey.net/
// @version      0.1
// @updateURL    
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/Martín/Desktop/mensaje.html
// @icon         https://www.google.com/s2/favicons?domain=google.com
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==

//const CryptoJS = require('crypto-js')
		// Tomo las clases del html para poder manejarlas.
const keyHex = CryptoJS.enc.Utf8.parse(document.getElementsByClassName('key')[0].id)
const iv1 = document.getElementsByClassName('vector')[0].id;
const mensaje = document.getElementsByClassName('algoritmo')[0].id;

var iv2=CryptoJS.enc.Utf8.parse(iv1);

// Desencriptando el mensaje.

var decoded = CryptoJS.DES.decrypt(
	{ciphertext: CryptoJS.enc.Hex.parse(document.getElementsByClassName('algoritmo')[0].id)},
	keyHex,{
		iv: iv2,
		mode: CryptoJS.mode.OFB,
		padding: CryptoJS.pad.NoPadding});
console.log(decoded.toString(CryptoJS.enc.Utf8))