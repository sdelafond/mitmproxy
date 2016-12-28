#!/usr/bin/env python3
"""
    This example shows how to build a proxy based on mitmproxy's Flow
    primitives.

    Heads Up: In the majority of cases, you want to use inline scripts.

    Note that request and response messages are not automatically replied to,
    so we need to implement handlers to do this.
"""
from mitmproxy import controller, options, master
from mitmproxy.proxy import ProxyServer, ProxyConfig


class MyMaster(master.Master):
    def run(self):
        try:
            master.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    @controller.handler
    def request(self, f):
        print("request", f)

    @controller.handler
    def response(self, f):
        print("response", f)

    @controller.handler
    def error(self, f):
        print("error", f)

    @controller.handler
    def log(self, l):
        print("log", l.msg)


opts = options.Options(cadir="~/.mitmproxy/")
config = ProxyConfig(opts)
server = ProxyServer(config)
m = MyMaster(opts, server)
m.run()
