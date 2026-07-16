# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Demand2
from . import Discrepancy1
from . import Max2000Text
from . import Max35Text
from . import Refused7Text
from . import Undertaking9

class DemandRefusal1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AdvsgPtyRefNb", "_CnfrmrRefNb", "_DmndDtls", "_Dscrpncy", "_DspstnOfDocs", "_ScndAdvsgPtyRefNb", "_Sts", "_UdrtkgId"]
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
	def DmndDtls(self):
		return self._DmndDtls

	@DmndDtls.setter
	def DmndDtls(self, value):
		self._DmndDtls = value if value is not None else base_types.UninitialisedField(self, 'DmndDtls', Demand2, False)

	@DmndDtls.deleter
	def DmndDtls(self):
		del self._DmndDtls
		self._DmndDtls = base_types.UninitialisedField(self, 'DmndDtls', Demand2, False)

	@property
	def Dscrpncy(self):
		return self._Dscrpncy

	@Dscrpncy.setter
	def Dscrpncy(self, value):
		self._Dscrpncy = value if value is not None else base_types.UninitialisedField(self, 'Dscrpncy', Discrepancy1, True)

	@Dscrpncy.deleter
	def Dscrpncy(self):
		del self._Dscrpncy
		self._Dscrpncy = base_types.UninitialisedField(self, 'Dscrpncy', Discrepancy1, True)

	@property
	def DspstnOfDocs(self):
		return self._DspstnOfDocs

	@DspstnOfDocs.setter
	def DspstnOfDocs(self, value):
		self._DspstnOfDocs = value if value is not None else base_types.UninitialisedField(self, 'DspstnOfDocs', Max2000Text, True)

	@DspstnOfDocs.deleter
	def DspstnOfDocs(self):
		del self._DspstnOfDocs
		self._DspstnOfDocs = base_types.UninitialisedField(self, 'DspstnOfDocs', Max2000Text, True)

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
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Refused7Text, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Refused7Text, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfrmrRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndDtls', type=Demand2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscrpncy', type=Discrepancy1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DspstnOfDocs', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndAdvsgPtyRefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Refused7Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))