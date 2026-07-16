# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementPostingReportV02

class CAMT_084_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.084.001.02"
		_docname = "camt.084.001.02"

		__slots__ = ["_IntraBalMvmntPstngRpt"]
		@property
		def IntraBalMvmntPstngRpt(self):
			return self._IntraBalMvmntPstngRpt

		@IntraBalMvmntPstngRpt.setter
		def IntraBalMvmntPstngRpt(self, value):
			self._IntraBalMvmntPstngRpt = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntPstngRpt', IntraBalanceMovementPostingReportV02, False)

		@IntraBalMvmntPstngRpt.deleter
		def IntraBalMvmntPstngRpt(self):
			del self._IntraBalMvmntPstngRpt
			self._IntraBalMvmntPstngRpt = base_types.UninitialisedField(self, 'IntraBalMvmntPstngRpt', IntraBalanceMovementPostingReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntPstngRpt', type=IntraBalanceMovementPostingReportV02, min=1, max=1, mutex_group=None, array=False),
		))