from webssh.main import main
import sys
from tornado.options import define, options

if __name__ == '__main__':
    # define("xsrf", default=False, help="Enable XSRF protection", type=bool)
    # define("xheaders", default=False, help="Enable X-headers", type=bool)
    define("origin", default="*", help="Origin for CORS", type=str)
    
    sys.argv.extend(['--xsrf=False', '--xheaders=False', '--origin=*'])
    options.parse_command_line()
    
    print("XSRF setting:", options.xsrf)  # 调试输出
    main()
