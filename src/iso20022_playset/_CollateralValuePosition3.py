# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODateTime
from . import SecuritiesAccount19
from . import SecurityCharacteristics3

class CollateralValuePosition3(base_types._BaseFieldType):

	__slots__ = ["_DataAccsTm", "_Scties", "_SctiesAcct", "_TtlCollValtn"]
	@property
	def DataAccsTm(self):
		return self._DataAccsTm

	@DataAccsTm.setter
	def DataAccsTm(self, value):
		self._DataAccsTm = value if value is not None else base_types.UninitialisedField(self, 'DataAccsTm', ISODateTime, False)

	@DataAccsTm.deleter
	def DataAccsTm(self):
		del self._DataAccsTm
		self._DataAccsTm = base_types.UninitialisedField(self, 'DataAccsTm', ISODateTime, False)

	@property
	def Scties(self):
		return self._Scties

	@Scties.setter
	def Scties(self, value):
		self._Scties = value if value is not None else base_types.UninitialisedField(self, 'Scties', SecurityCharacteristics3, True)

	@Scties.deleter
	def Scties(self):
		del self._Scties
		self._Scties = base_types.UninitialisedField(self, 'Scties', SecurityCharacteristics3, True)

	@property
	def SctiesAcct(self):
		return self._SctiesAcct

	@SctiesAcct.setter
	def SctiesAcct(self, value):
		self._SctiesAcct = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcct', SecuritiesAccount19, False)

	@SctiesAcct.deleter
	def SctiesAcct(self):
		del self._SctiesAcct
		self._SctiesAcct = base_types.UninitialisedField(self, 'SctiesAcct', SecuritiesAccount19, False)

	@property
	def TtlCollValtn(self):
		return self._TtlCollValtn

	@TtlCollValtn.setter
	def TtlCollValtn(self, value):
		self._TtlCollValtn = value if value is not None else base_types.UninitialisedField(self, 'TtlCollValtn', ActiveCurrencyAndAmount, False)

	@TtlCollValtn.deleter
	def TtlCollValtn(self):
		del self._TtlCollValtn
		self._TtlCollValtn = base_types.UninitialisedField(self, 'TtlCollValtn', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataAccsTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scties', type=SecurityCharacteristics3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCollValtn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))