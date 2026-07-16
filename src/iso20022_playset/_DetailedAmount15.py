# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DetailedAmount4
from . import ImpliedCurrencyAndAmount

class DetailedAmount15(base_types._BaseFieldType):

	__slots__ = ["_AmtGoodsAndSvcs", "_CshBck", "_Fees", "_Grtty", "_Rbt", "_Srchrg", "_ValAddedTax"]
	@property
	def AmtGoodsAndSvcs(self):
		return self._AmtGoodsAndSvcs

	@AmtGoodsAndSvcs.setter
	def AmtGoodsAndSvcs(self, value):
		self._AmtGoodsAndSvcs = value if value is not None else base_types.UninitialisedField(self, 'AmtGoodsAndSvcs', ImpliedCurrencyAndAmount, False)

	@AmtGoodsAndSvcs.deleter
	def AmtGoodsAndSvcs(self):
		del self._AmtGoodsAndSvcs
		self._AmtGoodsAndSvcs = base_types.UninitialisedField(self, 'AmtGoodsAndSvcs', ImpliedCurrencyAndAmount, False)

	@property
	def CshBck(self):
		return self._CshBck

	@CshBck.setter
	def CshBck(self, value):
		self._CshBck = value if value is not None else base_types.UninitialisedField(self, 'CshBck', ImpliedCurrencyAndAmount, False)

	@CshBck.deleter
	def CshBck(self):
		del self._CshBck
		self._CshBck = base_types.UninitialisedField(self, 'CshBck', ImpliedCurrencyAndAmount, False)

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if value is not None else base_types.UninitialisedField(self, 'Fees', DetailedAmount4, True)

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = base_types.UninitialisedField(self, 'Fees', DetailedAmount4, True)

	@property
	def Grtty(self):
		return self._Grtty

	@Grtty.setter
	def Grtty(self, value):
		self._Grtty = value if value is not None else base_types.UninitialisedField(self, 'Grtty', ImpliedCurrencyAndAmount, False)

	@Grtty.deleter
	def Grtty(self):
		del self._Grtty
		self._Grtty = base_types.UninitialisedField(self, 'Grtty', ImpliedCurrencyAndAmount, False)

	@property
	def Rbt(self):
		return self._Rbt

	@Rbt.setter
	def Rbt(self, value):
		self._Rbt = value if value is not None else base_types.UninitialisedField(self, 'Rbt', DetailedAmount4, True)

	@Rbt.deleter
	def Rbt(self):
		del self._Rbt
		self._Rbt = base_types.UninitialisedField(self, 'Rbt', DetailedAmount4, True)

	@property
	def Srchrg(self):
		return self._Srchrg

	@Srchrg.setter
	def Srchrg(self, value):
		self._Srchrg = value if value is not None else base_types.UninitialisedField(self, 'Srchrg', DetailedAmount4, True)

	@Srchrg.deleter
	def Srchrg(self):
		del self._Srchrg
		self._Srchrg = base_types.UninitialisedField(self, 'Srchrg', DetailedAmount4, True)

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTax', DetailedAmount4, True)

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = base_types.UninitialisedField(self, 'ValAddedTax', DetailedAmount4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtGoodsAndSvcs', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBck', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fees', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grtty', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rbt', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Srchrg', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValAddedTax', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
	))