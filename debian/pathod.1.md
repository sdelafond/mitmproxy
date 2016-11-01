% pathod(1)
%
% November 2016

# NAME

pathod - a pathological HTTP/S daemon

# SYNOPSIS

pathod [-h] [\--version] [-p *PORT*] [-l *ADDRESS*] [-a *ANCHOR*]\
\ \ \ \ \ \ \ [-c *CRAFTANCHOR*] [\--confdir *CONFDIR*] [-d *STATICDIR*] [-D]\
\ \ \ \ \ \ \ [-t *TIMEOUT*] [\--limit-size *SIZELIMIT*] [\--nohang] [\--nocraft]\
\ \ \ \ \ \ \ [\--webdebug] [-s] [\--cn *CN*] [-C] [\--cert *SPEC*]\
\ \ \ \ \ \ \ [\--ciphers *CIPHERS*] [\--san *SAN*]\
\ \ \ \ \ \ \ [\--ssl-version {`all`|`TLSv1_2`|`secure`|`TLSv1_1`|`TLSv1`|`SSLv3`|`SSLv2`}]\
\ \ \ \ \ \ \ [-e] [-f *LOGFILE*] [-q] [-r] [-x] [\--http2-framedump]

# DESCRIPTION

`pathod` is a pathological HTTP daemon designed to let you craft almost
any conceivable HTTP response, including ones that creatively violate the
standards. HTTP responses are specified using a small, terse language which
`pathod` shares with its evil twin, `pathoc`. To start playing with pathod,
fire up the daemon:

```
$ pathod
```

By default, the service listens on port `9999` of `localhost`, and the
default crafting anchor point is the path `/p/`. Anything after this URL
prefix is treated as a response specifier. So, hitting the following URL
will generate an HTTP 200 response with 100 bytes of random data:

```
http://localhost:9999/p/200:b@100
```

See the
[language documentation](http://docs.mitmproxy.org/en/latest/pathod/language.html#language)
to get (much) fancier.

# OPTIONS

## Optional Arguments:

-h, \--help
:   Show this help message and exit.

\--version
:   Show program's version number and exit.

-p *PORT*
:   Port. Specify `0` to pick an arbitrary empty port. (Default: `9999`)

-l *ADDRESS*
:   Listening address. (Default: `127.0.0.1`)

-a *ANCHOR*
:   Add an anchor. Specified as a string with the form `pattern=spec` or
    `pattern=filepath`, where pattern is a regular expression.

-c *CRAFTANCHOR*
:   URL path specifying prefix for URL crafting commands. (Default: `/p/`)

\--confdir *CONFDIR*
:   Configuration directory. (Default: `~/.mitmproxy`)

-d *STATICDIR*
:   Directory for static files.

-D
:   Daemonize.

-t *TIMEOUT*
:   Connection timeout.

\--limit-size *SIZELIMIT*
:   Size limit of served responses. Understands size suffixes, e.g. 100k.

\--nohang
:   Disable pauses during crafted response generation.

\--nocraft
:   Disable response crafting. If anchors are specified, they still work.

\--webdebug
:   Debugging mode for the web app (dev only).

## SSL:

-s
:   Run in HTTPS mode.

\--cn *CN*
:   CN for generated SSL certs. (Default: `pathod.net`)

-C
:   Don't expect SSL after a CONNECT request.

\--cert *SPEC*
:   Add an SSL certificate. SPEC is of the form `"[domain=]path"`. The domain
    may include a wildcard, and is equal to `"*"` if not specified. The file
    at path is a certificate in PEM format. If a private key is included
    in the PEM, it is used, otherwise the default key in the conf dir is
    used. Can be passed multiple times.

\--ciphers *CIPHERS*
:   SSL cipher specification.

\--san *SAN*
:   Subject Altnernate Name to add to the server certificate. May be passed
    multiple times.

\--ssl-version {`all`|`TLSv1_2`|`secure`|`TLSv1_1`|`TLSv1`|`SSLv3`|`SSLv2`}
:   Set supported SSL/TLS versions. `SSLv2`, `SSLv3` and `all` are
    INSECURE. Defaults to `secure`, which is TLS1.0+.

## Controlling Logging:

Some of these options expand generated values for logging. If you're
generating large data, use them with caution.

-e
:   Explain responses.

-f *LOGFILE*
:   Log to file.

-q
:   Log full request.

-r
:   Log full response.

-x
:   Log request/response in hexdump format.

\--http2-framedump
:   Output all received & sent HTTP/2 frames.

# AUTHORS

`pathod` was written by Aldo Cortesi.

This manual page was written for the Debian GNU/Linux system, but its use
elsewhere is encouraged.

# SEE ALSO

`pathod` documentation and examples are available online at
<http://docs.mitmproxy.org/en/latest/pathod/intro.html#pathod>.
