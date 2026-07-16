# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODateTime
from . import Number
from . import PreferenceToIncome5Choice

class Equity3(base_types._BaseFieldType):

	__slots__ = ["_MtrtyDt", "_NonPdAmt", "_ParVal", "_PrefToIncm", "_VtngRghtsPerShr"]
	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODateTime, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODateTime, False)

	@property
	def NonPdAmt(self):
		return self._NonPdAmt

	@NonPdAmt.setter
	def NonPdAmt(self, value):
		self._NonPdAmt = value if value is not None else base_types.UninitialisedField(self, 'NonPdAmt', ActiveCurrencyAndAmount, False)

	@NonPdAmt.deleter
	def NonPdAmt(self):
		del self._NonPdAmt
		self._NonPdAmt = base_types.UninitialisedField(self, 'NonPdAmt', ActiveCurrencyAndAmount, False)

	@property
	def ParVal(self):
		return self._ParVal

	@ParVal.setter
	def ParVal(self, value):
		self._ParVal = value if value is not None else base_types.UninitialisedField(self, 'ParVal', ActiveCurrencyAndAmount, False)

	@ParVal.deleter
	def ParVal(self):
		del self._ParVal
		self._ParVal = base_types.UninitialisedField(self, 'ParVal', ActiveCurrencyAndAmount, False)

	@property
	def PrefToIncm(self):
		return self._PrefToIncm

	@PrefToIncm.setter
	def PrefToIncm(self, value):
		self._PrefToIncm = value if value is not None else base_types.UninitialisedField(self, 'PrefToIncm', PreferenceToIncome5Choice, False)

	@PrefToIncm.deleter
	def PrefToIncm(self):
		del self._PrefToIncm
		self._PrefToIncm = base_types.UninitialisedField(self, 'PrefToIncm', PreferenceToIncome5Choice, False)

	@property
	def VtngRghtsPerShr(self):
		return self._VtngRghtsPerShr

	@VtngRghtsPerShr.setter
	def VtngRghtsPerShr(self, value):
		self._VtngRghtsPerShr = value if value is not None else base_types.UninitialisedField(self, 'VtngRghtsPerShr', Number, False)

	@VtngRghtsPerShr.deleter
	def VtngRghtsPerShr(self):
		del self._VtngRghtsPerShr
		self._VtngRghtsPerShr = base_types.UninitialisedField(self, 'VtngRghtsPerShr', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtrtyDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonPdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrefToIncm', type=PreferenceToIncome5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VtngRghtsPerShr', type=Number, min=0, max=1, mutex_group=None, array=False),
	))