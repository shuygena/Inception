<?php

define( 'WP_DEBUG', true );
define( 'WP_DEBUG_DISPLAY', false );
define( 'WP_DEBUG_LOG', true );

define( 'DB_NAME', '_db_name' );
define( 'DB_USER', '_db_user' );
define( 'DB_PASSWORD', '_db_password' );
define( 'DB_HOST', '_db_host' );
define( 'DB_CHARSET', 'utf8' );
define( 'DB_COLLATE', '' );

define('AUTH_KEY',         'Oe+Me -UmoS-shPMmMO`?Z#F_YM;k)-9Z;NHAv&Zm@3pqBZI;0JE%bjm<4bG_V&p');
define('SECURE_AUTH_KEY',  '<JZ8W*+?kjZ=pGCki+o;A|Vk+5r-V$pBx)}^&#{+.i(Gp~hSUFVr|a|)t5Nva3Df');
define('LOGGED_IN_KEY',    'vU;iPf$:wz(%6&O{7?0+i17UBq}{w3ob^aVgs`&xjX=^6{/09p?|pAeE`bX+&%$@');
define('NONCE_KEY',        'I;gV#k@ABY(;n&Sr`|Pn1/!_gQI7u/;z.&2=0/D6wYq_3/R0mK5NVwi|d+9cfC.+');
define('AUTH_SALT',        'Sh!(>JU@Ns:_W$z_+(Z|Ub-$+QIg-wMX~II;QC&ZR<|R:W&y#Y:8l+3@!C&|LaC]');
define('SECURE_AUTH_SALT', '9|4=^J[t?;A,o-YU~GBZ|<;D+4/jp3a](OCtb8D-RkT*zo):SIIR;z=#krteC$[$');
define('LOGGED_IN_SALT',   '3&:oh-PTnS.~hL=!m7d[K{2GdMW7f6GN-N)sNj%LQQJ=dO?jq|$rxdk[kV1O;dh5');
define('NONCE_SALT',       'wAF4%x5i,9Z6 MG)`fg3[y/LZqj;pNw >Q>{w$6]FcB,8sM/8R&,<Zcd!Hq|f/<2');

$table_prefix = 'wp_';

if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

require_once ABSPATH . 'wp-settings.php';