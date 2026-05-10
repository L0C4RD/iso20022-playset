from . import base_types
from .LiquidityCreditTransferV07 import LiquidityCreditTransferV07

class CAMT_050_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_LqdtyCdtTrf"]
		@property
		def LqdtyCdtTrf(self):
			return self._LqdtyCdtTrf

		@LqdtyCdtTrf.setter
		def LqdtyCdtTrf(self, value):
			self._LqdtyCdtTrf = value if type(value) != auto else self.make_default("LqdtyCdtTrf")

		@LqdtyCdtTrf.deleter
		def LqdtyCdtTrf(self):
			del self._LqdtyCdtTrf
			self._LqdtyCdtTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LqdtyCdtTrf', type=LiquidityCreditTransferV07, min=1, max=1, mutex_group=None, array=False),
		))

