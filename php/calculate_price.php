<?php

function calculatePrice(float $unitPrice, int $quantity) {
    return $unitPrice * $quantity;
}

$total1 = calculatePrice(125.30, 3);
$total2 = calculatePrice(69.20, 4);
$total3 = calculatePrice(76, 1);
echo "$total1\n";
echo "$total2\n";
echo "$total3\n";

?>
