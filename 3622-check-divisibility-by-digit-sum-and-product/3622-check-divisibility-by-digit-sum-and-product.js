var checkDivisibility = function(n) {
    let sum = 0;
    let product = 1;

    let x = n;

    while (x > 0) {
        const digit = x % 10;
        x = Math.floor(x / 10);

        sum += digit;
        product *= digit;
    }

    return n % (sum + product) === 0;
};