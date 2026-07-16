# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionPrice23Choice

class OptionMultipleBarrierLevels1(base_types._BaseFieldType):

	__slots__ = ["_LwrLvl", "_UpperLvl"]
	@property
	def LwrLvl(self):
		return self._LwrLvl

	@LwrLvl.setter
	def LwrLvl(self, value):
		self._LwrLvl = value if value is not None else base_types.UninitialisedField(self, 'LwrLvl', SecuritiesTransactionPrice23Choice, False)

	@LwrLvl.deleter
	def LwrLvl(self):
		del self._LwrLvl
		self._LwrLvl = base_types.UninitialisedField(self, 'LwrLvl', SecuritiesTransactionPrice23Choice, False)

	@property
	def UpperLvl(self):
		return self._UpperLvl

	@UpperLvl.setter
	def UpperLvl(self, value):
		self._UpperLvl = value if value is not None else base_types.UninitialisedField(self, 'UpperLvl', SecuritiesTransactionPrice23Choice, False)

	@UpperLvl.deleter
	def UpperLvl(self):
		del self._UpperLvl
		self._UpperLvl = base_types.UninitialisedField(self, 'UpperLvl', SecuritiesTransactionPrice23Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LwrLvl', type=SecuritiesTransactionPrice23Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpperLvl', type=SecuritiesTransactionPrice23Choice, min=1, max=1, mutex_group=None, array=False),
	))