class Token {
    constructor(text, index) {
        this.text = text;
        this.index = index;

        // Classify the token.
        if (/^[A-Za-z_]/.test(text)) {
            this.kind = 'identifier';
        } else if (/^[0-9]/.test(text)) {
            this.kind = 'number';
        } else {
            this.kind = 'operator';
        }
    }
}
