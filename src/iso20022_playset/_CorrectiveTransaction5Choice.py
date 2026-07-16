# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorrectiveInterbankTransaction3
from . import CorrectivePaymentInitiation5

class CorrectiveTransaction5Choice(base_types._BaseFieldType):

	__slots__ = ["_Initn", "_IntrBk"]
	@property
	def Initn(self):
		return self._Initn

	@Initn.setter
	def Initn(self, value):
		self._Initn = value if value is not None else base_types.UninitialisedField(self, 'Initn', CorrectivePaymentInitiation5, False)

	@Initn.deleter
	def Initn(self):
		del self._Initn
		self._Initn = base_types.UninitialisedField(self, 'Initn', CorrectivePaymentInitiation5, False)

	@property
	def IntrBk(self):
		return self._IntrBk

	@IntrBk.setter
	def IntrBk(self, value):
		self._IntrBk = value if value is not None else base_types.UninitialisedField(self, 'IntrBk', CorrectiveInterbankTransaction3, False)

	@IntrBk.deleter
	def IntrBk(self):
		del self._IntrBk
		self._IntrBk = base_types.UninitialisedField(self, 'IntrBk', CorrectiveInterbankTransaction3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Initn', type=CorrectivePaymentInitiation5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrBk', type=CorrectiveInterbankTransaction3, min=0, max=1, mutex_group=1, array=False),
	))