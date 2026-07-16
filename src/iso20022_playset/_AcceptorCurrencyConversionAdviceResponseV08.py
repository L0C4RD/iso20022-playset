# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCancellationAdviceResponse13
from . import ContentInformationType37
from . import Header70

class AcceptorCurrencyConversionAdviceResponseV08(base_types._BaseFieldType):

	__slots__ = ["_CcyConvsAdvcRspn", "_Hdr", "_SctyTrlr"]
	@property
	def CcyConvsAdvcRspn(self):
		return self._CcyConvsAdvcRspn

	@CcyConvsAdvcRspn.setter
	def CcyConvsAdvcRspn(self, value):
		self._CcyConvsAdvcRspn = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsAdvcRspn', AcceptorCancellationAdviceResponse13, False)

	@CcyConvsAdvcRspn.deleter
	def CcyConvsAdvcRspn(self):
		del self._CcyConvsAdvcRspn
		self._CcyConvsAdvcRspn = base_types.UninitialisedField(self, 'CcyConvsAdvcRspn', AcceptorCancellationAdviceResponse13, False)

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
		base_types.FieldEntry(name='CcyConvsAdvcRspn', type=AcceptorCancellationAdviceResponse13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
	))