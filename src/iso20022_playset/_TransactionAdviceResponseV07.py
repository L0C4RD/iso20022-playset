from . import base_types
from ._AcceptorCompletionAdviceResponse14 import AcceptorCompletionAdviceResponse14
from ._ContentInformationType37 import ContentInformationType37
from ._Header70 import Header70

class TransactionAdviceResponseV07(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_TxAdvcRspn"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def TxAdvcRspn(self):
		return self._TxAdvcRspn

	@TxAdvcRspn.setter
	def TxAdvcRspn(self, value):
		self._TxAdvcRspn = value if type(value) != base_types.auto else self.make_default("TxAdvcRspn")

	@TxAdvcRspn.deleter
	def TxAdvcRspn(self):
		del self._TxAdvcRspn
		self._TxAdvcRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAdvcRspn', type=AcceptorCompletionAdviceResponse14, min=1, max=1, mutex_group=None, array=False),
	))

