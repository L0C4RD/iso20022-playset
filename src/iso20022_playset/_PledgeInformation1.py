# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification36
from . import PartyIdentification232Choice
from . import ThirdPartyIdentification1
from . import YesNoIndicator

class PledgeInformation1(base_types._BaseFieldType):

	__slots__ = ["_PldgTp", "_Pldgr", "_RtrSctiesInd", "_ThrdPty"]
	@property
	def PldgTp(self):
		return self._PldgTp

	@PldgTp.setter
	def PldgTp(self, value):
		self._PldgTp = value if value is not None else base_types.UninitialisedField(self, 'PldgTp', GenericIdentification36, False)

	@PldgTp.deleter
	def PldgTp(self):
		del self._PldgTp
		self._PldgTp = base_types.UninitialisedField(self, 'PldgTp', GenericIdentification36, False)

	@property
	def Pldgr(self):
		return self._Pldgr

	@Pldgr.setter
	def Pldgr(self, value):
		self._Pldgr = value if value is not None else base_types.UninitialisedField(self, 'Pldgr', PartyIdentification232Choice, False)

	@Pldgr.deleter
	def Pldgr(self):
		del self._Pldgr
		self._Pldgr = base_types.UninitialisedField(self, 'Pldgr', PartyIdentification232Choice, False)

	@property
	def RtrSctiesInd(self):
		return self._RtrSctiesInd

	@RtrSctiesInd.setter
	def RtrSctiesInd(self, value):
		self._RtrSctiesInd = value if value is not None else base_types.UninitialisedField(self, 'RtrSctiesInd', YesNoIndicator, False)

	@RtrSctiesInd.deleter
	def RtrSctiesInd(self):
		del self._RtrSctiesInd
		self._RtrSctiesInd = base_types.UninitialisedField(self, 'RtrSctiesInd', YesNoIndicator, False)

	@property
	def ThrdPty(self):
		return self._ThrdPty

	@ThrdPty.setter
	def ThrdPty(self, value):
		self._ThrdPty = value if value is not None else base_types.UninitialisedField(self, 'ThrdPty', ThirdPartyIdentification1, False)

	@ThrdPty.deleter
	def ThrdPty(self):
		del self._ThrdPty
		self._ThrdPty = base_types.UninitialisedField(self, 'ThrdPty', ThirdPartyIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PldgTp', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgr', type=PartyIdentification232Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrSctiesInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPty', type=ThirdPartyIdentification1, min=0, max=1, mutex_group=None, array=False),
	))