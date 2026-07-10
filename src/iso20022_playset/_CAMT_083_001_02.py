# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementCancellationReportV02 import IntraBalanceMovementCancellationReportV02

class CAMT_083_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.083.001.02"
		_docname = "camt.083.001.02"

		__slots__ = ["_IntraBalMvmntCxlRpt"]
		@property
		def IntraBalMvmntCxlRpt(self):
			return self._IntraBalMvmntCxlRpt

		@IntraBalMvmntCxlRpt.setter
		def IntraBalMvmntCxlRpt(self, value):
			self._IntraBalMvmntCxlRpt = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntCxlRpt")

		@IntraBalMvmntCxlRpt.deleter
		def IntraBalMvmntCxlRpt(self):
			del self._IntraBalMvmntCxlRpt
			self._IntraBalMvmntCxlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlRpt', type=IntraBalanceMovementCancellationReportV02, min=1, max=1, mutex_group=None, array=False),
		))