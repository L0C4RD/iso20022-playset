# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SettlementReportingInitiationV03 import SettlementReportingInitiationV03

class CASR_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SttlmRptgInitn"]
		@property
		def SttlmRptgInitn(self):
			return self._SttlmRptgInitn

		@SttlmRptgInitn.setter
		def SttlmRptgInitn(self, value):
			self._SttlmRptgInitn = value if type(value) != base_types.auto else self.make_default("SttlmRptgInitn")

		@SttlmRptgInitn.deleter
		def SttlmRptgInitn(self):
			del self._SttlmRptgInitn
			self._SttlmRptgInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SttlmRptgInitn', type=SettlementReportingInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))