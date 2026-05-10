import base_types
import ThirdPartyRights2
import FormOfSecurity1Code
import OperationalStatus1Code
import SecurityIdentification25Choice
import Collateral1Code
import FundOwnership1Code
import Eligible1Code
import Max35Text
import DistributionPolicy1Code
import Max350Text
import FundIntention1Code
import BlockedHoldingDetails2
import Max140Text

class FinancialInstrument87(base_types._BaseFieldType):

	__slots__ = ["_SctiesForm", "_PdctGrp", "_ThrdPtyRghts", "_SplmtryId", "_DstrbtnPlcy", "_Pldgg", "_Coll", "_ClssTp", "_OprlSts", "_Id", "_Nm", "_FndIntntn", "_FndOwnrsh", "_ShrtNm", "_BlckdHldgDtls"]
	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if type(value) != auto else self.make_default("SctiesForm")

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = None

	@property
	def PdctGrp(self):
		return self._PdctGrp

	@PdctGrp.setter
	def PdctGrp(self, value):
		self._PdctGrp = value if type(value) != auto else self.make_default("PdctGrp")

	@PdctGrp.deleter
	def PdctGrp(self):
		del self._PdctGrp
		self._PdctGrp = None

	@property
	def ThrdPtyRghts(self):
		return self._ThrdPtyRghts

	@ThrdPtyRghts.setter
	def ThrdPtyRghts(self, value):
		self._ThrdPtyRghts = value if type(value) != auto else self.make_default("ThrdPtyRghts")

	@ThrdPtyRghts.deleter
	def ThrdPtyRghts(self):
		del self._ThrdPtyRghts
		self._ThrdPtyRghts = None

	@property
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if type(value) != auto else self.make_default("SplmtryId")

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = None

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if type(value) != auto else self.make_default("DstrbtnPlcy")

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = None

	@property
	def Pldgg(self):
		return self._Pldgg

	@Pldgg.setter
	def Pldgg(self, value):
		self._Pldgg = value if type(value) != auto else self.make_default("Pldgg")

	@Pldgg.deleter
	def Pldgg(self):
		del self._Pldgg
		self._Pldgg = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if type(value) != auto else self.make_default("ClssTp")

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = None

	@property
	def OprlSts(self):
		return self._OprlSts

	@OprlSts.setter
	def OprlSts(self, value):
		self._OprlSts = value if type(value) != auto else self.make_default("OprlSts")

	@OprlSts.deleter
	def OprlSts(self):
		del self._OprlSts
		self._OprlSts = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def FndIntntn(self):
		return self._FndIntntn

	@FndIntntn.setter
	def FndIntntn(self, value):
		self._FndIntntn = value if type(value) != auto else self.make_default("FndIntntn")

	@FndIntntn.deleter
	def FndIntntn(self):
		del self._FndIntntn
		self._FndIntntn = None

	@property
	def FndOwnrsh(self):
		return self._FndOwnrsh

	@FndOwnrsh.setter
	def FndOwnrsh(self, value):
		self._FndOwnrsh = value if type(value) != auto else self.make_default("FndOwnrsh")

	@FndOwnrsh.deleter
	def FndOwnrsh(self):
		del self._FndOwnrsh
		self._FndOwnrsh = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def BlckdHldgDtls(self):
		return self._BlckdHldgDtls

	@BlckdHldgDtls.setter
	def BlckdHldgDtls(self, value):
		self._BlckdHldgDtls = value if type(value) != auto else self.make_default("BlckdHldgDtls")

	@BlckdHldgDtls.deleter
	def BlckdHldgDtls(self):
		del self._BlckdHldgDtls
		self._BlckdHldgDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctGrp', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyRghts', type=ThirdPartyRights2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgg', type=Eligible1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=Collateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprlSts', type=OperationalStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndIntntn', type=FundIntention1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndOwnrsh', type=FundOwnership1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdHldgDtls', type=BlockedHoldingDetails2, min=0, max=1, mutex_group=None, array=False),
	))

