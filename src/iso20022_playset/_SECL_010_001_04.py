# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementObligationReportV04

class SECL_010_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.010.001.04"
		_docname = "secl.010.001.04"

		__slots__ = ["_SttlmOblgtnRpt"]
		@property
		def SttlmOblgtnRpt(self):
			return self._SttlmOblgtnRpt

		@SttlmOblgtnRpt.setter
		def SttlmOblgtnRpt(self, value):
			self._SttlmOblgtnRpt = value if value is not None else base_types.UninitialisedField(self, 'SttlmOblgtnRpt', SettlementObligationReportV04, False)

		@SttlmOblgtnRpt.deleter
		def SttlmOblgtnRpt(self):
			del self._SttlmOblgtnRpt
			self._SttlmOblgtnRpt = base_types.UninitialisedField(self, 'SttlmOblgtnRpt', SettlementObligationReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmOblgtnRpt', type=SettlementObligationReportV04, min=1, max=1, mutex_group=None, array=False),
		))