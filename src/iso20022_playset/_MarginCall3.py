# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockChainAddressWallet5
from . import CollateralAccount3
from . import ExpectedCollateral2Choice
from . import MarginCall1
from . import MarginCallResult3
from . import MarginRequirement1Choice

class MarginCall3(base_types._BaseFieldType):

	__slots__ = ["_BlckChainAdrOrWllt", "_CollAcctId", "_MrgnCallRslt", "_MrgnDtlDueToA", "_MrgnDtlDueToB", "_RqrmntDtlsDueToA", "_RqrmntDtlsDueToB", "_XpctdCollDueToA", "_XpctdCollDueToB"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if value is not None else base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@property
	def MrgnCallRslt(self):
		return self._MrgnCallRslt

	@MrgnCallRslt.setter
	def MrgnCallRslt(self, value):
		self._MrgnCallRslt = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRslt', MarginCallResult3, False)

	@MrgnCallRslt.deleter
	def MrgnCallRslt(self):
		del self._MrgnCallRslt
		self._MrgnCallRslt = base_types.UninitialisedField(self, 'MrgnCallRslt', MarginCallResult3, False)

	@property
	def MrgnDtlDueToA(self):
		return self._MrgnDtlDueToA

	@MrgnDtlDueToA.setter
	def MrgnDtlDueToA(self, value):
		self._MrgnDtlDueToA = value if value is not None else base_types.UninitialisedField(self, 'MrgnDtlDueToA', MarginCall1, False)

	@MrgnDtlDueToA.deleter
	def MrgnDtlDueToA(self):
		del self._MrgnDtlDueToA
		self._MrgnDtlDueToA = base_types.UninitialisedField(self, 'MrgnDtlDueToA', MarginCall1, False)

	@property
	def MrgnDtlDueToB(self):
		return self._MrgnDtlDueToB

	@MrgnDtlDueToB.setter
	def MrgnDtlDueToB(self, value):
		self._MrgnDtlDueToB = value if value is not None else base_types.UninitialisedField(self, 'MrgnDtlDueToB', MarginCall1, False)

	@MrgnDtlDueToB.deleter
	def MrgnDtlDueToB(self):
		del self._MrgnDtlDueToB
		self._MrgnDtlDueToB = base_types.UninitialisedField(self, 'MrgnDtlDueToB', MarginCall1, False)

	@property
	def RqrmntDtlsDueToA(self):
		return self._RqrmntDtlsDueToA

	@RqrmntDtlsDueToA.setter
	def RqrmntDtlsDueToA(self, value):
		self._RqrmntDtlsDueToA = value if value is not None else base_types.UninitialisedField(self, 'RqrmntDtlsDueToA', MarginRequirement1Choice, False)

	@RqrmntDtlsDueToA.deleter
	def RqrmntDtlsDueToA(self):
		del self._RqrmntDtlsDueToA
		self._RqrmntDtlsDueToA = base_types.UninitialisedField(self, 'RqrmntDtlsDueToA', MarginRequirement1Choice, False)

	@property
	def RqrmntDtlsDueToB(self):
		return self._RqrmntDtlsDueToB

	@RqrmntDtlsDueToB.setter
	def RqrmntDtlsDueToB(self, value):
		self._RqrmntDtlsDueToB = value if value is not None else base_types.UninitialisedField(self, 'RqrmntDtlsDueToB', MarginRequirement1Choice, False)

	@RqrmntDtlsDueToB.deleter
	def RqrmntDtlsDueToB(self):
		del self._RqrmntDtlsDueToB
		self._RqrmntDtlsDueToB = base_types.UninitialisedField(self, 'RqrmntDtlsDueToB', MarginRequirement1Choice, False)

	@property
	def XpctdCollDueToA(self):
		return self._XpctdCollDueToA

	@XpctdCollDueToA.setter
	def XpctdCollDueToA(self, value):
		self._XpctdCollDueToA = value if value is not None else base_types.UninitialisedField(self, 'XpctdCollDueToA', ExpectedCollateral2Choice, False)

	@XpctdCollDueToA.deleter
	def XpctdCollDueToA(self):
		del self._XpctdCollDueToA
		self._XpctdCollDueToA = base_types.UninitialisedField(self, 'XpctdCollDueToA', ExpectedCollateral2Choice, False)

	@property
	def XpctdCollDueToB(self):
		return self._XpctdCollDueToB

	@XpctdCollDueToB.setter
	def XpctdCollDueToB(self, value):
		self._XpctdCollDueToB = value if value is not None else base_types.UninitialisedField(self, 'XpctdCollDueToB', ExpectedCollateral2Choice, False)

	@XpctdCollDueToB.deleter
	def XpctdCollDueToB(self):
		del self._XpctdCollDueToB
		self._XpctdCollDueToB = base_types.UninitialisedField(self, 'XpctdCollDueToB', ExpectedCollateral2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallRslt', type=MarginCallResult3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlDueToA', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlDueToB', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqrmntDtlsDueToA', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqrmntDtlsDueToB', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToA', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToB', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
	))