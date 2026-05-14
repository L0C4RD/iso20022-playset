# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PaymentTime4Code(base_types._BaseDataType_String):

	_values = {
		"IREC",
		"CASH",
		"EPSD",
		"EPRR",
		"EPPO",
		"EPIN",
		"PRMR",
		"PRMD",
		"EPRD",
		"EPBE",
		"EMTR",
		"EMTD",
	}