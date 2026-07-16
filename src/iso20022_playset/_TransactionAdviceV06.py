# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCompletionAdvice14
from . import ContentInformationType37
from . import Header70

class TransactionAdviceV06(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_SctyTrlr", "_TxAdvc"]
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

	@property
	def TxAdvc(self):
		return self._TxAdvc

	@TxAdvc.setter
	def TxAdvc(self, value):
		self._TxAdvc = value if value is not None else base_types.UninitialisedField(self, 'TxAdvc', AcceptorCompletionAdvice14, False)

	@TxAdvc.deleter
	def TxAdvc(self):
		del self._TxAdvc
		self._TxAdvc = base_types.UninitialisedField(self, 'TxAdvc', AcceptorCompletionAdvice14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header70, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAdvc', type=AcceptorCompletionAdvice14, min=1, max=1, mutex_group=None, array=False),
	))