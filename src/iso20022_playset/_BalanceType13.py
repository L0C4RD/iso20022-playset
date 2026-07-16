# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceSubType1Choice
from . import BalanceType10Choice

class BalanceType13(base_types._BaseFieldType):

	__slots__ = ["_CdOrPrtry", "_SubTp"]
	@property
	def CdOrPrtry(self):
		return self._CdOrPrtry

	@CdOrPrtry.setter
	def CdOrPrtry(self, value):
		self._CdOrPrtry = value if value is not None else base_types.UninitialisedField(self, 'CdOrPrtry', BalanceType10Choice, False)

	@CdOrPrtry.deleter
	def CdOrPrtry(self):
		del self._CdOrPrtry
		self._CdOrPrtry = base_types.UninitialisedField(self, 'CdOrPrtry', BalanceType10Choice, False)

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if value is not None else base_types.UninitialisedField(self, 'SubTp', BalanceSubType1Choice, False)

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = base_types.UninitialisedField(self, 'SubTp', BalanceSubType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdOrPrtry', type=BalanceType10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=BalanceSubType1Choice, min=0, max=1, mutex_group=None, array=False),
	))