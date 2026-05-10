from . import base_types
import SecuritiesAccount19
import ISODateTime
import SecurityCharacteristics3
import ActiveCurrencyAndAmount

class CollateralValuePosition3(base_types._BaseFieldType):

	__slots__ = ["_TtlCollValtn", "_SctiesAcct", "_DataAccsTm", "_Scties"]
	@property
	def TtlCollValtn(self):
		return self._TtlCollValtn

	@TtlCollValtn.setter
	def TtlCollValtn(self, value):
		self._TtlCollValtn = value if type(value) != auto else self.make_default("TtlCollValtn")

	@TtlCollValtn.deleter
	def TtlCollValtn(self):
		del self._TtlCollValtn
		self._TtlCollValtn = None

	@property
	def SctiesAcct(self):
		return self._SctiesAcct

	@SctiesAcct.setter
	def SctiesAcct(self, value):
		self._SctiesAcct = value if type(value) != auto else self.make_default("SctiesAcct")

	@SctiesAcct.deleter
	def SctiesAcct(self):
		del self._SctiesAcct
		self._SctiesAcct = None

	@property
	def DataAccsTm(self):
		return self._DataAccsTm

	@DataAccsTm.setter
	def DataAccsTm(self, value):
		self._DataAccsTm = value if type(value) != auto else self.make_default("DataAccsTm")

	@DataAccsTm.deleter
	def DataAccsTm(self):
		del self._DataAccsTm
		self._DataAccsTm = None

	@property
	def Scties(self):
		return self._Scties

	@Scties.setter
	def Scties(self, value):
		self._Scties = value if type(value) != auto else self.make_default("Scties")

	@Scties.deleter
	def Scties(self):
		del self._Scties
		self._Scties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCollValtn', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataAccsTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scties', type=SecurityCharacteristics3, min=0, max=None, mutex_group=None, array=True),
	))

