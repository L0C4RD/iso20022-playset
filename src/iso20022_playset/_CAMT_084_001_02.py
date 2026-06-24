# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementPostingReportV02 import IntraBalanceMovementPostingReportV02

class CAMT_084_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.084.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_IntraBalMvmntPstngRpt"]
		@property
		def IntraBalMvmntPstngRpt(self):
			return self._IntraBalMvmntPstngRpt

		@IntraBalMvmntPstngRpt.setter
		def IntraBalMvmntPstngRpt(self, value):
			self._IntraBalMvmntPstngRpt = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntPstngRpt")

		@IntraBalMvmntPstngRpt.deleter
		def IntraBalMvmntPstngRpt(self):
			del self._IntraBalMvmntPstngRpt
			self._IntraBalMvmntPstngRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntPstngRpt', type=IntraBalanceMovementPostingReportV02, min=1, max=1, mutex_group=None, array=False),
		))