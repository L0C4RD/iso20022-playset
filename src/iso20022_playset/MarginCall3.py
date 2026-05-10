import base_types
import CollateralAccount3
import MarginCall1
import ExpectedCollateral2Choice
import MarginCallResult3
import BlockChainAddressWallet5
import MarginRequirement1Choice

class MarginCall3(base_types._BaseFieldType):

	__slots__ = ["_XpctdCollDueToA", "_RqrmntDtlsDueToB", "_BlckChainAdrOrWllt", "_MrgnDtlDueToB", "_CollAcctId", "_MrgnCallRslt", "_XpctdCollDueToB", "_RqrmntDtlsDueToA", "_MrgnDtlDueToA"]
	@property
	def XpctdCollDueToA(self):
		return self._XpctdCollDueToA

	@XpctdCollDueToA.setter
	def XpctdCollDueToA(self, value):
		self._XpctdCollDueToA = value if type(value) != auto else self.make_default("XpctdCollDueToA")

	@XpctdCollDueToA.deleter
	def XpctdCollDueToA(self):
		del self._XpctdCollDueToA
		self._XpctdCollDueToA = None

	@property
	def RqrmntDtlsDueToB(self):
		return self._RqrmntDtlsDueToB

	@RqrmntDtlsDueToB.setter
	def RqrmntDtlsDueToB(self, value):
		self._RqrmntDtlsDueToB = value if type(value) != auto else self.make_default("RqrmntDtlsDueToB")

	@RqrmntDtlsDueToB.deleter
	def RqrmntDtlsDueToB(self):
		del self._RqrmntDtlsDueToB
		self._RqrmntDtlsDueToB = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def MrgnDtlDueToB(self):
		return self._MrgnDtlDueToB

	@MrgnDtlDueToB.setter
	def MrgnDtlDueToB(self, value):
		self._MrgnDtlDueToB = value if type(value) != auto else self.make_default("MrgnDtlDueToB")

	@MrgnDtlDueToB.deleter
	def MrgnDtlDueToB(self):
		del self._MrgnDtlDueToB
		self._MrgnDtlDueToB = None

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if type(value) != auto else self.make_default("CollAcctId")

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = None

	@property
	def MrgnCallRslt(self):
		return self._MrgnCallRslt

	@MrgnCallRslt.setter
	def MrgnCallRslt(self, value):
		self._MrgnCallRslt = value if type(value) != auto else self.make_default("MrgnCallRslt")

	@MrgnCallRslt.deleter
	def MrgnCallRslt(self):
		del self._MrgnCallRslt
		self._MrgnCallRslt = None

	@property
	def XpctdCollDueToB(self):
		return self._XpctdCollDueToB

	@XpctdCollDueToB.setter
	def XpctdCollDueToB(self, value):
		self._XpctdCollDueToB = value if type(value) != auto else self.make_default("XpctdCollDueToB")

	@XpctdCollDueToB.deleter
	def XpctdCollDueToB(self):
		del self._XpctdCollDueToB
		self._XpctdCollDueToB = None

	@property
	def RqrmntDtlsDueToA(self):
		return self._RqrmntDtlsDueToA

	@RqrmntDtlsDueToA.setter
	def RqrmntDtlsDueToA(self, value):
		self._RqrmntDtlsDueToA = value if type(value) != auto else self.make_default("RqrmntDtlsDueToA")

	@RqrmntDtlsDueToA.deleter
	def RqrmntDtlsDueToA(self):
		del self._RqrmntDtlsDueToA
		self._RqrmntDtlsDueToA = None

	@property
	def MrgnDtlDueToA(self):
		return self._MrgnDtlDueToA

	@MrgnDtlDueToA.setter
	def MrgnDtlDueToA(self, value):
		self._MrgnDtlDueToA = value if type(value) != auto else self.make_default("MrgnDtlDueToA")

	@MrgnDtlDueToA.deleter
	def MrgnDtlDueToA(self):
		del self._MrgnDtlDueToA
		self._MrgnDtlDueToA = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpctdCollDueToA', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqrmntDtlsDueToB', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlDueToB', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallRslt', type=MarginCallResult3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdCollDueToB', type=ExpectedCollateral2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqrmntDtlsDueToA', type=MarginRequirement1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnDtlDueToA', type=MarginCall1, min=0, max=1, mutex_group=None, array=False),
	))

