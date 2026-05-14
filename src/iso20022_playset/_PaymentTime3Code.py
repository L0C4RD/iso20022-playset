# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PaymentTime3Code(base_types._BaseDataType_String):

	_values = {
		"EMTD",
		"EMTR",
		"EPBE",
		"EPRD",
		"PRMD",
		"PRMR",
		"EPIN",
		"EPAM",
		"EPPO",
		"EPRR",
		"EPSD",
		"CASH",
		"IREC",
	}