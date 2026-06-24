# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BackupPaymentV07 import BackupPaymentV07

class CAMT_023_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.023.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BckpPmt"]
		@property
		def BckpPmt(self):
			return self._BckpPmt

		@BckpPmt.setter
		def BckpPmt(self, value):
			self._BckpPmt = value if type(value) != base_types.auto else self.make_default("BckpPmt")

		@BckpPmt.deleter
		def BckpPmt(self):
			del self._BckpPmt
			self._BckpPmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BckpPmt', type=BackupPaymentV07, min=1, max=1, mutex_group=None, array=False),
		))