<?php

function normalizeValues(&...$values) {
    foreach ($values as &$value) {
        if ($value < 0) {
            $value = 0;
        } elseif ($value > 100) {
            $value = 100;
        }
    }
}

$a = -15;
$b = 25;
$c = 150;
$d = 75;
$e = 0;

normalizeValues($a, $b, $c, $d, $e);

var_dump($a, $b, $c, $d, $e);