import base64
from visual_regression_tracker import VisualRegressionTracker, TestRun
from robot.api import logger
from .version import __version__ as VERSION


class VRT(object):
    """
    VRT is a library for integrating Visual Regression Tracker with Robot Framework.
    For information about Visual Regression Tracker please visit the
    [https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker |project page].

    The library contains 3 keywords which must be used together.

    This library is being developed by [https://niceproject.eu/ |NiceProject Poland].
    \n [Images/niceproject-logo.svg |NiceProject Logo]

    = Configure connection =

    Connection with Visual Regression Tracker should be configured using environment variables:

    Example:

    | VRT_APIURL=            | http://localhost:4200 | URL where backend is running     |
    | VRT_PROJECT=           | Default project       | Project name or ID               |
    | VRT_APIKEY=            | YourAPIKey            | User apiKey                      |
    | VRT_CIBUILDID=         | $CI_COMMIT_SHA        | Current git commit SHA           |
    | VRT_BRANCHNAME=        | $CI_COMMIT_REF_NAME   | Current git branch               |
    | VRT_ENABLESOFTASSERT=  | "false"               | Log errors instead of exceptions |

    \n For local use and test debugging vrt.json file can be used. The file should be placed in the project root.

    \n *vrt.json*

    \n {
    \n "apiUrl":"http://localhost:4200",
    \n "project":"Default project",
    \n "apiKey":"YourAPIKey",
    \n "ciBuildId":"commit_sha",
    \n "branchName":"develop",
    \n "enableSoftAssert":false
    \n }
    """

    ROBOT_LIBRARY_SCOPE = "SUITE"
    ROBOT_LIBRARY_VERSION = VERSION

    def start(self):
        """Starts a new build in Visual Regression Tracker."""
        logger.info("Starting VRT with default config")
        self.instance = VisualRegressionTracker()
        self.instance.start()

    def stop(self):
        """Stops recently started build in Visual Regression Tracker."""
        self.instance.stop()

    def screenshot_should_match_baseline(
        self, name, image_file, diff_tolerance, browser, viewport
    ):
        """Tracks differences between screenshot and previously accepted baseline. ``image_file`` is send to
        Visual Regression Tracker which compare image with the baseline. The keyword will fail if the baseline
        is not set or there is a differance between the image and the baseline.

        ``name`` Test case name send to Visual Regression Tracker.

        ``image_file``  Path to the screenshot.

        ``diff_tolerance`` Allowed mismatch tolerance in %. Value between 0 and 100.

        ``browser``  Browser name.

        ``viewport``  Viewport size.

        Example:
        | `Start`                            |                                              |
        | `Screenshot Should Match Baseline` | ...    name=${TEST NAME}                     |
        |                                    | ...    image_file= /path/to/image_file.png   |
        |                                    | ...    diff_tolerance= 0                     |
        |                                    | ...    browser= chrome                       |
        |                                    | ...    viewport=${page_width}x${page_height} |
        | `Stop`                             |                                              |

        """

        with open(image_file, "rb") as img:
            self.instance.track(
                TestRun(
                    name=name,
                    imageBase64=base64.b64encode(img.read()).decode(encoding="UTF-8"),
                    diffTollerancePercent=int(diff_tolerance),
                    browser=browser,
                    viewport=viewport,
                )
            )
