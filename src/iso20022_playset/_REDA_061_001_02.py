# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NettingCutOffReferenceDataReportV02

class REDA_061_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.061.001.02"
		_docname = "reda.061.001.02"

		__slots__ = ["_NetgCutOffRefDataRpt"]
		@property
		def NetgCutOffRefDataRpt(self):
			return self._NetgCutOffRefDataRpt

		@NetgCutOffRefDataRpt.setter
		def NetgCutOffRefDataRpt(self, value):
			self._NetgCutOffRefDataRpt = value if value is not None else base_types.UninitialisedField(self, 'NetgCutOffRefDataRpt', NettingCutOffReferenceDataReportV02, False)

		@NetgCutOffRefDataRpt.deleter
		def NetgCutOffRefDataRpt(self):
			del self._NetgCutOffRefDataRpt
			self._NetgCutOffRefDataRpt = base_types.UninitialisedField(self, 'NetgCutOffRefDataRpt', NettingCutOffReferenceDataReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetgCutOffRefDataRpt', type=NettingCutOffReferenceDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))