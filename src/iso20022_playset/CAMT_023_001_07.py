from . import base_types
from .BackupPaymentV07 import BackupPaymentV07

class CAMT_023_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BckpPmt"]
		@property
		def BckpPmt(self):
			return self._BckpPmt

		@BckpPmt.setter
		def BckpPmt(self, value):
			self._BckpPmt = value if type(value) != auto else self.make_default("BckpPmt")

		@BckpPmt.deleter
		def BckpPmt(self):
			del self._BckpPmt
			self._BckpPmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BckpPmt', type=BackupPaymentV07, min=1, max=1, mutex_group=None, array=False),
		))

