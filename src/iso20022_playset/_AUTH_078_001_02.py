# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingPairingRequestV02 import SecuritiesFinancingReportingPairingRequestV02

class AUTH_078_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.078.001.02"
		_docname = "auth.078.001.02"

		__slots__ = ["_SctiesFincgRptgPairgReq"]
		@property
		def SctiesFincgRptgPairgReq(self):
			return self._SctiesFincgRptgPairgReq

		@SctiesFincgRptgPairgReq.setter
		def SctiesFincgRptgPairgReq(self, value):
			self._SctiesFincgRptgPairgReq = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgPairgReq")

		@SctiesFincgRptgPairgReq.deleter
		def SctiesFincgRptgPairgReq(self):
			del self._SctiesFincgRptgPairgReq
			self._SctiesFincgRptgPairgReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgPairgReq', type=SecuritiesFinancingReportingPairingRequestV02, min=1, max=1, mutex_group=None, array=False),
		))