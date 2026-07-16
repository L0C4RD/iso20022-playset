# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionPrice2Choice
from . import SecuritiesTransactionPrice6
from . import SecuritiesTransactionPrice7

class SecuritiesTransactionPrice22Choice(base_types._BaseFieldType):

	__slots__ = ["_DgtlTknPric", "_NoPric", "_Pric"]
	@property
	def DgtlTknPric(self):
		return self._DgtlTknPric

	@DgtlTknPric.setter
	def DgtlTknPric(self, value):
		self._DgtlTknPric = value if value is not None else base_types.UninitialisedField(self, 'DgtlTknPric', SecuritiesTransactionPrice7, False)

	@DgtlTknPric.deleter
	def DgtlTknPric(self):
		del self._DgtlTknPric
		self._DgtlTknPric = base_types.UninitialisedField(self, 'DgtlTknPric', SecuritiesTransactionPrice7, False)

	@property
	def NoPric(self):
		return self._NoPric

	@NoPric.setter
	def NoPric(self, value):
		self._NoPric = value if value is not None else base_types.UninitialisedField(self, 'NoPric', SecuritiesTransactionPrice6, False)

	@NoPric.deleter
	def NoPric(self):
		del self._NoPric
		self._NoPric = base_types.UninitialisedField(self, 'NoPric', SecuritiesTransactionPrice6, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice2Choice, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', SecuritiesTransactionPrice2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlTknPric', type=SecuritiesTransactionPrice7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoPric', type=SecuritiesTransactionPrice6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=1, array=False),
	))