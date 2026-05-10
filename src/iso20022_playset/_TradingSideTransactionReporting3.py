from . import base_types
from .Max35Text import Max35Text
from .PartyIdentification242Choice import PartyIdentification242Choice
from .UniqueTransactionIdentifier3 import UniqueTransactionIdentifier3

class TradingSideTransactionReporting3(base_types._BaseFieldType):

	__slots__ = ["_RptgJursdctn", "_RptgPty", "_TradgSdUnqTxIdr"]
	@property
	def RptgJursdctn(self):
		return self._RptgJursdctn

	@RptgJursdctn.setter
	def RptgJursdctn(self, value):
		self._RptgJursdctn = value if type(value) != base_types.auto else self.make_default("RptgJursdctn")

	@RptgJursdctn.deleter
	def RptgJursdctn(self):
		del self._RptgJursdctn
		self._RptgJursdctn = None

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if type(value) != base_types.auto else self.make_default("RptgPty")

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = None

	@property
	def TradgSdUnqTxIdr(self):
		return self._TradgSdUnqTxIdr

	@TradgSdUnqTxIdr.setter
	def TradgSdUnqTxIdr(self, value):
		self._TradgSdUnqTxIdr = value if type(value) != base_types.auto else self.make_default("TradgSdUnqTxIdr")

	@TradgSdUnqTxIdr.deleter
	def TradgSdUnqTxIdr(self):
		del self._TradgSdUnqTxIdr
		self._TradgSdUnqTxIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgJursdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdUnqTxIdr', type=UniqueTransactionIdentifier3, min=0, max=None, mutex_group=None, array=True),
	))

