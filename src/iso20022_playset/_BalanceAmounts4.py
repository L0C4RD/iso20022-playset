# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection14

class BalanceAmounts4(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_BookVal", "_ElgblCollVal", "_HldgVal", "_PrvsHldgVal"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection14, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection14, False)

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if value is not None else base_types.UninitialisedField(self, 'BookVal', AmountAndDirection14, False)

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = base_types.UninitialisedField(self, 'BookVal', AmountAndDirection14, False)

	@property
	def ElgblCollVal(self):
		return self._ElgblCollVal

	@ElgblCollVal.setter
	def ElgblCollVal(self, value):
		self._ElgblCollVal = value if value is not None else base_types.UninitialisedField(self, 'ElgblCollVal', AmountAndDirection14, False)

	@ElgblCollVal.deleter
	def ElgblCollVal(self):
		del self._ElgblCollVal
		self._ElgblCollVal = base_types.UninitialisedField(self, 'ElgblCollVal', AmountAndDirection14, False)

	@property
	def HldgVal(self):
		return self._HldgVal

	@HldgVal.setter
	def HldgVal(self, value):
		self._HldgVal = value if value is not None else base_types.UninitialisedField(self, 'HldgVal', AmountAndDirection14, False)

	@HldgVal.deleter
	def HldgVal(self):
		del self._HldgVal
		self._HldgVal = base_types.UninitialisedField(self, 'HldgVal', AmountAndDirection14, False)

	@property
	def PrvsHldgVal(self):
		return self._PrvsHldgVal

	@PrvsHldgVal.setter
	def PrvsHldgVal(self, value):
		self._PrvsHldgVal = value if value is not None else base_types.UninitialisedField(self, 'PrvsHldgVal', AmountAndDirection14, False)

	@PrvsHldgVal.deleter
	def PrvsHldgVal(self):
		del self._PrvsHldgVal
		self._PrvsHldgVal = base_types.UninitialisedField(self, 'PrvsHldgVal', AmountAndDirection14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgblCollVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsHldgVal', type=AmountAndDirection14, min=0, max=1, mutex_group=None, array=False),
	))