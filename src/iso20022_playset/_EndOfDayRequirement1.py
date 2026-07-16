# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection102

class EndOfDayRequirement1(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnRqrmnt", "_VartnMrgnRqrmnt"]
	@property
	def InitlMrgnRqrmnt(self):
		return self._InitlMrgnRqrmnt

	@InitlMrgnRqrmnt.setter
	def InitlMrgnRqrmnt(self, value):
		self._InitlMrgnRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnRqrmnt', ActiveCurrencyAndAmount, False)

	@InitlMrgnRqrmnt.deleter
	def InitlMrgnRqrmnt(self):
		del self._InitlMrgnRqrmnt
		self._InitlMrgnRqrmnt = base_types.UninitialisedField(self, 'InitlMrgnRqrmnt', ActiveCurrencyAndAmount, False)

	@property
	def VartnMrgnRqrmnt(self):
		return self._VartnMrgnRqrmnt

	@VartnMrgnRqrmnt.setter
	def VartnMrgnRqrmnt(self, value):
		self._VartnMrgnRqrmnt = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRqrmnt', AmountAndDirection102, False)

	@VartnMrgnRqrmnt.deleter
	def VartnMrgnRqrmnt(self):
		del self._VartnMrgnRqrmnt
		self._VartnMrgnRqrmnt = base_types.UninitialisedField(self, 'VartnMrgnRqrmnt', AmountAndDirection102, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnRqrmnt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRqrmnt', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
	))