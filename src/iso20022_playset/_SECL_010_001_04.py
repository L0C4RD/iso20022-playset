# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementObligationReportV04 import SettlementObligationReportV04

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
			self._SttlmOblgtnRpt = value if type(value) != base_types.auto else self.make_default("SttlmOblgtnRpt")

		@SttlmOblgtnRpt.deleter
		def SttlmOblgtnRpt(self):
			del self._SttlmOblgtnRpt
			self._SttlmOblgtnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmOblgtnRpt', type=SettlementObligationReportV04, min=1, max=1, mutex_group=None, array=False),
		))