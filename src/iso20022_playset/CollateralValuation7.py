import base_types
import ActiveCurrencyAndAmount
import SNA2008SectorIdentifier
import CFIOct2015Identifier
import CollateralPool1Code

class CollateralValuation7(base_types._BaseFieldType):

	__slots__ = ["_NmnlAmt", "_Tp", "_PoolSts", "_Sctr"]
	@property
	def NmnlAmt(self):
		return self._NmnlAmt

	@NmnlAmt.setter
	def NmnlAmt(self, value):
		self._NmnlAmt = value if type(value) != auto else self.make_default("NmnlAmt")

	@NmnlAmt.deleter
	def NmnlAmt(self):
		del self._NmnlAmt
		self._NmnlAmt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def PoolSts(self):
		return self._PoolSts

	@PoolSts.setter
	def PoolSts(self, value):
		self._PoolSts = value if type(value) != auto else self.make_default("PoolSts")

	@PoolSts.deleter
	def PoolSts(self):
		del self._PoolSts
		self._PoolSts = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NmnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolSts', type=CollateralPool1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=SNA2008SectorIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

