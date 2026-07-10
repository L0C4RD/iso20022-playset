# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementPendingReportV02 import IntraBalanceMovementPendingReportV02

class CAMT_085_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.085.001.02"
		_docname = "camt.085.001.02"

		__slots__ = ["_IntraBalMvmntPdgRpt"]
		@property
		def IntraBalMvmntPdgRpt(self):
			return self._IntraBalMvmntPdgRpt

		@IntraBalMvmntPdgRpt.setter
		def IntraBalMvmntPdgRpt(self, value):
			self._IntraBalMvmntPdgRpt = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntPdgRpt")

		@IntraBalMvmntPdgRpt.deleter
		def IntraBalMvmntPdgRpt(self):
			del self._IntraBalMvmntPdgRpt
			self._IntraBalMvmntPdgRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntPdgRpt', type=IntraBalanceMovementPendingReportV02, min=1, max=1, mutex_group=None, array=False),
		))