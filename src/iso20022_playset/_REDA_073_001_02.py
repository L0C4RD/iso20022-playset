# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestToPayDebtorActivationStatusReportV02

class REDA_073_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.073.001.02"
		_docname = "reda.073.001.02"

		__slots__ = ["_ReqToPayDbtrActvtnStsRpt"]
		@property
		def ReqToPayDbtrActvtnStsRpt(self):
			return self._ReqToPayDbtrActvtnStsRpt

		@ReqToPayDbtrActvtnStsRpt.setter
		def ReqToPayDbtrActvtnStsRpt(self, value):
			self._ReqToPayDbtrActvtnStsRpt = value if value is not None else base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnStsRpt', RequestToPayDebtorActivationStatusReportV02, False)

		@ReqToPayDbtrActvtnStsRpt.deleter
		def ReqToPayDbtrActvtnStsRpt(self):
			del self._ReqToPayDbtrActvtnStsRpt
			self._ReqToPayDbtrActvtnStsRpt = base_types.UninitialisedField(self, 'ReqToPayDbtrActvtnStsRpt', RequestToPayDebtorActivationStatusReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqToPayDbtrActvtnStsRpt', type=RequestToPayDebtorActivationStatusReportV02, min=1, max=1, mutex_group=None, array=False),
		))