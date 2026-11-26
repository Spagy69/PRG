<?php
function findMaximum(&$maximum, ...$numbers) {
    if (empty($numbers)) {
        $maximum = null;
        return;
    }
    $maximum = max($numbers);
}

$max = null;

findMaximum($max, 12, 45, 8, 32);
echo $max . "\n";

findMaximum($max, -5, -10, -3, -20);
echo $max . "\n";

findMaximum($max);
echo ($max === null ? "null" : $max) . "\n";
?>