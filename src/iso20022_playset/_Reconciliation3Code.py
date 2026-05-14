# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Reconciliation3Code(base_types._BaseDataType_String):

	_values = {
		"DPRW",
		"DPRV",
		"DSMA",
		"DSNM",
		"NORE",
		"SSMA",
		"SSPA",
		"SPRW",
		"SPRV",
		"SSUN",
		"SSNE",
	}