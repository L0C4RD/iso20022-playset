from . import base_types
from ._CountryCode import CountryCode
from ._Max20000Text import Max20000Text
from ._Period4Choice import Period4Choice
from ._Max10Text import Max10Text
from ._SupervisingAuthorityIdentification1 import SupervisingAuthorityIdentification1

class StatusDetail1(base_types._BaseFieldType):

	__slots__ = ["_Cmnt", "_StsRsn", "_Ctry", "_CmptntAuthrty", "_ActvtyPrd", "_Sts"]
	@property
	def ActvtyPrd(self):
		return self._ActvtyPrd

	@ActvtyPrd.setter
	def ActvtyPrd(self, value):
		self._ActvtyPrd = value if type(value) != base_types.auto else self.make_default("ActvtyPrd")

	@ActvtyPrd.deleter
	def ActvtyPrd(self):
		del self._ActvtyPrd
		self._ActvtyPrd = None

	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if type(value) != base_types.auto else self.make_default("Cmnt")

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = None

	@property
	def CmptntAuthrty(self):
		return self._CmptntAuthrty

	@CmptntAuthrty.setter
	def CmptntAuthrty(self, value):
		self._CmptntAuthrty = value if type(value) != base_types.auto else self.make_default("CmptntAuthrty")

	@CmptntAuthrty.deleter
	def CmptntAuthrty(self):
		del self._CmptntAuthrty
		self._CmptntAuthrty = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

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
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmnt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmptntAuthrty', type=SupervisingAuthorityIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
	))

