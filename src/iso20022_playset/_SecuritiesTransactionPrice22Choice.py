# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionPrice2Choice import SecuritiesTransactionPrice2Choice
from ._SecuritiesTransactionPrice6 import SecuritiesTransactionPrice6
from ._SecuritiesTransactionPrice7 import SecuritiesTransactionPrice7

class SecuritiesTransactionPrice22Choice(base_types._BaseFieldType):

	__slots__ = ["_DgtlTknPric", "_NoPric", "_Pric"]
	@property
	def DgtlTknPric(self):
		return self._DgtlTknPric

	@DgtlTknPric.setter
	def DgtlTknPric(self, value):
		self._DgtlTknPric = value if type(value) != base_types.auto else self.make_default("DgtlTknPric")

	@DgtlTknPric.deleter
	def DgtlTknPric(self):
		del self._DgtlTknPric
		self._DgtlTknPric = None

	@property
	def NoPric(self):
		return self._NoPric

	@NoPric.setter
	def NoPric(self, value):
		self._NoPric = value if type(value) != base_types.auto else self.make_default("NoPric")

	@NoPric.deleter
	def NoPric(self):
		del self._NoPric
		self._NoPric = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlTknPric', type=SecuritiesTransactionPrice7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoPric', type=SecuritiesTransactionPrice6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=1, array=False),
	))