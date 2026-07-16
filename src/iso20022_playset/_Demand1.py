# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount27
from . import DemandDocumentation1
from . import DemandType1Code
from . import ISODate
from . import Max2000Text
from . import Max35Text
from . import Presentation2
from . import Undertaking6
from . import UndertakingAmount3

class Demand1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AdvsgPtyRefNb", "_CnfrmrRefNb", "_DmndAmt", "_DmndDcmnttn", "_Id", "_PresntnDtls", "_ReqdXpryDt", "_ScndAdvsgPtyRefNb", "_SttlmAcct", "_Tp", "_UdrtkgId"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AdvsgPtyRefNb(self):
		return self._AdvsgPtyRefNb

	@AdvsgPtyRefNb.setter
	def AdvsgPtyRefNb(self, value):
		self._AdvsgPtyRefNb = value if value is not None else base_types.UninitialisedField(self, 'AdvsgPtyRefNb', Max35Text, False)

	@AdvsgPtyRefNb.deleter
	def AdvsgPtyRefNb(self):
		del self._AdvsgPtyRefNb
		self._AdvsgPtyRefNb = base_types.UninitialisedField(self, 'AdvsgPtyRefNb', Max35Text, False)

	@property
	def CnfrmrRefNb(self):
		return self._CnfrmrRefNb

	@CnfrmrRefNb.setter
	def CnfrmrRefNb(self, value):
		self._CnfrmrRefNb = value if value is not None else base_types.UninitialisedField(self, 'CnfrmrRefNb', Max35Text, False)

	@CnfrmrRefNb.deleter
	def CnfrmrRefNb(self):
		del self._CnfrmrRefNb
		self._CnfrmrRefNb = base_types.UninitialisedField(self, 'CnfrmrRefNb', Max35Text, False)

	@property
	def DmndAmt(self):
		return self._DmndAmt

	@DmndAmt.setter
	def DmndAmt(self, value):
		self._DmndAmt = value if value is not None else base_types.UninitialisedField(self, 'DmndAmt', UndertakingAmount3, False)

	@DmndAmt.deleter
	def DmndAmt(self):
		del self._DmndAmt
		self._DmndAmt = base_types.UninitialisedField(self, 'DmndAmt', UndertakingAmount3, False)

	@property
	def DmndDcmnttn(self):
		return self._DmndDcmnttn

	@DmndDcmnttn.setter
	def DmndDcmnttn(self, value):
		self._DmndDcmnttn = value if value is not None else base_types.UninitialisedField(self, 'DmndDcmnttn', DemandDocumentation1, False)

	@DmndDcmnttn.deleter
	def DmndDcmnttn(self):
		del self._DmndDcmnttn
		self._DmndDcmnttn = base_types.UninitialisedField(self, 'DmndDcmnttn', DemandDocumentation1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def PresntnDtls(self):
		return self._PresntnDtls

	@PresntnDtls.setter
	def PresntnDtls(self, value):
		self._PresntnDtls = value if value is not None else base_types.UninitialisedField(self, 'PresntnDtls', Presentation2, False)

	@PresntnDtls.deleter
	def PresntnDtls(self):
		del self._PresntnDtls
		self._PresntnDtls = base_types.UninitialisedField(self, 'PresntnDtls', Presentation2, False)

	@property
	def ReqdXpryDt(self):
		return self._ReqdXpryDt

	@ReqdXpryDt.setter
	def ReqdXpryDt(self, value):
		self._ReqdXpryDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdXpryDt', ISODate, False)

	@ReqdXpryDt.deleter
	def ReqdXpryDt(self):
		del self._ReqdXpryDt
		self._ReqdXpryDt = base_types.UninitialisedField(self, 'ReqdXpryDt', ISODate, False)

	@property
	def ScndAdvsgPtyRefNb(self):
		return self._ScndAdvsgPtyRefNb

	@ScndAdvsgPtyRefNb.setter
	def ScndAdvsgPtyRefNb(self, value):
		self._ScndAdvsgPtyRefNb = value if value is not None else base_types.UninitialisedField(self, 'ScndAdvsgPtyRefNb', Max35Text, False)

	@ScndAdvsgPtyRefNb.deleter
	def ScndAdvsgPtyRefNb(self):
		del self._ScndAdvsgPtyRefNb
		self._ScndAdvsgPtyRefNb = base_types.UninitialisedField(self, 'ScndAdvsgPtyRefNb', Max35Text, False)

	@property
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if value is not None else base_types.UninitialisedField(self, 'SttlmAcct', CashAccount27, True)

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = base_types.UninitialisedField(self, 'SttlmAcct', CashAccount27, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', DemandType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', DemandType1Code, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking6, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndAmt', type=UndertakingAmount3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDcmnttn', type=DemandDocumentation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnDtls', type=Presentation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdXpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAcct', type=CashAccount27, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=DemandType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking6, min=1, max=1, mutex_group=None, array=False),
	))