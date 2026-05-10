import base_types
import ThirdPartyIdentification1
import GenericIdentification36
import PartyIdentification232Choice
import YesNoIndicator

class PledgeInformation1(base_types._BaseFieldType):

	__slots__ = ["_Pldgr", "_RtrSctiesInd", "_PldgTp", "_ThrdPty"]
	@property
	def Pldgr(self):
		return self._Pldgr

	@Pldgr.setter
	def Pldgr(self, value):
		self._Pldgr = value if type(value) != auto else self.make_default("Pldgr")

	@Pldgr.deleter
	def Pldgr(self):
		del self._Pldgr
		self._Pldgr = None

	@property
	def RtrSctiesInd(self):
		return self._RtrSctiesInd

	@RtrSctiesInd.setter
	def RtrSctiesInd(self, value):
		self._RtrSctiesInd = value if type(value) != auto else self.make_default("RtrSctiesInd")

	@RtrSctiesInd.deleter
	def RtrSctiesInd(self):
		del self._RtrSctiesInd
		self._RtrSctiesInd = None

	@property
	def PldgTp(self):
		return self._PldgTp

	@PldgTp.setter
	def PldgTp(self, value):
		self._PldgTp = value if type(value) != auto else self.make_default("PldgTp")

	@PldgTp.deleter
	def PldgTp(self):
		del self._PldgTp
		self._PldgTp = None

	@property
	def ThrdPty(self):
		return self._ThrdPty

	@ThrdPty.setter
	def ThrdPty(self, value):
		self._ThrdPty = value if type(value) != auto else self.make_default("ThrdPty")

	@ThrdPty.deleter
	def ThrdPty(self):
		del self._ThrdPty
		self._ThrdPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pldgr', type=PartyIdentification232Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrSctiesInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PldgTp', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPty', type=ThirdPartyIdentification1, min=0, max=1, mutex_group=None, array=False),
	))

