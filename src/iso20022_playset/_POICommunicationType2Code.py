# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class POICommunicationType2Code(base_types._BaseDataType_String):

	_values = {
		"BLTH",
		"ETHR",
		"GPRS",
		"GSMF",
		"PSTN",
		"RS23",
		"USBD",
		"USBH",
		"WIFI",
		"WT2G",
		"WT3G",
		"WT4G",
		"WT5G",
	}