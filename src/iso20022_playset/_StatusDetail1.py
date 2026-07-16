# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max10Text
from . import Max20000Text
from . import Period4Choice
from . import SupervisingAuthorityIdentification1

class StatusDetail1(base_types._BaseFieldType):

	__slots__ = ["_ActvtyPrd", "_Cmnt", "_CmptntAuthrty", "_Ctry", "_Sts", "_StsRsn"]
	@property
	def ActvtyPrd(self):
		return self._ActvtyPrd

	@ActvtyPrd.setter
	def ActvtyPrd(self, value):
		self._ActvtyPrd = value if value is not None else base_types.UninitialisedField(self, 'ActvtyPrd', Period4Choice, False)

	@ActvtyPrd.deleter
	def ActvtyPrd(self):
		del self._ActvtyPrd
		self._ActvtyPrd = base_types.UninitialisedField(self, 'ActvtyPrd', Period4Choice, False)

	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if value is not None else base_types.UninitialisedField(self, 'Cmnt', Max20000Text, False)

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = base_types.UninitialisedField(self, 'Cmnt', Max20000Text, False)

	@property
	def CmptntAuthrty(self):
		return self._CmptntAuthrty

	@CmptntAuthrty.setter
	def CmptntAuthrty(self, value):
		self._CmptntAuthrty = value if value is not None else base_types.UninitialisedField(self, 'CmptntAuthrty', SupervisingAuthorityIdentification1, False)

	@CmptntAuthrty.deleter
	def CmptntAuthrty(self):
		del self._CmptntAuthrty
		self._CmptntAuthrty = base_types.UninitialisedField(self, 'CmptntAuthrty', SupervisingAuthorityIdentification1, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', Max10Text, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', Max10Text, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', Max10Text, False)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', Max10Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtyPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmnt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmptntAuthrty', type=SupervisingAuthorityIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
	))