% MITMWEB(1)
%
% November 2016

# NAME

mitmweb - a man-in-the-middle proxy with a web interface

# SYNOPSIS

mitmweb [*options*]

# DESCRIPTION

`mitmweb` provides a web interface to `mitmproxy`.

# OPTIONS

## Optional Arguments:

-h, \--help
:   Show this help message and exit.

\--conf *CONFIG_FILE*
:   Config file path.

\--version
:   Show program's version number and exit.

\--sysinfo
:   Show system info and exit.

\--shortversion
:   Show program's short version number and exit.

\--anticache
:   Strip out request headers that might cause the server to return
    304-not-modified.

\--cadir *CA_DIR*
:   Location of the default `mitmproxy` CA files. (Default: `~/.mitmproxy`)

\--host
:   Use the Host header to construct URLs for display.

-q, \--quiet
:   Quiet.

-r *RFILE*, \--read-flows *RFILE*
:   Read flows from file.

-s "script.py \--bar", \--script "script.py \--bar"
:   Run a script. Surround with quotes to pass script arguments. Can be
    passed multiple times.

-t *FILTER*, \--stickycookie *FILTER*
:   Set sticky cookie filter. Matched against requests.

-u *FILTER*, \--stickyauth *FILTER*
:   Set sticky auth filter. Matched against requests.

-v, \--verbose
:   Increase log verbosity.

-w *OUTFILE*, \--wfile *OUTFILE*
:   Write flows to file.

-a *OUTFILE*, \--afile *OUTFILE*
:   Append flows to file.

-z, \--anticomp
:   Try to convince servers to send us un-compressed data.

-Z *SIZE*, \--body-size-limit *SIZE*
:   Byte size limit of HTTP request and response bodies. Understands k/m/g
    suffixes, e.g. 3m for 3 megabytes.

\--stream *SIZE*
:   Stream data to the client if response body exceeds the given
    threshold. If streamed, the body will not be stored in any
    way. Understands k/m/g suffixes, e.g. 3m for 3 megabytes.

\--upstream-auth *UPSTREAM_AUTH*
:   Proxy Authentication: `username:password`

## Mitmweb:

\--wport *PORT*
:   Mitmweb port.

\--wiface *IFACE*
:   Mitmweb interface.

\--wdebug
:   Turn on mitmweb debugging.

\--wsingleuser *USER*
:   Allows access to a single user, specified in the form
    `username:password`.

\--whtpasswd *PATH*
:   Allow access to users specified in an Apache htpasswd file.

## Proxy Modes:

-R *REVERSE_PROXY*, \--reverse *REVERSE_PROXY*
:   Forward all requests to upstream HTTP server:
    `http[s]://host[:port]`. Clients can always connect both via HTTPS and
    HTTP, the connection to the server is determined by the specified scheme.

\--socks
:   Set SOCKS5 proxy mode.

-T, \--transparent
:   Set transparent proxy mode.

-U *UPSTREAM_PROXY*, \--upstream *UPSTREAM_PROXY*
:   Forward all requests to upstream proxy server: `http://host[:port]`

## Proxy Options:

-b *ADDR*, \--bind-address *ADDR*
:   Address to bind proxy to (defaults to all interfaces).

-I *HOST*, \--ignore *HOST*
:   Ignore host and forward all traffic without processing it. In
    transparent mode, it is recommended to use an IP address (range),
    not the hostname. In regular mode, only SSL traffic is ignored and
    the hostname should be used. The supplied value is interpreted as
    a regular expression and matched on the ip or the hostname. Can be
    passed multiple times.

\--tcp *HOST*
:   Generic TCP SSL proxy mode for all hosts that match the pattern. Similar
    to `--ignore`, but SSL connections are intercepted. The communication
    contents are printed to the log in verbose mode.

-n, \--no-server
:   Don't start a proxy server.

-p *PORT*, \--port *PORT*
:   Proxy service port.

\--no-http2
:   Explicitly disable HTTP/2 support. If your OpenSSL version supports
    ALPN, HTTP/2 is enabled by default.

\--raw-tcp | \--no-raw-tcp
:   Explicitly enable/disable experimental raw tcp support. Disabled by
    default. Default value will change in a future version.

\--websockets | \--no-websockets
:   Explicitly enable/disable experimental WebSocket support. Disabled
    by default as messages are only printed to the event log and not
    retained. Default value will change in a future version.

\--spoof-source-address
:   Use the client's IP for server-side connections.

## SSL:

\--cert *SPEC*
:   Add an SSL certificate. SPEC is of the form `"[domain=]path"`. The domain
    may include a wildcard, and is equal to `"*"` if not specified. The file
    at path is a certificate in PEM format. If a private key is included
    in the PEM, it is used, otherwise the default key in the conf dir is
    used. The PEM file should contain the full certificate chain, with
    the leaf certificate as the first entry. Can be passed multiple times.

\--ciphers-client *CIPHERS_CLIENT*
:   Set supported ciphers for client connections. (OpenSSL Syntax)

\--ciphers-server *CIPHERS_SERVER*
:   Set supported ciphers for server connections. (OpenSSL Syntax)

\--client-certs *CLIENT_CERTS*
:   Client certificate file or directory.

\--no-upstream-cert
:   Don't connect to upstream server to look up certificate details.

\--add-upstream-certs-to-client-chain
:   Add all certificates of the upstream server to the certificate chain
    that will be served to the proxy client, as extras.

\--insecure
:   Do not verify upstream server SSL/TLS certificates.

\--upstream-trusted-cadir *CA_DIR*
:   Path to a directory of trusted CA certificates for upstream server
    verification prepared using the `c_rehash` tool.

\--upstream-trusted-ca *CA_CERT*
:   Path to a PEM formatted trusted CA certificate.

\--ssl-version-client {`all`|`TLSv1_2`|`secure`|`TLSv1_1`|`TLSv1`|`SSLv3`|`SSLv2`}
:   Set supported SSL/TLS versions for client connections. `SSLv2`,
    `SSLv3` and `all` are INSECURE. Defaults to `secure`, which is TLS1.0+.

\--ssl-version-server {`all`|`TLSv1_2`|`secure`|`TLSv1_1`|`TLSv1`|`SSLv3`|`SSLv2`}
:   Set supported SSL/TLS versions for server connections. `SSLv2`,
    `SSLv3` and `all` are INSECURE. Defaults to `secure`, which is TLS1.0+.

## Onboarding App:

\--noapp
:   Disable the `mitmproxy` onboarding app.

\--app-host *HOST*
:   Domain to serve the onboarding app from. For transparent mode, use an IP
    when a DNS entry for the app domain is not present. (Default: `mitm.it`)

\--app-port *PORT*
:   Port to serve the onboarding app from. (Default: `80`)

## Client Replay:

-c *PATH*, \--client-replay *PATH*
:   Replay client requests from a saved file.

## Server Replay:

-S *PATH*, \--server-replay *PATH*
:   Replay server responses from a saved file.

-k, \--replay-kill-extra
:   Kill extra requests during replay.

\--server-replay-use-header *HEADER*
:   Request header to be considered during replay. Can be passed multiple
    times.

\--norefresh
:   Disable response refresh, which updates times in cookies and headers
    for replayed responses.

\--no-pop
:   Disable response pop from response flow. This makes it possible to
    replay same response multiple times.

\--replay-ignore-content
:   Ignore request's content while searching for a saved flow to replay.

\--replay-ignore-payload-param *PARAM*
:   Request's payload parameter (`application/x-www-form-urlencoded` or
    `multipart/form-data`) to be ignored while searching for a saved flow
    to replay. Can be passed multiple times.

\--replay-ignore-param *PARAM*
:   Request's parameter to be ignored while searching for a saved flow to
    replay. Can be passed multiple times.

\--replay-ignore-host
:   Ignore request's destination host while searching for a saved flow
    to replay.

## Replacements:

Replacements are of the form `"/pattern/regex/replacement"`, where the
separator can be any character. Please see the documentation for more
information.

\--replace *PATTERN*
:   Replacement pattern.

\--replace-from-file *PATH*
:   Replacement pattern, where the replacement clause is a path to a file.

## Set Headers:

Header specifications are of the form `"/pattern/header/value"`, where
the separator can be any character. Please see the documentation for
more information.

\--setheader *PATTERN*
:   Header set pattern.

## Proxy Authentication:

Specify which users are allowed to access the proxy and the method used
for authenticating them.

\--nonanonymous
:   Allow access to any user long as a credentials are specified.

\--singleuser *USER*
:   Allows access to a a single user, specified in the form
    `username:password`.

\--htpasswd *PATH*
:   Allow access to users specified in an Apache htpasswd file.

## Filters:

See help in `mitmproxy` for filter expression syntax.

-i *INTERCEPT*, \--intercept *INTERCEPT*
:   Intercept filter expression.

# FILES

~/.mitmproxy/mitmweb.conf
:   Settings for `mitmweb`. This file can contain any options supported by
    `mitmweb`.

~/.mitmproxy/common.conf
:   Settings shared between all command-line tools. Settings in this file
    are overridden by those in the tool-specific files. Only options shared
    by `mitmproxy` and `mitmdump` should be used in this file.

Options that start with `--` (e.g. `--wport`) can also be set in a
config file (`~/.mitmproxy/common.conf` or `~/.mitmproxy/mitmweb.conf`
or specified via `--conf`). Config file syntax allows:

    key=value, flag=true, stuff=[a,b,c]

(for details, see syntax at <https://goo.gl/R74nmi>). If an option is
specified in more than one place, then command-line values override config
file values which override defaults.

# AUTHORS

`mitmweb` was written by Aldo Cortesi.

This manual page was written for the Debian GNU/Linux system, but its use
elsewhere is encouraged.
