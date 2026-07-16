# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CFIOct2015Identifier
from . import CollateralPool1Code
from . import SNA2008SectorIdentifier

class CollateralValuation7(base_types._BaseFieldType):

	__slots__ = ["_NmnlAmt", "_PoolSts", "_Sctr", "_Tp"]
	@property
	def NmnlAmt(self):
		return self._NmnlAmt

	@NmnlAmt.setter
	def NmnlAmt(self, value):
		self._NmnlAmt = value if value is not None else base_types.UninitialisedField(self, 'NmnlAmt', ActiveCurrencyAndAmount, False)

	@NmnlAmt.deleter
	def NmnlAmt(self):
		del self._NmnlAmt
		self._NmnlAmt = base_types.UninitialisedField(self, 'NmnlAmt', ActiveCurrencyAndAmount, False)

	@property
	def PoolSts(self):
		return self._PoolSts

	@PoolSts.setter
	def PoolSts(self, value):
		self._PoolSts = value if value is not None else base_types.UninitialisedField(self, 'PoolSts', CollateralPool1Code, False)

	@PoolSts.deleter
	def PoolSts(self):
		del self._PoolSts
		self._PoolSts = base_types.UninitialisedField(self, 'PoolSts', CollateralPool1Code, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', SNA2008SectorIdentifier, False)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', SNA2008SectorIdentifier, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CFIOct2015Identifier, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CFIOct2015Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NmnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolSts', type=CollateralPool1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=SNA2008SectorIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CFIOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))