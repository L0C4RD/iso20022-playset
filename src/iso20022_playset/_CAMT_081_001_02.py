# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementModificationReportV02

class CAMT_081_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.081.001.02"
		_docname = "camt.081.001.02"

		__slots__ = ["_IntraBalMvmntModRpt"]
		@property
		def IntraBalMvmntModRpt(self):
			return self._IntraBalMvmntModRpt

		@IntraBalMvmntModRpt.setter
		def IntraBalMvmntModRpt(self, value):
			self._IntraBalMvmntModRpt = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntModRpt', IntraBalanceMovementModificationReportV02, False)

		@IntraBalMvmntModRpt.deleter
		def IntraBalMvmntModRpt(self):
			del self._IntraBalMvmntModRpt
			self._IntraBalMvmntModRpt = base_types.UninitialisedField(self, 'IntraBalMvmntModRpt', IntraBalanceMovementModificationReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModRpt', type=IntraBalanceMovementModificationReportV02, min=1, max=1, mutex_group=None, array=False),
		))