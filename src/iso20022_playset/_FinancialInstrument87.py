# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockedHoldingDetails2
from . import Collateral1Code
from . import DistributionPolicy1Code
from . import Eligible1Code
from . import FormOfSecurity1Code
from . import FundIntention1Code
from . import FundOwnership1Code
from . import Max140Text
from . import Max350Text
from . import Max35Text
from . import OperationalStatus1Code
from . import SecurityIdentification25Choice
from . import ThirdPartyRights2

class FinancialInstrument87(base_types._BaseFieldType):

	__slots__ = ["_BlckdHldgDtls", "_ClssTp", "_Coll", "_DstrbtnPlcy", "_FndIntntn", "_FndOwnrsh", "_Id", "_Nm", "_OprlSts", "_PdctGrp", "_Pldgg", "_SctiesForm", "_ShrtNm", "_SplmtryId", "_ThrdPtyRghts"]
	@property
	def BlckdHldgDtls(self):
		return self._BlckdHldgDtls

	@BlckdHldgDtls.setter
	def BlckdHldgDtls(self, value):
		self._BlckdHldgDtls = value if value is not None else base_types.UninitialisedField(self, 'BlckdHldgDtls', BlockedHoldingDetails2, False)

	@BlckdHldgDtls.deleter
	def BlckdHldgDtls(self):
		del self._BlckdHldgDtls
		self._BlckdHldgDtls = base_types.UninitialisedField(self, 'BlckdHldgDtls', BlockedHoldingDetails2, False)

	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if value is not None else base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if value is not None else base_types.UninitialisedField(self, 'Coll', Collateral1Code, False)

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = base_types.UninitialisedField(self, 'Coll', Collateral1Code, False)

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if value is not None else base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = base_types.UninitialisedField(self, 'DstrbtnPlcy', DistributionPolicy1Code, False)

	@property
	def FndIntntn(self):
		return self._FndIntntn

	@FndIntntn.setter
	def FndIntntn(self, value):
		self._FndIntntn = value if value is not None else base_types.UninitialisedField(self, 'FndIntntn', FundIntention1Code, False)

	@FndIntntn.deleter
	def FndIntntn(self):
		del self._FndIntntn
		self._FndIntntn = base_types.UninitialisedField(self, 'FndIntntn', FundIntention1Code, False)

	@property
	def FndOwnrsh(self):
		return self._FndOwnrsh

	@FndOwnrsh.setter
	def FndOwnrsh(self, value):
		self._FndOwnrsh = value if value is not None else base_types.UninitialisedField(self, 'FndOwnrsh', FundOwnership1Code, False)

	@FndOwnrsh.deleter
	def FndOwnrsh(self):
		del self._FndOwnrsh
		self._FndOwnrsh = base_types.UninitialisedField(self, 'FndOwnrsh', FundOwnership1Code, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification25Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification25Choice, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def OprlSts(self):
		return self._OprlSts

	@OprlSts.setter
	def OprlSts(self, value):
		self._OprlSts = value if value is not None else base_types.UninitialisedField(self, 'OprlSts', OperationalStatus1Code, False)

	@OprlSts.deleter
	def OprlSts(self):
		del self._OprlSts
		self._OprlSts = base_types.UninitialisedField(self, 'OprlSts', OperationalStatus1Code, False)

	@property
	def PdctGrp(self):
		return self._PdctGrp

	@PdctGrp.setter
	def PdctGrp(self, value):
		self._PdctGrp = value if value is not None else base_types.UninitialisedField(self, 'PdctGrp', Max140Text, False)

	@PdctGrp.deleter
	def PdctGrp(self):
		del self._PdctGrp
		self._PdctGrp = base_types.UninitialisedField(self, 'PdctGrp', Max140Text, False)

	@property
	def Pldgg(self):
		return self._Pldgg

	@Pldgg.setter
	def Pldgg(self, value):
		self._Pldgg = value if value is not None else base_types.UninitialisedField(self, 'Pldgg', Eligible1Code, False)

	@Pldgg.deleter
	def Pldgg(self):
		del self._Pldgg
		self._Pldgg = base_types.UninitialisedField(self, 'Pldgg', Eligible1Code, False)

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if value is not None else base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = base_types.UninitialisedField(self, 'SctiesForm', FormOfSecurity1Code, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@property
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if value is not None else base_types.UninitialisedField(self, 'SplmtryId', Max35Text, False)

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = base_types.UninitialisedField(self, 'SplmtryId', Max35Text, False)

	@property
	def ThrdPtyRghts(self):
		return self._ThrdPtyRghts

	@ThrdPtyRghts.setter
	def ThrdPtyRghts(self, value):
		self._ThrdPtyRghts = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyRghts', ThirdPartyRights2, False)

	@ThrdPtyRghts.deleter
	def ThrdPtyRghts(self):
		del self._ThrdPtyRghts
		self._ThrdPtyRghts = base_types.UninitialisedField(self, 'ThrdPtyRghts', ThirdPartyRights2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BlckdHldgDtls', type=BlockedHoldingDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=Collateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndIntntn', type=FundIntention1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndOwnrsh', type=FundOwnership1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprlSts', type=OperationalStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctGrp', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgg', type=Eligible1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyRghts', type=ThirdPartyRights2, min=0, max=1, mutex_group=None, array=False),
	))