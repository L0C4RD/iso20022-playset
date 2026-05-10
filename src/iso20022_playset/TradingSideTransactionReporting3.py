import base_types
import Max35Text
import PartyIdentification242Choice
import UniqueTransactionIdentifier3

class TradingSideTransactionReporting3(base_types._BaseFieldType):

	__slots__ = ["_RptgJursdctn", "_TradgSdUnqTxIdr", "_RptgPty"]
	@property
	def RptgJursdctn(self):
		return self._RptgJursdctn

	@RptgJursdctn.setter
	def RptgJursdctn(self, value):
		self._RptgJursdctn = value if type(value) != auto else self.make_default("RptgJursdctn")

	@RptgJursdctn.deleter
	def RptgJursdctn(self):
		del self._RptgJursdctn
		self._RptgJursdctn = None

	@property
	def TradgSdUnqTxIdr(self):
		return self._TradgSdUnqTxIdr

	@TradgSdUnqTxIdr.setter
	def TradgSdUnqTxIdr(self, value):
		self._TradgSdUnqTxIdr = value if type(value) != auto else self.make_default("TradgSdUnqTxIdr")

	@TradgSdUnqTxIdr.deleter
	def TradgSdUnqTxIdr(self):
		del self._TradgSdUnqTxIdr
		self._TradgSdUnqTxIdr = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgJursdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdUnqTxIdr', type=UniqueTransactionIdentifier3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))

