from . import base_types
from ._BlockChainAddressWallet5 import BlockChainAddressWallet5
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._ExposureType11Code import ExposureType11Code
from ._CollateralAccount3 import CollateralAccount3
from ._PartyIdentification178Choice import PartyIdentification178Choice

class Obligation9(base_types._BaseFieldType):

	__slots__ = ["_CollAcctId", "_SvcgPtyB", "_SvcgPtyA", "_XpsrTp", "_PtyB", "_ValtnDt", "_PtyA", "_BlckChainAdrOrWllt"]
	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if type(value) != base_types.auto else self.make_default("CollAcctId")

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = None

	@property
	def PtyA(self):
		return self._PtyA

	@PtyA.setter
	def PtyA(self, value):
		self._PtyA = value if type(value) != base_types.auto else self.make_default("PtyA")

	@PtyA.deleter
	def PtyA(self):
		del self._PtyA
		self._PtyA = None

	@property
	def PtyB(self):
		return self._PtyB

	@PtyB.setter
	def PtyB(self, value):
		self._PtyB = value if type(value) != base_types.auto else self.make_default("PtyB")

	@PtyB.deleter
	def PtyB(self):
		del self._PtyB
		self._PtyB = None

	@property
	def SvcgPtyA(self):
		return self._SvcgPtyA

	@SvcgPtyA.setter
	def SvcgPtyA(self, value):
		self._SvcgPtyA = value if type(value) != base_types.auto else self.make_default("SvcgPtyA")

	@SvcgPtyA.deleter
	def SvcgPtyA(self):
		del self._SvcgPtyA
		self._SvcgPtyA = None

	@property
	def SvcgPtyB(self):
		return self._SvcgPtyB

	@SvcgPtyB.setter
	def SvcgPtyB(self, value):
		self._SvcgPtyB = value if type(value) != base_types.auto else self.make_default("SvcgPtyB")

	@SvcgPtyB.deleter
	def SvcgPtyB(self):
		del self._SvcgPtyB
		self._SvcgPtyB = None

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if type(value) != base_types.auto else self.make_default("ValtnDt")

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyA', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyB', type=PartyIdentification178Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyA', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcgPtyB', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType11Code, min=0, max=1, mutex_group=None, array=False),
	))

