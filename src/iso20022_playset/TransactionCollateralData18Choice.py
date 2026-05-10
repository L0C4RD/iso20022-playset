import base_types
import CollateralFlag13Choice
import Collateral52
import Security55

class TransactionCollateralData18Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnLndg", "_SctiesLndg", "_BuySellBck", "_RpTrad"]
	@property
	def MrgnLndg(self):
		return self._MrgnLndg

	@MrgnLndg.setter
	def MrgnLndg(self, value):
		self._MrgnLndg = value if type(value) != auto else self.make_default("MrgnLndg")

	@MrgnLndg.deleter
	def MrgnLndg(self):
		del self._MrgnLndg
		self._MrgnLndg = None

	@property
	def SctiesLndg(self):
		return self._SctiesLndg

	@SctiesLndg.setter
	def SctiesLndg(self, value):
		self._SctiesLndg = value if type(value) != auto else self.make_default("SctiesLndg")

	@SctiesLndg.deleter
	def SctiesLndg(self):
		del self._SctiesLndg
		self._SctiesLndg = None

	@property
	def BuySellBck(self):
		return self._BuySellBck

	@BuySellBck.setter
	def BuySellBck(self, value):
		self._BuySellBck = value if type(value) != auto else self.make_default("BuySellBck")

	@BuySellBck.deleter
	def BuySellBck(self):
		del self._BuySellBck
		self._BuySellBck = None

	@property
	def RpTrad(self):
		return self._RpTrad

	@RpTrad.setter
	def RpTrad(self, value):
		self._RpTrad = value if type(value) != auto else self.make_default("RpTrad")

	@RpTrad.deleter
	def RpTrad(self):
		del self._RpTrad
		self._RpTrad = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnLndg', type=Security55, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesLndg', type=CollateralFlag13Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BuySellBck', type=Collateral52, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RpTrad', type=Collateral52, min=0, max=1, mutex_group=1, array=False),
	))

