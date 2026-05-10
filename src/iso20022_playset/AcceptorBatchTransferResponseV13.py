from . import base_types
from .Header56 import Header56
from .CardPaymentBatchTransferResponse12 import CardPaymentBatchTransferResponse12
from .ContentInformationType37 import ContentInformationType37

class AcceptorBatchTransferResponseV13(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_BtchTrfRspn"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def BtchTrfRspn(self):
		return self._BtchTrfRspn

	@BtchTrfRspn.setter
	def BtchTrfRspn(self, value):
		self._BtchTrfRspn = value if type(value) != auto else self.make_default("BtchTrfRspn")

	@BtchTrfRspn.deleter
	def BtchTrfRspn(self):
		del self._BtchTrfRspn
		self._BtchTrfRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header56, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchTrfRspn', type=CardPaymentBatchTransferResponse12, min=1, max=1, mutex_group=None, array=False),
	))

