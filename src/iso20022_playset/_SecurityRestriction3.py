# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod2
from . import InvestorRestrictionType3Choice
from . import InvestorType3Choice
from . import LegalRestrictions5Choice
from . import SecurityRestrictionType2Choice

class SecurityRestriction3(base_types._BaseFieldType):

	__slots__ = ["_FctvPrd", "_InvstrRstrctnTp", "_InvstrTp", "_LglRstrctnTp", "_RstrctnTp"]
	@property
	def FctvPrd(self):
		return self._FctvPrd

	@FctvPrd.setter
	def FctvPrd(self, value):
		self._FctvPrd = value if value is not None else base_types.UninitialisedField(self, 'FctvPrd', DateTimePeriod2, False)

	@FctvPrd.deleter
	def FctvPrd(self):
		del self._FctvPrd
		self._FctvPrd = base_types.UninitialisedField(self, 'FctvPrd', DateTimePeriod2, False)

	@property
	def InvstrRstrctnTp(self):
		return self._InvstrRstrctnTp

	@InvstrRstrctnTp.setter
	def InvstrRstrctnTp(self, value):
		self._InvstrRstrctnTp = value if value is not None else base_types.UninitialisedField(self, 'InvstrRstrctnTp', InvestorRestrictionType3Choice, True)

	@InvstrRstrctnTp.deleter
	def InvstrRstrctnTp(self):
		del self._InvstrRstrctnTp
		self._InvstrRstrctnTp = base_types.UninitialisedField(self, 'InvstrRstrctnTp', InvestorRestrictionType3Choice, True)

	@property
	def InvstrTp(self):
		return self._InvstrTp

	@InvstrTp.setter
	def InvstrTp(self, value):
		self._InvstrTp = value if value is not None else base_types.UninitialisedField(self, 'InvstrTp', InvestorType3Choice, True)

	@InvstrTp.deleter
	def InvstrTp(self):
		del self._InvstrTp
		self._InvstrTp = base_types.UninitialisedField(self, 'InvstrTp', InvestorType3Choice, True)

	@property
	def LglRstrctnTp(self):
		return self._LglRstrctnTp

	@LglRstrctnTp.setter
	def LglRstrctnTp(self, value):
		self._LglRstrctnTp = value if value is not None else base_types.UninitialisedField(self, 'LglRstrctnTp', LegalRestrictions5Choice, False)

	@LglRstrctnTp.deleter
	def LglRstrctnTp(self):
		del self._LglRstrctnTp
		self._LglRstrctnTp = base_types.UninitialisedField(self, 'LglRstrctnTp', LegalRestrictions5Choice, False)

	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if value is not None else base_types.UninitialisedField(self, 'RstrctnTp', SecurityRestrictionType2Choice, False)

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = base_types.UninitialisedField(self, 'RstrctnTp', SecurityRestrictionType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvPrd', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrRstrctnTp', type=InvestorRestrictionType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglRstrctnTp', type=LegalRestrictions5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnTp', type=SecurityRestrictionType2Choice, min=0, max=1, mutex_group=None, array=False),
	))