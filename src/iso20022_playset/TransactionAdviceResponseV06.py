from . import base_types
import AcceptorCompletionAdviceResponse13
import ContentInformationType37
import Header70

class TransactionAdviceResponseV06(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_Hdr", "_TxAdvcRspn"]
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
	def TxAdvcRspn(self):
		return self._TxAdvcRspn

	@TxAdvcRspn.setter
	def TxAdvcRspn(self, value):
		self._TxAdvcRspn = value if type(value) != auto else self.make_default("TxAdvcRspn")

	@TxAdvcRspn.deleter
	def TxAdvcRspn(self):
		del self._TxAdvcRspn
		self._TxAdvcRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAdvcRspn', type=AcceptorCompletionAdviceResponse13, min=1, max=1, mutex_group=None, array=False),
	))

