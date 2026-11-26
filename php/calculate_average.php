<?php

function calculateAverage(...$numbers): float {
    $filteredNumbers = array_filter($numbers, fn($num) => is_int($num) || is_float($num));
    if (count($filteredNumbers) === 0) {
        return 0.0;
    }
    return array_sum($filteredNumbers) / count($filteredNumbers);
}

echo calculateAverage(1, 2.5, 3, 4.7, 5) . "\n";
echo calculateAverage(10, 20) . "\n";
echo calculateAverage("abc", 5, 10.5) . "\n";
echo calculateAverage() . "\n";

?>