# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Percentage1
from . import UndertakingAmount4

class AmountOrPercentage1Choice(base_types._BaseFieldType):

	__slots__ = ["_DfndAmt", "_PctgAmt"]
	@property
	def DfndAmt(self):
		return self._DfndAmt

	@DfndAmt.setter
	def DfndAmt(self, value):
		self._DfndAmt = value if value is not None else base_types.UninitialisedField(self, 'DfndAmt', UndertakingAmount4, False)

	@DfndAmt.deleter
	def DfndAmt(self):
		del self._DfndAmt
		self._DfndAmt = base_types.UninitialisedField(self, 'DfndAmt', UndertakingAmount4, False)

	@property
	def PctgAmt(self):
		return self._PctgAmt

	@PctgAmt.setter
	def PctgAmt(self, value):
		self._PctgAmt = value if value is not None else base_types.UninitialisedField(self, 'PctgAmt', Percentage1, False)

	@PctgAmt.deleter
	def PctgAmt(self):
		del self._PctgAmt
		self._PctgAmt = base_types.UninitialisedField(self, 'PctgAmt', Percentage1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfndAmt', type=UndertakingAmount4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgAmt', type=Percentage1, min=0, max=1, mutex_group=1, array=False),
	))