
A simple web spider with several recursion strategies.

It doesn't do much except follow links and report status.  I mostly
use it for quick and dirty smoke testing and link checking.

The only unusual feature is the --traversal=pattern option, which does
recursive traversal in an unusual order: It tries to recognize
patterns in URLs, and will follow URLs of novel patterns before those
with patterns it has seen before.  If you use this for smoke-testing a
typical modern web app, it will very quickly hit all your
views/controllers at least once... usually.

Also, it's designed so that adding a new recursion strategy is
trivial. Spydey was originally written for the purpose of
experimenting with different recursive crawling strategies. Read the
source.

Oh, and if you install Fabulous, console output is in color.

For smoke testing, I typically run it like::

  spydey -r --max-requests=100 --traversal=pattern --profile --log-referrer URL

There are a number of other command-line options, many stolen from
wget. Use --help to see what they are.

Home page is at http://github.com/slinkp/spydey.
