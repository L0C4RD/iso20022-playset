# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import HighFrequencyTradingProfile1
from . import InvestorProfileStatus1Choice
from . import MarketMakerProfile2
from . import ProfileType1Choice
from . import TreasuryProfile1

class InvestorProfile2(base_types._BaseFieldType):

	__slots__ = ["_HghFrqcyTradg", "_MktMakr", "_Sts", "_Tp", "_Trsr"]
	@property
	def HghFrqcyTradg(self):
		return self._HghFrqcyTradg

	@HghFrqcyTradg.setter
	def HghFrqcyTradg(self, value):
		self._HghFrqcyTradg = value if value is not None else base_types.UninitialisedField(self, 'HghFrqcyTradg', HighFrequencyTradingProfile1, False)

	@HghFrqcyTradg.deleter
	def HghFrqcyTradg(self):
		del self._HghFrqcyTradg
		self._HghFrqcyTradg = base_types.UninitialisedField(self, 'HghFrqcyTradg', HighFrequencyTradingProfile1, False)

	@property
	def MktMakr(self):
		return self._MktMakr

	@MktMakr.setter
	def MktMakr(self, value):
		self._MktMakr = value if value is not None else base_types.UninitialisedField(self, 'MktMakr', MarketMakerProfile2, False)

	@MktMakr.deleter
	def MktMakr(self):
		del self._MktMakr
		self._MktMakr = base_types.UninitialisedField(self, 'MktMakr', MarketMakerProfile2, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', InvestorProfileStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', InvestorProfileStatus1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ProfileType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ProfileType1Choice, False)

	@property
	def Trsr(self):
		return self._Trsr

	@Trsr.setter
	def Trsr(self, value):
		self._Trsr = value if value is not None else base_types.UninitialisedField(self, 'Trsr', TreasuryProfile1, False)

	@Trsr.deleter
	def Trsr(self):
		del self._Trsr
		self._Trsr = base_types.UninitialisedField(self, 'Trsr', TreasuryProfile1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghFrqcyTradg', type=HighFrequencyTradingProfile1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktMakr', type=MarketMakerProfile2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=InvestorProfileStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ProfileType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trsr', type=TreasuryProfile1, min=0, max=1, mutex_group=None, array=False),
	))