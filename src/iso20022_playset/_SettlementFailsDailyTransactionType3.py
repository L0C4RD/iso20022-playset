# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsDailyCSD1Choice

class SettlementFailsDailyTransactionType3(base_types._BaseFieldType):

	__slots__ = ["_CollMgmtOpr", "_Othr", "_RpAgrmt", "_SctiesBuyOrSell", "_SctiesLndgOrBrrwg"]
	@property
	def CollMgmtOpr(self):
		return self._CollMgmtOpr

	@CollMgmtOpr.setter
	def CollMgmtOpr(self, value):
		self._CollMgmtOpr = value if value is not None else base_types.UninitialisedField(self, 'CollMgmtOpr', SettlementFailsDailyCSD1Choice, False)

	@CollMgmtOpr.deleter
	def CollMgmtOpr(self):
		del self._CollMgmtOpr
		self._CollMgmtOpr = base_types.UninitialisedField(self, 'CollMgmtOpr', SettlementFailsDailyCSD1Choice, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', SettlementFailsDailyCSD1Choice, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', SettlementFailsDailyCSD1Choice, False)

	@property
	def RpAgrmt(self):
		return self._RpAgrmt

	@RpAgrmt.setter
	def RpAgrmt(self, value):
		self._RpAgrmt = value if value is not None else base_types.UninitialisedField(self, 'RpAgrmt', SettlementFailsDailyCSD1Choice, False)

	@RpAgrmt.deleter
	def RpAgrmt(self):
		del self._RpAgrmt
		self._RpAgrmt = base_types.UninitialisedField(self, 'RpAgrmt', SettlementFailsDailyCSD1Choice, False)

	@property
	def SctiesBuyOrSell(self):
		return self._SctiesBuyOrSell

	@SctiesBuyOrSell.setter
	def SctiesBuyOrSell(self, value):
		self._SctiesBuyOrSell = value if value is not None else base_types.UninitialisedField(self, 'SctiesBuyOrSell', SettlementFailsDailyCSD1Choice, False)

	@SctiesBuyOrSell.deleter
	def SctiesBuyOrSell(self):
		del self._SctiesBuyOrSell
		self._SctiesBuyOrSell = base_types.UninitialisedField(self, 'SctiesBuyOrSell', SettlementFailsDailyCSD1Choice, False)

	@property
	def SctiesLndgOrBrrwg(self):
		return self._SctiesLndgOrBrrwg

	@SctiesLndgOrBrrwg.setter
	def SctiesLndgOrBrrwg(self, value):
		self._SctiesLndgOrBrrwg = value if value is not None else base_types.UninitialisedField(self, 'SctiesLndgOrBrrwg', SettlementFailsDailyCSD1Choice, False)

	@SctiesLndgOrBrrwg.deleter
	def SctiesLndgOrBrrwg(self):
		del self._SctiesLndgOrBrrwg
		self._SctiesLndgOrBrrwg = base_types.UninitialisedField(self, 'SctiesLndgOrBrrwg', SettlementFailsDailyCSD1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollMgmtOpr', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmt', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesBuyOrSell', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesLndgOrBrrwg', type=SettlementFailsDailyCSD1Choice, min=1, max=1, mutex_group=None, array=False),
	))