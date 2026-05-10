from . import base_types
from .SettlementFailsDailyCSD1Choice import SettlementFailsDailyCSD1Choice

class SettlementFailsDailyTransactionType3(base_types._BaseFieldType):

	__slots__ = ["_SctiesBuyOrSell", "_Othr", "_SctiesLndgOrBrrwg", "_RpAgrmt", "_CollMgmtOpr"]
	@property
	def SctiesBuyOrSell(self):
		return self._SctiesBuyOrSell

	@SctiesBuyOrSell.setter
	def SctiesBuyOrSell(self, value):
		self._SctiesBuyOrSell = value if type(value) != auto else self.make_default("SctiesBuyOrSell")

	@SctiesBuyOrSell.deleter
	def SctiesBuyOrSell(self):
		del self._SctiesBuyOrSell
		self._SctiesBuyOrSell = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def SctiesLndgOrBrrwg(self):
		return self._SctiesLndgOrBrrwg

	@SctiesLndgOrBrrwg.setter
	def SctiesLndgOrBrrwg(self, value):
		self._SctiesLndgOrBrrwg = value if type(value) != auto else self.make_default("SctiesLndgOrBrrwg")

	@SctiesLndgOrBrrwg.deleter
	def SctiesLndgOrBrrwg(self):
		del self._SctiesLndgOrBrrwg
		self._SctiesLndgOrBrrwg = None

	@property
	def RpAgrmt(self):
		return self._RpAgrmt

	@RpAgrmt.setter
	def RpAgrmt(self, value):
		self._RpAgrmt = value if type(value) != auto else self.make_default("RpAgrmt")

	@RpAgrmt.deleter
	def RpAgrmt(self):
		del self._RpAgrmt
		self._RpAgrmt = None

	@property
	def CollMgmtOpr(self):
		return self._CollMgmtOpr

	@CollMgmtOpr.setter
	def CollMgmtOpr(self, value):
		self._CollMgmtOpr = value if type(value) != auto else self.make_default("CollMgmtOpr")

	@CollMgmtOpr.deleter
	def CollMgmtOpr(self):
		del self._CollMgmtOpr
		self._CollMgmtOpr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesBuyOrSell', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesLndgOrBrrwg', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmt', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMgmtOpr', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
	))

