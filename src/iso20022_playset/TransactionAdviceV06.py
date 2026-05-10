from . import base_types
from .Header70 import Header70
from .AcceptorCompletionAdvice14 import AcceptorCompletionAdvice14
from .ContentInformationType37 import ContentInformationType37

class TransactionAdviceV06(base_types._BaseFieldType):

	__slots__ = ["_TxAdvc", "_SctyTrlr", "_Hdr"]
	@property
	def TxAdvc(self):
		return self._TxAdvc

	@TxAdvc.setter
	def TxAdvc(self, value):
		self._TxAdvc = value if type(value) != auto else self.make_default("TxAdvc")

	@TxAdvc.deleter
	def TxAdvc(self):
		del self._TxAdvc
		self._TxAdvc = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxAdvc', type=AcceptorCompletionAdvice14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
	))

