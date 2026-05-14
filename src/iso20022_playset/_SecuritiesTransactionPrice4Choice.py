# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionPrice1 import SecuritiesTransactionPrice1
from ._SecuritiesTransactionPrice2Choice import SecuritiesTransactionPrice2Choice

class SecuritiesTransactionPrice4Choice(base_types._BaseFieldType):

	__slots__ = ["_NoPric", "_Pric"]
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
		base_types.FieldEntry(name='NoPric', type=SecuritiesTransactionPrice1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice2Choice, min=0, max=1, mutex_group=1, array=False),
	))