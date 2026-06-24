# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementModificationQueryV02 import IntraBalanceMovementModificationQueryV02

class CAMT_080_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.080.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_IntraBalMvmntModQry"]
		@property
		def IntraBalMvmntModQry(self):
			return self._IntraBalMvmntModQry

		@IntraBalMvmntModQry.setter
		def IntraBalMvmntModQry(self, value):
			self._IntraBalMvmntModQry = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntModQry")

		@IntraBalMvmntModQry.deleter
		def IntraBalMvmntModQry(self):
			del self._IntraBalMvmntModQry
			self._IntraBalMvmntModQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModQry', type=IntraBalanceMovementModificationQueryV02, min=1, max=1, mutex_group=None, array=False),
		))