
A simple web spider with several recursion strategies.
Home page is at http://github.com/slinkp/spydey.

It doesn't do much except follow links and report status.  I mostly
use it for quick and dirty smoke testing and link checking.

The only unusual feature is the ``--traversal=pattern`` option, which does
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
wget. Use ``--help`` to see what they are, currently::

  Usage: spydey [options] URL

  Options:
  -h, --help            show this help message and exit
  -r, --recursive       recur into subdirectories
  -p, --page-requisites
                        get all images, etc. needed to display HTML page.
  --no-parent           don't ascend to the parent directory.
  -R REJECT, --reject=REJECT
                        Regex for filenames to reject. May be given multiple
                        times.
  -A ACCEPT, --accept=ACCEPT
                        Regex for filenames to accept. May be given multiple
                        times.
  -t TRAVERSAL, --traversal=TRAVERSAL
                        Recursive traversal strategy. Choices are: breadth-
                        first, depth-first, hybrid, pattern, random
  -H, --span-hosts      go to foreign hosts when recursive.
  -w WAIT, --wait=WAIT  wait SECONDS between retrievals.
  --random-wait=RANDOM_WAIT
                        wait from 0...2*WAIT secs between retrievals.
  --loglevel=LOGLEVEL   Log level.
  --log-referrer        Log referrer URL for each request.
  --transient-log       Use Fabulous transient logging config.
  --max-requests=MAX_REQUESTS
                        Maximum number of requests to make before exiting.
  -T TIMEOUT, --timeout=TIMEOUT
                        Set the network timeout in seconds. 0 means no
                        timeout.
  -P, --profile         Print the time to download each resource, and a
                        summary of the 20 slowest at the end.


