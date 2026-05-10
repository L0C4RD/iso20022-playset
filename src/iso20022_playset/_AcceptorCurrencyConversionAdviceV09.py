from . import base_types
from ._Header70 import Header70
from ._ContentInformationType37 import ContentInformationType37
from ._AcceptorCurrencyConversionAdvice9 import AcceptorCurrencyConversionAdvice9

class AcceptorCurrencyConversionAdviceV09(base_types._BaseFieldType):

	__slots__ = ["_AccptrCcyConvsAdvc", "_SctyTrlr", "_Hdr"]
	@property
	def AccptrCcyConvsAdvc(self):
		return self._AccptrCcyConvsAdvc

	@AccptrCcyConvsAdvc.setter
	def AccptrCcyConvsAdvc(self, value):
		self._AccptrCcyConvsAdvc = value if type(value) != base_types.auto else self.make_default("AccptrCcyConvsAdvc")

	@AccptrCcyConvsAdvc.deleter
	def AccptrCcyConvsAdvc(self):
		del self._AccptrCcyConvsAdvc
		self._AccptrCcyConvsAdvc = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptrCcyConvsAdvc', type=AcceptorCurrencyConversionAdvice9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))

