from . import base_types
from ._TransferInstructionStatusReportV09 import TransferInstructionStatusReportV09

class SESE_011_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TrfInstrStsRpt"]
		@property
		def TrfInstrStsRpt(self):
			return self._TrfInstrStsRpt

		@TrfInstrStsRpt.setter
		def TrfInstrStsRpt(self, value):
			self._TrfInstrStsRpt = value if type(value) != base_types.auto else self.make_default("TrfInstrStsRpt")

		@TrfInstrStsRpt.deleter
		def TrfInstrStsRpt(self):
			del self._TrfInstrStsRpt
			self._TrfInstrStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInstrStsRpt', type=TransferInstructionStatusReportV09, min=1, max=1, mutex_group=None, array=False),
		))

