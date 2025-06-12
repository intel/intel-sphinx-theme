"use strict";

function documentReady(callback) {
  if (document.readyState != "loading") callback();
  else document.addEventListener("DOMContentLoaded", callback());
}

/**
 * Set the header variant.
 * It can be one of ["spark-color", "spark-squares", "default"]
 *
 * @param {str} variant
 */

function setHeaderVariant(variant) {
    if (variant !== "spark-color" && variant !== "spark-squares" && variant !== "default") {
      console.error(`Got invalid header variant: ${variant}. Resetting to default.`);
      localStorage.setItem("header", "default");
    } else {
      localStorage.setItem("header", variant);
    }
}

function addVariantListener() {
  setHeaderVariant(document.documentElement.dataset.header);
}

/**
 * Set the footer variant.
 * It can be one of ["simple", "line", "default"]
 *
 * @param {str} variant
 */

function setFooterVariant(variant) {
    if (variant !== "simple" && variant !== "line" && variant !== "default") {
      console.error(`Got invalid footer variant: ${variant}. Resetting to default.`);
      localStorage.setItem("footer", "default");
    } else {
      localStorage.setItem("footer", variant);
    }
}

function addFooterListener() {
  setFooterVariant(document.documentElement.dataset.footer);
}

/**
 * Set the content width variant.
 * It can be one of ["small", "medium", "large"]
 *
 * @param {str} widthVariant
 */

function setContentWidthVariant(widthVariant) {
  if (widthVariant !== "small" && widthVariant !== "medium" && widthVariant !== "large") {
    console.error(`Got invalid content width variant: ${widthVariant}. Resetting to default.`);
    localStorage.setItem("contentWidth", "medium");
  } else {
    localStorage.setItem("contentWidth", widthVariant);
  }
}

function addContentWidthVariantListener() {
  setContentWidthVariant(document.documentElement.dataset.contentWidth);
}

documentReady(addVariantListener);
documentReady(addFooterListener);
documentReady(addContentWidthVariantListener);

var prevScrollPos = window.scrollY;
window.onscroll = function() {
  var currentScrollPos = window.scrollY;
  if (currentScrollPos != 0) {
    // Scrolling down
    document.getElementById("spark-header-s2").classList.add("hidden");
    document.getElementById("spark-header-s3").classList.add("hidden");
  } else {
    // Scrolling up
    document.getElementById("spark-header-s2").classList.remove("hidden");
    document.getElementById("spark-header-s3").classList.remove("hidden");
  }
  prevScrollPos = currentScrollPos;
};

// Code block line wrap
document.addEventListener('DOMContentLoaded', () => {
  const codeBlocks = document.querySelectorAll('div.highlight pre, div.highlight code');

  const wrapIcon = `<svg xmlns="http://www.w3.org/2000/svg" fill="#000000" width="16px" height="16px" viewBox="0 0 24 24">
      <path d="M4 19h6v-2H4v2zM20 5H4v2h16V5zm-3 6H4v2h13.25c1.1 0 2 .9 2 2s-.9 2-2 2H15v-2l-3 3 3 3v-2h2c2.21 0 4-1.79 4-4s-1.79-4-4-4z"/>
  </svg>`;

  const addWrapButton = (parent) => {
    const button = document.createElement('button');
    button.innerHTML = wrapIcon;
    button.className = 'linewrap-button';
    button.title = 'Toggle line wrap';
    button.onclick = () => {
      parent.classList.toggle('wrapped');
      parent.querySelectorAll('pre, code').forEach(block => {
        block.style.whiteSpace = parent.classList.contains('wrapped') ? 'pre-wrap' : 'pre';
      });
      parent.classList.add('scrollable');
    };
    parent.style.position = 'relative';
    parent.appendChild(button);
  };

  const checkAndAddButton = (parent) => {
    const pre = parent.querySelector('pre');
    if (pre && (pre.scrollWidth > pre.clientWidth || parent.classList.contains('wrapped'))) {
      if (!parent.querySelector('.linewrap-button')) {
        addWrapButton(parent);
      }
      parent.classList.add('scrollable');
    } else if (!parent.classList.contains('wrapped')) {
      parent.classList.remove('scrollable');
    }
  };

  codeBlocks.forEach((block) => {
    const parent = block.parentElement;
    checkAndAddButton(parent);
    new ResizeObserver(() => checkAndAddButton(parent)).observe(parent);
  });
});
