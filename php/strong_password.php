<?php

function isStrongPassword(string $password) {
    if (strlen($password) < 8) {
        return false;
    } else if (!preg_match('/[A-Z]/', $password)) {
        return false;
    } else if (!preg_match('/[0-9]/', $password)) {
        return false;
    }
    return true;
}

$password1 = isStrongPassword("Password123");
$password2 = isStrongPassword("heslo123");
$password3 = isStrongPassword("Samuel69");
$password4 = isStrongPassword("adamec1");

if ($password1) {
    echo "Password 1 is strong\n";
} else {
    echo "Password 1 is weak\n";
}

if ($password2) {
    echo "Password 2 is strong\n";
} else {
    echo "Password 2 is weak\n";
}

if ($password3) {
    echo "Password 3 is strong\n";
} else {
    echo "Password 3 is weak\n";
}

if ($password4) {
    echo "Password 4 is strong\n";
} else {
    echo "Password 4 is weak\n";
}

?>