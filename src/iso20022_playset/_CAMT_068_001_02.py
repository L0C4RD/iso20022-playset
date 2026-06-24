# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementConfirmationV02 import IntraBalanceMovementConfirmationV02

class CAMT_068_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.068.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_IntraBalMvmntConf"]
		@property
		def IntraBalMvmntConf(self):
			return self._IntraBalMvmntConf

		@IntraBalMvmntConf.setter
		def IntraBalMvmntConf(self, value):
			self._IntraBalMvmntConf = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntConf")

		@IntraBalMvmntConf.deleter
		def IntraBalMvmntConf(self):
			del self._IntraBalMvmntConf
			self._IntraBalMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntConf', type=IntraBalanceMovementConfirmationV02, min=1, max=1, mutex_group=None, array=False),
		))