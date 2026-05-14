# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionDetails53 import SecuritiesSettlementTransactionDetails53
from ._SecuritiesSettlementTransactionDetails54 import SecuritiesSettlementTransactionDetails54
from ._SecuritiesSettlementTransactionDetails55 import SecuritiesSettlementTransactionDetails55

class UpdateType38Choice(base_types._BaseFieldType):

	__slots__ = ["_Addtn", "_Deltn", "_Mod"]
	@property
	def Addtn(self):
		return self._Addtn

	@Addtn.setter
	def Addtn(self, value):
		self._Addtn = value if type(value) != base_types.auto else self.make_default("Addtn")

	@Addtn.deleter
	def Addtn(self):
		del self._Addtn
		self._Addtn = None

	@property
	def Deltn(self):
		return self._Deltn

	@Deltn.setter
	def Deltn(self, value):
		self._Deltn = value if type(value) != base_types.auto else self.make_default("Deltn")

	@Deltn.deleter
	def Deltn(self):
		del self._Deltn
		self._Deltn = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Addtn', type=SecuritiesSettlementTransactionDetails53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Deltn', type=SecuritiesSettlementTransactionDetails54, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=SecuritiesSettlementTransactionDetails55, min=0, max=1, mutex_group=1, array=False),
	))