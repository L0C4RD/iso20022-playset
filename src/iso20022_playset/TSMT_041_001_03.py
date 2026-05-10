from . import base_types
from .TransactionReportV03 import TransactionReportV03

class TSMT_041_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TxRpt"]
		@property
		def TxRpt(self):
			return self._TxRpt

		@TxRpt.setter
		def TxRpt(self, value):
			self._TxRpt = value if type(value) != auto else self.make_default("TxRpt")

		@TxRpt.deleter
		def TxRpt(self):
			del self._TxRpt
			self._TxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxRpt', type=TransactionReportV03, min=1, max=1, mutex_group=None, array=False),
		))

