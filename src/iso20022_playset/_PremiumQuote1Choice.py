# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import PercentageRate

class PremiumQuote1Choice(base_types._BaseFieldType):

	__slots__ = ["_PctgOfCallAmt", "_PctgOfPutAmt", "_PtsOfCallAmt", "_PtsOfPutAmt"]
	@property
	def PctgOfCallAmt(self):
		return self._PctgOfCallAmt

	@PctgOfCallAmt.setter
	def PctgOfCallAmt(self, value):
		self._PctgOfCallAmt = value if value is not None else base_types.UninitialisedField(self, 'PctgOfCallAmt', PercentageRate, False)

	@PctgOfCallAmt.deleter
	def PctgOfCallAmt(self):
		del self._PctgOfCallAmt
		self._PctgOfCallAmt = base_types.UninitialisedField(self, 'PctgOfCallAmt', PercentageRate, False)

	@property
	def PctgOfPutAmt(self):
		return self._PctgOfPutAmt

	@PctgOfPutAmt.setter
	def PctgOfPutAmt(self, value):
		self._PctgOfPutAmt = value if value is not None else base_types.UninitialisedField(self, 'PctgOfPutAmt', PercentageRate, False)

	@PctgOfPutAmt.deleter
	def PctgOfPutAmt(self):
		del self._PctgOfPutAmt
		self._PctgOfPutAmt = base_types.UninitialisedField(self, 'PctgOfPutAmt', PercentageRate, False)

	@property
	def PtsOfCallAmt(self):
		return self._PtsOfCallAmt

	@PtsOfCallAmt.setter
	def PtsOfCallAmt(self, value):
		self._PtsOfCallAmt = value if value is not None else base_types.UninitialisedField(self, 'PtsOfCallAmt', BaseOneRate, False)

	@PtsOfCallAmt.deleter
	def PtsOfCallAmt(self):
		del self._PtsOfCallAmt
		self._PtsOfCallAmt = base_types.UninitialisedField(self, 'PtsOfCallAmt', BaseOneRate, False)

	@property
	def PtsOfPutAmt(self):
		return self._PtsOfPutAmt

	@PtsOfPutAmt.setter
	def PtsOfPutAmt(self, value):
		self._PtsOfPutAmt = value if value is not None else base_types.UninitialisedField(self, 'PtsOfPutAmt', BaseOneRate, False)

	@PtsOfPutAmt.deleter
	def PtsOfPutAmt(self):
		del self._PtsOfPutAmt
		self._PtsOfPutAmt = base_types.UninitialisedField(self, 'PtsOfPutAmt', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PctgOfCallAmt', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgOfPutAmt', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtsOfCallAmt', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PtsOfPutAmt', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
	))