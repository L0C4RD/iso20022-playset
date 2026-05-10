from . import base_types
from ._CashAccount27 import CashAccount27
from ._Undertaking6 import Undertaking6
from ._DemandDocumentation1 import DemandDocumentation1
from ._Max2000Text import Max2000Text
from ._DemandType1Code import DemandType1Code
from ._Max35Text import Max35Text
from ._Presentation2 import Presentation2
from ._UndertakingAmount3 import UndertakingAmount3
from ._ISODate import ISODate

class Demand1(base_types._BaseFieldType):

	__slots__ = ["_DmndAmt", "_ReqdXpryDt", "_PresntnDtls", "_AdvsgPtyRefNb", "_Tp", "_DmndDcmnttn", "_SttlmAcct", "_UdrtkgId", "_Id", "_AddtlInf", "_CnfrmrRefNb", "_ScndAdvsgPtyRefNb"]
	@property
	def DmndAmt(self):
		return self._DmndAmt

	@DmndAmt.setter
	def DmndAmt(self, value):
		self._DmndAmt = value if type(value) != base_types.auto else self.make_default("DmndAmt")

	@DmndAmt.deleter
	def DmndAmt(self):
		del self._DmndAmt
		self._DmndAmt = None

	@property
	def ReqdXpryDt(self):
		return self._ReqdXpryDt

	@ReqdXpryDt.setter
	def ReqdXpryDt(self, value):
		self._ReqdXpryDt = value if type(value) != base_types.auto else self.make_default("ReqdXpryDt")

	@ReqdXpryDt.deleter
	def ReqdXpryDt(self):
		del self._ReqdXpryDt
		self._ReqdXpryDt = None

	@property
	def PresntnDtls(self):
		return self._PresntnDtls

	@PresntnDtls.setter
	def PresntnDtls(self, value):
		self._PresntnDtls = value if type(value) != base_types.auto else self.make_default("PresntnDtls")

	@PresntnDtls.deleter
	def PresntnDtls(self):
		del self._PresntnDtls
		self._PresntnDtls = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DmndDcmnttn(self):
		return self._DmndDcmnttn

	@DmndDcmnttn.setter
	def DmndDcmnttn(self, value):
		self._DmndDcmnttn = value if type(value) != base_types.auto else self.make_default("DmndDcmnttn")

	@DmndDcmnttn.deleter
	def DmndDcmnttn(self):
		del self._DmndDcmnttn
		self._DmndDcmnttn = None

	@property
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if type(value) != base_types.auto else self.make_default("SttlmAcct")

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = None

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
	def ScndAdvsgPtyRefNb(self):
		return self._ScndAdvsgPtyRefNb

	@ScndAdvsgPtyRefNb.setter
	def ScndAdvsgPtyRefNb(self, value):
		self._ScndAdvsgPtyRefNb = value if type(value) != base_types.auto else self.make_default("ScndAdvsgPtyRefNb")

	@ScndAdvsgPtyRefNb.deleter
	def ScndAdvsgPtyRefNb(self):
		del self._ScndAdvsgPtyRefNb
		self._ScndAdvsgPtyRefNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmndAmt', type=UndertakingAmount3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdXpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnDtls', type=Presentation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DemandType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDcmnttn', type=DemandDocumentation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAcct', type=CashAccount27, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

