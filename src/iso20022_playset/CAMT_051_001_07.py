from . import base_types
import LiquidityDebitTransferV07

class CAMT_051_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_LqdtyDbtTrf"]
		@property
		def LqdtyDbtTrf(self):
			return self._LqdtyDbtTrf

		@LqdtyDbtTrf.setter
		def LqdtyDbtTrf(self, value):
			self._LqdtyDbtTrf = value if type(value) != auto else self.make_default("LqdtyDbtTrf")

		@LqdtyDbtTrf.deleter
		def LqdtyDbtTrf(self):
			del self._LqdtyDbtTrf
			self._LqdtyDbtTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LqdtyDbtTrf', type=LiquidityDebitTransferV07, min=1, max=1, mutex_group=None, array=False),
		))

