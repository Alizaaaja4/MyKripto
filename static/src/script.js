function toggleKeyInput() {
    const cipherType = document.getElementById("cipher-type").value;
    const keyInputContainer = document.getElementById("key-input-container");
    const rsaKeyInputContainer = document.getElementById("rsa-key-input-container");

    // Show or hide key input fields based on the selected cipher
    if (cipherType === "caesar" || cipherType === "vigenere") {
        keyInputContainer.classList.remove("hidden");
        rsaKeyInputContainer.classList.add("hidden");
    } else if (cipherType === "rsa") {
        rsaKeyInputContainer.classList.remove("hidden");
        keyInputContainer.classList.add("hidden");
    } else {
        keyInputContainer.classList.add("hidden");
        rsaKeyInputContainer.classList.add("hidden");
    }
}