# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementCancellationQueryV02 import IntraBalanceMovementCancellationQueryV02

class CAMT_082_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.082.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_IntraBalMvmntCxlQry"]
		@property
		def IntraBalMvmntCxlQry(self):
			return self._IntraBalMvmntCxlQry

		@IntraBalMvmntCxlQry.setter
		def IntraBalMvmntCxlQry(self, value):
			self._IntraBalMvmntCxlQry = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntCxlQry")

		@IntraBalMvmntCxlQry.deleter
		def IntraBalMvmntCxlQry(self):
			del self._IntraBalMvmntCxlQry
			self._IntraBalMvmntCxlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlQry', type=IntraBalanceMovementCancellationQueryV02, min=1, max=1, mutex_group=None, array=False),
		))