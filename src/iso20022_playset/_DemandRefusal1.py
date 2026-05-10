from . import base_types
from .Max35Text import Max35Text
from .Demand2 import Demand2
from .Max2000Text import Max2000Text
from .Discrepancy1 import Discrepancy1
from .Undertaking9 import Undertaking9
from .Refused7Text import Refused7Text

class DemandRefusal1(base_types._BaseFieldType):

	__slots__ = ["_CnfrmrRefNb", "_DmndDtls", "_Sts", "_DspstnOfDocs", "_UdrtkgId", "_AdvsgPtyRefNb", "_ScndAdvsgPtyRefNb", "_Dscrpncy", "_AddtlInf"]
	@property
	def CnfrmrRefNb(self):
		return self._CnfrmrRefNb

	@CnfrmrRefNb.setter
	def CnfrmrRefNb(self, value):
		self._CnfrmrRefNb = value if type(value) != base_types.auto else self.make_default("CnfrmrRefNb")

	@CnfrmrRefNb.deleter
	def CnfrmrRefNb(self):
		del self._CnfrmrRefNb
		self._CnfrmrRefNb = None

	@property
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if type(value) != base_types.auto else self.make_default("DmndDtls")

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def DspstnOfDocs(self):
		return self._DspstnOfDocs

	@DspstnOfDocs.setter
	def DspstnOfDocs(self, value):
		self._DspstnOfDocs = value if type(value) != base_types.auto else self.make_default("DspstnOfDocs")

	@DspstnOfDocs.deleter
	def DspstnOfDocs(self):
		del self._DspstnOfDocs
		self._DspstnOfDocs = None

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if type(value) != base_types.auto else self.make_default("UdrtkgId")

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = None

	@property
	def AdvsgPtyRefNb(self):
		return self._AdvsgPtyRefNb

	@AdvsgPtyRefNb.setter
	def AdvsgPtyRefNb(self, value):
		self._AdvsgPtyRefNb = value if type(value) != base_types.auto else self.make_default("AdvsgPtyRefNb")

	@AdvsgPtyRefNb.deleter
	def AdvsgPtyRefNb(self):
		del self._AdvsgPtyRefNb
		self._AdvsgPtyRefNb = None

	@property
	def ScndAdvsgPtyRefNb(self):
		return self._ScndAdvsgPtyRefNb

	@ScndAdvsgPtyRefNb.setter
	def ScndAdvsgPtyRefNb(self, value):
		self._ScndAdvsgPtyRefNb = value if type(value) != base_types.auto else self.make_default("ScndAdvsgPtyRefNb")

	@ScndAdvsgPtyRefNb.deleter
	def ScndAdvsgPtyRefNb(self):
		del self._ScndAdvsgPtyRefNb
		self._ScndAdvsgPtyRefNb = None

	@property
	def Dscrpncy(self):
		return self._Dscrpncy

	@Dscrpncy.setter
	def Dscrpncy(self, value):
		self._Dscrpncy = value if type(value) != base_types.auto else self.make_default("Dscrpncy")

	@Dscrpncy.deleter
	def Dscrpncy(self):
		del self._Dscrpncy
		self._Dscrpncy = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDtls', type=Demand2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Refused7Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DspstnOfDocs', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscrpncy', type=Discrepancy1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

