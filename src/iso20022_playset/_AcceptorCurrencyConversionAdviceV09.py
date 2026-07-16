# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCurrencyConversionAdvice9
from . import ContentInformationType37
from . import Header70

class AcceptorCurrencyConversionAdviceV09(base_types._BaseFieldType):

	__slots__ = ["_AccptrCcyConvsAdvc", "_Hdr", "_SctyTrlr"]
	@property
	def AccptrCcyConvsAdvc(self):
		return self._AccptrCcyConvsAdvc

	@AccptrCcyConvsAdvc.setter
	def AccptrCcyConvsAdvc(self, value):
		self._AccptrCcyConvsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AccptrCcyConvsAdvc', AcceptorCurrencyConversionAdvice9, False)

	@AccptrCcyConvsAdvc.deleter
	def AccptrCcyConvsAdvc(self):
		del self._AccptrCcyConvsAdvc
		self._AccptrCcyConvsAdvc = base_types.UninitialisedField(self, 'AccptrCcyConvsAdvc', AcceptorCurrencyConversionAdvice9, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header70, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header70, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType37, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType37, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptrCcyConvsAdvc', type=AcceptorCurrencyConversionAdvice9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))